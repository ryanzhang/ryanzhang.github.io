---
layout: post
title:  "Monitoring Github Page Traffic via Google Analytics"
date:   2020-09-16
desc: ""
keywords: "gh-page, google-analytics"
categories: [Life]
tags: [gh-page,google-analytics]
icon: icon-html
---
# Problem:
I want to know the traffic about my github page.

# Solution:
It's pretty straight forward since I used jekyll framework.
So all you need to do is to add your google analitics trackid into 
_config.yml
```yaml
# analytics
## google analytics
ga:  # if you wanna this feature, go to https://www.google.com/analytics/ to get your configuration; if not, comment following line.
  id: your_tracking_id
```

# Note:
