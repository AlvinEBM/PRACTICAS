disponeble= {100:3,50:6,20:10,10:50,1:50}

# k=denominacion del billete
# v=cantidad del billete
def cantidad_disponible():   
    total=0
    for k,v in disponeble.items():
        total+=k*v
    return total


def retirar(monto):
    if monto>cantidad_disponible():
        print("no hay efectivo para retirar el monto")
    saldo=monto
    while saldo>0:
        for k,v in disponeble.items():
            count=get_denominacion(k,saldo)
            print("billete o moneda de ",k,count)
            saldo-=count*k

def get_denominacion(denominacion,saldo):
    count=saldo//denominacion
    if (count>disponeble[denominacion]):
        count=disponeble[denominacion]
    disponeble[denominacion]-=count
    return count    

print(cantidad_disponible())
monto=1300
retirar(monto)
#print(cantidad_disponible())