def sum_two(low, high):
    if high-low==1:
        return low+high
    return high+sum_two(low, high-1)

def main():
    print()
    print(sum_two(1,5))

if __name__ == "__main__":
    main()
