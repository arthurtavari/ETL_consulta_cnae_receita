#### IMPORTANDO BIBLIOTECAS ####
import pandas as pd
import http.client
import json
import time
import requests
import sys
import re

#### IMPORTAÇÃO DE DADOS ####
dados = pd.read_csv('data/database.csv', sep=',')
cnpj = dados['CNPJ']
razao_social = dados['Razão social']

#### TRATAMENTO DE RETIRADA DA PONTUAÇÃO PARA CONSULTA ####
for caracteres in "./-":
    cnpj = cnpj.str.replace(caracteres,"")
    
dados.info()

#### VARIÁVEIS API ####
    # CRIEI AS VARIÁVEIS PARA RECEBER OS DADOS DA API
nome_list = [] 
abertura_list = []  
cnpj_list = [] 
email_list = []
telefone_list = []
tipo_list = []
natureza_juridica_list = []
bairro_list = []
cep_list = []
uf_list = []
fantasia_list = []   
cnae_list = []
erro_list = []
situacao_list = []
text_list = [] 

#### PROCESSO DE INTEGRAÇÃO COM API E COLETA DE DADOS ####

# DADOS PARA CONEXÃO COM A API RECEITAWS
def api_receita_ws():
    i = 0
    while i < len(cnpj):
        conn = requests.get("https://www.receitaws.com.br/v1/cnpj/" + str(cnpj[i]))
        JSON = conn.json()      
        
        #### LISTAS PARA CONSULTAR O JSON E SALVAR INFORMAÇÕES DA API ####
        if(JSON['status'] == 'OK' ):
            atividade_principal = JSON['atividade_principal']
            zero = atividade_principal[0]
            if('nome' in JSON):            
                nome_list.extend([JSON['nome']])
            else:
                nome_list.extend('-')     
                
            if('abertura' in JSON):
                abertura_list.extend([JSON['abertura']])
            else:
                abertura_list.extend('-')
            
            if('cnpj' in JSON): 
                cnpj_list.extend([JSON['cnpj']])
            else:
                cnpj_list.extend('-')
            
            if('email' in JSON):
                email_list.extend([JSON['email']])
            else: 
                   email_list.extend('-')
            
            if('telefone' in JSON):
                telefone_list.extend([JSON['telefone']])
            else: 
                telefone_list.extend('-')
            
            if('tipo' in JSON): 
                tipo_list.extend([JSON['tipo']])
            else: 
                tipo_list.extend('-')  
            
            if('natureza_juridica' in JSON):
                natureza_juridica_list.extend([JSON['natureza_juridica']])
            else: 
                natureza_juridica_list.extend('-')
            
            if('code' in zero):
                cnae_list.extend([zero['code']])
            else:
                cnae_list.extend('-')
                
            if('text' in zero):
                text_list.extend([zero['text']])
            else:
                text_list.extend('-')  
                
            if('bairro' in JSON):
                bairro_list.extend([JSON['bairro']])
            else: 
                bairro_list.extend('-')  
            
            if('cep' in JSON):
                cep_list.extend([JSON['cep']])
            else:
                cep_list.extend('-')
                
            if('uf' in JSON):
                uf_list.extend([JSON['uf']])
            else: 
                uf_list.extend('-') 
            
            if('fantasia' in JSON):    
                fantasia_list.extend([JSON['fantasia']])
            else:
                fantasia_list.extend('-') 
                
            if('situacao' in JSON):    
                situacao_list.extend([JSON['situacao']])
            else:
                fantasia_list.extend('-')

            # AQUI RETORNA O CNPJ CONSULTADO, STATUS E QUAL A LINHA DE CONSULTA
            print(cnpj[i],'STATUS:',JSON['status'], 'LINHA:', i)

        # AQUI RETORNA O CNPJ CONSULTADO, STATUS E QUAL A LINHA DE CONSULTA / OBJETIVO É IDENTIFICAR QUAL CNPJ DEU ERRO      
        else: 
            erro_list.extend(str(cnpj[i]))
            print(cnpj[i],'ERRO NA LINHA', i, JSON['message']) 
           
        i += 1
        # TEMPORIZADOR PARA FAZER 3 CONSULTAS POR MINUTO / REGRAS DA API GRATUITA RECEITAWS
        time.sleep(20)
        
        # CRIEI ESSA CONDICIONAL PARA SER UTILIZADA EM BASE DE DADOS MUITO GRANDE, CASO DÊ UM ERRO NO MEIO DO PROCESSO TEMOS UMA LINHA DE BACKUP. BASTA CRIAR UMA COPIA DO SCRIPT DAS LINHAS 135 A 138 E REPLICAR, ALTERANDO A CONDIÇÃO E NOME DO CSV (SUGESTÃO A CADA 10 MIL CONSULTAS)
        if(i == 5):
         CSV_API = pd.DataFrame(list(zip(razao_social, nome_list, cnpj_list, text_list, cnae_list, situacao_list, fantasia_list, abertura_list, email_list, telefone_list, tipo_list, natureza_juridica_list, bairro_list, cep_list, uf_list)), columns =['razao_social', 'nome', 'cnpj', 'text', 'cnae', 'situacao', 'fantasia', 'abertura', 'email', 'telefone', 'tipo', 'natureza_juridica', 'bairro', 'cep', 'uf'])
         CSV_API.to_csv('data/backup_inicial.csv', index=False)
         print("IMPRESSÃO BKP")

api_receita_ws()

# APÓS RODAR TODO O PROCESSO SALVAMOS UMA VERSÃO FINAL COM OS DADOS COMPLETOS PARA UTILIZAÇÃO 
CSV_API = pd.DataFrame(list(zip(razao_social, nome_list, cnpj_list, text_list, cnae_list, situacao_list, fantasia_list, abertura_list, email_list, telefone_list, tipo_list, natureza_juridica_list, bairro_list, cep_list, uf_list)), columns =['razao_social', 'nome', 'cnpj', 'text', 'cnae', 'situacao', 'fantasia', 'abertura', 'email', 'telefone', 'tipo', 'natureza_juridica', 'bairro', 'cep', 'uf'])
CSV_API.to_csv('data/base_tratada.csv', index=False)     
  
print('PROCESSO FINALIZADO')