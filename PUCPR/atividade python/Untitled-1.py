lista_estudantes = []

def incluir_estudante():
    print("---- INCLUSÃO DE ESTUDANTE ----")
    
    codigo = int(input("Digite o código do estudante: "))
    nome = input("Digite o nome do estudante: ")
    cpf = input("Digite o CPF do estudante: ")
    
    # Adiciona o estudante à lista
    lista_estudantes.append({
        "codigo": codigo,
        "nome": nome,
        "cpf": cpf
    })
    print(f"Estudante {nome} incluído com sucesso.")

def listar_estudantes():
    print("---- LISTAGEM DE ESTUDANTES ----")
    if not lista_estudantes:
        print("Nenhum estudante cadastrado.")
    else:
        for estudante in lista_estudantes:
            print(f"Código: {estudante['codigo']}, Nome: {estudante['nome']}, CPF: {estudante['cpf']}")

def atualizar_estudante():
    print("---- ATUALIZAÇÃO DE ESTUDANTE ----")
    
    codigo = int(input("Digite o código do estudante que deseja atualizar: "))
    estudante_encontrado = next((e for e in lista_estudantes if e['codigo'] == codigo), None)
    
    if estudante_encontrado:
        print(f"Estudante encontrado: Nome: {estudante_encontrado['nome']}, CPF: {estudante_encontrado['cpf']}")
        
        novo_nome = input("Digite o novo nome do estudante (deixe em branco para manter o atual): ")
        novo_cpf = input("Digite o novo CPF do estudante (deixe em branco para manter o atual): ")
        
        if novo_nome:
            estudante_encontrado['nome'] = novo_nome
        if novo_cpf:
            estudante_encontrado['cpf'] = novo_cpf
        
        print("Estudante atualizado com sucesso.")
    else:
        print("Estudante não encontrado.")

def excluir_estudante():
    print("---- EXCLUSÃO DE ESTUDANTE ----")
    
    codigo = int(input("Digite o código do estudante que deseja excluir: "))
    global lista_estudantes
    lista_estudantes = [e for e in lista_estudantes if e['codigo'] != codigo]
    
    print("Estudante excluído com sucesso.")

def gerenciar_estudantes():
    while True:
        print("----[ESTUDANTES] MENU DE OPERAÇÕES----")
        print("1. Incluir")
        print("2. Listar")
        print("3. Atualizar")
        print("4. Excluir")
        print("0. Voltar")
        
        acao = input('Informe a ação desejada: ')
        
        if acao.isdigit():
            acao = int(acao)
            if acao == 1:
                incluir_estudante()
            elif acao == 2:
                listar_estudantes()
            elif acao == 3:
                atualizar_estudante()
            elif acao == 4:
                excluir_estudante()
            elif acao == 0:
                break
            else:
                print("Opção incorreta!")
        else:
            print("Por favor, digite um número válido.")

def menu_principal():
    while True:
        # Menu Principal
        print("MENU PRINCIPAL")
        print("(1) GERENCIAR ESTUDANTES")
        print("(2) GERENCIAR PROFESSORES")
        print("(3) GERENCIAR TURMAS")
        print("(4) GERENCIAR MATRICULAS")
        print("(0) SAIR")
        
        opcao = input("Digite uma opção: ")
        
        if opcao.isdigit():
            opcao = int(opcao)
            if opcao == 1:
                gerenciar_estudantes()
            elif opcao == 2:
                print("Funcionalidade não implementada ainda.")
                # Função para gerenciar professores
            elif opcao == 3:
                print("Funcionalidade não implementada ainda.")
                # Função para gerenciar turmas
            elif opcao == 4:
                print("Funcionalidade não implementada ainda.")
                # Função para gerenciar matrículas
            elif opcao == 0:
                print("----[FINALIZANDO....]----")
                break
            else:
                print("Opção inválida.")
        else:
            print("Por favor, digite um número válido.")

# Início do programa
menu_principal()