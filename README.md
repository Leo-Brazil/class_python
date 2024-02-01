# class_python
(PT-BR) - Apenas para afins de estudos, classes em python. | (EN) - Just for study purposes, Python.

# EN 
This code demonstrates the use of various functionalities of object-oriented programming (OOP) in Python, through the definition and manipulation of several classes and objects. Here is a simple summary of the code and what it does:

1. **Class `ver_arquivo`**: This class is designed to handle file reading. It accepts a file name as a parameter during initialization and has a method `ler_arquivo` that reads the file content and returns it.

2. **Class `person_say`**: Represents a person who can say something, containing name and age. The method `retorna_say` returns a greeting that includes the person's name and age.

3. **Class `another_test`**: This class performs basic arithmetic operations (addition, subtraction, multiplication and division) with two numbers provided during initialization. Each operation is implemented in a separate method.

4. **Class `Person` and `Students`**: `Person` is a base class that represents a person with first and last name. `Students` inherits from `Person` and adds the feature of "year", representing the student's year. `Students` has a method `greet` that prints a personalized greeting.

5. **Class `Teste` and `Testes`**: `Teste` is a base class that represents a test with a name. `Testes` inherits from `Teste` and adds a last name to the test. It has a method `imprimir` that prints a personalized message with the name and last name.

6. **Interaction with the user and creation of objects**: The code prompts the user to enter a name and a first name, creating objects of the classes `Testes` and `Students`, respectively, with the information provided and executing specific methods of these objects.

7. **File reading**: Creates an object of the class `ver_arquivo` for a file called "seila.txt", reads its content and prints the content without whitespace at the beginning or end.

8. **Creation of object `person_say` and `another_test`**: Creates objects of these classes and executes their respective methods, showing their functionalities such as returning a personalized greeting and performing arithmetic operations.

This code is a didactic example that covers several concepts of OOP in Python, such as encapsulation (methods and attributes), inheritance (using `super()` to call the constructor of the base class), and polymorphism (overriding methods in the derived class). In addition, it demonstrates file reading and basic interaction with the user through the terminal.


# PT-BR
Este código demonstra o uso de várias funcionalidades da programação orientada a objetos (POO) em Python, através da definição e manipulação de várias classes e objetos. Aqui está um resumo simples do código e o que faz:

1. **Classe `ver_arquivo`**: Esta classe é projetada para lidar com a leitura de arquivos. Ela aceita um nome de arquivo como parâmetro durante a inicialização e tem um método `ler_arquivo` que lê o conteúdo do arquivo e o retorna.

2. **Classe `person_say`**: Representa uma pessoa que pode dizer algo, contendo nome e idade. O método `retorna_say` retorna uma saudação que inclui o nome e a idade da pessoa.

3. **Classe `another_test`**: Esta classe realiza operações aritméticas básicas (adição, subtração, multiplicação e divisão) com dois números fornecidos durante a inicialização. Cada operação é implementada em um método separado.

4. **Classe `Person` e `Students`**: `Person` é uma classe base que representa uma pessoa com nome e sobrenome. `Students` herda de `Person` e adiciona a característica de "ano", representando o ano do estudante. `Students` tem um método `greet` que imprime uma saudação personalizada.

5. **Classe `Teste` e `Testes`**: `Teste` é uma classe base que representa um teste com um nome. `Testes` herda de `Teste` e adiciona um sobrenome ao teste. Tem um método `imprimir` que imprime uma mensagem personalizada com o nome e o sobrenome.

6. **Interação com o usuário e criação de objetos**: O código solicita ao usuário que insira um nome e um primeiro nome, criando objetos das classes `Testes` e `Students`, respectivamente, com as informações fornecidas e executando métodos específicos desses objetos.

7. **Leitura de arquivo**: Cria um objeto da classe `ver_arquivo` para um arquivo chamado "seila.txt", lê seu conteúdo e imprime o conteúdo sem espaços em branco no início ou no fim.

8. **Criação de objeto `person_say` e `another_test`**: Cria objetos destas classes e executa seus respectivos métodos, mostrando suas funcionalidades como retornar uma saudação personalizada e realizar operações aritméticas.

Este código é um exemplo didático que cobre vários conceitos de POO em Python, como encapsulamento (métodos e atributos), herança (usando `super()` para chamar o construtor da classe base), e polimorfismo (sobrescrevendo métodos na classe derivada). Além disso, demonstra a leitura de arquivos e a interação básica com o usuário através do terminal.
