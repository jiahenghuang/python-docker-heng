#docker日志设置上限
#vim /etc/docker/daemon.json
{
"registry-mirrors":["http://f613ce8f.m.daocloud.io"],
"log-driver":"json-file",
"log-opts":{"max-size":"500m","max-file":"3"}
}

#docker build方法
重启docker服务  sudo service docker restart
关闭docker服务  service docker stop
开启docker服务  service docker start

#build镜像
docker build -t chat-bot:v1.x .
进入 ./chat-bot/目录，sudo docker build .

#运行镜像
sudo docker run -p 127.0.0.1:8080:8080 chat-bot:v1.x
#开机自启动服务
sudo docker run -p 127.0.0.1:8700:8700 --restart=always chat-bot:v1.2
sudo docker run -d -p 10.1.71.252:8700:8700 --restart=always chat-bot:v1.2

#停止镜像运行
sudo docker stop imageid

#删除所有容器
sudo docker rm $(sudo docker ps -a -q)

#测试数据
{"requestId":"123456","message":"亲爱的晚上不好意思这么晚才给你打电话哈，来呼叫你出山了啊啊啊","contextId":"haha","serviceCode":"hehe","reqType":1,"status":"A","describe":"asdfasd","startStamp":1,"requestType":0,"questionId":"single","keywordVersion":"V20190101"}

#查看日志
sudo docker logs --since 30m container-id
sudo docker logs container-id

#
systemctl daemon-reload
systemctl restart docker

#测试网址
http://www.blue-zero.com/WebSocket/

#自动部署
sudo vi /etc/profile
sudo docker run container-id