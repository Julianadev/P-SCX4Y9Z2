from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import os
import traceback


def buscar_cep(navegador, cep):
    navegador.get('https://buscacepinter.correios.com.br/app/endereco/index.php')

    try:
        WebDriverWait(navegador, 10).until(EC.visibility_of_element_located((By.NAME, 'endereco')))

        navegador.find_element(By.NAME, 'endereco').send_keys(cep)
        navegador.find_element(By.NAME, 'btn_pesquisar').click()

        WebDriverWait(navegador, 10).until(EC.visibility_of_element_located((By.XPATH, xpath_rua)))

        rua = navegador.find_element(By.XPATH, xpath_rua).text
        bairro = navegador.find_element(By.XPATH, xpath_bairro).text
        localizacao = navegador.find_element(By.XPATH, xpath_localizacao).text
        cep = navegador.find_element(By.XPATH, xpath_cep).text

        return rua, bairro, localizacao, cep
    except Exception as e:
        print(f'Erro ao buscar CEP {cep}: {str(e)}')

        traceback.print_exc()
        return None, None, None, None

xpath_rua = '//*[@id="resultado-DNEC"]/tbody/tr/td[1]'
xpath_bairro = '//*[@id="resultado-DNEC"]/tbody/tr/td[2]'
xpath_localizacao = '//*[@id="resultado-DNEC"]/tbody/tr/td[3]'
xpath_cep = '//*[@id="resultado-DNEC"]/tbody/tr/td[4]'

df = pd.DataFrame(columns=['Endereço', 'Bairro', 'Localidade', 'CEP'])

try:
    caminho_arquivo = input('Digite o caminho do arquivo: ').strip('"')
    if caminho_arquivo.lower().endswith(('xlsx', '.xls', '.csv')):
        caminho_arquivo = os.path.abspath(caminho_arquivo)

        df_leitura = pd.read_excel(caminho_arquivo)

        options = webdriver.EdgeOptions()
        options.add_argument("--headless=new")
        navegador = webdriver.Edge(options=options)

        for linha, row in df_leitura.iterrows():
            cep_atual = row['CEP']
            rua, bairro, localizacao, cep = buscar_cep(navegador, cep_atual)

            df.loc[len(df.index)] = [rua, bairro, localizacao, cep]

        navegador.close()

        df.to_excel(caminho_arquivo, index=False)
        print(f'Arquivo foi salvo com sucesso em {caminho_arquivo}')

        os.startfile(caminho_arquivo)
    else:
        print('Caminho inválido.')
except FileNotFoundError as e:
    print('Caminho inválido', e)
