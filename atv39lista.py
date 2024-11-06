# Faça um programa que receba a temperatura média de cada mês do ano e armazene-as em uma lista.  Em seguida, calcule a média anual das temperaturas  e mostre a média calculada juntamente com todas as
#temperaturas acima da média anual, e em que mês elas ocorreram (mostrar o mês por extenso: 1
#elas ocorreram (mostrar o mês por extenso: 1 Janeiro, 2– Fevereiro, . . . )

meses = ["Janeiro", "Fevereiro", "Março", "abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]

temperatura = []
for i in range(12):
    a = float(input(f"Coloque a temperatura do mês de {meses[i]}:"))
    temperatura.append(a)

media = sum(temperatura) / len(temperatura)
print("A média anual é de: {}graus".format(media))
print("Meses com a temperatura acima da média anual:")
for i in range(12):
    if temperatura[i] > media:
        print(f"{i+1} - {meses[i]}: {temperatura[i]} graus")