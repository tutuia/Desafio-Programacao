<h1 align="center">Desafio Programacao Academia Capgemini 2022</h1>
<p align="center">Projeto composto por três arquivos de código desenvolvido com o objetivo de cumprir o desafio de programação proposto pela Academia Capgemini como uma das etapas do processo seletivo </p>
<p align="center">
 <a href="#Pré requisitos">Pré-requisitos</a> •
 <a href="#Questões do desafio">Questões</a> • 
 <a href="#autor">Autor</a>
</p>
<h4 align="center"> 
	Projeto Concluído
</h4>

### Pré requisitos
Para executar os códigos desse projeto é necessário a instalação do Python em sua máquina, a versão mais recente (até a data em que este documento foi escrito) e que foi utilizada para o desenvolvimento e teste deste foi [Python 3.10.2](https://www.python.org/)

### Questões do desafio
As questões propostas foram resolvidas utilizando a linguagem de programação Python.

#### Questão 1
##### Escreva um algoritmo que mostre na tela uma escada de tamanho n utilizando o caractere * e espaços. A base e altura da escada devem ser iguais ao valor de n. A última linha não deve conter nenhum espaço.
##### Solução obtida:
O arquivo desafio_q1_v2.py recebe como entrada um valor inteiro maior ou igual a zero, para qualquer outro valor de entrada (n) é retornada a mensagem 'entrada invalida. Informe um inteiro positivo' e solicitado que o usuário informe um novo valor. Após a entrada de um valor válido o programa retorna uma escada conforme solicitado.

Resposta obtida à entrada 12 no IDLE Shell 3.10.2:

![image](https://user-images.githubusercontent.com/16008722/154345021-10aeda60-78e6-4ea6-804d-5f2ab1f1443e.png)

#### Questão 2
##### Débora se inscreveu em uma rede social para se manter em contato com seus amigos. A página de cadastro exigia o preenchimento dos campos de nome e senha, porém a senha precisa ser forte. O site considera uma senha forte quando ela satisfaz os seguintes critérios: Possui no mínimo 6 caracteres; Contém no mínimo 1 digito; Contém no mínimo 1 letra em minúsculo; Contém no mínimo 1 letra em maiúsculo; Contém no mínimo 1 caractere especial; Os caracteres especiais são: !@#$%^&*()-+
##### Solução obtida:
O arquivo desafio_q2_v3.py recebe como entrada uma string e primeiro armazena na variável missing_size a diferença entre a quantidade mínima de caracteres (nesse caso 6) e o tamanho da string. Depois, transformando a string em lista e com o auxílio da função for, analisa cada caractere da senha recebida até que os outros quatro elementos obrigatórios sejam encontrados ou até que chegue ao final da lista de caracteres, sempre que um novo requisito é cumprido -1 é adicionado à variável inteira missing_char. A variável control foi implementada para garantir que cada requisito seja descontado apenas uma vez por meio de operações de bit onde: 
* 00000001 = contém dígito
* 00000010 = contém minúscula
* 00000100 = contém maiúscula
* 00001000 = contém caractere especial 

Obs.: Os caractéres especiais considerados são apenas aqueles citados explicitamente no enunciado da questão.
Ao final do programa a variável com maior valor, entre missing_char e missing_size, representa a quantidade de caractéres mínima que devem ser acrescidos à senha.
Resposta obtida à entrada '@GGGGGGG' no IDLE Shell 3.10.2:

![image](https://user-images.githubusercontent.com/16008722/154349622-ead16b18-2283-4c80-9005-a4d5a4237e80.png)


#### Questão 3
##### Duas palavras podem ser consideradas anagramas de si mesmas se as letras de uma palavra podem ser realocadas para formar a outra palavra. Dada uma string qualquer, desenvolva um algoritmo que encontre o número de pares de substrings que são anagramas.
##### Solução obtida:
O arquivo desafio_q3.py recebe uma palavra como entrada e converte todos os caracteres para minúsculo e percorre cada caractere em busca de alguma repetição, cada caractere inédito é aramazendo em uma lista, se um caractere se repete temos um par de anagramas e o contador é incrementado em um. Também são armazenados e comparados os valores entre (posição_da_ocorrencia_anterior) até (posição_da_ocorrencia_atual - 1) e (posição_da_ocorrencia_anterior + 1) até (posição_da_ocorrencia_aual), se forem iguais há outro par de anagramas e o contador é incrementado em 1.
Resposta obtida à entrada 'beterraba' no IDLE Shell 3.10.2:

![image)](https://user-images.githubusercontent.com/16008722/154352398-22e05c3f-da71-45bc-92eb-37993205a4f7.png)


Obs.: As quatro linhas de código que estão comentadas permitem o armazenamento e visualização dos pares encontrados.
Obs.2: Quando os pares são de caracteres únicos a lista 'anagramas' armazena o valor apenas uma vez. 

### Autora
Thuanny Luiza, Estudante de Engenharia de Computação - UFG.
