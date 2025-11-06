tarefas = []

while True:
    print('\n---Gerenciador de tarefas---')
    print('1) Mostrar a lista de tarefas')
    print('2) Adicionar nova tarefa')
    print('3) Marcar tarefas como concluídas')
    print('4) Sair')

    opcao = input('\nEscolha uma opção: ')

    if opcao == '1':
        if len(tarefas) == 0:
            print('\nNão há tarefas!')
        else:
            print('\nLista de Tarefas')
            for i, tarefa in enumerate(tarefas):
                print(f'{i + 1}. {tarefa}')

    elif opcao == '2':
        nova_tarefa = input('\nInsira uma nova tarefa: ')
        tarefas.append(nova_tarefa)
        print('\nTarefa adicionada com sucesso!')

    elif opcao == '3':
        if not tarefas:
            print('\nNão há tarefas para concluir!')
        else:
            for i, tarefa in enumerate(tarefas):
                print('\nLista de tarefas')
                print(f'{i + 1}. {tarefa}')

            concluida = int(input('\nDigite o número da tarefa concluída: '))
            if 1 <= concluida <= len(tarefas):
                tarefas[concluida - 1] += " (concluída)"
                print('\nTarefa marcada como concluída!')
            else:
                print('\nNúmero inválido!')

    elif opcao == '4':
        print('Saindo...')
        break

    else:
        print('\nAção inválida!')