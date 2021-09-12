R , L = input().split()
R, L = [int(R),int(L)]
if R<L:
    divisor = R
else:
    divisor = L

while True:
    if  (L%divisor == 0) and (R%divisor == 0):
        print(divisor)
        break
    divisor-=1

