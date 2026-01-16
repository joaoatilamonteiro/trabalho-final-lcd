import time
from estrutura import planilhas
import pandas as pd


inicio = time.time()
dict_vivos = {
    "vivos20": "https://dados.fortaleza.ce.gov.br/dataset/af6e1ab3-7978-4c21-9f8f-defea2158cd6/resource/1f513892-839a-4759-8acf-ba5c463caa3b/download/dados-de-nascidos-vivos.csv",
    "vivos21": "https://dados.fortaleza.ce.gov.br/dataset/af6e1ab3-7978-4c21-9f8f-defea2158cd6/resource/0f683b26-ad45-466f-a4dd-fde1de82e31c/download/dados-de-nascidos-vivos-2021.csv",
    "vivos22": "https://dados.fortaleza.ce.gov.br/dataset/af6e1ab3-7978-4c21-9f8f-defea2158cd6/resource/18a62112-6375-4397-b906-f45c3420c5d1/download/dados-de-nascidos-vivos-2022.csv",
    "vivos23": "https://dados.fortaleza.ce.gov.br/dataset/af6e1ab3-7978-4c21-9f8f-defea2158cd6/resource/d3a81220-639d-4dc7-bd91-2e8171873a55/download/dados-de-nascidos-vivos-2023.csv",
    "vivos24": "https://dados.fortaleza.ce.gov.br/dataset/af6e1ab3-7978-4c21-9f8f-defea2158cd6/resource/a19af922-15c8-43e7-8a8b-3fbe6532eeac/download/dados-de-nascidos-vivos-2024-jun.csv"
}

dict_mortos = {
    "mortos20": "https://dados.fortaleza.ce.gov.br/dataset/af6e1ab3-7978-4c21-9f8f-defea2158cd6/resource/e121a844-c95a-49ad-8c31-ecfcdd6ef32b/download/dados-dos-obitos.csv",
    "mortos21": "https://dados.fortaleza.ce.gov.br/dataset/af6e1ab3-7978-4c21-9f8f-defea2158cd6/resource/1a6a178f-90f8-4920-aadc-0b4c8ec652eb/download/dados-dos-obitos-2021.csv",
    "mortos22": "https://dados.fortaleza.ce.gov.br/dataset/af6e1ab3-7978-4c21-9f8f-defea2158cd6/resource/65adaf6d-a3b3-4029-902d-9975772ea693/download/dados-dos-obitos-2022.csv",
    "mortos23": "https://dados.fortaleza.ce.gov.br/dataset/af6e1ab3-7978-4c21-9f8f-defea2158cd6/resource/c7ea26cf-af88-4816-8e66-512e7d6c3817/download/dados-dos-obitos-2023.csv",
    "mortos24": "https://dados.fortaleza.ce.gov.br/dataset/af6e1ab3-7978-4c21-9f8f-defea2158cd6/resource/9a6b5532-c5a1-4ac3-a5bb-a94b713ae6ed/download/dados-dos-obitos-2024-jun.csv"
}


print("\n--- Processando VIVOS ---")
lista_vivos = planilhas(dict_vivos)

if lista_vivos:
    dfs_final_vivos = pd.concat(lista_vivos, ignore_index=True)
    dfs_final_vivos.to_csv("dfs_final_vivos.csv", index=False)
    print(f"Arquivo 'dfs_final_vivos.csv' salvo com sucesso!")
else:
    print("NENHUMA planilha de VIVOS foi baixada.")

print("\n--- Processando MORTOS ---")
lista_mortos = planilhas(dict_mortos)

if lista_mortos:
    dfs_final_mortos = pd.concat(lista_mortos, ignore_index=True)
    dfs_final_mortos.to_csv("dfs_final_mortos.csv", index=False)
    print(f"Arquivo 'dfs_final_mortos.csv' salvo com sucesso!")
else:
    print("NENHUMA planilha de MORTOS foi baixada.")

fim = time.time()
print("-" * 30)
print(f"Tempo total: {fim - inicio:.2f} segundos")