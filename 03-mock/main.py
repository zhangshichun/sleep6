import os
defaultPic = './default-img/default.png'
dirName = './.temp'
picName = 'test.png'

def write():
    print('开始下载...')
    os.makedirs(dirName, exist_ok=True)
    with open(defaultPic, "rb") as source_file:
        with open(os.path.join(dirName, picName), "wb") as target_file:
            target_file.write(source_file.read())
    print('{}下载完成！'.format(picName))

if __name__ == '__main__':
    write()
