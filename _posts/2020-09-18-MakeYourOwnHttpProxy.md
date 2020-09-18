---
layout: post
title:  "Build your own Http Proxy via Squid(搭建Squid Http Proxy)"
date:   2020-09-18
desc: ""
keywords: "proxy, firewall, httpproxy"
categories: [Life]
tags: [network,proxy]
icon: icon-html
---
# 为什么要搭 http proxy?
  * 我的笔记本可以通过企业vpn 访问外网 但是我的手机需要通过我的电脑访问外网
  * 在客户现场， 我的笔记本可以访问外网，但是我的客户需要通过我的电脑访问外网

# Solution:
> 我的环境是 Fedora 32
## 安装 squid
```bash
sudo dnf install squid
```
## 增加三行配置到 /etc/squid/squid.conf
```
#configure upstream parent proxy
cache_peer squid.xxx.xxx.xxx parent 3128 0 no-query default
cache_peer_domain squid.xxx.xxx.xxx *
never_direct allow all
```
此处squid.xxx.xxx.xxx是外部的http proxy. 也就是我本机安装的squid的上游 proxy. 

所以,假设在局域网中Laptop ip为192.168.2.111, 以手机路由为例,是这样

手机浏览器 -> 192.168.2.111:3128 -> 上游squid 域名(squid.xxx.xxx.xxx):3128 -> 外网 

# 测试
可以通过Laptop 浏览器 配置本机127.0.0.1:3128 作为http proxy进行测试

# 配置手机
以iphone为例

设置->无线网络

<img src="{{ site.img_path }}/blog/http-proxy/1.jpg" width="25%">
<img src="{{ site.img_path }}/blog/http-proxy/2.jpg" width="25%">





