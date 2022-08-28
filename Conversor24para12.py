# Faça um programa que converta da notação de 12 horas para a notação de 24 horas. Por
# exemplo, o programa deve converter 2:25 P.M em 14:25. A entrada é dada em dois inteiros e
# uma string que irá registrar se as horas são A.M. ou P.M. Deve haver pelo menos uma função:
# para fazer a conversão e para a saída.

def converteHora (hora,aux):
    if aux=="PM" and hora!=12:
        HoraConvertida=hora+12
        return str(HoraConvertida)
    elif hora==12 and aux=="PM":
        return str(0)
    else:
        return str(hora)

hora = int(input("Digite a hora a ser convertida: "))
minuto = input("Digite o minuto: ")
aux=input("Digite se a hora é AM ou PM: ")
print ("Convertido:",converteHora(hora,aux),':',minuto)