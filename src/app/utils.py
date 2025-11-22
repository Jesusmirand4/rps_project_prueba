def rps_winner(a, b):
    # Manejo de undecided
    if a == "undecided" or b == "undecided":
        return "undecided", "No se puede determinar un ganador"

    if a == b:
        return "tie", f"Ambos eligieron {a}"

    rules = {
        "Piedra": "Tijera",
        "Tijera": "Papel",
        "Papel": "Piedra"
    }

    if rules[a] == b:
        return "player_a", f"{a} vence a {b}"

    return "player_b", f"{b} vence a {a}"
