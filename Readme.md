

## Cenário
  compilar uma lista dos 10 maiores bancos do mundo classificados por capitalização de mercado em bilhões de dólares americanos. Além disso, é necessário transformar os dados e armazená-los em dólares americanos, libras esterlinas, euros e rúpias indianas de acordo com as informações de taxa de câmbio disponibilizadas em um arquivo CSV. A tabela de informações processadas deve ser salva localmente em formato CSV e como uma tabela de banco de dados. Gerentes de diferentes países irão consultar a tabela do banco de dados para extrair a lista e observar o valor da capitalização de mercado em sua própria moeda.

### Fonte:
  [Lista dos maiores bancos](https://web.archive.org/web/20230908091635 /https://en.wikipedia.org/wiki/List_of_largest_banks)

## Etapas:

* Escrever uma função para extrair as informações tabulares da URL fornecida sob o título "Por Capitalização de Mercado" e salvá-las em um data frame.
* Escrever uma função para transformar o data frame adicionando colunas para Capitalização de Mercado em libras esterlinas (GBP), euros (EUR) e rúpias indianas (INR), arredondadas para 2 casas decimais, com base nas informações de taxa de câmbio compartilhadas em um arquivo CSV.
* Escrever uma função para carregar o data frame transformado para um arquivo CSV de saída.
* Escrever uma função para carregar o data frame transformado para um servidor de banco de dados SQL como uma tabela.
* Escrever uma função para executar consultas na tabela do banco de dados.
* Excecutar as seguintes consultas na tabela do banco de dados:
  - Extrair as informações para o escritório de Londres, ou seja, Nome e MC_GBP_Billion.
  - Extrair as informações para o escritório de Berlim, ou seja, Nome e MC_EUR_Billion.
  - Extrair as informações para o escritório de Nova Delhi, ou seja, Nome e MC_INR_Billion.
* Escrever uma função para registrar o progresso do código.

**
Este projeto foi desenvolvido como parte da Formação de Engenheiro de Dados da IBM na plataforma Coursera. Créditos ao curso e aos seus instrutores por fornecerem a base para este exercício.





