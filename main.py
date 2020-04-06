print ("+--------------------------------------------------------------+")
print ("|######################## SHOW DO TRILHÃO #######################|")
print ("+--------------------------------------------------------------+")

Reais = 0
cont = 1
print ("ESCOLHA OS SEGUINTES TESMAS: \n 1 Saude \n 2 Educação")

Resposta = int(input(" Digite sua escolha: "))

if Resposta == 1:
    
    print ("PERGUNTA NUMERO 1")
    print ("Quantos ovos são necessários para se fazer um bolo? \n Alternativa 1: 3 Ovos \n Alternativa 2: 5 Ovos \n Alternativa 3: 10 Ovos")
    questao1 = int(input("Digite sua resposta: "))
    if questao1 != 2:
          break
    print (" Resposta errada ")
    print (" Para fazer um bolo são necessários 5 ovos para que ele possa ficar consistente")
         
    else:
        print (" Certa resposta ")
        print ("Para fazer um bolo são necessários 5 Ovos para que ele possa ficar consistente")
        Reais += 1
        
    print ("PERGUNTA NUMERO 2")
    print ("Quantas xícaras de arroz são necessárias para se fazer um bolo? \n Alternativa 1: 3 Xícaras \n Alternativa 2: 5 Xícaras \n Alternativa 3: 10 Xícaras")
    questao2 = int(input("Digite sua resposta: "))
    if questao2 != 1:
        print (" Resposta errada")
        print ("Para fazer um bolo são necessárias  3 Xícaras para que ele possa ficar consistente")
        Reais +=  1
    else:
        print (" Certa resposta")
        print ("Para fazer um bolo são necessárias 3 Xícaras para que ele possa ficar consistente")
        
    print ("Você possui até o momento R$ %2.8f" % (Reais))
    
