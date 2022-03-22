until=2*10**6
liste = range(2,until)
print liste

for factor in range(2,until/2):
    ffactor = 1
    efactor = factor
    print factor
    while efactor <= until:
        if efactor in liste:
            liste.remove(efactor)        
        ffactor += 1
        efactor = ffactor * factor
        
print liste