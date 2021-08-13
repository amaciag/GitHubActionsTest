import argparse

def print_hello(name):
    print("Hello {}!".format(name))

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--name')
    args = parser.parse_args()
    print_hello(args.name)