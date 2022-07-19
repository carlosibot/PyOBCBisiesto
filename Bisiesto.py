bisiesto = (int(input("Introduce un año: ")))

def abisiesto (bisiesto):
    while  bisiesto % 4 == 0 and (bisiesto % 100 !=0 or bisiesto % 400 ==0):
        return True

if abisiesto(bisiesto) == True:
    print("Este año es bisiesto")
else:
    print("Este año no bisiesto")

