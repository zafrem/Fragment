import datetime
import argparse

parser = argparse.ArgumentParser(description='args')
parser.add_argument('--mode', default='backtest', type=str, help='Start Mode')
parser.add_argument('--start', default='2020-01-01', type=str, help='Start Day "%Y-%m-%d" fmt')
parser.add_argument('--end', default='2020-12-31', type=str, help='End Day "%Y-%m-%d" fmt')
args = parser.parse_args()

def main(mode, start, end):
    try:
        if not (mode == "backtest" or mode == "run"):
            raise ValueError
        start_day = datetime.datetime.strptime(start, '%Y-%m-%d')
        end_day = datetime.datetime.strptime(end, '%Y-%m-%d')
    except ValueError:
        print("Input Error Value")

    if mode == 'backtest':
        pass
    elif mode == 'run':
        pass

if __name__ == "__main__":
    main(args.mode, args.start, args.end)

