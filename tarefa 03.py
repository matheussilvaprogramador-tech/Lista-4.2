#10. Par ou Ímpar:  Peça um número ao usuário. Use o  operador  %  e uma estrutura if/else  para dizer se o número é par ou ímpar.
numero=int(input("Digite um Numero:"))
numero2 = numero%2
if numero2 == 0:
    print(f"{numero} que  e  PAR")
else:
    print("impar")

