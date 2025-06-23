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

def append_file_string(file_name, string_of_lines):
    # Takes two strings, appends the string to the end of the file
    f = open(file_name, 'a')
    f.write(string_of_lines)
    f.close()
    return

def write_file_list(file_name, list_of_lines):
    # Takes a string and list, writes all items from list to file where each item is one line
    f = open(file_name, 'w')
    for i in list_of_lines:
        f.write(str(i) + '\n')
    f.close()
    return

def copy_file_add_line_numbers(file_name_read, file_name_write):
    # Takes two strings, reads data from first file, writes data to new file, adds line number to new file
    # Open file to read, and convert into a list
    infile = open(file_name_read, 'r')
    lines = infile.readlines()
    infile.close()

    # Open the file to write
    outfile = open(file_name_write, 'w')

    line_number = 1 # Start counting from 1
    for line in lines:
        outfile.write(str(line_number) + ':' + line)
        line_number += 1
    
    outfile.close()
    return


if __name__ == '__main__':
    file1 = 'seneca1.txt'
    file2 = 'seneca2.txt'
    file3 = 'seneca3.txt'
    string1 = 'First Line\nSecond Line\nThird Line\n'
    list1 = ['Line 1', 'Line 2', 'Line 3']
    append_file_string(file1, string1)
    print(read_file_string(file1))
    write_file_list(file2, list1)
    print(read_file_string(file2))
    copy_file_add_line_numbers(file2, file3)
    print(read_file_string(file3))
