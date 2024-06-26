import shutil
import datetime
import os
from tkinter.filedialog import askdirectory

pastaselecionada = askdirectory()

lista_arquivos = os.listdir(pastaselecionada)

pastabackup = "backup"
nomecompletopastabackup = f"{pastaselecionada}/{pastabackup}"

if not os.path.exists(nomecompletopastabackup):
    os.mkdir(nomecompletopastabackup)

data_atual = datetime.datetime.today().strftime("%Y-%m-%d %H%M%S")

for arquivo in lista_arquivos:
    nomecompletoarquivo = f"{pastaselecionada}/{arquivo}"
    nomefinalarquivo = f"{nomecompletopastabackup}/{data_atual}/{arquivo}"

    if not os.path.exists(f"{nomecompletopastabackup}/{data_atual}"):
        os.mkdir(f"{nomecompletopastabackup}/{data_atual}")

    if "." in arquivo:
        shutil.copy2(nome_completo_arquivo, nome_final_arquivo)
    elif "backup" != arquivo:
        shutil.copytree(nome_completo_arquivo, nome_final_arquivo)
