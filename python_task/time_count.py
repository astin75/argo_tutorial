import argparse
from tqdm import tqdm
import time

parser = argparse.ArgumentParser(description='second count')

parser.add_argument('--sec',          type=int,   default=10)
parser.add_argument('--batch_size',     type=int,   default=128)
parser.add_argument('--lr_initial',     type=float, default=0.1)

args    = parser.parse_args()

print(args.sec)
# print(args.batch_size)
# print(args.lr_initial)

for i in tqdm(range(args.sec)):
    time.sleep(1)
    print(f"count: {i}/{args.sec}")