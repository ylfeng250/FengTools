## 预览插件

* MarkdownLivePreview 

实现实时预览,在Preferences中添加下面的配置

```
"markdown_live_preview_on_open": true
```

* Markdown Preview

这个插件可以设置插件，然后在浏览器中查看Markdown渲染之后的效果
配置如下
1.设置快捷键`alt+m`
```json
{ 
    "keys": ["f6"], 
    "command": "markdown_preview", 
    "args": { 
                "target": "browser"
            } 
}
```
2.设置语法高亮和mathjax支持和显示浏览器为Chrome

```json

{
    "browser": "chrome",//社遏制显示的浏览器
  
    "enable_mathjax": true,//支持公式

    "enable_highlight": true,//支持语法高亮

    "enable_uml": true,//支持UML
}

```

## 语法高亮
* Monokai Extended & Markdown Extended
Markdown 格式在 Sublime 中默认无高亮，很多主题也不支持 Markdown 的高亮（包括 Markdown 代码块内的代码），`Monokai Extended` 和 `Markdown Extended` 是一套解决方案。

插件的安装方式是 `Shift + Command + P` 调出 `Command Palette`，输入 pci（模糊匹配），找到 `Package Control: Install` `Package`、回车，输入插件名称、回车，等待安装。

注意需要将 Markdown 的文件格式与 Markdown Extended 这种语法关联起来，做法是点击 Sublime 右下角文档格式，在列表最上方名为 Open all with current extension as 二级列表中选择 Markdown Extended。一种临时设置方式可以是 `Shift + Command + P` 调出 `Command Palette`，输入 `ssm`，选择 `Set Syntax: Markdown Extended`。

## 表格 Table Editor
用于编辑表格的工具。
键入表格是个体力活，Table Editor 可以帮助我们减轻工作量
`Ctrl + Shift + P` 输入 `teecv`，进入`Enable`模式
详细的请查看 `Preferences -> Package Settings -> Table Editor -> README`

## 论文
在查找资料的过程中发现可以用 Sublime + Markdown 写论文，就跟着学了一把。

`AcademicMarkdown` 通过在 Markdown 文档中添加一定的信息，具体说是文件头，来帮助我们将 Markdown 文档渲染为符合指定论文格式的文章。以下文件头摘自插件作者给出的 样例。

```
title: A sample paper
author: Donald Duck
date: October 1, 2014
csl: /Users/frank/Documents/My Markdown/sample-paper/chicago.csl
abstract: Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enimad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
```
`csl` 是论文模板格式，更多格式可在 [Zotero Style Repository](https://www.zotero.org/styles) 寻找。

`Academic` 还允许指定 bib 文件，在 Markdown 文档内添加引用，格式是 `@citation_key`， [Citer](https://github.com/mangecoeur/Citer) 暂时我还没有用过

[Pandoc](https://github.com/tbfisher/sublimetext-Pandoc)可将`AcademicMarkdown`编译成论文

## 主题
`Boxy Theme`安装主题插件之后，我选择的是`Boxy Monokai`这一款
## 参考

[Sublime for Markdown](http://blog.csdn.net/u014015972/article/details/50468584)
[Sublime Text 安装 Markdown Preview](https://www.jianshu.com/p/c48b03f78028)
[SublimeTableEditor](https://github.com/vkocubinsky/SublimeTableEditor)
[在 Sublime 中配置 Markdown 环境](http://frank19900731.github.io/blog/2015/04/13/zai-sublime-zhong-pei-zhi-markdown-huan-jing/#pandoc)
[Sublime插件：Markdown篇](https://www.jianshu.com/p/aa30cc25c91b)