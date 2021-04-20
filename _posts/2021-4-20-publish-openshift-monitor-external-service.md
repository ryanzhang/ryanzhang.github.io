---
layout: post
title:  "Utilize OpenShift to monitor external service"
date:   2021-4-19

desc: "OpenShift Monitoring, Use Cloud native monitoring for your legacy services"
keywords: "blog, OpenShift 4, Monitoring"
categories: [Work]
tags: [appdev, openshift, monitoring]
icon: icon-html
---
# 这篇文章发表在
## 摘要
TLDR;
Openshift 4 provided great metrics monitor suites, we can use them to monitor and create dashboard for both infra and application layer services; What’s more we can leverage that to manage external services and infra as well.

The benefits why I want to address this issue are:

Establish and maintaining a sophisticated monitoring solution can be very hard and time-consuming.

The monitoring components are almost coming free with embedded in Openshift. They are managed by Openshift Cluster Monitoring operator which is stable, self-healing and well-structured.
Manage and scale infra configuration like monitoring components in OpenShift is easier than doing it in VM, because it’s declarative nature and we can even manage them by gitops.
Of course if you have both OpenShift Platform to manage container world and VM world to manage other business, you don’t have to manage two complicated Monitoring solutions for time and cost saving.

## Medium: 
* https://ryanzhangcheng.medium.com/utilize-openshift-to-manage-external-services-metrics-1a9fcfc8a746



