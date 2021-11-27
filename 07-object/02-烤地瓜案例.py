class SweetPotatoes:
    def __init__(self):
        self.cook_time = 0
        self.cook_state = '生的'
        self.condiments = ''

    def cook(self, time):
        """烤地瓜"""
        self.cook_time += time
        if 0 <= self.cook_time < 3:
            self.cook_state = '生的'
        elif 3 <= self.cook_time < 5:
            self.cook_state = '半生不熟'
        elif 5 <= self.cook_time < 8:
            self.cook_state = '熟的'
        elif self.cook_time >= 8:
            self.cook_state = '被烤糊了'

    def add_condiments(self, condiment):
        """添加调料"""
        self.condiments = condiment

    def __str__(self):
        return f'这个地瓜将要烤{self.cook_time}分钟，状态将会是' \
               f'{self.cook_state}，且是{self.condiments}口味的'


n = int(input('您打算把这个地瓜烤多少分钟呢？请输入具体时间数字（单位是minute）：'))
i = int(input('1、酱香 2、麻辣 3、甜辣 4、番茄' + '\n' +
              '请在以上选项中选择您想要给这个地瓜添加的口味，请输入相关序号：'))
List = ['酱香', '麻辣', '甜辣', '番茄']
sw = List[i - 1]

dg = SweetPotatoes()
# print(dg)
dg.cook(n)
dg.add_condiments(sw)
print(dg)
