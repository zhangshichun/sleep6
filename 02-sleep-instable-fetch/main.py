import requests,os
defaultPic = './default-img/default.png'
dirName = './.temp'
picName = 'test.png'
def realWrite():
    req = requests.get('https://www.hello-what-is-your-name-baby.com')
    os.makedirs(dirName, exist_ok=True)
    with open(os.path.join(dirName, picName),'wb') as f:
        f.write(req.content)
    print('{}下载完成！'.format(picName))

def write():
    os.makedirs(dirName, exist_ok=True)
    with open(defaultPic, "rb") as source_file:
        with open(os.path.join(dirName, picName), "wb") as target_file:
            target_file.write(source_file.read())
    print('{}下载完成！'.format(picName))

if __name__ == '__main__':
    try:
        realWrite()
    except Exception as e:
        write()