from models.restaurante import Restaurante
from models.cardapio.bebida import Bebida
from models.cardapio.prato import Prato

restaurante_praca = Restaurante('praça', 'gourmet')
bebida_suco = Bebida('Suco de Melância', 5.00, 'grande')
prato_paozinho = Prato('Pãozinho', 2.00, 'O melhor pão da cidade')

def main():
    print(bebida_suco)
    print(prato_paozinho)


if __name__ == '__main__':
    main()