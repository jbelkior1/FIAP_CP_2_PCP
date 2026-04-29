def pode_aprovar(idade, renda, valor):
    if idade > 18 and valor <= (20 * renda):
        return "APROVADO"
    else:
        return "NEGADO"

def definir_taxa(parcelas):
    if parcelas <= 6:
        juros = 0.05
    elif parcelas >= 7 and parcelas <= 12:
        juros = 0.08
    elif parcelas >= 13 and parcelas <= 24:
        juros = 0.10
    return juros

def calcular_parcela(valor, taxa_juros, parcelas):
    fator = (1 + taxa_juros) ** parcelas
    valor_p = valor * (taxa_juros * fator) / (fator - 1)
    return round(valor_p, 2)

def calcular_total(parcela, parcelas):
    total_pr = parcela * parcelas
    return round(total_pr, 2)

def calcular_juros(total, valor):
    juros = total - valor
    return round(juros, 2)

nome_do_cliente = str(input("Digite o nome do cliente: "))
idade = int(input("Digite a idade do cliente: "))
renda = float(input("Digite a renda mensal do cliente: "))
valor = float(input("Digite o valor do emprestimo do cliente: "))
parcelas = int(input("Digite a quantidade de parcelas: "))
while parcelas < 1 or parcelas > 24:
    print("Só trabalhamos com parcelas de até 24 vezes")
    parcelas = int(input("Digite a quantidade de parcelas: "))

validacao_aprovado = pode_aprovar(idade, renda, valor)

if validacao_aprovado == "APROVADO":

    taxa_juros = definir_taxa(parcelas)
    valor_parcelas = calcular_parcela(valor, taxa_juros, parcelas)
    valor_total = calcular_total(valor_parcelas, parcelas)
    juros_final = calcular_juros(valor_total, valor)

    print("-" * 30)
    print(f"Status da Aprovação: {validacao_aprovado}")
    print(f"Nome do cliente: {nome_do_cliente}")
    print()
    print(f"Valor financiado: {valor}")
    print(f"Taxa de juros:  {taxa_juros}")
    print(f"Valor da parcela: {valor_parcelas}")
    print(f"Valor total pago: {valor_total}")
    print(f"Total de juros pagos: {juros_final}")
else:
    print(f"Status: {validacao_aprovado}")