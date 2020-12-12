# Prova técnica

O desafio consiste em criar uma spider com o framework Scrapy (https://docs.scrapy.org/en/latest/intro/tutorial.html ) que deverá acessar o site http://quotes.toscrape.com e obter todos os quotes que:

**Condições da Busca:**
 - Regra 1: contenham a tag "life" e que sejam do autor "Mark Twain"
 - Regra 2: contenham a palavra "truth" no texto do quote, de qualquer  
   autor


**Condições do Desafio:**
 - Embora seja possível acessar este site sem efetuar login, para
   completar este desafio o login será obrigatório. Qualquer usuário e
   senha funciona neste site.
 - Deverá ser criado um pipeline no scrapy para tratar o armazenamento
   dos quotes obtidos.
 - O texto dos quotes obtidos deverão ser armazenados cada um num
   arquivo txt separado.
 - Os seguintes dados sobre os quotes deverão ser armazenados em um
   arquivo CSV, utilizando a biblioteca pandas: autor, tags, número da
   página, número da regra, nome do arquivo txt correspondente.
 - O CSV deverá ser salvo com codificação "utf 8 com BOM" e separado por
   ";".
 - O código deverá ser disponibilizado num repositório do GitHub. Ao
   invés de colocar o código todo de uma vez, faça os commits
   gradualmente, com mensagens claras a respeito de cada alteração
   enviada para o repositório, demonstrando bom uso da ferramenta.
   

**Desafio Adicional:**

 - Como desafio adicional, crie testes unitários (com pytest) para todas
   as funções que você criou, testando o valor de retorno e todas as
   chamadas que foram feitas a outras funções (assert_called_with,
   assert_has_calls, etc). Deverão ser criados mocks para que não sejam
   chamadas funções externas à função que está sendo testada. Utilize o
   pytest-cov para verificar a porcentagem de cobertura.
