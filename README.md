#### IK分词器自定义词库服务，热更新ES自定义词库。

##### 构建
```
docker build -t dict-server:1.0.0 .
```

##### 部署
```
docker run -d --name my-dict-server -v /host/path/ext_dict:/usr/src/app/static:rw -p 10006:10006  dict-server:1.0.0
```
`/host/path/ext_dict` 替换为宿主机实际es自定义词典文件路径

##### API
* 热更新词库请求
```bash
curl -X POST 'http://127.0.0.1:10006/dict' \
-H 'Content-Type: application/json' \
-d '{
  "dictSource": "hot_search",
  "dicts": [
    "小米15",
    "小米手机",
    "小米手环7"
  ]
}'
```

* 查看自定义词库
```bash
curl -X GET 'http://127.0.0.1:10006/static/mydict.dic'
```

##### 热更新 IK 分词使用方法
IKAnalyzer.cfg.xml can be located at {conf}/analysis-ik/config/IKAnalyzer.cfg.xml or {plugins}/elasticsearch-analysis-ik-*/config/IKAnalyzer.cfg.xml
```
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE properties SYSTEM "http://java.sun.com/dtd/properties.dtd">
<properties>
	<comment>IK Analyzer 扩展配置</comment>
	<!--用户可以在这里配置自己的扩展字典 -->
	<entry key="ext_dict">custom/mydict.dic;custom/single_word_low_freq.dic</entry>
	 <!--用户可以在这里配置自己的扩展停止词字典-->
	<entry key="ext_stopwords">custom/ext_stopword.dic</entry>
 	<!--用户可以在这里配置远程扩展字典 -->
	<entry key="remote_ext_dict">http://127.0.0.1:10006/static/mydict.dic</entry>
 	<!--用户可以在这里配置远程扩展停止词字典-->
	<entry key="remote_ext_stopwords">http://xxx.com/xxx.dic</entry>
</properties>
```
