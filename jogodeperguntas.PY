import random

# Lista de perguntas
perguntas = [
    {"pergunta": "Qual a capital de Portugal?", "resposta": "Lisboa"},
    {"pergunta": "Quanto é 2 + 2?", "resposta": "4"},
    {"pergunta": "Cor primária misturada com azul para formar roxo?", "resposta": "Vermelho"},
    {"pergunta": "Qual é o maior oceano da Terra?", "resposta": "Pacífico"},
    {"pergunta": "Python é uma linguagem de programação? (sim/não)", "resposta": "sim"},
    {"pergunta": "Qual é o planeta mais próximo do Sol?", "resposta": "Mercúrio"},
    {"pergunta": "Quem é o autor do romance Romeu e Julieta?", "resposta": "William Shakespeare"},
    {"pergunta": "Qual é o elemento químico com símbolo H?", "resposta": "Hidrogênio"}
]

utilizador = {"nome": "Jogador"}
historico = []

def configurar_utilizador():
    nome = input("Digite seu nome: ")
    utilizador["nome"] = nome
    print(f"Bem-vindo(a), {nome}!")

def jogar_quiz():
    print(f"\n🎮 Iniciando o jogo para {utilizador['nome']}...\n")
    perguntas_sorteadas = random.sample(perguntas, k=len(perguntas))

    for p in perguntas_sorteadas:
        print("❓", p["pergunta"])
        resposta = input("Resposta: ").strip()
        acertou = resposta.lower() == p["resposta"].lower()
        resultado = "✅ Correto!" if acertou else f"❌ Errado! Resposta certa: {p['resposta']}"
        print(resultado + "\n")

        historico.append({
            "pergunta": p["pergunta"],
            "resposta_user": resposta,
            "correta": p["resposta"],
            "acertou": acertou
        })
def mostrar_estatisticas():
    total = len(historico)
    acertos = sum(1 for h in historico if h["acertou"])
    erros = total - acertos
    print(f"\n📊 Estatísticas de {utilizador['nome']}:")
    print(f"- Total de perguntas respondidas: {total}")
    print(f"- Acertos: {acertos}")
    print(f"- Erros: {erros}")

    print("\n📘 Histórico de respostas:")
    for h in historico:
        status = "✅" if h["acertou"] else "❌"
        print(f"{status} Pergunta: {h['pergunta']}")
        print(f"   Sua resposta: {h['resposta_user']} | Correta: {h['correta']}\n")
def menu():
    while True:
        print("\n=== MENU ===")
        print("1. Configurar utilizador")
        print("2. Jogar")
        print("3. Ver estatísticas")
        print("4. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            configurar_utilizador()
        elif opcao == "2":
            jogar_quiz()
        elif opcao == "3":
            mostrar_estatisticas()
        elif opcao == "4":
            print("\n🔚 Saindo do jogo...")
            mostrar_estatisticas()
            print("Obrigado por jogar!")
            break
        else:
            print("⚠️ Opção inválida. Tente novamente.")

menu()
