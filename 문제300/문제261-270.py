#261
class stock:
    #262 #266
    def __init__(self,name,code,PER,PBR,bds):
        self.name = name
        self.code = code
        self.per = PER
        self.pbr = PBR
        self.bds = bds

    # 263
    def set_name(self, name):
        self.name = name

    # 264
    def set_name(self, code):
       self.code = code

    #265
    def get_name(self):
        return self.name

    def get_code(self):
        return self.code
    #268
    def set_per(self, per):
        self.per = per

    def set_pbr(self, pbr):
        self.pbr = pbr

    def set_bds(self, bds):
        self.bds = bds

#267
samsung = stock("삼성전자","005930",15.79,1.33,2.83)
#269
samsung.set_per(12.75)
#270
st = []
st.append(stock("삼성전자","005930",15.79,1.33,2.83))
st.append(stock("현대차","005380",8.70,0.35,4.27))
st.append(stock("LG전자","066570",317.34,0.63,1.37))
for i in st:
    print(i.name,i.code,i.per,i.pbr,i.bds)