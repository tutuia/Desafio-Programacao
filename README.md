<h1 align="center">Desafio Programacao Academia Capgemini 2022</h1>
<p align="center">Projeto composto por três arquivos de código desenvolvido com o objetivo de cumprir o desafio de programação proposto pela Academia Capgemini como uma das etapas do processo seletivo </p>
<p align="center">
 <a href="#objetivo">Objetivo</a> •
 <a href="#roadmap">Roadmap</a> • 
 <a href="#tecnologias">Tecnologias</a> • 
 <a href="#contribuicao">Contribuição</a> • 
 <a href="#licenc-a">Licença</a> • 
 <a href="#autor">Autor</a>
</p>
<h4 align="center"> 
	Projeto Concluído
</h4>

### Pré requisitos
Para executar os códigos desse projeto é necessário a instalação do Python em sua máquina, a versão mais recente (até a data em que este documento foi escrito) e que foi utilizada para o desenvolvimento e teste deste foi [Python 3.10.2](https://www.python.org/)

### Questões do desafio

#### Questão 1
##### Escreva um algoritmo que mostre na tela uma escada de tamanho n utilizando o caractere * e espaços. A base e altura da escada devem ser iguais ao valor de n. A última linha não deve conter nenhum espaço.
##### Solução obtida:
O arquivo desafio_q1_v2 recebe como entrada um valor inteiro maior ou igual a zero, para qualquer outro valor de entrada (n) é retornada a mensagem 'entrada invalida. Informe um inteiro positivo' e solicitado que o usuário informe um novo valor. Após a entrada de um valor válido o programa retorna uma escada conforme solicitado.

![image](https://user-images.githubusercontent.com/16008722/154345021-10aeda60-78e6-4ea6-804d-5f2ab1f1443e.png)

#### Questão 2
##### Débora se inscreveu em uma rede social para se manter em contato com seus amigos. A página de cadastro exigia o preenchimento dos campos de nome e senha, porém a senha precisa ser forte. O site considera uma senha forte quando ela satisfaz os seguintes critérios: Possui no mínimo 6 caracteres; Contém no mínimo 1 digito; Contém no mínimo 1 letra em minúsculo; Contém no mínimo 1 letra em maiúsculo; Contém no mínimo 1 caractere especial; Os caracteres especiais são: !@#$%^&*()-+
##### Solução obtida:
O arquivo desafio_q2_v3 recebe como entrada uma string e primeiro armazena na variável missing_size a diferença entre a quantidade mínima de caracteres (nesse caso 6) e o tamanho da string. Depois, transformando a string em lista e com o auxílio da função for, analisa cada caractere da senha recebida até que os outros quatro elementos obrigatórios sejam encontrados ou até que chegue ao final da lista de caracteres, sempre que um novo requisito é cumprido -1 é adicionado à variável inteira missing_char. A variável control foi implementada para garantir que cada requisito seja descontado apenas uma vez por meio de operações de bit onde: 
* 00000001 = contém dígito
* 00000010 = contém minúscula
* 00000100 = contém maiúscula
* 00001000 = contém caractere especial 

Obs.: Os caractéres especiais considerados são apenas aqueles citados explicitamente no enunciado da questão.
Ao final do programa a variável com maior valor, entre missing_char e missing_size, representa a quantidade de caractéres mínima que devem ser acrescidos à senha.

![image](https://user-images.githubusercontent.com/16008722/154349622-ead16b18-2283-4c80-9005-a4d5a4237e80.png)

#### Questão 3
#### Questão 4

### Autora
Thuanny Luiza, Estudante de Engenharia de Computação - UFG
