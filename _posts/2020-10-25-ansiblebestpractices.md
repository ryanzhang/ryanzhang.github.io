---
layout: post
title:  "Ansible Best Practices"
date:   2020-10-23

desc: "Ansible best practices"
keywords: "test, paas, kubernetes"
categories: [Work]
tags: [paas, test]
icon: icon-html
---
 # 总的原则-PRD原则
* Productivity Over Complexity
        
* Readability Over Best Practices

    运维脚本可读性应该放在第一位；要把代码当作文档一样来维护; 有的时候是可以牺牲一些代码上的原则；本质上不能像编写程序一样，去编写Ansible 开发人员很容易把Ansible脚本写的非常复杂，而不易维护的注意事项
* Declaritive Over Imperative

    要按照声明式的方式 去编写；而不是命令式； Ansible脚本需要是幂等，并且他的目标是一种配置状态;

* 1. 代码树

    ansible code 是一棵代码树；维护代码的一些模式同样适用于ansible code. 比如: 先简单，后重构; 统一的风格；
    一个Playbook干一件事情, 就像一个class文件，一个task就像一个function一样；单一原则，简单可读;
* 2. 成双的Inventory， 和二分的变量-变量和逻辑要分离

    这里指inventory不要用IP，而是有意义的名字 +IP或域名；并且要分组；
    
    变量和逻辑要分离；不要柔到一起，变量要内聚有利于抽象成role

* 3. Role的三板斧
    * 减少不必要依赖，内聚
    * 依赖明确声明到requirements.yml 使用ansible-galaxy install -r requirements.yml
    * Role总是先与task执行，如果要控制顺序，使用pre_tasks, post_tasks

* 4. Jinjia模板 

    切忌写的太复杂，切忌使用复杂逻辑和循环;
