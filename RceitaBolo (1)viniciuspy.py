#Rceita de Bolo
#ENTRADA -> PROCESSAMENTO ->SAIDA
#Problema: fazer um bolo chocolate
#IDE vscode LP Python

#Passo 1: Identificação do problema. 
#Passo 2: Escolha das Ferramentas
#Passo 3: Implementação, Testes, Validações ... 

###Entradas###
#Ingredientes 
#uma colher de chá fermento
#3 xícaras de farinha
#3 ovos
#2 xicaras cacau em pó(chocolate)
#1 xicara leite
#1/2 xicara margarina
#uma lata chatilly
#3 xícaras açucar
#meia colher de chá de sal

###Processamento###
#seprar uma vasilha para misturar os ingredientes
#acrescentar os ingredientes na vasilha
#misturar os ingedientes na vasilha ate ficar homogeneo
#untar um forma com margarina e colocar os ingedientes misturados
#ligar o forno 180 graus por 10 minutos
#colocar a vasilha no forno pré-aquecido
#esperar 45 minutos para assar (Verificar!!)
#retirar o bolo do forno, apenas se tiver pronto
#colocar o bolo na mesa para esfriar
#prepara a cobertura
#servir 
#Fim

def fazer_bolo():
        # fermento =  1
        # ovos = 3 
        # farinha = 3
        # chocolate = 2
        # leite = 1
        # margarina = 0.5
        # chantilly = 1
        # acucar = 3
        # sal = 0.05
    
    ingredientes = {
         "fermento":   1,
         "ovos": 3, 
         "farinha":  3,
         "chocolate": 2,
         "leite": 1,
         "margarina":  0.5,
         "chantilly": 1,
         "acucar": 3,
         "sal": 0.05
    }

#modo de preparo
print('-'*50)
print("Separe uma vasilha para misturar os ingredientes")
print("Acrescentar os ingredientes na vasilha")
print('-'*50)
mistura_massa = ["fermento", "ovos", "farinha", "chocolate", "leite", "acucar","sal"]
print("Misturar os ingedientes na vasilha ate ficar homogeneo")
print("unte a forma e coloque os ingredientes")

#temperatura = 180
# alterei o int para o float
temp = float(input("digite a temperatura do forno"))
#alterei o int para o float
temp_pre = float(input("entre com o tempo de pre-aquecimento"))
#reduzi o numero de print e usei \n para quebrar uma linha facili
print('aqueça o forno em {0}graus por {1}minutos'.format(temp, temp_pre))
#inseri um novo if e else para melhorar o codigo 
if temp >= 200:
    print('cuidado com essa temperatura ai ')

else:
    print('muito bem vamos nessa')

print('coloque a vasilha no forno pré-aquecido')
#tempo_preparo = 45
tempo_preparo = float(input("Digite o tempo de preparo"))

#verificar se o bolo esta assado
print("Verificando se o bolo esta assado")
if tempo_preparo >= 45:
    print("Bolo Assado! Pode retirar do forno e colocar na mesa")

else:
    print("Bolo está cru, apressado! Espere")

print("Colocar a cobertura e Servir!!")

#clear
