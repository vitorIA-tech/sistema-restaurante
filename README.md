<h1 align="center">🍔 Sistema de Restaurante Interativo (CLI)</h1>

<p align="center">
  Uma aplicação de terminal em formato de "Command Line Interface" (CLI) que simula o atendimento, controle de comandas e pagamentos de um restaurante em tempo real.
</p>

---

### 🚀 Sobre o Projeto
Para encerrar a primeira fase da construção do meu portfólio, desenvolvi um sistema de restaurante que funciona de forma 100% interativa. Em vez de apenas rodar um código estático, este projeto mantém um menu ativo rodando em loop (semelhante a um jogo de texto), permitindo que o usuário interaja com o banco de dados enviando comandos ao vivo.

### 🛠️ Funcionalidades
* **Menu Dinâmico:** Interface de texto que reage às escolhas do usuário.
* **Gestão de Comandas:** Adição de pedidos com atualização automática do valor total da conta.
* **Fechamento de Caixa:** Processamento de pagamento que zera a comanda e libera a mesa para o próximo cliente.
* **Validação de Erros:** O sistema impede que o programa quebre se o usuário digitar um código que não existe no cardápio.

### 💻 Tecnologias e Conceitos
* **Interatividade (`input`):** Captura de dados inseridos pelo usuário em tempo real.
* **Laços Infinitos (`while True`):** Manutenção da execução do programa até que a condição de saída (fechar o sistema) seja acionada.
* **Cálculos Matemáticos Básicos:** Atualização contínua de variáveis de valor flutuante (`float`) para gerenciar o total da conta.

---
*Projeto interativo construído para consolidar os fundamentos de Python, unindo lógica estruturada e experiência do usuário (UX) em linha de comando.*
