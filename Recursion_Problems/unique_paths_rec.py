def get_unique_paths(rows, cols):
    if (rows== 1) or (cols== 1):
        return 1
    
    return get_unique_paths(rows- 1, cols)+ get_unique_paths(rows, cols- 1)

def main():
    test_row= 13
    test_col= 13
    print("\nNumber of rows: {0}\nNumber of coumns: {1}\n".format(test_row, test_col))

    paths= get_unique_paths(test_row, test_col)
    print("Number of uniques paths is: {0}\n".format(paths))

if __name__== "__main__":
    main()
