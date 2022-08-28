def menu():
    print("Escolha uma opção: ")
    print("1 - Para converter de 24 horas para 12 horas.")
    print("2 - Para converter de 12 horas para 24 horas.")
    print("3 - Sair.")


def converteHora24p12 (hora):
    if hora>12 and hora !=24:
        aux=hora-12
        return str(aux)
    elif hora ==24:
        return str(0)
    else :
        return str(hora)

def verificaHoraAMPM (hora):
    if hora>12 and hora !=24:
        aux=hora-12
        return "PM"
    else :
        return "AM"

def converteHora12p24 (hora,aux):
    if aux=="PM" and hora!=12:
        HoraConvertida=hora+12
        return str(HoraConvertida)
    elif hora==12 and (aux=="PM" or aux=="pm" or aux=="Pm" or aux=="pM"):
        return str(0)
    else:
        return str(hora)

def verificaMinutos (hora,minuto):
    if(minuto>=60):
        hora=hora+(minuto//60)
        aux=(minuto%60)
        minuto=aux
        return hora,minuto
    else:
        return hora,minuto

op=True
while op!=3 or op==True:
    menu()
    op=int(input("Digite uma opção: "))
    if op ==1:
        hora = int(input("Digite a hora a ser convertida: "))
        minuto = int(input("Digite o minuto: "))
        hora,minuto=verificaMinutos (hora,minuto)
        print ("Convertido:",converteHora24p12(hora),":",minuto,verificaHoraAMPM(hora))
    elif op==2:
        hora = int(input("Digite a hora a ser convertida: "))
        minuto = int(input("Digite o minuto: "))
        aux=input("Digite se a hora é AM ou PM: ")
        hora,minuto=verificaMinutos (hora,minuto)
        print ("Convertido:",converteHora12p24(hora,aux),":",minuto)
    elif op==3:
        print("Até Logo.")
        break;
    else:
        print("Opção Invalida. Digite novamente.\n")