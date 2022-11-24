import argparse
from Scanner import Scanner


def run():
    parser = argparse.ArgumentParser(description="Main parser", formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('-p', '--path', help='Path to start scanner.')
    args = parser.parse_args()
    path = vars(args)['path']
    
    s = Scanner(path)
    s.generate_report()


if __name__ == "__main__":
    run()
