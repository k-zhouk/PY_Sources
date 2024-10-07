def print_every_other(low, high):
    if low> high:
        return
    print(low)
    print_every_other(low+ 2, high)

def main():
    print()
    print_every_other(0,10)

if __name__ == "__main__":
    main()
