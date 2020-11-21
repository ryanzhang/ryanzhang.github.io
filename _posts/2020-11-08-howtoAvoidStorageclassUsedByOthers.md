---
layout: post
title:  "如何保证Storage Class不被别的项目使用"
date:   2020-11-08
desc: ""
keywords: "container, business, cost saving"
categories: [Work]
tags: [container,  value]
icon: icon-html
---
# 即如何把Storage Class绑定到Namespace上面
Storage class是cluster wide资源，正常kubernetes不支持你这么做。

但是可以自己写Operator来坚持你自己的PVC,然后自动去创建这个资源， 已经有人实现了这个方案:
https://github.com/banzaicloud/pvc-operator

