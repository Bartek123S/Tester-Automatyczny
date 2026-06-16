def oblicz_pole_trojkata():
    try:
        a = float(input("Podaj długość podstawy (a): "))
        h = float(input("Podaj wysokość (h): "))

        if a <= 0 or h <= 0:
            raise ValueError("Długość podstawy i wysokość muszą być większe od zera.")

        pole = 0.5 * a * h
        print(f"Pole trójkąta wynosi: {pole}")

    except ValueError as e:
        print(f"Błąd danych: {e}")
    except Exception as e:
        print(f"Wystąpił nieoczekiwany błąd: {e}")

oblicz_pole_trojkata()