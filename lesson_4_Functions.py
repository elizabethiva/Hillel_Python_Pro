from typing import Any


def players_repr(players: list[dict], verbose: bool) -> None:
    if verbose:
        for player in players:
            print(
                f"The player's name is {player['name']}. Age of the player is  {player['age']}. Number of the player is {player['number']}"
            )
    elif not verbose:
        for player in players:
            print(
                f"The player's name is {player['name']}. Age of the player is {player['age']}"
            )


def players_add(players: list[dict], name, age, number) -> list[dict]:
    temp = {'name': name, 'age': int(age), 'number': int(number)}
    players.append(temp)
    return players


def players_del(players: list[dict], name: str) -> list[dict]:
    for i in players:
        if i["name"] == name:
            players.remove(i)
    return players


def players_find(players: list[dict], field: str, value: Any) -> list[dict]:
    res = []
    for i in players:
        for key, val in i.items(): 
            if (key, val) == (field, value if not value.isdigit() else int(value)):
                res.append(i)
    return res


def players_get_by_name(players: list[dict], name: str) -> dict | None:
    for i in players:
        if i["name"] == name:
            return i


def main():
    team = [
        {"name": "John", "age": 20, "number": 1},
        {"name": "Marry", "age": 33, "number": 3},
        {"name": "Cavin", "age": 33, "number": 12},
    ]

    options = ["represent", "add", "delete", "find", "get"]

    while True:
        user_input = input(f"Enter your choice {options}:")
        if not user_input:
            break
        elif user_input.lower() == "represent":
            print(
                players_repr(
                    team,
                    verbose=input(
                        "Enter 'True' if you want to see verbose and 'False' otherwise: "
                    )
                )
            )
        elif user_input.lower() == "add":
            print(players_add(team, name=input("Enter name of the player: "),
                              age=input("Enter age of the player: "),
                              number=input("Enter number of the player: ")))
        elif user_input.lower() == "delete":
            print(players_del(team, name=input("Enter the name: ")))
        elif user_input.lower() == "find":
            print(
                players_find(
                    team,
                    field=input("Enter the field: "),
                    value=input("Enter the value: "),
                )
            )
        elif user_input.lower() == "get":
            print(players_get_by_name(team, name=input("Enter the name: ")))


if __name__ == "__main__":
    main()
