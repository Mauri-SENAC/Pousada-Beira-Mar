// Função para mostrar a promoção no banner
function mostrarPromocao() {
    let texto = document.getElementById("texto-promocao");
    texto.innerText = "🔥 Promoção: Diárias a partir de R$ 150,00 o casal com café da manhã!";
}

// Função para validar o formulário e calcular o valor da estadia
function enviarContato() {
    let nome = document.getElementById("nome").value;
    let email = document.getElementById("email").value;
    let dias = document.getElementById("dias").value;
    let resposta = document.getElementById("resposta-form");

    // Verifica se a pessoa preencheu os campos
    if (nome === "" || email === "" || dias === "") {
        alert("Por favor, preencha o nome, e-mail e a quantidade de dias!");
        return;
    }

    // Calcula o valor (R$ 150 por dia)
    let valorTotal = dias * 150;

    alert("Obrigado, " + nome + "! Recebemos seu pedido de reserva.");
    resposta.innerText = "Pedido enviado! Valor estimado para " + dias + " dias: R$ " + valorTotal + ",00.";

    // Limpa os campos depois de enviar
    document.getElementById("nome").value = "";
    document.getElementById("email").value = "";
    document.getElementById("dias").value = "";
    document.getElementById("mensagem").value = "";
}