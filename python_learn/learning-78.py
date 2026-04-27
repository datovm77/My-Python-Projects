class People:
    # 请在下面填入声明两个变量名分别为name和country的字符串变量的代码
    #********** Begin *********#
    name = ""
    country = ""
    #********** End **********#
    def introduce(self,name,country):
        self.name = name
        self.country = country
        print("%s来自%s" %(name,country))
name = input()
country = input()
# 请在下面填入对类People进行实例化的代码，对象为p
#********** Begin *********#
p = People()
#********** End **********#
p.introduce(name,country)
