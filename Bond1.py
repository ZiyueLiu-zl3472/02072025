

face = 2000000
ytm = .03
couponrate = .04
maturity = 10


class bond():
    def __init__(self,face,ytm,couponrate,m):
        self.face = face
        self.ytm = ytm
        self.couponrate = couponrate
        self.m = m
        
# Look at the bond instance
b1 = bond(2e6,.03,.04,10)
b1

# Look at the print function
print(b1)


#%%
# the __repr__ function
class bond():
    def __init__(self,face,ytm,couponrate,m):
        self.face = face
        self.ytm = ytm
        self.couponrate = couponrate
        self.maturity = m
    def __repr__(self):
        return "{},{},{},{},".format(self.face,self.ytm,self.couponrate,self.maturity)
    


# Look at the bond instance
b2 = bond(2e6,.03,.04,10)
print(b2)


#%%
# The __str__ function
class bond():
    def __init__(self,face,ytm,couponrate,maturity):
        self.face = face
        self.ytm = ytm
        self.couponrate = couponrate
        self.maturity = maturity
    def __repr__(self):
        return "{},{},{},{}".format(self.face,self.ytm,self.couponrate,self.maturity)
    def __str__(self):
        return "I'm James Bond"

b3 = bond(2e6,.03,.04,10)
print(b3)

