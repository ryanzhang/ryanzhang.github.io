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
### Config
### Concurrency
## 3D
### Dependencies
### Deposable
### Dev/prod parity
## 2B
### Backing services
### Build,Release,Run
### 3P
### Processes
### Port Binding

# 另外两条跑哪去了?
你看，没有忘记吧，我们中国人数学是最好的， 三三两两为十， 十二条金规还有两条
## Logging
## Admin Processes

To Be Continue




