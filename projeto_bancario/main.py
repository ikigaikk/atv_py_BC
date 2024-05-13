
menu = ''' 
========MENU========   

[d] - Depositar 💰
[s] - Sacar 💸
[e] - Extrato 📋
[q] - Sair ❌

=> ''' 
        

saldo = 1000
limite = 500


while True: # REGRAS DOS SAQUES PRECISAM SER APLICADAS...

    opcao = input(menu)

    if opcao == "d": # ✅
       deposito = int(input("Quanto você deseja depositar: "))
       if deposito > 0:
           print("Valor depositado com sucesso!")
           print(f"O saldo disponivel na sua conta => {saldo + deposito}")
           saldo += deposito
           cont_op = input("Deseja realizar alguma outra operação? [s] ou [n]  ")
           if cont_op == "s":
               continue
           elif cont_op == "n":
               break
           else:
               print("informe uma opção valida!")
    elif opcao == "s": # saques ✅ ✅ ✅
        qt_saque = input("Você gostaria de fazer quantos saques?  (Valor máximo de R$500 por saque)  [Minímo: 1, Máximo: 3] ")

        if qt_saque == "1": # ✅
            saque1 = int(input("insira o valor que gostaria de sacar: "))
            if (saque1 > 0) and (saque1 < 500):
                cont_op1 = input(f'''O seu saldo total é : {saldo - saque1}
                          Deseja sair?  [s] ou [n]   
                        => ''')
                if cont_op1 == "s":
                    break
                else:
                    continue
            elif saque1 > saldo:
                print("Saldo insuficiente.")
            else:
                cont_op2 = input('''
                            [ERRO]
                      INSIRA UM VALOR VÁLIDO.
                      Deseja tentar novamente? [s] ou [n] 
                      => ''')  # tela de continue
                if cont_op2 == "s":
                    continue
                else:
                    break

        elif qt_saque == "2": # ✅
            saque1 = int(input("Qual o valor do primeiro saque: "))
            saque2 = int(input("Qual o valor do segundo saque: "))
            saque12 = saque1 + saque2
            if (saque12 <= 0) or (saque1 > 500) or (saque2 > 500) :
                print(f'''
                      insira um valor valido.
                      
                      Saldo disponivel em conta: R${saldo}.00

                      SALDO INSUFICIENTE PARA SAQUE, TENTE NOVAMENTE.
                       => ''')
                continue
            else:
                print(f'''
                      
                      Saque realizado com sucesso. dinheio restante em sua conta: R${saldo - saque12}.00
                      
                      ''')
                continue


        elif qt_saque == "3": # realizar os saques dessa parte ✅
            saque1 = int(input("Qual o valor do primeiro saque: "))
            saque2 = int(input("Qual o valor do segundo saque: "))
            saque3 = int(input("Qual o valor do terceiro saque: "))

            saque_total = saque1 + saque2 + saque3

            if (saque_total >= 0) or (saque1 > 500) or (saque2 > 500) or (saque3 > 500):
                cont_op3 = print(f'''
                      insira um valor valido.
                      
                      Saldo disponivel em conta: R${saldo}.00

                      SALDO INSUFICIENTE PARA SAQUE, TENTE NOVAMENTE.
                       => ''')
                continue
            else:
                print(f'''
                      
                      Saque realizado com sucesso. dinheio restante em sua conta: R${saldo - saque_total}.00
                      
                      ''')
                continue
        else:
            print("[ERRO] Insira uma opção valida!")


    elif opcao == "e": # strings dos extratos
        if qt_saque == "1": # extrato com 1 saque
            input(f''' 
                  
                    Saldo: 
                  
                    R${saldo - saque1}.00

                    
                    Deposito realizado: 
                    
                    R${deposito}.00
                    

                    Saque realizado: R${saque1}.00

                    
                    🏦 OBRIGADO POR ESCOLHER NOSSOS SERVIÇOS. 

                  ''')
            continue
        elif qt_saque == "2": # extrato com 2 saques
            input(f'''
                  
                    Saldo: 
                  
                    R${saldo - saque1 - saque2}.00

                    Deposito Realizado: R${deposito}.00

                    Saques Realizados: [1] - R${saque1}.00
                                       [2] - R${saque2}.00

                                       
                    🏦 OBRIGADO POR ESCOLHER NOSSOS SERVIÇOS. 
                    
                  ''')
            continue
        elif qt_saque == "3": # extrato com 3 saques
            input(f'''
                  
                    Saldo: 
                  
                    R${saldo - saque_total}.00

                    Deposito Realizado: R${deposito}.00

                    Saques Realizados: [1] - R${saque1}.00
                                       [2] - R${saque2}.00
                                       [3] - R${saque3}.00
                                       
                    🏦 OBRIGADO POR ESCOLHER NOSSOS SERVIÇOS. 
                    
                  ''')
            continue
        else:
            print('''
                            [ERRO]
                    DIGITE UM OPÇÃO VALIDA.

                  ''')
            

    elif opcao == "q":
        break

    else:
        print("Digite um opção valida e tente novamente!")


