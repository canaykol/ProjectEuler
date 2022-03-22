liste = [0,1,1]
for n in range(3,1000000):
    result = liste[n-1] + liste[n-2]
    if len(str(result)) >= 1000:
        print n, result
        break
    liste.insert(n,result)
    