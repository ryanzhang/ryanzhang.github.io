---
layout: post
title:  "Set your linux route to access both side of firewall-通过设置Route如何同时访问防火墙内网和外网"
date:   2020-09-24
desc: ""
keywords: "proxy, firewall, httpproxy"
categories: [Life]
tags: [network,proxy]
icon: icon-html
---

# 要解决的问题
要么访问内网，要么访问外网， 来回切换很麻烦。 一般有两种情况

 * 企业里面经常有防火墙，连接网线后 就是内网 无法访问外网。 

# 方案
下面命令 使用与Linux
192.168.41.254是有线网卡 连接的网关
172.31.0.0/16是指目标网段 走有线


```bash
#使用ip route查看本机路由表
ip route
default via 192.168.2.1 dev wlp4s0 proto dhcp metric 600  <-这个是默认路由表 经过无线网卡
10.0.0.0/8 via 10.72.8.1 dev tun0 proto static metric 50  <- 10.0.0.0/8网端走的是vpn 虚拟网卡tun0通道
10.72.8.0/22 dev tun0 proto kernel scope link src 10.72.8.19 metric 50

#使用route add命令添加特点网卡 经过无线网卡网关
sudo route add -net 172.31.0.0/16 gw 192.168.41.254 enp0s31f6
sudo route add -net 172.30.0.0/16 gw 192.168.41.254 enp0s31f6
sudo route add -net 192.168.26.0/24 gw 192.168.41.254 enp0s31f6
sudo route add -net 10.150.175.0/24 gw 192.168.41.254 enp0s31f6

```


