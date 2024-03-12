#@title Calculadora
escolha_1_ok = False
while not escolha_1_ok:
  try:
    escolha_1 = int(input("Você gostaria de fazer uma conta com inteiros ou decimais?\n1-Inteiros\n2-Decimais\n"))
    if(escolha_1 == 1):
      A = int(input("Digite o segundo valor inteiro:\n"))
      B = int(input("Digite o primeiro valor inteiro:\n"))
      escolha_1_ok = True
    elif(escolha_1 == 2):
      A = float(input("Digite o primeiro valor float:\n"))
      B = float(input("Digite o segundo valor float:\n"))
      escolha_1_ok =True
    else:
      print("digite um valor correto")
  except:
    print("Digite um valor correto")
escolha_2_ok = False
while not escolha_2_ok:
  try:
    escolha_2 = int(input("Qual conta você gostaria de fazer?\n1-Soma\n2-Subtração\n3-Divisão\n4-Multiplicação\n"))
    if(escolha_2==1):
      resultado = A+B
      escolha_2_ok = True
    elif(escolha_2==2):
      resultado = A-B
      escolha_2_ok = True
    elif(escolha_2==3):
      resultado = A/B
      escolha_2_ok = True
    elif(escolha_2==4):
      resultado = A*B
      escolha_2_ok = True
    else:
      print("Digite um valor correto")
  except:
    print("Digite um valor correto")

print(f"Seu resultado foi {resultado}")