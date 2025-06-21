#!/usr/bin/env python3
# Author ID: salakoozi

def read_file_string(file_name):
    # Takes file_name as string for a file name, returns its entire contents as a string
    result = open(file_name, 'r')
    read_data = result.read()
    result.close()
    return read_data

def read_file_list(file_name):
    # Takes a file_name as string for a file name, 
    # return its entire contents as a list of lines without new-line characters
    f = open(file_name, 'r')
    read_data = list(f)
    stripped_lines = []
    for line in read_data:
        stripped_lines.append(line.strip())
    f.close()
    return stripped_lines


if __name__ == '__main__':
    file_name = 'data.txt'
    print(read_file_string(file_name))
    print(read_file_list(file_name))