print("🏀Witaj w Basketball Quiz!!!")
print("Sprawdź swoją wiedzę o koszykówce.")

pytania = [
    {
        "pytanie": "Ile sekund ma drużyna na przeprowadzenie całej akcji?",
        "odpowiedzi": ["A. 12", "B. 8", "C. 24", "D. 30"],
        "poprawna": "C"
    },
    {
        "pytanie": "Na co podzielony jest czas meczu kowszykówki?",
        "odpowiedzi": ["A. na sety", "B. na części", "C. na ćwiartki", "D. na kwarty"],
        "poprawna": "D"
    },
    {
        "pytanie": "Ile zawodników z każdej drużyny gra podczas meczu?",
        "odpowiedzi": ["A. 10", "B. 5", "C. 4", "D. 11"],
        "poprawna": "B"
    },
    {
        "pytanie": "Ile maksymalnie można zrobić kroków?",
        "odpowiedzi": ["A. 2", "B. 4", "C. 3", "D. 1"],
        "poprawna": "A"
    },
    {
        "pytanie": "Za ile punktów jest jeden rzut osobisty?",
        "odpowiedzi": ["A. 1", "B. 3", "C. 2", "D. 4"],
        "poprawna": "A"
    },
    {
        "pytanie": "Ile trwa jedna kwarta meczu w NBA?",
        "odpowiedzi": ["A. 1h", "B. 15min", "C. 5min", "D. 12min"],
        "poprawna": "D"
    },
    {
        "pytanie": "Ile jest kwart w całym meczu?",
        "odpowiedzi": ["A. 2", "B. 8", "C. 4", "D. 1"],
        "poprawna": "C"
    },
    {
        "pytanie": "Między którymi kwartami jest najdłuższa przerwa?",
        "odpowiedzi": ["A. 1 a 2", "B. 2 a 3", "C. 3 a 4", "D. 4 a 5"],
        "poprawna": "B"
    },
    {
        "pytanie": "Jaka z pośród podanych nazw fauli nie istnieje?",
        "odpowiedzi": ["A. techniczne", "B. fizyczne", "C. niesportowe", "D. kontaktowe"],
        "poprawna": "D"
    },
    {
        "pytanie": "Ile sekund ma drużyna na przeprowadzenie piłki za połowe?",
        "odpowiedzi": ["A. 8", "B. 12", "C. 24", "D. 18"],
        "poprawna": "A"
    }
]
punkty = 0
liczba_pytan = len(pytania)

print(f"Zaczynajmy!!! Masz {liczba_pytan} pytań.")

for i, q in enumerate(pytania, 1):
    print(f"Pytanie {i}: {q["pytanie"]}")
    for odpowiedz in q["odpowiedzi"]:
        print(odpowiedz)

    odpowiedz = input("Twoja odpowiedź (A, B, C, D): ").strip().upper()


    if odpowiedz == q["poprawna"]:
        print("✅ Poprawna odpowiedź")
        punkty += 1
    else:
        print(f"❌ Błąd! Poprawna odpowiedź to {q["poprawna"]}")

print(f"Twój wynik to {punkty}/{liczba_pytan}")

if punkty == 10:
    print("🎉Jesteś ekspertem od koszykówki!!!")
elif punkty >= 6:
    print("🏀Świetna wiedza! Jesteś prawdziwym fanem!")
else:
    print("💪Masz się jeszcze czego uczyć, ale dobry początek!")
