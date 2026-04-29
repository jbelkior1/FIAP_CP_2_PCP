#CP 3

cp1 = float(input("Digite a nota do Checkpoint 1: "))
while cp1 < 0 or cp1 > 10:
    cp1 = float(input("Nota inválida (0-10). Digite novamente: "))

cp2 = float(input("Digite a nota do Checkpoint 2: "))
while cp2 < 0 or cp2 > 10:
    cp2 = float(input("Nota inválida (0-10). Digite novamente: "))

cp3 = float(input("Digite a nota do Checkpoint 3: "))
while cp3 < 0 or cp3 > 10:
    cp3 = float(input("Nota inválida (0-10). Digite novamente: "))

sp1 = float(input("Digite a nota da Sprint 1: "))
while sp1 < 0 or sp1 > 10:
    sp1 = float(input("Nota inválida (0-10). Digite novamente: "))

sp2 = float(input("Digite a nota da Sprint 2: "))
while sp2 < 0 or sp2 > 10:
    sp2 = float(input("Nota inválida (0-10). Digite novamente: "))

gs = float(input("Digite a nota da Global Solution: "))
while gs < 0 or gs > 10:
    gs = float(input("Nota inválida (0-10). Digite novamente: "))

if cp1 <= cp2 and cp1 <= cp3:
    menor = cp1
elif cp2 <= cp1 and cp2 <= cp3:
    menor = cp2
else:
    menor = cp3

nota_cp_usadas = cp1 + cp2 + cp3 - menor
notas_sprint = sp2 + sp1

soma_atividades = (cp1 + cp2 + cp3 - menor) + sp1 + sp2
media_atividades = soma_atividades / 4


media_final = (media_atividades * 0.4) + (gs * 0.6)

print("-" * 30)
print(f"Soma notas Checkpoint: {nota_cp_usadas:.1f}")
print(f"Soma nota Sprint: {notas_sprint:.1f}")
print(f"Nota  GS: {gs:.1f}")
print(f"Menor nota de Checkpoint descartada: {menor:.1f}")
print()
print("-" * 30)
print()
print(f"Média das atividades (sem peso): {media_atividades:.1f}")
print(f"Média final do semestre (com peso): {media_final:.1f}")