import lan


def do_test():
    # Read test case
    with open("test/test_list.txt") as file_in:
        for file_line in file_in:
            file, result = file_line.split(';')
            assert lan.main(file) == int(result), "Test error; file " + file
    print("Test is OK")

if __name__ == '__main__':
    do_test()
