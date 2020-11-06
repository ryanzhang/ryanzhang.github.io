# Ryan Zhang Page
This page site is used to collect some of my activity and information in internet 

- Revise config 配置修改: _config.yml
- Revise Slides Configuration 修改Slides默认模板: _layouts/reveal.html
- Add Slides goto  _slides/
- Add blog goto _post/

中文说明:
poem的样式定义在_includes/index_head.html中 

静态页面的模板入口是在 
index.html
slides/*.html
blog/*.html
中 ， 其中**permalink"定义了最终生成的html的路径

landing配置内容是在 data/landing.yml中

静态页面生成顺序是
index.html -> layout/blog.html -> 内容render ->调用动态数据 site, data, 这些


# How to build & Run
## Install ruby and ruby-dev
dnf install ruby ruby-devel
or 
ruby -v
You might need to install gcc-c++ as well

## Install github-pages
gem install github-pages

## 运行
1) bundle exec jekyll build
2) bundle exec jekyll serve

Centos如何ruby
https://tecadmin.net/install-ruby-latest-stable-centos/

or 

* bundle exec jekyll s --host=10.72.12.44 --port=80 
_80 needs root permission_
* bundle exec jekyll build --incremental --watch

# Description

## Upstream 
https://github.com.cnpmjs.org/jarrekk/Jalpc

## Technical stack
* Jekyll
* Jalpc
* Reveal.js

# Feature added
* Writing md markdown file , Get Online presentation slide 
* Online resume template
* Writing md markdown file, Get pretty Blog artical

