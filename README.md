# BuscaCorreiosTeste

O objetivo deste projeto é obter as informações das buscas que fazemos no site dos correios (https://www2.correios.com.br/sistemas/buscacep/buscaFaixaCEP.cfm). Em seu resultado teremos um arquivo no formato JSONL com as informações de Localidade dos estados, a faixa do CEP de cada local, e um ID do tempo de execução criado para cada linha.

Foi criada uma lista com as siglas dos estados para que fossem lidas um a um. O Link que trazia essas informações foi achado inspecionando o botão de busca da tela dos correios, onde há uma função ConsultarLocalidade. Ou seja, essa função busca o que foi preenchido no campo.

Observação importante: Para criação desse projeto utilizei a IDE PyCharm

# ♡ Configurando o projeto no PyCharm

- Você precisará de uma IDE que leia py. 
- Você usará o Selenium no seu projeto, e se estiver utilizando o GoogleChrome, deverá baixar o chromedriver - Para baixar o chromedriver você precisará saber a versão do navegador, e então baixar o arquivo correto através desse link: https://chromedriver.chromium.org/downloads 
- Coloque o arquivo baixado dentro da pasta do seu projeto 
- Vamos à IDE escolhida, o Pycharm. Precisei importar: Selenium, re, json, datetime, time. Instale no seu terminal com _pip install_

# ♡ Executando o projeto

- Após ter tudo configurado no seu computador, com os arquivos disponibilizados por aqui, execute o projeto. Nessa IDE, o executor é o "Run". 
- O projeto irá fazer uma leitura de todos os estados citados no código. Nesse mesmo tempo, na pasta do seu projeto, você verá os arquivos sendo criados com as informações solicitadas.



Aviso ❤
_Se por acaso você deseja executar o seu arquivo em outra IDE que leia py. é importante ter essas configurações. Ou se deseja criar uma cópia desses arquivos e visualizar no seu prompt de comando, tenha o python instalado no seu windows. Feito isso, basta abrir o prompt de comando, ir até o local do código e digitar o python código.py.

