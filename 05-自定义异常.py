class ShortInterError(Exception):
    def __init__(self, length, min_length):
        self.length = length
        self.min_length = min_length

    def __str__(self):
        return f'密码长度设置不规范，您输入的长度是{self.length}位，' \
                                    f'输入的长度不能少于{self.min_length}位'


def main():
    try:
        password = input('请输入密码：')
        if len(password) < 6:
            # 抛出异常类创建的对象
            raise ShortInterError(len(password), 6)
    except Exception as result:
        print(result)
    else:
        print('密码设置成功！！！')


main()
