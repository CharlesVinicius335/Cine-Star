from filmes import Filme

class Cinema:
    def __init__(self,nome):
        self.nome = nome
        self.filmes = []
    
    def adicionar_filme(self,filme):
        self.filmes.append(filme)


    def __str__(self):
            texto = f"Cinema: {self.nome}\n\n"

            for filme in self.filmes:
                texto += str(filme) + '\n\n'

            return texto
    
    def alterar_status_filme(self, nome):
        for filme in self.filmes: 
            if filme.nome.lower() == nome.lower():
                filme.alterar_status()
                print(f"Status do filme '{filme.nome}' alterado com sucesso!")
                return

            print("Filme não encontrado.")

    def buscar_filme(self, nome):
            for filme in self.filmes:
                if filme.nome.lower() == nome.lower():
                    print(f"\nFilme encontrado: {filme}")
                    return
            print("Filme não encontrado.")