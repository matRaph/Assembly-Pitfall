import sys
import numpy as np 
import matplotlib.pyplot as plt 
from PIL import Image

# Load the data variable with the selected image
data = np.array(Image.open(r"C:\Users\rapha\OneDrive\Área de Trabalho\Facul\Arquitetura\Pitfall_Project/pitfallO.png"))

linhas = data.shape[0]
colunas = data.shape[1]
indx=0
x=0

# Print the hexadecimal rgb code of each pixel in the image and add "lnx: .word " in each line for mips to recognize
for i in data:
    linha="ln0"+str(x).format('999')+": .word "
    x+=1
    for j in i:
        indx+=1
        r = hex(int(j[0])).replace('0x', '')
        g = hex(int(j[1])).replace('0x', '')
        b = hex(int(j[2])).replace('0x', '')
        linha = linha = linha+'0x00'+r+g+b+' '

    print(linha)