# 🚀 TITAN RESEARCH MISSION

print("=" * 50)
print("🚀 TITAN RESEARCH MISSION")
print("=" * 50)

# LISTA DE MENSAGENS

mensagens = []

# RECEBIMENTO DOS DADOS

temperatura = float(input("🌡 Temperatura da nave: "))
energia = float(input("🔋 Energia (%): "))
comunicacao = float(input("📡 Comunicação (%): "))
oxigenio = float(input("🫁 Oxigênio (%): "))

# STATUS DOS MÓDULOS

modulos = {
    "Painel Solar": input("🔋 Painel Solar: "),
    "Controle Térmico": input("❄ Controle Térmico: "),
    "Comunicação": input("📡 Sistema de Comunicação: "),
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

# ALERTAS

mensagens.append("\n⚠ ALERTAS\n")

if temperatura > 80:
    mensagens.append("🚨 Temperatura crítica!")

if energia < 20:
    mensagens.append("🚨 Energia muito baixa!")

if comunicacao < 30:
    mensagens.append("🚨 Comunicação instável!")

if oxigenio < 60:
    mensagens.append("🚨 Oxigênio abaixo do ideal!")

# ALERTAS DOS MÓDULOS

for modulo, status in modulos.items():

    if status.lower() == "falha":

        mensagens.append(f"🚨 Falha detectada em {modulo}")

    elif status.lower() == "instável":

        mensagens.append(f"⚠ {modulo} instável")

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

mensagens.append("✅ Monitoramento concluído")

mensagens.append("🚀 Titan Research Mission finalizada")

# EXIBIÇÃO FINAL

for mensagem in mensagens:

    print(mensagem)