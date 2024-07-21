- Aula 1
  - Explorado o conceito de classe no desenvolvimento orientado a objetos (OO) e compreendi que uma classe é uma estrutura que define um tipo específico de objeto.
  - Compreendi a importância das classes no paradigma de programação orientada a objetos, destacando como elas permitem organizar o código de forma mais modular e reutilizável.
  - Iniciei a construção da primeira classe, denominada Restaurante, em que aprendi a definir atributos específicos da instância de um restaurante, como nome, categoria e ativo.
  

- Aula 2
  - Demonstrei a utilização do construtor __init__, o qual é responsável por inicializar os atributos da instância, incluindo a definição padrão de ativo como False.
  - Explorei a criação de instâncias da classe Restaurante, destacando como atribuir valores aos atributos da instância durante a criação de um objeto.
  - Compreendi a distinção entre atributos de classe e atributos de instância, e foquei como os atributos específicos da instância são acessados e manipulados dentro da classe.


- Aula 3
  - Explorei como criar atributos em classes e utilizando 'underscore' (underline) para indicar que um atributo é protegido.
  - Pratiquei o uso da função property em outros atributos, como categoria e ativo, proporcionando uma abordagem mais controlada e facilitando o acesso aos valores desses atributos.
  - Criei e utilizei métodos de classe, que são métodos que agem sobre a classe como um todo, em vez de uma instância específica. No exemplo, criei o método listar_restaurantes para exibir uma lista formatada dos restaurantes.
  - Demonstrei o conceito de abstração ao utilizar a propriedade ativo para apresentar visualmente o estado ativo ou inativo de um restaurante.


- Aula 4
  - Aprendi a importar classes em arquivos Python, utilizando essa habilidade para importar a classe Restaurante para o arquivo principal (app.py), permitindo utilizar suas funcionalidades no programa.
  - Explorei ainda mais os princípios da Programação Orientada a Objetos (OO), criando uma nova classe para reforçar conceitos fundamentais. Entendemos como a criação de classes e instâncias proporciona uma estrutura organizada e modular para o código.
  - Avançamos na integração entre classes, especificamente entre as classes Restaurante e Avaliação. Agora, temos uma lista de objetos de avaliação associados a cada restaurante, demonstrando a relação e interdependência entre diferentes entidades em um sistema.
  - Utilizei técnicas de listagem para criar funcionalidades que permitam visualizar as avaliações associadas a cada restaurante. Isso consolidou meu entendimento sobre como gerenciar e apresentar dados de maneira eficiente no programa.


- Aula 5
  - Abordei a importância de criar docstrings no código, que são comentários incorporados diretamente no código-fonte para documentar funções, métodos, módulos ou classes.
  - Explorei o momento adequado para criar docstrings, destacando que elas são especialmente úteis quando se desenvolve aplicações que podem ser compartilhadas com outros desenvolvedores. Documentar o propósito, parâmetros e comportamento de funções facilita a compreensão e colaboração no código.
  - Entendi que nas situações em que pode não ser necessário criar docstrings, como em códigos muito simples e autoexplicativos, onde o propósito das funções é óbvio ou em projetos pessoais de curto prazo.
  - Enfatizei que a prática consistente de documentar o código através de docstrings contribui para a manutenção eficiente do código ao longo do tempo, facilitando a resolução de problemas, a implementação de novos recursos e a colaboração entre membros da equipe.


- Aula 6
  - Criei a classe principal chamada ItemCardapio com um construtor que aceita os parâmetros nome e preço;
  - Implementei duas classes chamadas Bebida e Prato que herdam atributos e métodos da classe ItemCardapio, utilizando super() no construtor para aproveitar a estrutura da classe pai;
  - Criei objetos das classes Prato e Bebida, demonstrando como a herança pode ser utilizada para compartilhar funcionalidades entre diferentes tipos de itens de cardápio.


- Aula 7
  - Criei um método para adicionar itens ao cardápio e refatorei a função para receber qualquer objeto que seja uma instância de ItemCardapio;
  - Utilizei o conceito de property para exibir o cardápio de cada restaurante, proporcionando uma visão clara dos itens disponíveis;
  - Desenvolvi o método abstrato chamado aplicar_desconto que permite aplicar descontos de forma flexível a diferentes tipos de itens no cardápio;
  - Apliquei um valor de desconto tanto em bebidas quanto em pratos, destacando o polimorfismo na prática, onde diferentes classes respondem ao mesmo método de maneiras distintas.