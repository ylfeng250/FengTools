## 下载安装
地址:http://www.sublimetext.com/

## 安装package Control

打开->Preferences->package Control

**相关命令介绍**
* `install` 显示安装列表
* `List Packages` 显示所有已安装的插件
* `Remove Packages` 移除一个指定的插件
* `Upgrade Package` 更新一个指定的插件
* `Upgrade/Overwrite All Packages` 更新所有已安装的插件

## 安装插件
`Ctrl+shift+p`打开`package control`输入`install`

* 1.SideBarEnhancements => 侧边栏管理
* 2.Anaconda （最强的Python IDE插件）http://damnwidget.github.io/anaconda/
* 3.SublimeTmpl =>新建模板文件的时候添加
* 4.Terminal => 打开一个命令窗口 `ctrl+shift+t`
* 5.SublimeREPL => 直接运行当前文件，可以方便调试
* 6.AutoFileName => 自动补全文件名和文件路径
## Anaconda使用
设置自己的配置文件
```
{
	"python_interpreter": "C:/Python36-32/python.exe", //Python路径

	"complete_parameters": true,//是否匹配必要参数

	"complete_all_parameters": false,//是否匹配所有参数

	"suppress_word_completions": true,//禁止代码补全

	"suppress_explicit_completions": false,//禁止精确补全

	"auto_formatting": true,//代码格式检查
	"pep8_ignore":
    [
        "E501"
    ],  // 忽略每行长度的限定，默认是79个字符
}
```
* `Goto Definitions` 能够在你的整个工程中查找并且显示任意一个变量，函数或者类的定义。
* `Find Usage` 能够快速的查找某个变量，函数或者类在某个特定文件中的什么地方被使用了。
* `Show Documentation`： 能够显示一个函数或者类的说明性字符串(当然，是在定义了字符串的情况下)

## SublimeTmpl 配置 && SublimeREPL 配置
在`user-setting`中配置
```
{  
    "disable_keymap_actions": false, // "all"; "html,css"  
    "date_format" : "%Y-%m-%d %H:%M:%S",  
    "attr": {  
        "author": "no96",  
        "email": "1119030015@qq.com",  
        "link": "https://github.com/No-96"  
    }  
}
```
绑定快捷键`key-building-users`
```
[
    {
        "caption": "Tmpl: Create python", "command": "sublime_tmpl",  
        "keys": ["ctrl+alt+n"], "args": {"type": "python"}  
    },
    {
        "keys": ["f5"],//按F5直接运行当前文件
        "caption": "SublimeREPL: Python - RUN current file",
        "command": "run_existing_window_command",
        "args": {
            "id": "repl_python_run",
            "file": "config/Python/Main.sublime-menu"
        }
    }
]
```
之后只要按`ctrl+alt+n`就可以创建一个python模板了

## 常用快捷键
```
Ctrl + shift + n 新建窗口
ctrl + shift + w 关闭窗口
Ctrl + n 新建文件
Ctrl + w 关闭当前文件

ctrl + tab 在两个标签之间跳转
ctrl +　j 在某行末尾敲该快捷键，会将下一行合并上来
ctrl + shift + d 将当前行复制到下一行
ctrl + shift + up/down 上下交换行
ctrl + ]/[  当前行缩进一个级别/取消缩进
ctrl + l 选择当前行
Ctrl+Shift+l 先选中多行，再按下快捷键，会在每行行尾插入光标，即可同时编辑这些行。
ctrl + d 选中一个后，按此快捷键可以同时选中另一个，同时多了另一个光标
ctrl +　enter 在下面新开一行
ctrl +　shift + enter 在上面新开一行

Ctrl+Shift+K 删除整行。
Ctrl+Shift+[ 选中代码，按下快捷键，折叠代码。
Ctrl+Shift+] 选中代码，按下快捷键，展开代码。
Ctrl+K+0 展开所有折叠代码。
Ctrl+← 向左单位性地移动光标，快速移动光标。
Ctrl+→ 向右单位性地移动光标，快速移动光标。
shift+↑ 向上选中多行。
shift+↓ 向下选中多行。
Shift+← 向左选中文本。
Shift+→ 向右选中文本。

Alt+Shift+1~4 窗口左右分1-4屏，恢复默认1屏（非小键盘的数字）
Alt+Shift+5 等分4屏
Alt+Shift+8 垂直分屏-2屏
Alt+Shift+9 垂直分屏-3屏

Ctrl + g，输入行号，可以快速跳转到该行。
Ctrl+K+B 开启/关闭侧边栏。

Ctrl + \  打开控制行
Ctrl + Shift + P 打开命令面板
```

## 参考

[sublime配置python篇](https://segmentfault.com/a/1190000007967722)
[sublime配置使用教程整理](https://segmentfault.com/a/1190000004463984)
[sublime配置分析与我的分析](http://blog.csdn.net/hexrain/article/details/13997565)
