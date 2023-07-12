import sys
import wit

print("Hello")
class WitInterface:
    @staticmethod
    def handle_commands(command, args):
        print("Hello there")
        if command == "init":
            print("Helloooooooooooo")

            wit.Wit.init()
        elif command == "add":
            wit.Wit.add(args)
        elif command == "commit":
            wit.Wit.commit(args)

print("Why?")

if __name__ == "__main__":
    if len(sys.argv) == 1:
        raise ValueError("Oopsie no command")
    command = sys.argv[1]
    args = sys.argv[2:]
    WitInterface.handle_commands(command, args)
