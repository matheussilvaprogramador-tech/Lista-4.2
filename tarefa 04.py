#11. Sistema de Notas:  Crie um programa que receba  a nota de um aluno: ●  Se for 7 ou mais: "Aprovado". ●  Se for entre 5 e 6.9: "Recuperação". ●  Se for menor que 5: "Reprovado". 
nota=float(input("Digite sua nota:"))
if nota >=7 or nota >=10:
    print("Aprovado")
elif nota <=6.9 and nota >=5:
    print("Recuperaçao")

elif nota <=4.9:
    print("Repravado")
else:
    print("Valor ivalido")
