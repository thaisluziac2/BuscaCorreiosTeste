from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import re
import json
import datetime
import time


options = Options()
options.add_argument('window-size=400,800')

navegador = webdriver.Chrome(options=options)


estados = ["AC", "AL", "AM", "AP", "BA", "CE", "DF", "ES", "GO", "MA", "MG", "MS", "MT", "PA", "PB", "PE", "PI",
           "PR", "RJ", "RN", "RO", "RR", "RS", "SC", "SE", "SP", "TO"]
for uf in estados:
   
    url = f'https://www2.correios.com.br/sistemas/buscacep/consultaLocalidade.cfm?mostrar=1&UF={uf}'
    navegador.get(url)
    letras = navegador.find_elements_by_name('Letra')
    tamanho_alfabeto = len(letras)
    # inicializa listas
    localidades = []
    ceps = []
    ids = []

    # itera sobre as letras do alfabeto
    pagina = 1
    for n in range(tamanho_alfabeto-1):
        # clica na letra
        letras = navegador.find_elements_by_name('Letra')
        letras[n].click()

        # busca os dados e formata
        text = str(navegador.page_source)
        localidades_letra = re.findall('(?<=<td width="150">)(.*?)(?=\</td>)', text)
        ceps_letra = re.findall('[0-9]{5}-[0-9]{3}', text)
        ceps_letra = [cep + " a " + str(int(cep[:-4])+1) + "-999" for cep in ceps_letra]
        ids_letras = [datetime.datetime.now().timestamp() for _ in ceps_letra]

        # salva os dados
        localidades += localidades_letra
        ceps += ceps_letra
        ids += ids_letras

        # delay para processar
        time.sleep(1)


        # volta a tela de selecao de letras
        voltar = navegador.find_element_by_xpath('/html/body/div/a[1]')
        voltar.click()

    # reseta o contator
    pagina = 1

    resultado = {"localidades": localidades, "ceps": ceps, "id": ids}
    output_filepath = f"{uf}.jsonl"
    with open(output_filepath, "w") as jsonl_file:
        json.dump(resultado, jsonl_file, indent=4, ensure_ascii=False)