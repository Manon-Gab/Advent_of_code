"""
Init the script:
add session cookie value in config.json
=> inspect >> application >> Cookies >> select https://adventofcode.com/ and copy value
Run in terminal:
python init.py -y 2023 -d 1
"""
import os
import requests
import argparse
import sys
import shutil
import json


def main(args=sys.argv[1:]):
    parser = argparse.ArgumentParser(description="Advent of Code initiate.")
    parser.add_argument("-y", "--year", help="input year like : YYYY")
    parser.add_argument("-d", "--day", help="input day like : D")
    options = parser.parse_args(args)

    work_dir = os.getcwd()
    target_input_dir = f"{work_dir}/{options.year}/inputs"
    target_day_dir = f"{work_dir}/{options.year}/"
    url = f"https://adventofcode.com/{options.year}/day/{options.day}/input"

    with open(work_dir + "/config.json", "r") as file:
        headers = json.load(file)
        code = requests.get(url, headers=headers)
        open(f"{target_input_dir}/input{options.day}", "wb").write(code.content)
        shutil.copy(f"{work_dir}/base.py", f"{target_day_dir}/day{options.day}.py")


if __name__ == "__main__":
    main()
