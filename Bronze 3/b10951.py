while True:
    try:
        a, b = list(map(int, input().split()))
    except EOFError:
        break
    print(a + b)
