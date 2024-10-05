def array_sum(in_arr):
    if len(in_arr)==1:
        return in_arr[0]
    return in_arr[0]+ array_sum(in_arr[1:len(in_arr)])

def main():
    test_arr=[1,2,3,4,5]
    print(f"\nTest array: {test_arr}")
    res= array_sum(test_arr)
    print(f"Sum of array elements: {res}")

if __name__ == "__main__":
    main()
