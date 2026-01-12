import requests, io,pandas as pd

def planilhas(dicionario_links):
    lista_dfs = []

    # Cabeçalho para simular um navegador real
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }

    for nome, link in dicionario_links.items():
        print(f"Baixando: {nome}...")
        url_limpa = link.strip()

        try:
            response = requests.get(url_limpa, headers=headers)
            response.raise_for_status()  # Verifica se deu erro 400 ou 404

            # Lê o CSV a partir do texto baixado usando a biblioteca IO como um tradutor, ja que o pandas espera receber um caminho e o
            #requests entrega uma string de texto grande
            df_planilha = pd.read_csv(io.StringIO(response.text))

            indicador_ano = nome[-2:]
            rotulo_ano = f"20{indicador_ano}-DATA"
            df_planilha.insert(0,"FONTE_DF", rotulo_ano)

            lista_dfs.append(df_planilha)

            # Verificação extra: Se baixou HTML por engano, o Pandas vai criar apenas 1 coluna estranha ou falhar
            #se tiver menos que duas colunas avise que pode ser um erro
            if df_planilha.shape[1] < 2:
                print(f"AVISO: O arquivo baixado de {nome} parece suspeito (poucas colunas). Verifique o link.")
            else:
                lista_dfs.append(df_planilha)
                print(f"{nome} OK ({df_planilha.shape[0]} linhas)")

        except Exception as e:
            print(f"FALHA em {nome}: {e}")

    return lista_dfs


def med_mortes_ano(df_analisado_total_v,df_analisado_total_m):
    lista_anos = ["2020","2021","2022","2023","2024"]
    """o que tem que fazer?
    pegar quantidade mortos totais(nascidos mortos estao inclusos aqui, só pra lembrar)/total de nascidos vivos e mortos
    
    dito isso tenho que entrar na planilha mortos, selecionar todos de um ano. 
    entrar na planilha de vivos e pegar todos os nascimentos de um ano
    e depois entrar de novo na planilha de mortos para pegar todas as linhas com TIPOBITO = 1"""

    for ano in lista_anos:
        filtro_ano_vivos = df_analisado_total_v["FONTE_DF"].str.contains(ano)

        vivos_ano = df_analisado_total_v[filtro_ano_vivos]

        print(f"Linhas totais = {vivos_ano.shape[0]} de {vivos_ano}")
        print(f"total de nascimentos registrados: {vivos_ano.shape[0]}")

        filtro_ano_mortos = df_analisado_total_m["FONTE_DF"]

        mortos_ano = df_analisado_total_m[filtro_ano_mortos]

        print(f"Linhas totais = {vivos_ano.shape[0]} de {vivos_ano}")
        print(f"total de mortes registradas: {vivos_ano.shape[0]}")


