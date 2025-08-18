import random

def gra():
    print("Witaj w grze 'Zgadnij liczbę'!!!")
    print("Zgadnij liczbę z zakresu od 0 do 200.")

    number_of_games = 0
    number_of_wins = 0
    your_attempts = []

    while True:
        hidden_number = random.randint(0, 200)
        number_of_attempts = 0
        max_attempts = 10
        guessed = False

        print(f"\nNowa gra! Masz {max_attempts} prób, aby zgadnąć liczbę z zakresu 0–200.")

        while number_of_attempts < max_attempts:
            try:
                shot = int(input("Podaj swoją liczbę: "))
                number_of_attempts += 1

                if shot < 0 or shot > 200:
                    print("Liczba musi być z zakresu 0-200 Spróbuj ponownie.")
                    number_of_attempts -= 1
                    continue

                if shot < hidden_number:
                    print("Za mało! Spróbuj większej liczby.")
                elif shot > hidden_number:
                    print("Za dużo! Spróbuj mniejszej liczby.")
                else:
                    print(f"🎉 Brawo! Zgadłeś! Ukryta liczba to {hidden_number}.")
                    print(f"Potrzebowałeś {number_of_attempts} prób.")
                    guessed = True
                    break

            except ValueError:
                print("To nie jest liczba! Wpisz poprawną liczbę całkowitą.")
                number_of_attempts -= 1
        if not guessed:
            print(f"🙁 Nie zgadłeś! Ukryta liczba to {hidden_number}.")

        number_of_games += 1
        if guessed:
            number_of_wins += 1
        your_attempts.append(number_of_attempts if guessed else "przegrana")

        print("\n--- Statystyki ---")
        print(f"Liczba rozegranych gier: {number_of_games}")
        print(f"Liczba wygranych: {number_of_wins}")
        print(f"Skuteczność: {number_of_wins / number_of_games * 100}%")

        if [p for p in your_attempts if isinstance(p, int)]:
            average = sum(p for p in your_attempts if isinstance(p, int)) / len(
                [p for p in your_attempts if isinstance(p, int)])
            print(f"Średnia liczba prób (tylko wygrane gry): {average}")

        while True:
            question = input("\nCzy chcesz zagrać jeszcze raz? (tak/nie): ").lower().strip()
            if question in ['tak', 't', 'yes', 'y', 'Tak', 'TAK']:
                break
            elif question in ['nie', 'n', 'no', 'Nie', 'NIE']:
                print("Dziękuję za grę! Do zobaczenia!")
                return
            else:
                print("Proszę wpisać 'tak' lub 'nie'.")

if __name__ == "__main__":
    gra()