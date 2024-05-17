import requests,os

def write():
    req = requests.get('https://www.hello-what-is-your-name-baby.com')
    dirName = './.temp'
    picName = 'test.png'
    os.makedirs(dirName, exist_ok=True)
    with open(os.path.join(dirName, picName),'wb') as f:
        f.write(req.content)
    print('{}下载完成！'.format(picName))

if __name__ == '__main__':
    try:
        write()
    except Exception as e:
        print('出错了：')
        print(e)