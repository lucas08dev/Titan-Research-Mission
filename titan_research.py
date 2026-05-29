print("=" * 35)
print("🚀 TITAN RESEARCH MISSION")
print("=" * 35)

# LISTA DE MENSAGENS

mensagens = []

# RECEBIMENTO DOS DADOS

temperatura = float(input("🌡 Temperatura da nave (°C): "))
energia = float(input("🔋 Energia (%): "))
comunicacao = float(input("📡 Comunicação (%): "))
oxigenio = float(input("🫁 Oxigênio (%): "))

# STATUS DOS MÓDULOS

print("\nDigite:")
print("- Operacional")
print("- Instável")
print("- Falha")

modulos = {
    "Painel Solar": input("\n🔋 Painel Solar: "),
    "Controle Térmico": input("❄ Controle Térmico: "),
    "Sistema de Comunicação": input("📡 Sistema de Comunicação: "),
    "Suporte de Vida": input("🫁 Suporte de Vida: ")
}

# DADOS DA MISSÃO

mensagens.append("\n📊 DADOS DA MISSÃO\n")

mensagens.append(f"🌡 Temperatura: {temperatura}°C")
mensagens.append(f"🔋 Energia: {energia}%")
mensagens.append(f"📡 Comunicação: {comunicacao}%")
mensagens.append(f"🫁 Oxigênio: {oxigenio}%")

# STATUS DOS MÓDULOS

mensagens.append("\n🛰 STATUS DOS MÓDULOS\n")

for modulo, status in modulos.items():

    mensagens.append(f"{modulo}: {status}")

# ALERTAS DA MISSÃO

mensagens.append("\n⚠ ALERTAS DA MISSÃO\n")

alerta = False

# TEMPERATURA

if temperatura > 80:

    mensagens.append("🚨 Temperatura crítica!")
    alerta = True

else:

    mensagens.append("✅ Temperatura normal")

# ENERGIA

if energia < 20:

    mensagens.append("🚨 Energia muito baixa!")
    alerta = True

else:

    mensagens.append("✅ Energia normal")

# COMUNICAÇÃO

if comunicacao < 30:

    mensagens.append("🚨 Comunicação instável!")
    alerta = True

else:

    mensagens.append("✅ Comunicação normal")

# OXIGÊNIO

if oxigenio < 60:

    mensagens.append("🚨 Oxigênio abaixo do ideal!")
    alerta = True

else:

    mensagens.append("✅ Oxigênio normal")

# VERIFICAÇÃO DOS MÓDULOS

mensagens.append("\n🛰 VERIFICAÇÃO DOS MÓDULOS\n")

for modulo, status in modulos.items():

    status = status.lower()

    if status == "falha":

        mensagens.append(f"🚨 Falha detectada em {modulo}")
        alerta = True

    elif status == "instável":

        mensagens.append(f"⚠ {modulo} operando de forma instável")
        alerta = True

    else:

        mensagens.append(f"✅ {modulo} operacional")

# DECISÕES AUTOMÁTICAS

mensagens.append("\n🤖 DECISÕES AUTOMÁTICAS\n")

if temperatura > 80:

    mensagens.append("❄ Sistema de resfriamento ativado")

if energia < 20:

    mensagens.append("🔋 Modo econômico ativado")

if comunicacao < 30:

    mensagens.append("📡 Reinicialização da antena")

if oxigenio < 60:

    mensagens.append("🫁 Liberação emergencial de oxigênio")

# SUSTENTABILIDADE

mensagens.append("\n🌱 SUSTENTABILIDADE\n")

if energia < 30:

    mensagens.append("🌱 Estratégia sustentável ativada")

else:

    mensagens.append("✅ Consumo energético estável")

# RELATÓRIO FINAL

mensagens.append("\n📄 RELATÓRIO FINAL\n")

if alerta:

    mensagens.append("⚠ Situações críticas foram detectadas")

else:

    mensagens.append("✅ Nenhuma situação crítica detectada")

mensagens.append("✅ Monitoramento concluído")
mensagens.append("🚀 Titan Research Mission finalizada")

# EXIBIÇÃO FINAL

for mensagem in mensagens:

    print(mensagem)
