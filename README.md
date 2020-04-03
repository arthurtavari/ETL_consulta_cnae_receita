### CONSULTA DE EMPRESAS NA RECEITA FEDERAL

Participei de um projeto para enriquecimento da base de clientes de um e-commerce e precisei desenvolver um script em Python onde ele consulta o banco de dados e retorna o CNPJ das empresas para integração com a API da ReceitaWS.

Para este repositório criei uma versão resumida onde ao invés de fazer uma consulta direta no banco de dados, fiz o input da base através de um arquivo csv.

#### Recursos utilizados
Para executar o script utilizei a IDE do Visual Studio Code, versão 3 do Python e as bibliotecas pandas, http.client, json, time, requests, sys e re.

#### Base de dados:
     
    database.csv - > Contém os dados das empresas que desejamos buscar. 
    
    backup_inicial.csv - > Dados de backup.  
    
    base_tratada.csv - > Base de dados após finalização completa do processo. 
#    

#### Script para execução do processo:

    consulta_api.py - > Script em Python que todo o processo de busca na base de dados e API

    analise_dados.ipynb -> Script em Python/Jupyter que faz a análise dos dados em CSV. 
    
    
    
    
  
 
  
 
 
 
