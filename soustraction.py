"""Programme pour soustraire deux nombres selon la convention PEP8."""


def soustraction(a: float, b: float) -> float:
    """Retourne la différence entre deux nombres."""
    return a - b


def main() -> None:
    """Point d'entrée du programme."""
    premier = float(input("Entrez le premier nombre : "))
    deuxieme = float(input("Entrez le deuxième nombre : "))
    resultat = soustraction(premier, deuxieme)
    print(f"La différence entre {premier} et {deuxieme} est : {resultat}")


if __name__ == "__main__":

    main()
