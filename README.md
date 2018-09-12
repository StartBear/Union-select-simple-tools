# Union select simple tools
Python 2.7  + QT4 
源码在Source里面，比较简单的一个Union Select查询工具

然后使用urllib2发送请求，读取返回值，通过re抓取
http://www.xxxx.com/xxx.php?id=23 order by n
依次低价当response的值与http://www.xxxx.com/xxx.php?id=23不同时，
返回，记下n
然后开始union select 
将<zz>n</zz>带入查询，根据返回值查询
<zz>(*.?)</zz>
记下显示位，进行database,table等关键字查询

最后使用pyinstaller 进行打包成exe
http://www.sut56.com/fuwuview.php?id=10

针对这个网站写的，查询字段那个模块，输入adminName,adminPwd 输出的值我使用了切片，所以查询其他字段的时候可能会显示错误。
