import numpy as np
data=open('uruguay.txt','r')
datastring=[]
cb1=data.readline()#Salva/apaga primer Cabecalho
cb2=data.readline()#Salva/apaga segundo Cabecalho
e=0 #Contador
M=[] #Matriz usada para imprimir resultados
for line in data:
    L=[] #Matriz auxiliar transforma string- int ou float
    line=line.replace(' ' ,'\t') #O dado nao vem com o \t
    datastring.append(line[:-1].split('\t'))
    datastring[e] = list(filter(None, datastring[e])) #retira elementos vazios ' '
    L.append(int(datastring[e][0])) #Posicao 0 em inteiro, Ano
    L.append(int(datastring[e][1])) #Posicao 1 em inteiro, dia do ano
    L.append(int(datastring[e][2])) #Posicao 2 em inteiro, hora
    L.append(float(datastring[e][3])) #Posicao 3 em real, Densidade
    L.append(float(datastring[e][4])) #Posicao 4 em real, Vx
    L.append(float(datastring[e][5])) #Posicao 5 em real, Vy
    L.append(float(datastring[e][6])) #Posicao 6 em real, Vz
    L.append(float(datastring[e][7])) #Posicao 7 em real, Bx
    L.append(float(datastring[e][8])) #Posicao 8 em real, By
    L.append(float(datastring[e][9])) #Posicao 9 em real, Bz
    M.append(L) #Preenche a matriz M que pode ser graficada
    e+=1 #aumenta o contador e
data.close()
#Acrescentar colunas
M=np.array(M) #Converte a lista M, que contém os dados processados, em um array NumPy chamado M.
B=[] #Cria uma lista vazia chamada B para armazenar os valores do módulo do campo magnético.
B=(M[:,7]**2+ M[:,8]**2+M[:,9]**2)**(0.5) #Calcula o módulo do campo magnético para cada linha do array M, usando os valores das colunas 7, 8 e 9. Os cálculos são feitos utilizando a fórmula do módulo: B = sqrt(Bx^2 + By^2 + Bz^2). Os valores resultantes são atribuídos à lista B.
V=(M[:,4]**2+ M[:,5]**2+M[:,6]**2)**(0.5) #Calcula o módulo da velocidade para cada linha do array M, usando os valores das colunas 4, 5 e 6. Os cálculos são feitos utilizando a fórmula do módulo: V = sqrt(Vx^2 + Vy^2 + Vz^2). Os valores resultantes são atribuídos à lista V.
data1=open('ACE_MULTI_Data-1Novo.txt','w') #Abre um novo arquivo chamado "ACE_MULTI_Data-1Novo.txt" em modo de escrita e atribui o objeto de arquivo resultante à variável data1.
data1.write('Arquivo processado por: Arian Ojeda Gonzalez'+'\n') #Escreve uma linha no arquivo indicando o nome do autor do processamento.
data1.write(cb1[:-1]+'\t'+'B'+'\t'+'V'+'\n') #Escreve a linha do primeiro cabeçalho no arquivo, removendo o caractere de nova linha no final, e adiciona as colunas "B" e "V" separadas por tabulação.
data1.write(cb2) #Escreve a linha do segundo cabeçalho no arquivo.
for i in range(len(M)): #percorre cada linha do array M.
    a1=str(int(M[i,0]))+'\t'; a2=str(int(M[i,1]))+'\t' #
    a3=str(int(M[i,2]))+'\t'; a4=str(M[i,3])+'\t' #
    a5=str(M[i,4])+'\t'; a6=str(M[i,5])+'\t' #
    a7=str(M[i,6])+'\t'; a8=str(M[i,7])+'\t' #
    a9=str(M[i,8])+'\t'; a10=str(M[i,9])+'\t' #
    a11=str(round(B[i],4))+'\t'; a12=str(round(V[i],4)) #os valores de cada linha do array M, juntamente com os valores de B e V correspondentes a essa linha, são convertidos em strings e concatenados com tabulações.
    data1.write(a1+a2+a3+a4+a5+a6+a7+a8+a9+a10+a11+a12+'\n') # Escreve a linha atual no arquivo, contendo os valores convertidos e separados por tabulações.
data1.close() #Fecha o arquivo de saída.
#Graficos e calculos
#A partir daqui, o código realiza a geração de gráficos e cálculos estatísticos usando a biblioteca Matplotlib.
import matplotlib.pyplot as plt
#Os valores médios, mínimos e máximos do módulo do campo magnético (B) e da velocidade (V) são impressos na tela.
print('De B: Valor medio = {0}, minimo = {1} e maximo = {2}'.format(round(B.mean(),3),round(B.min(),3),round(B.max(),3))) #
print('De V: Valor medio = {0}, minimo = {1} e maximo = {2}'.format(round(V.mean(),3),round(V.min(),3),round(V.max(),3))) #
plt.rcParams['font.size'] = '14' # As configurações do tamanho da fonte dos gráficos são definidas.
plt.figure(1) #Figura do subplot
plt.subplot(2,2,1) #Define o primeiro subplot como um grid de 2x2 e seleciona o primeiro (superior esquerdo) subplot para o gráfico Bz.
plt.plot(M[:,9],'-b',label='Bz') # Plota a coluna 9 do array M (que representa Bz) em função do índice da linha. A linha é representada por um traço azul (-b) e é adicionada uma legenda para identificar o gráfico.
plt.legend();plt.xlabel('t (h)');plt.ylabel('Bz (nT)');plt.grid(True) #
plt.subplot(2,2,2) #
plt.plot(M[:,4],'-b',label='Vx') #
plt.legend(); plt.xlabel('t (h)'); plt.ylabel('Vx (km/s)');plt.grid(True) #
plt.subplot(2,2,3)#
plt.plot(B,'-b',label='B')#
plt.legend();plt.xlabel('t (h)'); plt.ylabel('B (nT)'); plt.grid(True)#
plt.subplot(2,2,4)#
plt.plot(V,'-b',label='V')#
plt.legend(); plt.xlabel('t (h)'); plt.ylabel('V (km/s)'); plt.grid(True)#
plt.tight_layout()#  Ajusta automaticamente os espaços entre os subplots.
plt.savefig('FigureGrid-Bz-Vx-B-V.png')#  Salva a figura gerada em um arquivo chamado 'FigureGrid-Bz-Vx-B-V.png'.
plt.figure(2) #Figura de By e Bz Cria uma nova figura para o segundo conjunto de subplots.
plt.plot(M[:,8],'-b',label='By')# Plota a coluna 8 do array M (que representa By) em função do índice da linha. A linha é representada por um traço azul (-b) e é adicionada uma legenda para identificar o gráfico
plt.plot(M[:,9],'-r',label='Bz')#  Plota a coluna 9 do array M (que representa Bz) em função do índice da linha. A linha é representada por um traço vermelho (-r) e é adicionada uma legenda para identificar o gráfico.
plt.legend(); plt.title('Day 265-365 - 2003'); plt.xlabel('t (h)'); plt.ylabel('Bx and By (nT)')#
plt.savefig('FigureByBy.png')# Salva a figura gerada em um arquivo chamado 'FigureByBy.png'.
plt.grid(True)# Salva a figura gerada em um arquivo chamado 'FigureByBy.png'.
plt.show()#  Exibe os gráficos na tela.