---
layout: post
title:  "怎么做才能为您的PaaS节省IT成本"
date:   2020-11-08
desc: ""
keywords: "container, business, cost saving"
categories: [Work]
tags: [container,  value]
icon: icon-html
---
# 直接节省资源
##  选用更轻量的操作系统，基础镜像
要记住容器不是一个完整的操作系统，而是一些必要的OS文件 可以很小的。
## 直接裸机部署
省去了Hypervisor那一层软件，并且多份的省去了full os 所占的资源。 

## 使用更加轻量的开发工具
使用比如Quarkus这样的现代化微服务框架，可以把Java程序直接编译微native binary运行于容器之上, 摆脱JVM的困扰

## 使用Serverless部署架构
不用的时候不启动，或者动态扩容

## 增加资源利用率
一方面是可以很容易提高部署密度，

另一方面容器编排更加只能的规划资源使用. 可以根据机器资源使用情况， 更加合理的Schedule容器的部署


# 节省软件开销
## 容器技术是基于Linux 也就是开源的
虚拟机技术有的是开源的，有的不是， 企业里面用的比较多的还是VMware
容器技术，选者就多很多，价格也要便宜很多
当然如果虚拟机上再加容器编排，价格也不便宜

好在，可以直接再裸机上部容器
## 单体转微服务
伴随这容器化，一般企业会将单体转向微服务， 这里面隐含了一个IT费用转变，往往是由大的应用服务器的很多功能 转向PaaS平台资源
由于上面提到的很多基础功能，和原因， 应用服务器上面的IT开销就可以节省下来。

# 节省时间
时间就是金钱，节省了时间，就是节省了金钱
## Devops
容器化技术赋予了现代化DevOps全新的生命， CI/CD 以及基础设施代码化，无疑重构了整个IT的整体规划；节省了大量的时间，加速了效率
## 开发和运维的管理成本以及沟通成本
容器是一种自包含，自部署的一种软件形式；这解决了Dev -> Ops很大的沟通和协调问题。
## 运维简单
容器以及容器编排技术解决了软件升级、运维、自修复问题；大大节省了企业运维人员的时间 并且保证了软件的健壮性
## 容器化技术使得 统一开发环境成为可能
增加质量 也是节省金钱
