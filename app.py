# 💧 Projeto: Consumo de Água
# 🌱 Campanha de conscientização ambiental

# Solicita o tipo de imóvel ao usuário
print("💧 SISTEMA DE CONSUMO DE ÁGUA 💧")
print("--------------------------------")
print("Tipos de imóvel:")
print("1 - Comercial")
print("2 - Casa")
print("3 - Apartamento")

tipo_imovel = input("\n🏠 Informe o tipo de imóvel: ").strip().lower()

# Solicita o consumo mensal em metros cúbicos
try:
    consumo = float(input("🚿 Informe o consumo mensal em m³: ").replace(",", "."))

    # Verifica se o consumo informado é válido
    if consumo < 0:
        print("❌ O consumo não pode ser negativo.")

    # Classifica o consumo de acordo com o imóvel
    elif tipo_imovel == "comercial":
        print("\n🏬 Imóvel comercial")
        print("💼 Tarifa comercial aplicada — consulte o plano corporativo.")

    elif tipo_imovel in ("casa", "apartamento"):
        nome = "Casa" if tipo_imovel == "casa" else "Apartamento"
        print(f"\n🏡 Imóvel residencial: {nome}")

        if consumo < 10:
            print("💧 Consumo econômico — excelente controle de água!")
        elif consumo <= 25:
            print("💧 Consumo moderado — dentro do padrão residencial.")
        else:
            print("⚠️ Consumo excessivo — adote medidas de economia e verifique vazamentos.")

    else:
        print("❌ Tipo de imóvel inválido.")
        print("Digite comercial, casa ou apartamento.")

except ValueError:
    print("❌ Entrada inválida! Informe o consumo usando números.")

# Mensagem final de conscientização
print("\n🌎 Cada gota conta!")
print("💙 Economize água e ajude a preservar o planeta!")
