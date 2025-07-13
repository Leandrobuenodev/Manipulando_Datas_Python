from func import *

print("Formato aceito: DD-MM-AAAA ou DD/MM/AAAA")
print("Qual a data de vencimento? ")


due_date = input("→ ")

try:
    if verify_due(due_date):
        print("⚠️  A data de vencimento já passou.")
    else:
        print("✅ A data de vencimento ainda está em dia.")
except ValueError as e:
    print(f"❌ Erro: {e}")