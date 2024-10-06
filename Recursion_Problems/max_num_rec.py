def get_max(in_arr):
    print("Iteration")

    if len(in_arr)== 1:
        return in_arr[0]
    
    # Memoization of the result
    max_num= get_max(in_arr[1: len(in_arr)])

    if in_arr[0]> max_num:
        return in_arr[0]
    else:
        return max_num

def main():
    test_arr= [1, 2, 10, 75, 0, -5, 20, -100]
    print("Input array: ", test_arr)

    max_num= get_max(test_arr)
    print("Maximum element is: {0}".format(max_num))

if __name__== "__main__":
    main()
