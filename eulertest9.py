h=6
for i in range(1,1000):
    for j in range(i,1000):
        c=1000-i-j
        if (i**2+j**2==c**2):
            print (i*j*c)
            print(i , j, c)
            h=5
            break
    if h==5:
        break
