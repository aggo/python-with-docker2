import argparse

def parse_args():
    parser = argparse.ArgumentParser(
        description="Read file")
    parser.add_argument("--file")
    parser.add_argument("--out")
    return parser.parse_args()


if __name__ == '__main__':
    args = parse_args()
    print("testing")
    with open(f"data/{args.file}") as f:
        content = f.read()
        print(content)
        f=open(f"/data/{args.out}","w")
        f.write(content)
        print("Duplicated!")
