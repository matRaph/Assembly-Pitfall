import sys
import numpy as np 
import matplotlib.pyplot as plt 
from PIL import Image

data = np.array(Image.open(r"C:\Users\rapha\OneDrive\Área de Trabalho\Facul\Arquitetura\Pitfall_Project/pitfallO.png"))
linhas = data.shape[0]
colunas = data.shape[1]
indx=0
x=0

for i in data:
    linha="l3n"+str(x).format('999')+": .word "
    x+=1
    for j in i:
        indx+=1
        r = hex(int(j[0])).replace('0x', '')
        g = hex(int(j[1])).replace('0x', '')
        b = hex(int(j[2])).replace('0x', '')
        linha = linha = linha+'0x00'+r+g+b+' '

    print(linha)