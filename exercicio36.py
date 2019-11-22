vc = float(input('Digite o valor da casa que você quer financiar R$'))
sal = float(input('Qual sua renda mensal RS'))
ta = int(input('Em quantos anos você pretende pagar o financiamento: '))
pm = vc / (ta * 12)
if pm <= (sal * 0.3):
    print('Para uma casa no valor de R${:.0f} ser financiada em {} anos a parcela será de R${:.2f} ao mês. \n\033[1;36mFINANCIAMENTO APROVADO!\033[m'.format(vc, ta, pm))
else:
    print('Para uma casa no valor de R${:.0f} ser financiada em {} anos a parcela será de R${:.2f} ao mês. \n\033[1;31mFINANCIAMENTO NEGADO!\033[m'.format(vc, ta, pm))
