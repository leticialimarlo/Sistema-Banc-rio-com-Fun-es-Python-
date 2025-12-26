🏦 Sistema Bancário Otimizado com Python
Refatoração de um sistema bancário simples para um modelo modularizado, aplicando conceitos de Clean Code e boas práticas de desenvolvimento em Python.

📝 Descrição do Desafio
O objetivo deste projeto foi otimizar a estrutura de um sistema bancário anterior, dividindo as operações em funções reutilizáveis e implementando novas funcionalidades para gestão de clientes e contas correntes.

🛠️ Funcionalidades Implementadas
Operações Bancárias
Depósito: Realizado através de argumentos estritamente posicionais (positional-only).

Saque: Implementado com argumentos estritamente nomeados (keyword-only), garantindo maior clareza na passagem de limites e saldo.

Extrato: Exibe as movimentações formatadas utilizando uma mistura de argumentos posicionais e nomeados.

Gestão de Clientes e Contas
Filtragem de Usuário: Busca otimizada por CPF dentro de uma lista de dicionários.

Criação de Usuário: Cadastro de nome, data de nascimento e endereço, com validação de CPF único para evitar duplicidade.

Criação de Conta Corrente: Vincula automaticamente uma nova conta a um usuário existente através do CPF.

Listagem de Contas: Exibição tabular das contas criadas utilizando a biblioteca textwrap para formatação visual limpa.

🛠️ Além dos requisitos do professor, adicionei camadas extras de robustez:

Tratamento de Exceções: Uso de blocos try/except para capturar ValueError e impedir que o programa feche caso o usuário digite letras em campos de valor.

Sanitização de CPF: Implementação de limpeza de strings para aceitar CPFs com ou sem pontuação (., -), padronizando o armazenamento.

Interface de Usuário (UI): Uso de constantes para padronizar mensagens de Alerta e Sucesso em todo o sistema.# Sistema-Banc-rio-com-Fun-es-Python-