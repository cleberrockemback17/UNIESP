codigo = 0
controle = 1
dados = []


while controle != 0:
    print ('-' *50)
    print ("1 - Cadastrar Funcionário")
    print ("2 - Alterar Funcionário")
    print ("3 - Listar todos os Funcionários")
    print ("4 - Excluir um Funcionário")
    print ("5 - Adicionar um aumento de salário")
    print ("0 - Sair")
    print ('-' *50)
    controle = int(input("Digite a opção: "))

#Cadastros
    if controle == 1:

        dados_auxiliar = {}

        dados_auxiliar['codigo'] = codigo = codigo + 1
        dados_auxiliar['nome'] = str(input("Qual o seu nome: "))
        dados_auxiliar['email'] = input("Qual o seu email: ")  
        dados_auxiliar['data'] = str(input("Qual a data de admissão: "))
        dados_auxiliar['salario'] = int(input("Qual o seu salário: "))
        print("Cadastro executado com sucesso")
        dados.append(dados_auxiliar)


#Alterar funcionario
    elif controle == 2:
        print(dados)
        a = int(input("Qual a posição/índice do funcionário que você deseja alterar? "))

        dados1 = {}
        dados1['codigo'] = codigo = codigo + 1
        dados1['nome'] = str(input("Qual o seu nome: "))
        dados1['email'] = input("Qual o seu email: ")  
        dados1['data'] = str(input("Qual a data de admissão: "))
        dados1['salario'] = int(input("Qual o seu salário: "))
        print("Cadastro modificado com sucesso")
        del(dados[a])
        dados.insert(a, dados1)




# listar funcioonario
    elif controle == 3:
        
        if dados is None:
            
            print("Não temos registros")
        
        else: 
            print(dados)



# Deletar funcionario
    if controle == 4:
        print(dados)
        func = int(input("Digite a posição/índice do Funcionário que deseja deletar: "))
        dados.pop(func)

# Aumento de salário
    # if controle == 5:
    #     print(dados)
    #     s = int(input("Qual posição/índice do Funcionário que deseja alterar? "))
    #     novo_salario = float(input("Quanto de aumento no salário você quer dar a esse funcionário? "))
    #     novo_salario1 = novo_salario + dados_auxiliar[{s, 'salario' }]
    #     dados_auxiliar[{s, 'salario'}] = novo_salario1
    #     dados.insert(s, ['salario'])
        
print("FIM")