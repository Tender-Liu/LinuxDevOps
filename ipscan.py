#!/usr/bin/env python3

import socket
import asyncio
import platform
import ipaddress
from typing import List, Tuple

# 获取本机IP和子网掩码
def get_network_info() -> tuple:
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        # 连接一个公网IP(不会真实建立连接)来获取本机IP
        s.connect(('8.8.8.8', 80))
        ip_addr = s.getsockname()[0]
        # 默认使用24位子网掩码
        netmask = '255.255.255.0'
        return ip_addr, netmask
    except Exception as e:
        return '127.0.0.1', '255.255.255.0'
    finally:
        s.close()

# ping检测主机是否在线
async def check_host(ip: str) -> str:
    try:
        # 根据操作系统选择ping参数
        params = '-n 1 -w 1000' if platform.system().lower() == 'windows' else '-c 1 -W 1'
        cmd = f'ping {params} {ip}'
        
        proc = await asyncio.create_subprocess_shell(
            cmd,
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE
        )
        await proc.communicate()
        
        return ip if proc.returncode == 0 else None
    except:
        return None

async def scan_network() -> Tuple[List[str], List[str]]:
    # 获取网络信息
    ip_addr, netmask = get_network_info()
    network = ipaddress.IPv4Network(f'{ip_addr}/{netmask}', strict=False)
    
    print(f"正在扫描网段: {network}")
    
    # 创建所有主机的检测任务
    all_hosts = [str(ip) for ip in network.hosts()]
    tasks = [check_host(ip) for ip in all_hosts]
    results = await asyncio.gather(*tasks)
    
    # 过滤有效IP和未使用IP并排序
    active_hosts = sorted(
        [ip for ip in results if ip],
        key=lambda x: int(ipaddress.IPv4Address(x))
    )
    
    inactive_hosts = sorted(
        [ip for ip in all_hosts if ip not in active_hosts],
        key=lambda x: int(ipaddress.IPv4Address(x))
    )
    
    return active_hosts, inactive_hosts

def main():
    try:
        # 运行异步扫描
        active_hosts, inactive_hosts = asyncio.run(scan_network())
        
        # 输出结果
        print("\n已使用的IP地址:")
        for host in active_hosts:
            print(host)
            
        print("\n未使用的IP地址:")
        for host in inactive_hosts:
            print(host)
            
    except Exception as e:
        print(f"发生错误: {e}")

if __name__ == "__main__":
    main()
