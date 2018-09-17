var express = require("express");

var app = new express();

// 获取得到的字母
app.get('/:key',function(req,res){
    // console.log(req.headers);
    console.log(req.params.key);
    res.send("hello world");
});

app.listen(3000,function(){
    console.log('listening on port 3000!');
});