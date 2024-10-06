def add_until_100(array):
    print("Iteration")
    if len(array)== 0:
        return 0
    
    sum= add_until_100(array[1: len(array)])

    if (array[0]+ sum) > 100:
        return sum
    else:
        return array[0]+ sum

def main():
    test_arr= [1, 2, 10, 75, 0, 5, 20, 99]
    print("Test array: ", test_arr)

    sum= add_until_100(test_arr)
    print("Sum: {0}".format(sum))

if __name__== "__main__":
    main()
