def get_even_nums(in_list):

    def is_even(number):
        if number% 2== 0:
            return True
        else:
            return False

    if len(in_list)== 0:
        return []

    if is_even(in_list[0]):
        return [in_list[0]]+ get_even_nums(in_list[1: len(in_list)])
    else:
        return get_even_nums(in_list[1: len(in_list)])
    
    
def main():
    test_list=[0, 1, 2, 3, 4, 5, 6]
    print("Input list: ", test_list)

    even_nums= get_even_nums(test_list)
    print("List with even numbers: ", even_nums)
    
if __name__== "__main__":
    main()
