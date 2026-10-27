#12. Comparando Dois Números:  Peça ao usuário dois  números (  n1  e  n2  ). O programa deve dizer qual deles é o maior ou se são iguais. 
n1=int(input("Digite um numero:"))
n2=int(input("Digite outro:"))
if n1 > n2:
    print(f"O maior numero é :{n1}")
elif n2 > n1:
    print(f"O maoir numero é:{n2}")
else:
    print("Os dois Numeros sao iguais")
