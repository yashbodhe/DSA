def two_sets(n):
    k = (n * (n + 1)) / 2

    if k % 2 == 1:
        return
    
    target = k / 2
    left, right = [], []
    for num in range(n, 0, -1):
        if num <= target:
            left.append(num)
            target = target - num
        else:
            right.append(num)

    return left, right
    
    
def main():
    n = int(input())
    sets = two_sets(n)

    if sets:
        print("YES")
        left, right = sets
        print(len(left))
        print(*left)

        print(len(right))
        print(*right)
    else:
        print("NO")

if __name__ == "__main__":
    main()