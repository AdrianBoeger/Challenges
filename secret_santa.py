# Write a Python script to assign Secret Santa pairs for a group of participants.

import random


def secret_santa(players):
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
        receiver = random.choice(temp_players)
        secret_santa_dict.update({player: receiver})
        # add chosen person from "hat" to recipients(already picked)
        recipients.append(receiver)
        # clear temp_players
        temp_players.clear()
    return secret_santa_dict


def main():
    persons = ['Anton', 'Berta', 'Caesar', 'Dora', 'Emil', 'Friedrich', 'Gustav']
    print(secret_santa(persons))


if __name__ == '__main__':
    main()
