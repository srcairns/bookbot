from collections import defaultdict
import argparse
import pathlib


DEFAULT_FILE_PATH = './books/frankenstein.txt'

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--file_path', nargs=1, default=DEFAULT_FILE_PATH)
    args = parser.parse_args(['--file_path', DEFAULT_FILE_PATH])
    return report(vars(args)['file_path'][0])


def open_file(file_path):
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents


def count_words(file_path):
    contents = open_file(file_path)
    return len(contents.split())


def count_chars(file_path):
    contents = open_file(file_path).lower()
    ret_dict = defaultdict(int)
    for char in contents:
        ret_dict[char] += 1
    return ret_dict


def report(file_path):
    print(f'--- Begin report of {file_path} ---')
    print(f'{count_words(file_path)} words found in the doco')
    for (char, count) in count_chars(file_path).items():
        print(f'The {char} character was found {count} times')
    print(f'--- End report ---')


main()