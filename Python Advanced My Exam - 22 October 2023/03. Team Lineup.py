def team_lineup(*players):
    player_count = {}
    for player in players:
        country = player[1]
        player_count[country] = player_count.get(country, 0) + 1


    sorted_data = sorted(players, key=lambda x: (-player_count[x[1]], x[1]))

    output = []
    current_country = ""
    for player in sorted_data:
        country = player[1]
        if country != current_country:
            output.append(f"{country}:")
            current_country = country
        output.append(f"  -{player[0]}")

    return "\n".join(output)


print(team_lineup(
   ("Harry Kane", "England"),
   ("Manuel Neuer", "Germany"),
   ("Raheem Sterling", "England"),
   ("Toni Kroos", "Germany"),
   ("Cristiano Ronaldo", "Portugal"),
   ("Thomas Muller", "Germany"),
   ("Bruno Fernandes", "Portugal"),
   ("Bernardo Silva", "Portugal"),
   ("Harry Maguire", "England")))
