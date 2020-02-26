print ("Δώστε έναν θετικό αριθμό")
x = int(input())
while x<=0:
    print ("Ο αριθμός δεν ήταν έγκυρος,δώστε εναν θετικό αριθμό")
    x = int(input())
while True:
    x=x*3+1
    x = str(x)
    a=0
    for i in x:
        a=a+int(i)
    x=a
    if len(str(x)) == 1:
        break
print ("Το τελικό νούμερο είναι:",x)