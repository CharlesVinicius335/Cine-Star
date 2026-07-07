

class Filme:
    def __init__(self,nome, duracao, genero):
        self.nome = nome
        self.duracao = duracao
        self.genero = genero
        self.cartaz = False
        
    def alterar_status(self):
        self.cartaz = not self.cartaz

    def __str__(self):
        if self.cartaz:
            status = 'Em cartaz'
        else:
            status = 'Fora de cartaz'
        
        return (
            f'Nome: {self.nome}\n'
            f'Duração: {self.duracao} minutos\n'
            f'genero: {self.genero}\n'
            f'Status: {status}'
        )
    
    
        
        