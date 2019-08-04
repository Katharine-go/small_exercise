class videotape:
    def __init__(self,name,price,index,number):
        """

        :param name: 录像带的名字
        :param price: 录像带的价格
        :param index: 录像带的类别编号
        :param number: 录像带的数量
        """
        self.name = name
        self.price = price
        self.index = index
        self.number = number

    def __str__(self):
        return 'name:%s, price:%s, index:%s, number:%s'%(self.name, self.price, self.index
                                                         ,self.number)
