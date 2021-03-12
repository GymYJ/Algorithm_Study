memory = {0: (1, 0), 1: (0, 1)}


def count(num):
    if num in memory:
        return memory[num]
    else:
        memory[num] = (count(num - 1)[0] + count(num - 2)[0], count(num - 1)[1] + count(num - 2)[1])
        return memory[num]


def main():
    n = int(input())
    test = []
    for _ in range(n):
        test.append(int(input()))
    for num in test:
        print(count(num)[0], count(num)[1])


if __name__ == "__main__":
    main()
