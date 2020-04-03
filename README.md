### CONSULTA DE EMPRESAS NA RECEITA FEDERAL

Participei de um projeto para enriquecimento da base de clientes de um e-commerce e precisei desenvolver um script em Python onde ele consulta o banco de dados e retorna o CNPJ das empresas para integração com a API da ReceitaWS.

Para este repositório criei uma versão resumida onde ao invés de fazer uma consulta direta no banco de dados, fiz o input da base através de um arquivo csv.

#### Recursos utilizados:
Para executar o script utilizei a IDE do Visual Studio Code, versão 3 do Python e as bibliotecas pandas, http.client, json, time, requests, sys e re.

#### Estrutura:
    Pasta data
    Contém 3 arquivos em csv para integração com o script
#
    database.csv
    Contém os dados das empresas que desejamos buscar. 

#
    
    /backup_inicial.csv
    Após o script iniciar, ele salva um backup após x consultas, no nosso teste fizemos apenas backup após 5 consultas

#

    /base_tratada.csv
    Após término da consulta o script salva um arquivo final que contém a Razão Social e demais dados de retorno da API.


    



consulta_api.py
    
    
  
 
  
 
 
 
