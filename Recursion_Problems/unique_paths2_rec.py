# Problem of getting unique paths with memoization

# Doesn't work
def get_unique_paths_memo(rows, cols, cache):
    print("Iteration")
    if (rows== 1) or (cols== 1):
        return 1

    if [rows, cols] not in cache:
        cache[[rows, cols]]= get_unique_paths_memo(rows-1 , cols, cache)+ get_unique_paths_memo(rows, cols-1 , cache)

    return cache[[rows. cols]]

def main():
    test_row= 5
    test_col= 7
    print("\nNumber of rows: {0}\nNumber of coumns: {1}\n".format(test_row, test_col))

    paths= get_unique_paths_memo(test_row, test_col, {})
    print("Number of uniques paths is: {0}\n".format(paths))

if __name__== "__main__":
    main()
