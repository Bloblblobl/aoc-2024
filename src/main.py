import os

from utils import get_day


def main():
    day = get_day()

    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    print(f"Set CWD to {os.getcwd()}")

    filename = f"day{day}.py"
    if not os.path.isfile(filename):
        print(f"Error: File '{filename}' does not exist.")
        return

    print(f"Executing solution for day {day}...")
    try:
        with open(filename) as file:
            exec(file.read(), {"__name__": "__main__"})
    except Exception as e:
        print(f"An error occurred while executing '{filename}': {e}")


if __name__ == "__main__":
    main()
