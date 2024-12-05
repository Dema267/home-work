# Функция для расчета итоговой суммы вклада
def calculate_final_amount(principal, years, interest_rate):
    final_amount = principal
    for year in range(years):
        final_amount += final_amount * interest_rate
    return final_amount

# Ввод данных от пользователя
try:
    a = float(input("Введите сумму вклада в рублях (например, 1000): "))
    years = int(input("Введите срок вклада в годах (например, 5): "))
    interest_rate = 0.10  # 10% годовых

    if a < 0 or years < 0:
        print("Сумма вклада и срок должны быть неотрицательными.")
    else:
        final_amount = calculate_final_amount(a, years, interest_rate)
        print(f"Итоговая сумма вклада через {years} лет составит: {final_amount:.2f} рублей")

except ValueError:
    print("Пожалуйста, введите корректные значения.")