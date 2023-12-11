salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.03  # Ежемесячный рост цен

money_capital = 0

for month in range(1, months + 1):
    total_expenses = spend - salary
    money_capital += total_expenses
    spend *= (1 + increase)

money_capital = round(money_capital, 2)

print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов: {money_capital}")

