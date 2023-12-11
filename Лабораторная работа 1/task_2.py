list_players = ["Маша", "Петя", "Саша", "Оля", "Кирилл", "Коля"]

total_players = len(list_players)

middle_index = total_players // 2
team1 = list_players[:middle_index]
team2 = list_players[middle_index:]

print(team1)
print(team2)
