# Sistema de Calculo de Reservas - Pousada Beira Mar (Grupo 2)

def calcular_hospedagem(nome, opcao_suite, dias):
    suites = {
        1: ("Suite Brisa Casal", 180.0),
        2: ("Suite Master Vista Mar", 260.0),
        3: ("Chale Familia Completo", 350.0)
    }

    nome_suite, valor_diaria = suites.get(opcao_suite, ("Suite Padrao", 180.0))
    subtotal = valor_diaria * dias

    # Desconto de 10% para 5 diarias ou mais
    if dias >= 5:
        desconto = subtotal * 0.10
    else:
        desconto = 0.0

    valor_final = subtotal - desconto

    return {
        "cliente": nome,
        "suite": nome_suite,
        "dias": dias,
        "subtotal": subtotal,
        "desconto": desconto,
        "total": valor_final
    }


# Teste rapido caso rode no terminal: python sistema.py
if __name__ == "__main__":
    print("=== SIMULADOR POUSADA BEIRA MAR (GRUPO 2) ===")
    resultado = calcular_hospedagem("Visitante Teste", 2, 5)
    print(f"Cliente: {resultado['cliente']}")
    print(f"Acomodacao: {resultado['suite']} ({resultado['dias']} diarias)")
    print(f"Desconto aplicado: R$ {resultado['desconto']:.2f}")
    print(f"Total a pagar: R$ {resultado['total']:.2f}")