# Projeto - Calculadora de idade

<div style="text-align: justify">A calculadora de idade é uma incrível ideia de projeto de codificação para iniciantes. Se você é novo em qualquer linguagem de programação, tente fazer uma calculadora de idade. É um aplicativo onde um usuário insere sua data de nascimento como entrada e o aplicativo fornece sua idade como saída.</div>

## Calculadora de idade usando Python

Para criar uma calculadora de idade, você precisa de duas datas:

- Data de hoje
- Data de nascimento

<div style="text-align: justify">
Você pode pedir ao usuário as duas datas ou apenas pedir a data de nascimento e usar a data de hoje no próprio computador. Pedir o aniversário parece apenas uma opção mais amigável.
</div>

## Passos realizados 

1. Primeiro é definida uma função Python onde estou pedindo três entradas do usuário:
   - a: ano do nascimento
   - m: mês do nascimento 
   - d: dia do nascimento  

2. Logo após, estou importando o módulo datetime em Python 
3. Então, na próxima linha, estou pegando a data de hoje usando o método datetime.now() do módulo datetime
4. Em seguida, introduzi uma nova variável na próxima linha como data_nascimento, onde estou usando a data de nascimento como entrada fornecida pelo usuário
5. Por fim, subtraio o data_nascimento com a data de hoje e dividindo por 365,25 e em seguida é retornada a idade do usuário.