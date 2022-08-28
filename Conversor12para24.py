# Faça um programa que converta da notação de 24 horas para a notação de 12 horas. Por
# exemplo, o programa deve converter 14:25 em 2:25 P.M. A entrada é dada em dois inteiros.
# Deve haver pelo menos uma função: para fazer a conversão e para a saída. Registre a
# informação A.M./P.M.

def converteHora (hora):
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

hora = int(input("Digite a hora a ser convertida: "))
minuto = input("Digite o minuto: ")
print ("Convertido:",converteHora(hora),':',minuto,verificaHoraAMPM(hora))