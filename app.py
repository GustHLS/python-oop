from models.restaurante import Restaurante

restaurante_praca = Restaurante('praça', 'gourmet')
restaurante_praca.receber_avaliacao('Gustavo', 10)
restaurante_praca.receber_avaliacao('Gisele', 8)
restaurante_praca.receber_avaliacao('Teste', 2)

def main():
    Restaurante.listar_restaurante()


if __name__ == '__main__':
    main()