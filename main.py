from filmes import Filme
from cinema import Cinema

def menu():
    print("""

╰☆☆ ℂ𝕚𝕟𝕖 𝕊𝕥𝕒𝕣 ☆☆╮
          
1 - Cadastrar filme
2 - Listar filmes
3 - buscar filme
4 - Alterar status do filme
5 - Sair
          
    """)


filme1 = Filme('Vingadores', '180 min', 'Ação')
filme2 = Filme('As Branquelas', '200 minutos', ' Comédia')
filme3 = Filme('Zootopia', '200 minitos', 'Animação')

filme1.alterar_status()

cinema1 = Cinema('Cine Star')

cinema1.adicionar_filme(filme1)
cinema1.adicionar_filme(filme2)


def cadastrar_filme():
    nome = input('Digite o nome do filme: ')
    duracao = input('Digite a duração do filme: ')
    genero = input('Digite o gênero do filme: ')

    novo_filme = Filme(nome, duracao, genero)

    cinema1.adicionar_filme(novo_filme)

while True: 
    menu()
    opcao = input('Escolha uma opção: ')

    if opcao == '1':
        cadastrar_filme()
    
    elif opcao == '2':
        print(cinema1)

    elif opcao == '3':
        nome = input("\nNome do filme que deseja buscar: ")
        cinema1.buscar_filme(nome)

    elif opcao == '4':
        nome = input("Digite o nome do filme: ")
        cinema1.alterar_status_filme(nome)
    
    elif opcao == '5':
        print('Encerrando')
        break
    else:
        print('Opção invalida !!')


