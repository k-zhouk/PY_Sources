def number_of_paths(n):
    if n<=0:
        return 0
    if n==1:
        return 1
    if n==2:
        return 2
    if n==3:
        return 4
    return number_of_paths(n-1)+ number_of_paths(n-2)+ number_of_paths(n-3)

def main():
    stairs= 25
    steps_way= [1,2,3] # Number of steps at a time. Not passed as a parameter
    paths= number_of_paths(stairs)
    print(f"For a staircase of {stairs} stairs and {len(steps_way)} steps way, there are {paths} paths")

if __name__ == "__main__":
    main()
