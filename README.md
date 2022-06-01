#### 用来接收业务系统提取的自定义热词，热更新ES自定义词库。

##### 构建
```
docker build -t dict-server:1.0.0 .
```

##### 部署
```
docker run -d --name my-dict-server -v /host/path/ext_dict:/usr/src/app/static:rw -p 10006:10006  dict-server:1.0.0
```
`/host/path/ext_dict` 替换为宿主机实际es自定义词典文件路径

##### 接口
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