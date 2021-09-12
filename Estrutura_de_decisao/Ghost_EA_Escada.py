a,b = input().split()
a,b = [int(a),int(b)]

num = b - a
if num > 1 or (b<a) or ((0 == a and b == 0)):
    print("{} {} errados".format(a,b))
else:
    print("{} {} ok".format(a,b))
