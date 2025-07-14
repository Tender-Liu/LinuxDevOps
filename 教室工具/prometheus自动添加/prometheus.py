import requests
import json

class JumpServerAPI:
    def __init__(self):
        self.base_url = "http://192.168.110.163"
        self.access_key = "dfe7caaa-9150-49f4-868c-f1821fe20719"
        self.secret_key = "RqaMFx9AbqJ7Wl0SaU2KlIjDRlxb4HRSdTTf"
        self.token = self._get_token()

    def _get_token(self):
        """获取JumpServer API token"""
        url = f"{self.base_url}/api/v1/authentication/auth/"
        headers = {
            'Accept': 'application/json',
            'X-JMS-ORG': '00000000-0000-0000-0000-000000000002'  # 默认组织
        }
        data = {
            "access_key": self.access_key,
            "secret_key": self.secret_key
        }
        
        try:
            response = requests.post(url, json=data, headers=headers)
            response.raise_for_status()
            return response.json().get('token')
        except requests.exceptions.RequestException as e:
            print(f"获取token失败: {e}")
            return None

    def get_assets(self):
        """获取资产树中的学员练习主机"""
        if not self.token:
            print("Token未获取，无法执行操作")
            return []

        url = f"{self.base_url}/api/v1/assets/assets/"
        headers = {
            'Authorization': f'Bearer {self.token}',
            'Accept': 'application/json',
        }
        params = {
            'node_id': 'default',  # 这里需要根据实际的节点ID调整
            'search': '学员练习主机',
        }

        try:
            response = requests.get(url, headers=headers, params=params)
            response.raise_for_status()
            assets = response.json()
            
            # 格式化输出资产信息
            for asset in assets:
                print(f"资产名称: {asset.get('hostname')}")
                print(f"IP地址: {asset.get('ip')}")
                print(f"系统平台: {asset.get('platform')}")
                print("-" * 50)
            
            return assets
        except requests.exceptions.RequestException as e:
            print(f"获取资产失败: {e}")
            return []

def main():
    # 创建JumpServer API实例
    js_api = JumpServerAPI()
    
    # 获取资产信息
    assets = js_api.get_assets()
    
    # 将结果保存到文件（可选）
    with open('assets.json', 'w', encoding='utf-8') as f:
        json.dump(assets, f, ensure_ascii=False, indent=2)

if __name__ == '__main__':
    main()

