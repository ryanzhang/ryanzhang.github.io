---
layout: post
title:  "Published a blog how to handle 100k decision table in drools"
date:   2021-3-1

desc: "How to handle 100k decision table rows in Drools?"
keywords: "blog, performance"
categories: [Work]
tags: [appdev, drools, mw]
icon: icon-html
---
# 这篇文章发表在
## 摘要
TLDR;

How to handle 100k decision table rows in Drools?
When handling large rows of decision tables， one of the pain points is performance. In this article, I prepared a prototype setup to a simple scenario to simulate the large decision table use case and provided three solutions to utilize drools ( a rules oriented application framwork). I would focus on the decision table rule execution performance.

For the sake of explanation of the core concept of problem solving, I prepared two decision tables 10k & 100k row data to simulate decision making procedure usage in rules application.

I provide 3 different solutions in three git branches, for coding fans, feel free to jump directly into the following github links and check the code.
* [rule-template-solution](https://github.com/ryanzhang/drools-bigtable/tree/rule-template-solution) — Use Rule Template + XLS raw format decision table
* [precompile-rule-solution](https://github.com/ryanzhang/drools-bigtable/tree/precompile-rule-solution) — Use Kie-Maven-Plugin to precompile Formatted Drools Decision Table
* [row-as-fact-solution](https://github.com/ryanzhang/drools-bigtable/tree/row-as-fact-solution) — Use Large row data as Fact instead of Rules as a solution;

If you are interested in this topic, let me guide you dive into the details.
```
## Medium: 
* https://medium.com/nerd-for-tech/how-to-run-100k-rules-in-drools-7b9308e75687
* https://medium.com/nerd-for-tech/how-to-handle-100k-rows-decision-table-in-drools-part2-2b7fb4de3532 
* https://medium.com/nerd-for-tech/how-to-handle-100k-rows-decision-table-in-drools-part3-a185641a905e

## Dzone:
https://dzone.com/articles/how-to-handle-100k-rows-decision-table-in-drools-1


