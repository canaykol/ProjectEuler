num = ""

for n in range(1,100000000):
    num + str(n)
    if len(num) > 1000000:
     break
    
print num[1]*num[10]*num[100]*num[1000]*num[10000]*num[100000]*num[1000000]