![img](https://raw.githubusercontent.com/arthurtavari/portfolio_data_science/master/img/layout.jpg)
# Projeto:
### Consulta de Empresas na Receita Federal
Projeto para enriquecimento da base de clientes de um e-commerce, precisei desenvolver um script em Python onde ele consulta o banco de dados e retorna o CNPJ das empresas para integração com a API da ReceitaWS, retornando os dados cadastrais na Receita Federal. 
     <br>
     <br>
Para este repositório criei uma versão resumida onde ao invés de fazer uma consulta direta no banco de dados, fiz o input da base através de um arquivo csv.
     <br>
     <br>
#### Base de dados:
    
    database.csv - > Contém os dados das empresas que desejamos buscar. 
    
    base_tratada.csv - > Base de dados da consulta na Receita Federal já tratada.     

#### Script para execução do processo:

    consulta_api.py - > Script em Python com todo o processo de busca na base de dados e API

    analise_dados.ipynb -> Script em Python/Jupyter que faz a análise dos dados em CSV. 
    
    
<i>Toda base que utilizei para consulta são de empresas de capital aberto e informações disponíveis no site da B3</i>
