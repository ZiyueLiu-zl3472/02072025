

bonds = []
n = 5
for i in range(n):
    bonds.append(bond())

#%%
for b in bonds:
    print(b)

#%%
for b in bonds:
    b.getPrice()
    b.getDuration()

#%%    
for b in bonds:
    print(b)

#%%
def PortfolioDuration(bonds):
    num = 0
    den = 0
    for x in bonds:
        D_i = x.duration
        w_i = x.price
        num += D_i * w_i
        den += w_i
    duration = num/den
    return(duration)
    
#%%
print(PortfolioDuration(bonds))
