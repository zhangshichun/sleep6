import requests,os

def write():
    req = requests.get('http://pic.zhangshichun.top/pic/20240517-01.png')
    dirName = './.temp'
    picName = 'test.png'
    os.makedirs(dirName, exist_ok=True)
    with open(os.path.join(dirName, picName),'wb') as f:
        f.write(req.content)
    print('{}下载完成！'.format(picName))

if __name__ == '__main__':
    write()