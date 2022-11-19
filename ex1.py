import math

CatetoOposto = int(input('Digite o cateto oposto: '))
CatetoAdjacente = int(input('Digite o cateto Adjacente: '))

quadradocatetoo = CatetoOposto*CatetoOposto
quadradocatetoadj = CatetoAdjacente*CatetoAdjacente

hipotenusa = math.sqrt((quadradocatetoo + quadradocatetoadj))

print('A hipotenusa do Cateto Oposto({}) e Cateto Adjacente({}) é : {} '.format(CatetoOposto,CatetoAdjacente,hipotenusa))





#ceil pra cima 
#floor pra baixo
#trunc é o número inteiro