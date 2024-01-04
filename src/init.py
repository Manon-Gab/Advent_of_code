"""
Init the script:
add session cookie value in config.json
=> inspect >> application >> Cookies >> select https://adventofcode.com/ and copy value
Run in terminal:
python init.py -y 2023 -d 1
"""
import os
import subprocess

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
        with open(f"{target_day_dir}/day{options.day}.py", "r") as target_file:
            base = target_file.readlines()
            base[5] = base[5].replace("year", options.year)
            base[6] = base[6].replace("year", options.year)
            base[5] = base[5].replace("input_nb", f"input{options.day}")
            base_bytes = [line.encode("utf-8") for line in base]
            with open(f"{target_day_dir}/day{options.day}.py", "wb") as save_file:
                save_file.writelines(base_bytes)


if __name__ == "__main__":
    main()
