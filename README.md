# python-search-sharelink

查找百度网盘有效的分享链接

## 运行

> python > 2.6

``` python
python index.py
```

## 原理

采用`urllib`模块，通过检查http状态，判断链接是否有效。

也因此会存在一个问题，http状态为`302`时，也判定位有效。

## TODO

- 使用`urllib2`替换`urllib`
- 构建`url`算法需要强化
- 指定内容查找链接

