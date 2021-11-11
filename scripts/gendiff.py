import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--foo', nargs='+')
parser.add_argument('bar', nargs='+')
args = parser.parse_args()
