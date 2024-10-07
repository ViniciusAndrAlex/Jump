# Jump
Desafio de Processamento de Dados de Grande Volume

O objetivo deste teste Ã© avaliar suas habilidades em manipular e analisar grandes volumes de dados em Python, de forma eficiente e com consumo otimizado de recursos.

VocÃª receberÃ¡ um arquivo CSV de grande porte, denominado 'vendas.csv', com cerca de 5GB. O arquivo contÃ©m dados de vendas de uma cadeia de varejo. As colunas incluem: Data, Produto, Quantidade, PreÃ§o_UnitÃ¡rio, e Loja.

InstruÃ§Ãµes:
1. Implemente uma soluÃ§Ã£o para ler o arquivo 'vendas.csv' de forma eficiente, considerando o grande volume de dados.
2. Identifique o produto mais vendido em termos de quantidade e canal.
3. Determine qual pais e regiÃ£o teve o maior volume de vendas (em valor).
4. Calcule a mÃ©dia de vendas mensais por produto, considerando o perÃ­odo dos dados disponÃ­veis.

Requisitos:
- Sua soluÃ§Ã£o deve ser capaz de rodar em uma mÃ¡quina com memÃ³ria limitada, nÃ£o assuma que o arquivo inteiro pode ser carregado na memÃ³ria de uma vez.
- Use tÃ©cnicas como leitura em partes (chunking).
- Priorize a eficiÃªncia do processamento.
- O uso de bibliotecas como Pandas Ã© permitido, especialmente com seu recurso de leitura em chunks.
- Documente seu cÃ³digo adequadamente e inclua comentÃ¡rios explicativos sobre suas escolhas de implementaÃ§Ã£o.

Entrega:
- Link do Script Python (.py) no GitHub.
- Um relatÃ³rio em texto explicando como sua soluÃ§Ã£o aborda o problema de grandes volumes de dados, incluindo qualquer otimizaÃ§Ã£o de performance que vocÃª tenha implementado.

Dicas:
- Explore a funÃ§Ã£o `read_csv` do Pandas com o parÃ¢metro `chunksize` para processar o arquivo em partes.
- Considere o uso de estruturas de dados eficientes para armazenamento temporÃ¡rio de informaÃ§Ãµes durante o processamento.
- Avalie o consumo de memÃ³ria e tempo de execuÃ§Ã£o para garantir que sua soluÃ§Ã£o seja realmente eficiente.
