import argparse
import inspect
import os

from datetime import datetime


def get_day():
    parser = argparse.ArgumentParser(
        description="Run the Advent of Code 2024 solution script corresponding to the given day."
    )
    parser.add_argument(
        "day",
        type=int,
        nargs="?",
        default=None,
        help="The integer corresponding to the day.",
    )
    args = parser.parse_args()
    day = args.day
    if day is None:
        print("No day specified, getting default value...")
        now = datetime.now()
        if now.month != 12 or now.day > 25:
            print("We are past Christmas, setting the day to Christmas (25)")
            day = 25
        else:
            day = now.day
            print(f"Setting day to {day}")

    return day


def get_input():
    day = get_day()
    input_file = f"day{day}.txt"
    input_path = f"input/{input_file}"

    with open(input_path) as f:
        file_contents = f.read()

    return file_contents.splitlines()
