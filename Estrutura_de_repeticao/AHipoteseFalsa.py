n  = int(input())
m = 1
while(True):
    i=2
    while  i<=(n*m+1)/2:

        if   (n*m+1)%i ==0:
            print(m)
            exit()
        i+=1
    m+=1