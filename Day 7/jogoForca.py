import random

def printForcaDesenho(qrd_erro):
    print("|" + "x|" * qrd_erro)

words_list = ['Pato', 'Quack', 'Ombro']

num = random.randint(0,len(words_list) - 1)
qtd_erro = 0;


while(qtd_erro <= 6):
        
    
    
    
    qtd_erro+=1;
    printForcaDesenho(qtd_erro)