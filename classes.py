# Define a classe ver_arquivo que lê o conteúdo de um arquivo
class ver_arquivo:
    # Inicializa a classe com o nome do arquivo
    def __init__(self, file):
        self.file = file

    # Define o método ler_arquivo que abre o arquivo e retorna o seu conteúdo
    def ler_arquivo(self):
        # Usa o gerenciador de contexto with para abrir o arquivo em modo de leitura
        with open(self.file, "r") as gta:
            # Lê todo o conteúdo do arquivo e armazena na variável content
            content = gta.read()
            # Retorna o conteúdo do arquivo
            return content
        

# Define a classe person_say que representa uma pessoa que diz algo
class person_say:
    # Inicializa a classe com o nome e a idade da pessoa
    def __init__(self, nome, age):
        self.nome = nome
        self.age = age

    # Define o método retorna_say que retorna uma saudação com o nome e a idade da pessoa
    def retorna_say(self):
        # Usa f-strings para formatar a saída
        return f"Olá {self.nome}! Você tem {self.age} anos?"
    

# Define a classe another_test que realiza operações aritméticas com dois números
class another_test:
    # Inicializa a classe com os dois números
    def __init__(self, a, b):
        self.a = a
        self.b = b
    
    # Define o método plus que retorna a soma dos dois números
    def plus(self):
        # Calcula a soma e armazena na variável conteudo
        conteudo = self.a + self.b
        # Retorna o resultado
        return conteudo
    
    # Define o método vezes que retorna o produto dos dois números
    def vezes(self):
        # Calcula o produto e armazena na variável conteudo_vezes
        conteudo_vezes = self.a * self.b
        # Retorna o resultado
        return conteudo_vezes
    
    # Define o método menos que retorna a diferença dos dois números
    def menos(self):
        # Calcula a diferença e armazena na variável conteudo_menos
        conteudo_menos = self.a - self.b
        # Retorna o resultado
        return conteudo_menos
    
    # Define o método divisao que retorna a divisão dos dois números
    def divisao(self):
        # Calcula a divisão e armazena na variável conteudo_divisao
        conteudo_divisao = self.a / self.b
        # Retorna o resultado
        return conteudo_divisao
        
        
# Define a classe Person que representa uma pessoa com nome e sobrenome
class Person:
  # Inicializa a classe com o nome e o sobrenome da pessoa
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  # Define o método printname que imprime o nome e o sobrenome da pessoa
  def printname(self):
    print(self.firstname, self.lastname)

# Define a classe Students que herda da classe Person e representa um estudante com nome, sobrenome e ano
class Students(Person):
    # Inicializa a classe com o nome, o sobrenome e o ano do estudante, usando o método super para herdar os atributos da classe Person
    def __init__(self, fname, lname, year):
        super().__init__(fname, lname)
        self.year = year

    # Define o método greet que imprime uma saudação com o nome e o ano do estudante
    def greet(self):
        # Usa f-strings para formatar a saída
        print(f"Olá Mr.{self.firstname} e você esta no ano {self.year}")


# Define a classe Teste que representa um teste com um nome
class Teste:
    # Inicializa a classe com o nome do teste
    def __init__(self, myName):
        self.myName = myName

    # Define o método mostrar que imprime o nome do teste
    def mostrar(self):
        print(self.myName)

# Define a classe Testes que herda da classe Teste e representa um teste com um nome e um sobrenome
class Testes(Teste):
    # Inicializa a classe com o nome e o sobrenome do teste, usando o método super para herdar o atributo da classe Teste
    def __init__(self, myName, myLastname):
        super().__init__(myName)
        self.myLastname = myLastname

    # Define o método imprimir que imprime uma mensagem com o nome e o sobrenome do teste
    def imprimir(self):
        # Usa f-strings para formatar a saída
        print(f"Voltando a testar classes em python. Mr.{self.myName} {self.myLastname}")

# Solicita ao usuário que digite o seu nome e armazena na variável putName
putName = input("Type your name here: ")

# Cria um objeto da classe Testes com o nome e o sobrenome do usuário e armazena na variável takeClass
takeClass = Testes(putName, "Nascimento")

# Executa o método imprimir do objeto takeClass
takeClass.imprimir()

# Solicita ao usuário que digite o seu primeiro nome e armazena na variável userInput
userInput = input("Type your firts name (only): ")

# Cria um objeto da classe Students com o primeiro nome, o sobrenome e o ano do usuário e armazena na variável x
x = Students(userInput, "Doe", 2019)

# Executa o método greet do objeto x
x.greet()     


# Cria um objeto da classe ver_arquivo com o nome do arquivo "seila.txt" e armazena na variável ler
ler = ver_arquivo("seila.txt")

# Executa o método ler_arquivo do objeto ler e armazena o conteúdo do arquivo na variável content
content = ler.ler_arquivo()

# Imprime o conteúdo do arquivo sem espaços em branco no início e no fim
print(content.strip())


# Cria um objeto da classe person_say com o nome "Olá" e a idade 30 e armazena na variável say
say = person_say("Olá", 30)

# Executa o método retorna_say do objeto say e imprime o resultado
print(say.retorna_say())


# Cria um objeto da classe another_test com os números 2 e 2 e armazena na variável contar
contar = another_test(2, 2)

# Executa o método plus do objeto contar e armazena o resultado na variável conteudo
conteudo = contar.plus()

# Imprime o resultado da soma
print(conteudo)

# Executa o método vezes do objeto contar e armazena o resultado na variável conteudo_vezes
contar_vezes = another_test(2, 2)
conteudo_vezes = contar_vezes.vezes()

# Imprime o resultado do produto
print(conteudo_vezes)

