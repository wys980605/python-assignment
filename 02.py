#作业1

class animal():
    def __init__(self,name):
        self.name=name
class mammal():
    def breath(self):
        print(self.name,'can breath.')
class bird():
    def fly(self):
        print(self.name,'can fly.')

class Mrun(animal,mammal):
    pass

class Brun(animal,bird):
    pass


dog=Mrun('dahuang')
dog.breath()



#作业2 用if语句：

catalog={'bearing': 30, 'gear': 10, 'pump': 50, 'sealing': 0}

class OutofStockException(Exception):
    pass
class no_such_thing(Exception):
    pass

def take(name,number):
    if name in catalog:
        if catalog[name]<=0:
            raise OutofStockException
        else:
            catalog[name]=catalog[name]-number

    else:
        raise no_such_thing

while True:
    name=input('请输入需要的物品：')
    number=eval(input('请输入需要的数量：'))
    take(name,number)
    print('{}还剩{}个'.format(name,catalog[name]))



#转化为try......except.......：

 
catalog={'bearing':30,'gear':10,'pump':50,'sealing':0}
class InvalidParts(Exception):
    pass
class OutOfStock(Exception):
    pass

class Inventory:
    def __init__(self,parts,num):
        self.parts=parts
        self.num=num
    def assign(self,parts,num):
        try:
            if parts not in catalog.keys():
                raise InvalidParts
            if catalog[parts]==0 or catalog[parts]<num:
                raise OutOfStock
            else:
                num=catalog[parts]-num
                print('assignment is completed.There are ''{} {}s'.format(num,parts))
        except InvalidParts:
            print('Sorry,we don\'t have ''{}s'.format(parts))
        except OutOfStock:
            print('Sorry,that item is out of stock.The number of the parts is {}'.format(catalog[parts]))
        finally:
            print('程序继续执行')
 
item=input('请输入需要的零件:')
num=eval(input('请输入需要的个数:'))

inv=Inventory(item,num)
inv.assign(item,num)


