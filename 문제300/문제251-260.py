#251

#252
class Human:
    def __init__(self, name, age, gend):
        # 254
        self.age = age
        self.name = name
        self.gend = gend
        print("응애응애")
        return
    def who(self):
        print(self.name,self.age,self.gend)

    def setInfo(self, name, age, gend):
        # 254
        self.age = age
        self.name = name
        self.gend = gend
    def __del__(self):
        print("나의 죽음을 알리지 말라")

#255
a=Human('s','1','5')
#256
print(a.age)
#257
a.who()
#258
a.setInfo("aa","15","m")
a.who()
#259
del a

#260
#__init__이 없음