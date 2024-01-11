# Write a Python script to assign Secret Santa pairs for a group of participants.

import random


def secret_santa(players):
    recipients = []
    secret_santa_dict = {}

    for player in players:
        # temporary list of possible players for the "hat"
        hat = players.copy()
        # remove current drawer from "hat"
        try:
            hat.remove(player)
        except ValueError:
            pass
        # remove recipients(already picked) from "hat"
        for recipient in recipients:
            try:
                hat.remove(recipient)
            except ValueError:
                pass

        # solving problem for list out of range for random.choice(hat)
        # if last player is still in the hat and possibly will draw itself
        def two_hat_last_person_in_it(bucket, persons):
            pass
        if len(hat) == 2 and players[-1] in hat:
            receiver = players[-1]
            secret_santa_dict.update({player: receiver})
            recipients.append(receiver)
        else:
            # random player from the temporary players list aka "hat"
            receiver = random.choice(hat)
            secret_santa_dict.update({player: receiver})
            # add chosen person from "hat" to recipients(already picked)
            recipients.append(receiver)

        # clear hat
        hat.clear()
    return secret_santa_dict


def main():
    persons = ['Anton', 'Berta', 'Caesar', 'Dora', 'Emil', 'Friedrich', 'Gustav']
    print(secret_santa(persons))


if __name__ == '__main__':
    main()

# ToDo: ...
