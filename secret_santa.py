# Write a Python script to assign Secret Santa pairs for a group of participants.
# The script should ensure that no participant is assigned to themselves, and no one is assigned to the same person they had last year.

import random

players = ['Anton', 'Berta', 'Caesar', 'Dora', 'Emil', 'Friedrich', 'Gustav']

recipients = []

secret_santa_dict = {}

for player in players:
    # temporary list of possible players for the "hat"
    temp_players = players.copy()
    # remove current drawer from "hat"
    try:
        temp_players.remove(player)
    except ValueError:
        pass
    # remove recipients(already picked) from "hat"
    for recipient in recipients:
        try:
            temp_players.remove(recipient)
        except ValueError:
            pass
    # random player from the temporary players list aka "hat"
    secret_santa = random.choice(temp_players)
    secret_santa_dict.update({player: secret_santa})
    # add chosen person from "hat" to recipients(already picked)
    recipients.append(secret_santa)
    # clear temp_players
    temp_players.clear()
print(secret_santa_dict)
