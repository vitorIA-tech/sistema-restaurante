# Sistema de Restaurante Interativo (Simulador de Terminal)
cardapio = {
    "1": ("Hambúrguer Clássico", 25.00),
    "2": ("Hambúrguer Bacon supremo", 30.00),
    "3": ("Hambúrguer Baconcheddar", 35.00),
    "4": ("Hambúrguer Vegano", 45.00),
    "5": ("Batata Frita Rústica", 15.00),
    "6": ("Suco Natural", 10.00),
    "7": ("Refrigerante em Lata", 7.50),
    "8": ("Combo Tech (Hambúrguer + Batata + Refri)", 42.00),
    "9": ("Brownie com Sorvete", 18.90)
}
comanda = []
total_conta = 0.0

print("🍔 BEM-VINDO AO RESTAURANTE TECH 🍔")
print("O seu turno de atendimento começou!")

while True:
    print("\n--- Painel de Controle ---")
    print("1. Mostrar Cardápio")
    print("2. Adicionar Pedido à Comanda")
    print("3. Visualizar Status da Mesa e Fechar Conta")
    print("4. Encerrar Expediente (Sair)")
    
    acao = input("Digite o número da ação desejada: ")
    
    if acao == "1":
        print("\n📜 CARDÁPIO:")
        for codigo, (item, preco) in cardapio.items():
            print(f"[{codigo}] {item} - R$ {preco:.2f}")
            
    elif acao == "2":
        pedido = input("Digite o código numérico do produto: ")
        if pedido in cardapio:
            nome_item, preco_item = cardapio[pedido]
            comanda.append(nome_item)
            total_conta += preco_item
            print(f"✅ STATUS: {nome_item} enviado para a cozinha!")
        else:
            print("❌ Erro: Produto não encontrado no cardápio.")
            
    elif acao == "3":
        print("\n🧾 COMANDA DA MESA:")
        if not comanda:
            print(" A mesa está vazia no momento.")
        else:
            for item in comanda:
                print(f" 🍽️ {item}")
            print(f"💰 Total acumulado: R$ {total_conta:.2f}")
            
            pagar = input("O cliente deseja realizar o pagamento agora? (s/n): ")
            if pagar.lower() == "s":
                print("💳 Pagamento processado com sucesso. Mesa liberada!")
                comanda.clear()
                total_conta = 0.0
                
    elif acao == "4":
        print("👋 Fechando o caixa. Bom descanso!")
        break
        
    else:
        print("⚠️ Comando não reconhecido. Tente novamente.")
