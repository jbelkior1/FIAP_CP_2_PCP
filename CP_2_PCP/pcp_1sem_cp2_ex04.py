#CP - 4
def calcular_horas_extras(salario_base, total_hr_extras):
    valor_he = (salario_base * 0.015) * total_hr_extras
    return valor_he

def calcular_descontos_faltas(salario_base, total_faltas_mes):
    valor_df = (salario_base * 0.02) * total_faltas_mes
    return valor_df

def calcular_bonus(cargo, bonus_desempenho):
    if cargo == 1 and bonus_desempenho == "S":
        bonus = 1000
    elif cargo == 2 and bonus_desempenho == "S":
        bonus = 500
    elif cargo == 3 and bonus_desempenho == "S":
        bonus = 300
    elif cargo == 4 and bonus_desempenho == "S":
        bonus = 100
    else:
        bonus = 0
    return bonus

def cargo_text(cargo):
    if cargo == 1:
        ctx = "Gerente"
    elif cargo == 2:
        ctx = "Analista"
    elif cargo == 3:
        ctx = "Assistente"
    elif cargo == 4:
        ctx = "Estagiário"
    return ctx

Nome_do_funcionario  = str(input("Digite o Nome do Funcionario: "))

cargo = int(input("Digite o codigo de Cargo (1-Gerente, 2-Analista, 3-Assistente, 4-Estagiário): "))
while cargo not in [1,2,3,4]:
    print (" Resposta Invalida valor deve ser (1 a 4)")
    cargo = int(input("Digite o codigo de Cargo: "))

salario_base = float(input("Digite o Salario Base do Funcionario: "))

total_hr_extras = float(input("Digite o Total de horas extras trabalhadas: "))

total_faltas_mes = int(input("Digite o Total de faltas no mês: "))

bonus_desempenho = str(input("Recebeu Bônus (S ou N): ")).upper()
while bonus_desempenho not in ["S", "N"]:
    print(" Resposta Invalida valor deve ser (S ou N)")
    bonus_desempenho = str(input("Recebeu Bônus (S ou N): ")).upper()

total_acrescimos_sl = calcular_horas_extras(salario_base, total_hr_extras)
total_desc_falta =  calcular_descontos_faltas(salario_base, total_faltas_mes)
bonus_final = calcular_bonus(cargo, bonus_desempenho)
cargo_funcionario = cargo_text(cargo)
salario_final = total_acrescimos_sl + bonus_final - total_desc_falta + salario_base
total_acrescimos = total_acrescimos_sl + bonus_final

print("-" * 30)
print("Informações cadastrais")
print()
print(f"Nome do Funcionario: {Nome_do_funcionario}")
print(f"Cargo: {cargo_funcionario}")
print("-" * 30)
print("Informações Salariais")
print()
print(f"Salário Bruto: {salario_base}")
print(f"Total de acréscimos: {total_acrescimos}")
print(f"Total de descontos: {total_desc_falta}")
print(f"Salário Final: {salario_final}")

