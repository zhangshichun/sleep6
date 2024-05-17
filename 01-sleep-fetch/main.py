import requests,random,os,time,asyncio

dirName = './.temp'
picName = str(random.randint(1, 99999)) + '.png'

async def download():
    req = requests.get('https://pic.zhangshichun.top/pic/20240517-01.png')
    os.makedirs(dirName, exist_ok=True)
    with open(os.path.join(dirName, picName),'wb') as f:
        f.write(req.content)

def write(): 
    # 异步启动下载任务
    asyncio.run(download())

    # 我先睡6秒，图片肯定存下来了，我太聪明了
    time.sleep(6)
    print('{}下载完成！'.format(picName))

if __name__ == '__main__':
    write()
