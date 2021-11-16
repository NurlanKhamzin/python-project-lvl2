from gendiff_folder.gendiff import generate_diff, read_json
import argparse


def main():
    parser = argparse.ArgumentParser(description='Generate diff')
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument('-f', '--format', help="set format of output")
    parser.print_help()

    args = parser.parse_args()

    print(generate_diff(
          read_json(args.first_file), read_json(args.second_file)))


if __name__ == '__main__':
    main()
