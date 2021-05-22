class 차:
    def __init__(self,tire,price):
        self.tire = tire
        self.price = price
    def 바퀴(self):
        print(self.tire)
    def 가격(self):
        print(self.price)

car = 차(2, 1000)
car.바퀴()
car.가격()

class 자전차(차):
    def __init__(self,tire,price,구동):
        self.tire = tire
        self.price = price
        self.구동 = 구동
    def 구동계(self):
        print(self.구동)
    def 정보(self):
        print(self.tire)
        print(self.price)
        print(self.구동)
    pass

bicycle = 자전차(2,100,"시마노")
bicycle.가격()
bicycle.구동계()
bicycle.정보()

class 자동차(차):
    def 정보(self):
        print(self.tire)
        print(self.price)
car = 자동차(4,1000)
car.정보()