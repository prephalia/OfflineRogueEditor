import json

import getpass

from modules.rogueClass import Rogue

if __name__ == '__main__':

    with open("./data/data.json") as f:
         data = json.loads(f.read())

    print(data["startup_message"])

    rogue = Rogue()

    func = {
        "1": rogue.unlock_all_starters,
    }

    term = [
        "**************************** COMMANDS ****************************",
        "1: Unlock all starters",
        "--------------------------------------------------------------------"
    ]

    while True:
        print("\n".join(term))
        command = input("Command: ")

        if command in func:
            func[command]()
        elif command == "exit":
            quit()
        else:
            print("Command not found")