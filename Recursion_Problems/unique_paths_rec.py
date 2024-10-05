def get_unique_paths(rows, columns):
    if (rows== 0) and (columns== 0):
        return 0

def main():
    test_row= 3
    test_col= 4
    print("\nNumber of rows: {0}\nNumber of coumns: {1}\n".format(test_row, test_col))

    paths= get_unique_paths(test_row, test_col)
    print("Number of uniques paths is: {0}\n".format(paths))

if __name__== "__main__":
    main()
