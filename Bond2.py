import numpy as np


class bond:
    def __init__(self):        
        self.face = (round(np.random.uniform()*10,0)+1)*1e6
        self.couponRate = round(np.random.uniform()/3,3)
        self.pmtperyear = int(round(np.random.uniform(),0)+1)
        self.m = int(round(np.random.uniform()*10,0))
        self.ytm = round(np.random.uniform()/3,3)
        self.m = round(np.random.uniform()*5+5)
        self.price = 0
        self.duration = 0
    def __repr__(self):
        return "{},{},{},{}".format(self.face,self.ytm,self.couponRate,self.m)
        
b1 = bond()
print(b1)

#%%

class bond:
    def __init__(self):        
        self.face = (round(np.random.uniform()*10,0)+1)*1e6
        self.couponrate = round(np.random.uniform()/3,3)
        self.pmtperyear = int(round(np.random.uniform(),0)+1)
        self.m = int(round(np.random.uniform()*10,0))
        self.ytm = round(np.random.uniform()/3,3)
        self.m = round(np.random.uniform()*5+5)
        self.price = 0
        self.duration = 0
    def __repr__(self):
        return "{},{},{},{}".format(self.face,self.ytm,self.couponrate,self.m)
    def Assign(self,face,couponrate,m,ytm,pmtperyear):
        self.face = face
        self.couponrate = couponrate
        self.pmtperyear = pmtperyear
        self.m = m
        self.ytm = ytm
        
b2 = bond()
print(b2)
b2.Assign(2e6,.03,.04,100,1)
print(b2)



#%%

class bond:
    def __init__(self):        
        self.face = (round(np.random.uniform()*10,0)+1)*1e6
        self.couponrate = round(np.random.uniform()/3,3)
        self.pmtperyear = int(round(np.random.uniform(),0)+1)
        self.m = int(round(np.random.uniform()*10,0))
        self.ytm = round(np.random.uniform()/3,3)
        self.m = round(np.random.uniform()*5+5)
        self.price = 0
        self.duration = 0
    def __repr__(self):
        return "{},{},{},{},{},{}".format(self.face,self.ytm,self.couponrate,self.m,round(self.price,2),round(self.duration,2))
    def Assign(self,face,ytm,couponrate,m,pmtperyear):
        self.face = face
        self.couponrate = couponrate
        self.pmtperyear = pmtperyear
        self.m = m
        self.ytm = ytm
    def getPrice(self):
        face = self.face
        couponrate = self.couponrate
        pmtperyear = self.pmtperyear
        m = self.m
        y = self.ytm
        
        C = face * couponrate / pmtperyear
        n = m * pmtperyear
        y_eff = y/pmtperyear
        B = 0
        for i in range(1,n+1):
            pv = (1+y_eff)**(-i)
            B_i = C * pv
            B += B_i
        B += face * pv
        self.price = B
    def getDuration(self):
        face = self.face
        couponrate = self.couponrate
        pmtperyear = self.pmtperyear
        m = self.m    
        y = self.ytm
        C = face * couponrate / pmtperyear
        n = m * pmtperyear
        y_eff = y/pmtperyear
        B = 0
        Btime = 0
        for i in range(1,n+1):
            pv = (1+y_eff)**(-i)
            B_i = C * pv
            B += B_i
            Btime_i = i * B_i
            Btime += Btime_i
        B += face * pv
        Btime += face * pv * i
        self.duration = Btime/B
        
b3 = bond()
b3.Assign(2e6,.03,.04,10,1)
print(b3.price)
b3.getPrice()
print(b3.price)
b3.getDuration()
print(b3.duration)
