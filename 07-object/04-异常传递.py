import time

try:
    f = open('text.txt')
    try:
        while True:
            content = f.readline()
            if len(content) == 0:
                break
            time.sleep(1.5)
            print(content)
    except Exception as result:
        print('意外中止了读取文件')
    finally:
        f.close()
        print('文件已关闭！！！')

except:
    print('没有这个文件')
