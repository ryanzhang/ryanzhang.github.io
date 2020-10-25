---
layout: post
title:  "微服务实现原则三三两两"
date:   2020-10-24
desc: ""
keywords: "MSA, microservice, 12factor"
categories: [Work]
tags: [microservice]
icon: icon-html
---
# 微服务十二条金规

"微服务实现有什么最佳实践，和原则? "

"怎样对微服务进行划分，设计?"

这是我在做企业客户咨询工作中经常遇到的问题。 我今天就来聊一下第一个问题. 

如果对第二个问题感兴趣请移步
 [DDD part1](https://ryanzhang.github.io/work/2020/09/02/DDD-DomainDriveDesignOrDeadlineDrivenDesign.html)  [DDD part2](https://ryanzhang.github.io/work/2020/09/12/DDD-SoftwareDesign-A-TwoPersonJob.html)。

 让我们先从现代应用的12条金规说起:
 https://12factor.net/

 虽然这个12条金规2011年就已经随着互联网产业的兴起而被提出，但对于企业客户，以及企业软件开发现状，好像也不是尽人皆知。 然后随着容器化技术的普及，以及PaaS平台的大量采纳，现代应用开发的一些模式，和软件早已经渗透到各行各业的软件开发当中，已经不再是互联网弄潮儿的独门绝技了。只是你问起企业软件领域的开发人员，你们知道微服务12条金规吗？很多人还是会感到陌生。

 12条金规总结的非常好，但是缺点是不太容易记住。 我总结了一个三三两两的顺序去理解和记忆，这样不容易遗漏，并且可以比较系统的对照自己的微服务开发的问题与改进。

# 三三两两-3C 3D， 2B 2P

## 3C
### CodeBase
一个微服务一个代码仓库。 同一个服务不同的环境的部署也是共用的一个仓库。
微服务的运维、编译、自动化程序以及配置、依赖等等都应该放在一个仓库里面。 尽可能少的让一个微服务分散到两个或者以上的代码仓库中。

当然任何规则都有特例， 高级玩家可以无视这些规则，比如Google, Facebook他们经常一个repo容纳很多的微服务，模块。但是交付出很多的部署单元。


### Config
配置两个方案

环境变量

配置文件

### Concurrency
平发靠复制进程

## 3D
### Dependencies
依赖要明确指出。

必须很简单能够启动，运行，在任何环境。 不能有各种隐含依赖

必须能够 "just work", "work out of box"。 人类对于懒惰的渴望已经是永无止境的，多一步都不行。

### Deposable
像日抛型商品，或者纸杯一样, 它应该是很容易安全抛弃，并且很容易用新实例代替的。
这里要求两个指标：

启动容易，快，不冲突。尤其是要初始化数据的时候。

关闭要优雅，就是关闭的时候要考虑用户的请求得到妥善处理，不能说停就停了。

### Dev/prod parity
## 2B
### Backing services
状态应该隔离到 Backing services当中，比如数据库，或者能够存储数据库的微服务。
或者nosql数据库
### Build,Release,Run
DevOps, CICD
### 2P
### Processes
无状态、share-nothing规则
Cache应该放到Backing services当中，不应该设计在Process里面。

### Port Binding
一个微服务 应该将自己的服务可以绑定到一个port上面，这样以便于别人可以通过服务发现访问和使用。 
这并不限于http服务。

现代容器技术 也专门有一项就是将容器的端口暴露出去然后容器内部映射到服务当中。

并且这一条也要求我们的服务是自包含的，也就是说一个服务就要对应一个(或者多个端口也可以)服务端口。 像以前把多个应用程序 部署到tomcat中 然后统一通过8080端口，只是通过访问路径的方式是一种反模式。 但是现在springboot jar包方式将tomcat自包含到应用中就使得这一条原则得到满足。

# 另外两条跑哪去了?
你看，没有忘记吧，我们中国人数学是最好的， 三三两两为十， 十二条金规还有两条
## Logging
## Admin Processes

To Be Continue




