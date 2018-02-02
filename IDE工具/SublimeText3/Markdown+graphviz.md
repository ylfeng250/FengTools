## 下载安装Graphviz

官网链接 http://www.graphviz.org/。在下使用的是Windows,安装完成之后把 `bin` 目录加入环境变量，在`CMD`中用`dot -V`检验时候安装配置完毕

## 安装插件

安装插件能够实现预览,然而在windows上安装插件没有什么软用

* GraphvizPreview
* Graphvizer

手动解决
1.下载离线插件 [https://github.com/munro/SublimeGraphvizPreview/archive/master.zip](https://github.com/munro/SublimeGraphvizPreview/archive/master.zip )
2.打开Preferences -> Packages Settings-> Packages Control -> Settings User，来确认一下installed_packages没有GraphVizPreview。并且增加”remove_orphaned”: false防止Sublime Text 把手动安装的插件包给删除了。
下面是我的配置文件

```json
{
	"bootstrapped": true,
	"in_process_packages":
	[
	],
	"installed_packages":
	[
		"A File Icon",
		"Anaconda",
		"AutoFileName",
		"Boxy Theme",
		"Markdown Extended",
		"Markdown Preview",
		"MarkdownEditing",
		"MarkdownLivePreview",
		"Monokai Extended",
		"Package Control",
		"SideBarEnhancements",
		"SublimeREPL",
		"SublimeTmpl",
		"Table Editor",
		"Terminal"
	],
	"remove_orphaned": false,//防止sublime将手动安装的插件删除
}

```
3.打开Preferences -> Browse Packages…进入到Sublime Text的插件包下Packagas。 
4.解压zip文件到Packagas下，并且更改文件夹SublimeGraphvizPreview-master为GraphVizPreview。
5.重启
>之后用鼠标选中需要渲染的代码段按`shift+win+g`即可在pdf中查看绘制的图像

## 语法

1.无向图

```
graph graphname{
	a -- b -- c;
	b -- d;
}
```
![](https://upload-images.jianshu.io/upload_images/1026876-7d06474294723e0d.png!web?imageMogr2/auto-orient/strip%7CimageView2/2/w/179)

2.有向图

```
digraph graphname{
	a -> b -> c;
	b -> d;
}
```
![](https://upload-images.jianshu.io/upload_images/1026876-25acc35b080b22db.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/179)

3.属性

```
//DOT语言中，可以对节点和边添加不同的属性。

digraph graphname {
    //节点的属性，节点的名称
    a [lable = "Foo"];

    //节点的属性，节点的形状
    b [shape = box];

    //边的属性，边的颜色
    a -> b -> c [color = blue];

    //边的属性，边的线状
    b -> d [style = dotted];
}
```
4.基本图形

```
digraph G {
//把图片的尺寸设为4inch * 4inch
size = "4,4";
main [shape = box];

//边的重要程度，默认是1
main->parse [weight = 8];
parse->execute;

//点状线
main->init[style = dotted];
main->cleanup;

//连接了两条线
execute->{make_string;printf}
init->make_string;

//把边的默认颜色设为red
edge [color = red];
main->printf [sytle=bold, label = "100times"];

//节点的名称
make_string [label = "make a\nstring"];

//设置节点的默认属性
node [shape=box,style =filled,color=lightgrey];
execute->compare;
}

```
![](https://upload-images.jianshu.io/upload_images/1026876-4ea0421f32fdfa97.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/341)

5.多边形

```
digraph G{
a -> b -> c;
b -> d;

/* 形状为多边形，边数为5，外框为3条，颜色为淡蓝，样式为填充 */
a [shape = polygon, sides = 5, peripheries = 3, color = lightblue, style = filled];

/* 形状为多边形，边数为4，角的倾斜度为0.4，内容为hellow world*/
c [shape = polygon, sides = 4, skew = 0.4, label = "hello world"];

/* 形状为倒三角，整体旋转30度 */
d [shape = invtriangle,orientation = 30];

/* 形状为多边形，边数为4，扭曲度为0.7 */
e [shape = polygon, sides = 4, distortion = 0.7];
}
```
![](https://upload-images.jianshu.io/upload_images/1026876-6cc94a6ea0465146.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/349)

6.数据结构

复杂的标签

```
digraph structs {
/* 把节点的默认形状设为矩形record，默认的是圆角矩形Mrecord */
node [shape = record];

struct1 [label = "left|middle|right"];
struct2 [label = "one|two"];
struct3 [label = "hello\nworld|{b|{c|d|e}|f}|g|h"];

struct1 -> struct2;
struct1 -> struct3;
}

```
![](https://upload-images.jianshu.io/upload_images/1026876-ee4fc8ae6553bcd3.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/353)

```
graph picture {
//这幅图的名字
label = "I love you";

//图名字的位置在bottom，也可以是t
labelloc = b;

//图名字的位置在left，也可以是r
labeljust = l;

edge[decorate = true];

C -- D [label = "s1"];
C -- E [label = "s2"];
C -- F [label = "s3"];
D -- E [label = "s4"];
D -- F [label = "s5"];

edge[decorate = false, labelfontcolor = blue, fontcolor = red];
C1 -- D1 [headlabel = "c1",taillabel = "d1",label = "c1 - d1"];
}

```
![](https://upload-images.jianshu.io/upload_images/1026876-5c14d725e55c75c9.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/324)

行列对齐

```
digraph html {
rankdir = LR;
{
node[shape = plaintext];
1995 -> 1996 -> 1997 -> 1998 -> 1999 -> 2000 -> 2001;
}
{
node[shape = box, style = filled];
WAR3 -> Xhero -> Footman -> DOTA:
WAR3 -> Battleship;
}
{rank = same; 1996; WAR3;}
{rank = same; 1998; Xhero; Battleship;}
{rank = same; 1999; Footman;}
{rank = same; 2001; DOTA;}
}

```
![](https://upload-images.jianshu.io/upload_images/1026876-f6b626cba7c99226.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/550)

二叉树

```
digraph G {
label = "Binary search tree";
node [shape = record];

A [label = "<f0>|<f1>A|<f2>"];
B [label = "<f0>|<f1>B|<f2>"];
C [label = "<f0>|<f1>C|<f2>"];
D [label = "<f0>|<f1>D|<f2>"];
E [label = "<f0>|<f1>E|<f2>"];
F [label = "<f0>|<f1>F|<f2>"];
G [label = "<f0>|<f1>G|<f2>"];

A:f0 -> B:f1;
A:f2 -> C:f1;
B:f0 -> D:f1;
B:f2 -> E:f1;
C:f0 -> F:f1;
C:f2 -> G:f1;
}
```
![](https://upload-images.jianshu.io/upload_images/1026876-e1939ea611eb5c4f.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/433)

哈希表

```
digraph G{
nodesep = .05;
rankdir = LR;

node [shape = record,width = .1,height = .1];
node0 [label = "<f0>|<f1>|<f2>|<f3>|<f4>|<f5>|<f6>|",height = 2.5];

node [width = 1.5];
node1 [label = "{<n>n14|719|<p>}"];
node2 [label = "{<n>a1|805|<p>}"];
node3 [label = "{<n>i9|718|<p>}"];
node4 [label = "{<n>e5|989|<p>}"];
node5 [label = "{<n>t20|959|<p>}"];
node6 [label = "{<n>o15|794|<p>}"];
node7 [label = "{<n>s19|659|<p>}"];

node0:f0 -> node1:n;
node0:f1 -> node2:n;
node0:f2 -> node3:n;
node0:f5 -> node4:n;
node0:f6 -> node5:n;
node2:p -> node6:n;
node4:p -> node7:n;
}

```
![](https://upload-images.jianshu.io/upload_images/1026876-ccb8b8d1805cf981.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/421)

流程图

```
digraph G{
subgraph cluster0 {
node [style = filled,color = white];
style = filled;
color = lightgrey;
a0 -> a1 -> a2 -> a3;
label = "process #1";
}

subgraph cluster1 {
node [style = filled];
b0 -> b1 -> b2 -> b3;
label = "process #2";
color = blue;
}

start -> a0;
start -> b0;
a1 -> b3;
b2 -> a3;
a3 -> a0;
a3 -> end;
b3 -> end;
start [shape = Mdiamond];
end [shape = Msquare];
}

```
![](https://upload-images.jianshu.io/upload_images/1026876-481d4d91c80089f5.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/299)
## 参考

[Sublime Text预览Graphviz图](https://www.chenyudong.com/archives/sublime-text-graphviz-preview.html)
[程序员绘图利器 — Graphviz](https://www.jianshu.com/p/d18a7b7afa83)
[Sublime Text + Graphviz + Dot = 有向图](http://blog.csdn.net/yuliying/article/details/68715123)