def  fatorial(num):
    for i in range(num-1, 1,-1):
        num=num*i
    return num

n = int(input())
fat = fatorial(n)
#fibonacci

if n < 2 :
    fib = n
else:
    fib_ant = 1
    fib = 1
    i=2
    while(i<n):
        aux = fib
        fib =  fib +fib_ant
        fib_ant = aux
        i+=1
#caso o fibonacci seja par mostre o anterior
if fib%2 == 0:
    
    print("{} {} {:.0f}".format(fib,fat,fib_ant))
else:
    print("{} {}".format(fib,fat))