import sys


def main():
    n = int(sys.stdin.readline())
    arr = list(map(int, sys.stdin.readline().split()))
    lis = [arr[0]]
    for i in range(1, n):
        if arr[i] > lis[-1]:
            lis.append(arr[i])
        else:
            index = len(lis) - 2
            while index >= 0:
                if lis[index] < arr[i]:
                    lis[index + 1] = arr[i]
                    break
                index -= 1
            if index == -1:
                lis[0] = arr[i]
    print(len(lis))


if __name__ == '__main__':
    main()
