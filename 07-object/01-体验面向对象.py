class Washer:
    # __init__方法在只要有对象被创建之后就会默认被调用的
    def __init__(self, width, height):
        self.height = height
        self.width = width

    # 以下代码将会覆盖打印对象和打印self的值，此代码一般用于说明解释的文字
    def __str__(self):
        return "这是洗衣机的说明书"

    def wash(self):
        print('我能洗衣服')
        #  self指代的就是调用该函数的对象，也就是co对象
        print(self)

    # 在类的里面获取对象属性
    def print_info(self):
        print(f'hr洗衣机的宽度是{self.width}，高度是{self.height}')


hr = Washer(60, 120)
print(hr)
hr.wash()

"""
    # 在类的外面添加对象属性
    hr.width = 100
    hr.height = 500
    # 在类的外面获取对象的属性
    print(f 'hr洗衣机的宽度是{hr.width}' )
    print(f 'hr洗衣机的高度是{hr.height}' )
"""

hr.print_info()

# 一个类可以创建多个对象，此时打印出来的self内存地址不一样
re = Washer(80, 140)
re.wash()
re.print_info()
