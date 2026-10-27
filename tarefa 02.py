#9. Teste de Maioridade:  Crie um script que peça a  idade do usuário. Se for 18 ou mais, exiba "Acesso Liberado ao Jogo". Caso contrário, exiba "Acesso Negado". 
idade=int(input("iforme sua idade:"))
if idade >18:
    print("Acesso Liberado ao Jogo")
elif idade <18:
    print("Acesso negado ao jogo")
