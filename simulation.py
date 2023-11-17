import csv
import random

players = []
with open('player_data.csv', newline='') as infile:
    inReader = csv.reader(infile, quotechar="'", quoting=csv.QUOTE_NONNUMERIC)
    for inRow in inReader:
        players.append(inRow)

random.seed()
i = 0
cycles = 100
while i < cycles:
    for player in players:  
        for opponent in players:
            if(player != opponent):
                deviatedScorePlayer = player[1] + player[2] * random.uniform(-2, 2)
                deviatedScorePlayer = deviatedScorePlayer - (deviatedScorePlayer % 0.25)
                deviatedScoreOpp = opponent[1] + opponent[2] * random.uniform(-2, 2)
                deviatedScoreOpp = deviatedScoreOpp - (deviatedScoreOpp % 0.25)
                if  deviatedScorePlayer > deviatedScoreOpp:
                    player[3] += 1
                    opponent[4] += 1
                elif deviatedScorePlayer < deviatedScoreOpp:
                    opponent[3] += 1
                    player[4] += 1
                elif deviatedScorePlayer == deviatedScoreOpp:
                    player[5] += 1
                    opponent[5] += 1
    i += 1

standings = sorted(players, key=lambda manager: manager[3], reverse=True)
print(standings)
saveStandings = False
if saveStandings:
    with open('simulation.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Team', 'Wins', 'Loss', 'Draw'])
        for row in standings:
            writer.writerow([row[0], row[3], row[4], row[5]])
        writer.writerow(['Weeks Simulated:', (cycles * 34)])
            



