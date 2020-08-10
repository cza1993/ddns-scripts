# ddns脚本
内容:

```
1.支持阿里云和dnspod的域名
2.支持ipv4和ipv6
3.均尝试两种方式获取当前公网ip
```



### 使用方法：

aliddns.py  基于aliyun sdk

```
1.有个阿里云上购买或者托管给阿里云进行解析的域名
2.获取阿里云AccessKey id和Secret，如果用子账号的AccessKey也需要保证有域名解析的相关权限(在阿里云控制台-右上角图标-AccessKey管理)
3.python3的环境，需要安装aliyun-python-sdk-core和aliyun-python-sdk-alidns两个库，可以用pip安装
4.根据脚本注释提示修改相应内容，然后设置一个定时任务定期执行
```



dnspod.py

```
1.有个dnspod上购买或者托管给dnspod进行解析的域名
2.登录https://support.dnspod.cn/Kb/showarticle/tsid/227获取id和token
3.python3环境，保证requests库安装
4.根据脚本注释提示修改相应内容，然后设置一个定时任务定期执行
```



### 更新说明：

##### 2020.8.10：

1. 更新支持dnspod
2. 更新说明文档
