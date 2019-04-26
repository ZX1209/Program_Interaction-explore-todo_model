# server socket
# server task

# local

假设 ,最后都归结于这几个api
add
update
delete

show

本地的操作就是
命令行解析,于操作

类似
if add:
    add
elif update:
    update
elif delete:
    delete

但加了其他终端后,,嗯,,加入任务模型

tasks.append(task)


一个线程本地处理,,另一个线程添加远程任务
类似
for task in tasks:
    for server in servers :
        server.task.append(task)

    execute(task)


threads.Thead(target = server.run())...

    for task in tasks:
        for server in servers:
            send(server.task[task])


new connection and servername

# 节点 还是 列表呢??

# 还是先假设一个离线应用,而不是,分布式系统把..

# server
listen  clients and execute(task)


# client


# 判断数据是否同步??
client name


# socketserver 是一个一次性的服务器框架呢..
# 虽说也可以啊..


所以,服务器上用sock接受请求??还是http,,还是都是,,
嗯...
cli,
编程接口.算是socket 吧..
本地,还是网络???
http接口...

os.system??全cli??

同一个数据库就好,,或者是,,大数据库..就好...

pull,push...

push ,pull??
只能假设是小数据啊...


# 比较大的数据呢.???
同个鬼步啊...

hash 吗???


# 长连接
心跳

## server 
accept 
lists
select
delete

## client
connect
heart



