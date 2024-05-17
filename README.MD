# sleep6

## 关于

认真阐述，“你”会在什么情况下，在一个名为 `write` 的函数里写下 `time.sleep(6)`。

## 01. 尝试异步请求，但不知道咋取值，先睡6秒

常规的写法：( `demo` 见 `01-fetch` )

```python
req = requests.get('...')
os.makedirs(dirName, exist_ok=True)
with open(os.path.join(dirName, picName),'wb') as f:
    f.write(req.content)
print('{}下载完成！'.format(picName))
```

“你”的写法：( `demo` 见 `01-sleep-fetch` )

```python
async def download():
    req = requests.get('...')
    os.makedirs(dirName, exist_ok=True)
    with open(os.path.join(dirName, picName),'wb') as f:
        f.write(req.content)
# 异步启动下载任务
asyncio.run(download())

# 我先睡6秒，图片肯定存下来了，我太聪明了
time.sleep(6)
print('{}下载完成！'.format(picName))
```

## 02. 从一个【不稳定】的服务拉取结果

假设，一个服务方可能存在不稳定的情况（即：报错、崩溃、返回非预期的结果等），但你需要从它那里拉取结果。

正常写法：( `demo` 见 `02-instable-fetch` )

```python
    try:
        write()
    except Exception as e:
        print('出错了：')
        print(e)
```

“你”的写法：( `demo` 见 `02-sleep-instable-fetch` )

```python
def realWrite():
    # ... 真实下载逻辑，略

def write():
    os.makedirs(dirName, exist_ok=True)
    time.sleep(6)
    # 从本地复制一张图片兜底
    with open(defaultPic, "rb") as source_file:
        with open(os.path.join(dirName, picName), "wb") as target_file:
            target_file.write(source_file.read())
    print('{}下载完成！'.format(picName))

if __name__ == '__main__':
    try:
        realWrite()
    except Exception as e:
        write()
```

这样哪怕服务不稳定，报错了，你依然可以表现得很正常。

## 03. 你没有一个可用服务，但需要给客户演示

常规的写法：

> 对不起，客户。

“你”的写法：

```python
def write():
    print('开始下载...')
    os.makedirs(dirName, exist_ok=True)
    with open(defaultPic, "rb") as source_file:
        with open(os.path.join(dirName, picName), "wb") as target_file:
            target_file.write(source_file.read())
    print('{}下载完成！'.format(picName))

if __name__ == '__main__':
    write()
```
