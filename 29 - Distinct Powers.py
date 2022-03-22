liste = []
for base in range(2,101):
    for power in range(2,101):
        liste.append(base**power)
        
liste.sort()
for n in range(0,len(liste)-1):
    if n == len(liste)-1:
        break
    while liste[n] == liste[n+1]:
        liste.pop(n)    
        
print len(liste)
