import matplotlib.pyplot as plt

dados = open('TABELA2.csv').readlines()

x = []
y = []

for i in range(len(dados)):
    if i!=0:
         linha = dados[i].split(';')
         linha2 = linha[2].split('R$ ')
         linha3 = linha2[0].strip()
         linha4 = linha3.replace(',', '.')
                  
         y.append(float(linha4))
         x.append(linha[0])
         



plt.rcParams.update({'font.size': 8})

plt. title('PIB per capita segundo Município. Período: 2013')
    
plt.xlabel('Município')
plt.ylabel('PIB_per_capita. (MIL)')
plt.xticks(rotation=90)
plt.plot(x, y, color='black')
plt.bar(x, y, color='red')
#plt.scatter(x, y, color='b', marker='.')
plt.show()
