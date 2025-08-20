print("Kalkulator BMI")

height = float(input("Podaj swój wzrost w metrach: "))
weight = float(input("Podaj swoją wage w kilogramach: "))
BMI = weight / (height ** 2 )

print(f"Twoje BMI wynosi {BMI:.2f}")

if BMI < 18.5:
    print("Masz niedowagę!!!")
elif BMI >= 18.5 and BMI <= 25:
    print("Masz prawidłową wagę!!!")
elif 25 <= BMI <30:
    print("Masz nadwagę!!!")
else:
    print("Masz otyłość!!!")