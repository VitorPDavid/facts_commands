import argparse


def compare(first_file_path: str, second_file_path: str) -> bool:
    first_lines: list[str] = []
    second_lines: list[str] = []

    with open(first_file_path, 'r') as first_file:
        with open(second_file_path, 'r') as second_file:
            for first_file_line in first_file:
                first_file_values = first_file_line.rstrip('\n')
                first_lines.append(first_file_values)

            for first_second_file in second_file:
                second_file_values = first_second_file.rstrip('\n')
                second_lines.append(second_file_values)

    for line in first_lines:
        if line not in second_lines:
            return False

    return True


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Script to compare facts in two files.')

    parser.add_argument('-ff', '--first_file_path',
                        action='store',
                        default='./first.txt',
                        type=str,
                        help='the path to the first file to compare')

    parser.add_argument('-sf', '--second_file_path',
                        action='store',
                        default='./second.txt',
                        type=str,
                        help='the path to the second file to compare')

    args = parser.parse_args()

    file_has_same_facts = compare(args.first_file_path, args.second_file_path)

    message = "Files has Same Facts."

    if not file_has_same_facts:
        message = "Files not has Same Facts."

    print(message)
