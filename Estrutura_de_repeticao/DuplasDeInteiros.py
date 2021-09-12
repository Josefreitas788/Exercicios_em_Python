t = int(input())
soma = 0
for i in range(t):
    a,n = input().split()
    a,n = [int(a),int(n)]
    for j in range(n):
        print(a, end = " ")
        soma = soma+a
        a = a+1
    print("\n{}".format(soma))
    soma=0
