class Restaurante:


    def __init__(self, nome, categoria):
        # Método construtor, chamado automaticamente quando uma nova instância da classe é criada
        self.nome = nome
        self.categoria = categoria
        self.ativo = False

    def __str__(self):
        # Método especial que retorna uma 'string' representando a instância da classe
        return f"{self.nome} | {self.categoria}"

restaurante_praca = Restaurante('Praça', 'Gourmet')
restaurante_pizza = Restaurante('Pizza Express', 'Italiana')

print(restaurante_praca)
print(restaurante_pizza)