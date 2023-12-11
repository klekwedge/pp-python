money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен

months = 0

while money_capital > 0:
    total_expenses = spend - salary
    money_capital -= total_expenses
    spend *= (1 + increase)
    if money_capital < 0:
        break
    months += 1

print("Количество месяцев, которое можно протянуть без долгов:", months)
