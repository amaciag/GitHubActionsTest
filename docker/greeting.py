import argparse

def print_hello(name):
    if name is None:
	    name = 'there'
    print("Hello {}!".format(name))
    print("Hope you're well")

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--name')
    args = parser.parse_args()
    print_hello(args.name)