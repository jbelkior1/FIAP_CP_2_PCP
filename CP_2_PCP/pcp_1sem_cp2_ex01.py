#CP-1

def peso_kilos(ps_cam):
    return ps_cam * 1000


def definir_imposto(c_est_cam):
    if c_est_cam == 1:
        imposto = 0.35
    elif c_est_cam == 2:
        imposto = 0.25
    elif c_est_cam == 3:
        imposto = 0.15
    elif c_est_cam == 4:
        imposto = 0.05
    elif c_est_cam == 5:
        imposto = 0.0
    return imposto


def definir_preco(c_carg_cam):
    preco_p_kg = 0
    if c_carg_cam in range(10,21):
        preco_p_kg = 100
    elif c_carg_cam in range(21,31):
        preco_p_kg = 250
    elif c_carg_cam in range(31,41):
        preco_p_kg = 340
    return preco_p_kg

ps_cam = float(input('Digite o Peso do Caminhão em Toneladas: '))

c_est_cam = int(input('Digite o código do estado (1 a 5): '))
while c_est_cam <= 0 or c_est_cam > 5:
    print('Digite o valor de 1 a 5')
    c_est_cam = int(input("Digite a primeira nota novamente: "))

c_carg_cam = int(input('Digite o código da carga (10 a 40): '))
while c_carg_cam <= 9 or c_carg_cam > 40:
    print('Digite o valor de 10 a 40')
    c_carg_cam = int(input("Digite a primeira nota novamente: "))


preco_codigo_carga = definir_preco(c_carg_cam)
porcentagem_imposto = definir_imposto(c_est_cam)
peso_convertido = peso_kilos(ps_cam)

peso_por_kilos = peso_convertido * preco_codigo_carga
valor_do_imposto = peso_por_kilos  * porcentagem_imposto
valor_total = peso_por_kilos  + valor_do_imposto


print('\n' + '='*30)
print('Esses são os valores')
print()
print(f'O Peso em Kilos do Caminhão são: {peso_convertido:.2f}Kg ')
print(f'Preço da carga: R${peso_por_kilos:.2f}')
print(f'Porcentagem de Impostos: {porcentagem_imposto:.2f}')
print(f'Valor total transportado: R${valor_total:.2f}')
print('\n' + '='*30)



