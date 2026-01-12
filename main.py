import time
from estrutura import planilhas
import pandas as pd


inicio = time.time()
dict_vivos = {
    "vivos20": "https://docs.google.com/spreadsheets/d/1n5Pw1Yahm1kvRNKXw_cfRdmveP-hTWuJ01pWrJti3oU/gviz/tq?tqx=out:csv&gid=884066373",
    "vivos21": "https://docs.google.com/spreadsheets/d/1YMKgQkopv1tPtn7xnwVbmkS2grfpI_pXY2md_yfn_FA/gviz/tq?tqx=out:csv&gid=1373927302",
    "vivos22": "https://docs.google.com/spreadsheets/d/11_E4kRnFBNid55lkbz5aBWnTQywF_aGM8mNcb7L68Vo/gviz/tq?tqx=out:csv&gid=1190011185",
    "vivos23": "https://docs.google.com/spreadsheets/d/1OTavt2nCziBzDrrcS0kDpGxPmi4F_wwJtrWwvend2-s/gviz/tq?tqx=out:csv&gid=549944355",
    "vivos24": "https://docs.google.com/spreadsheets/d/1wWPoblBouNx8mpqx3d63FgaF2oPnzJ8_wPqalQVCYtY/gviz/tq?tqx=out:csv&gid=1055378626"
}

dict_mortos = {
    "mortos20": "https://docs.google.com/spreadsheets/d/1OtFJws2CXaS4240uDJhtawwhr8hQFZiuqOaN3qdDTJ8/gviz/tq?tqx=out:csv&gid=658561597",
    "mortos21": "https://docs.google.com/spreadsheets/d/1Lcg6ZvxW25jfiIFxDkeNsaPeCUYJwmuGO69I84-Yy5c/gviz/tq?tqx=out:csv&gid=1654654312",
    "mortos22": "https://docs.google.com/spreadsheets/d/10Ek1M6PCkVMf39YC55Qy9aNXjZhotVui5DgXqzg5ivM/gviz/tq?tqx=out:csv&gid=709207175",
    "mortos23": "https://docs.google.com/spreadsheets/d/130z1cbT73SXnWGXSdW1QFpyX_-ESD_iismrSz4y4tGk/gviz/tq?tqx=out:csv&gid=1910813370",
    "mortos24": "https://docs.google.com/spreadsheets/d/11libakcuJNOnU3nm81xoRXXFn2oWHA-9z-rbur_ACNk/gviz/tq?tqx=out:csv&gid=708934713"
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