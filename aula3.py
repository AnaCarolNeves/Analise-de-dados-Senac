print('*'*30, 'BEM VINDO AO CINEMA', '*'*30)

print('Digite a sua idade: ')
idade = int(input())


if idade >= 18:
    print('Entrada liberada')

elif idade >=16:
    resposta = input('Você está com responsável? Digite Sim ou Não      ').upper()
    
    if resposta == 'SIM':
        print ('Entrada liberada \nBom filme')

    #print('O filme é para maiores de 18 anos, para acessar precisa de um responsável)
    # responsavel = input().upper()    
    #if responsavel == 'SIM':
        #print('acesso liberado')
    #else:
        #print('você precisa estar acompanhado do responsável')    

    elif resposta == "NÃO":
        print ('Entrada liberada apenas com responsável')  
    
    else:
        print ('Digite uma resposta válida')
    

      

else:
    print ('Entrada negado')    