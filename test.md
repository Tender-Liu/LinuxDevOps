接下来编写第四部分，ingress-nginx的语法学习，与练习
1. 先介绍语法，结构
2. 路由匹配有哪些方法
3. 怎么匹配service
语法介绍清清楚楚

---
apiVersion: v1
kind: Service
metadata:
  name: service-admin3-server
  namespace: shiqi
spec:
  ports:
    - name: http
      port: 8080
      protocol: TCP
      targetPort: 8080
  selector:
    app: pod-admin3-server
  type: ClusterIP


---
apiVersion: v1
kind: Service
metadata:
  name: service-admin3-ui
  namespace: shiqi
spec:
  ports:
    - name: http
      port: 80
      protocol: TCP
      targetPort: 80
  selector:
    app: pod-admin3-ui
  type: ClusterIP

---
apiVersion: v1
kind: Service
metadata:
  name: service-light-year-admin-template
  namespace: shiqi
spec:
  ports:
    - name: http
      port: 80
      protocol: TCP
      targetPort: 80
  selector:
    app: pod-light-year-admin-template
  type: ClusterIP


---
apiVersion: v1
kind: Service
metadata:
  name: service-stars-emmision
  namespace: shiqi
spec:
  ports:
    - name: http
      port: 80
      protocol: TCP
      targetPort: 80
  selector:
    app: pod-stars-emmision
  type: ClusterIP
我准备了4个service
域名分别：
1. shiqi.admin.labworlds.cc 给admin3 前后端
2. shiqi-stars.labworlds.cc
3. shiqi-light.labworlds.cc
使用命令自己生成证书
  mkdir /root/shiqi.admin.labworlds.cc
  cd /root/shiqi.admin.labworlds.cc
sudo openssl req -x509 -nodes -days 365 -newkey rsa:2048 \
    -keyout /root/shiqi.admin.labworlds.cc/tls.key \
    -out /root/shiqi.admin.labworlds.cc/tls.crt \
    -subj "/CN=touch.shiqi.com"

将输出的内容都给我按照域名的名字创建对应的secret-shiqi-admin-labworlds-cc
由于点实在特殊我们只能用-