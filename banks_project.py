
import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
import sqlite3
from datetime import datetime 


def log_progress(message):
    timestamp_format = '%Y-%h-%d-%H:%M:%S' # Year-Monthname-Day-Hour-Minute-Second 
    now = datetime.now() # get current timestamp 
    timestamp = now.strftime(timestamp_format) 
    with open(r".\\code_log.txt","a") as f: 
        f.write(timestamp + ' : ' + message + '\n')

    
def extract(url, table_attribs):
    pag = requests.get(url).text
    data = BeautifulSoup(pag, 'html.parser')
    df = pd.DataFrame(columns = table_attributes_extract)
    tabelas = data.find_all('tbody')
    linhas = tabelas[0].find_all('tr')
    for linha in linhas:
        col = linha.find_all('td')
        if len(col) != 0:
            data_dict = {'name': col[1].text.strip(),
                         'mc_usd_billion': col[2].text.strip()}
            df1 = pd.DataFrame(data_dict, index=[0])
            df = pd.concat([df, df1], ignore_index=True)  
    return df
def transform(df):
    ''' This function accesses the CSV file for exchange rate
    information, and adds three columns to the data frame, each
    containing the transformed version of Market Cap column to
    respective currencies'''
    mc_usd_list = df["mc_usd_billion"].tolist()
    mc_usd_list = [float(x) for x in mc_usd_list]
    
    mc_eur_list = [np.round(x*0.93, 2) for x in mc_usd_list]
    mc_gbp_list = [np.round(x*0.8, 2) for x in mc_usd_list]
    mc_inr_list = [np.round(x*82.95, 2) for x in mc_usd_list]
    
    df['mc_eur_billion'] = mc_eur_list
    df['mc_gbp_billion'] = mc_gbp_list
    df['mc_inr_billion'] = mc_inr_list
    return df
def load_to_csv(df, output_path):
    ''' This function saves the final data frame as a CSV file in
    the provided path. Function returns nothing.'''
    df.to_csv(output_path)
    
    
def load_to_db(df, sql_connection, table_name):
    
    df.to_sql(table_name, sql_connection, if_exists='replace', index=False)
    
def run_query(query_statement, sql_connection):
    
    print(query_statement)
    query_output = pd.read_sql(query_statement, sql_connection)
    print(query_output)
    
    
url = 'https://web.archive.org/web/20230908091635 /https://en.wikipedia.org/wiki/List_of_largest_banks'

taxa_cambio = 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMSkillsNetwork-PY0221EN-Coursera/labs/v2/exchange_rate.csv'

table_attributes_extract = ['name', 'mc_usd_billion']

table_attributes = ['Name', 'MC_USD_Billion', 'MC_GBP_Billion', 'MC_EUR_Billion', 'MC_INR_Billion']

csv_ = './Largest_banks_data.csv'

database_name = 'banks.db'

table_name = 'largest_banks'

sql_connection = sqlite3.connect('Largest_banks.db')

log_progress('Preliminaries complete. Initiating ETL process')

df = extract(url, table_attributes_extract)

log_progress('Data extraction complete. Initiating Transformation process')

df= transform(df)

log_progress('Data transformation complete. Initiating Loading process')

load_to_csv(df, csv_)

log_progress('Data saved to CSV file')

load_to_db(df, sql_connection, table_name)

log_progress('SQL Connection initiated')

load_to_db(df, sql_connection, table_name)

log_progress('Data loaded to Database as a table, Executing queries')

query_statment = f"SELECT AVG(mc_gbp_billion) FROM {table_name}"

run_query(query_statment, sql_connection)

log_progress('Process complete')

sql_connection.close()

log_progress('Server Connection closed')
