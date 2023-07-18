
a = (2,9,24)
b = (30,18,1)
c = (8,8,8)

for n,b,m in zip(a,b,c):
    print(n+b+m, end=" ")
abc_start = "abcdefghijk"
vocales = "aeiou"
for i , letra in enumerate(abc_start):
    if letra in vocales:
        print("{} está en la posición {}".format(letra, i))

l = ["gato","perro","búho"]
li = iter(l)
print(next(li))
print(next(li))
print(next(li))
set_1 = {1,2,3}
set_2 = {2,4,5}
set_3 = set_1.intersection(set_2)
print(set_3)
a, b, c = map(int, input("Introduzca los números: ").split())
print(a,b, sep=" Separador intralíneas ", end= " Separandor líneas ")
print(c)

print("{} es el valor de a, {} el de b y {} el de c".format(a,b,c))
print(f"{a} es el valor de a, {b} el de b y {c} el de c")
print("%d es el valor de a" %a)
def indexador(objeto,índice):
    try:
        objeto[índice]
    except IndexError:
        print("Índice demasiado alto") 
var = input("Escribe algo: ")
num = int(input("Pon un entero: "))
print(indexador(var,num))