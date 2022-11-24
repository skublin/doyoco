import os
from glob import glob
from pathlib import Path


def scan_repo(start_path):
    p = Path(start_path)
    if p.is_dir():
        print(f"Start : {p}")
        sub_directories = [x for x in p.iterdir() if x.is_dir()]
        files = list(p.glob('*'))
        print("-> Sub-directories: ")
        for d in sub_directories:
            print(f"  -> {d}")
        print("-> Files:")
        for f in files:
            print(f"  -> {f}")

def run(start_path=os.getcwd()):
    scan_repo(start_path)


if __name__ == "__main__":
    run("C:\\Users\\szymo\\OneDrive\\Pulpit\\doyoco\\test")
    # run()
