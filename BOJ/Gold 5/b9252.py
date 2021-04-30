import sys

S1 = sys.stdin.readline().strip()
S2 = sys.stdin.readline().strip()
len1 = len(S1)
len2 = len(S2)
matrix = [[''] * (len2 + 1) for _ in range(len1 + 1)]
for i in range(1, len1 + 1):
    for j in range(1, len2 + 1):
        if S1[i - 1] == S2[j - 1]:
            matrix[i][j] = matrix[i - 1][j - 1] + S1[i - 1]
        else:
            if len(matrix[i - 1][j]) > len(matrix[i][j - 1]):
                matrix[i][j] = matrix[i - 1][j]
            else:
                matrix[i][j] = matrix[i][j - 1]
print(len(matrix[-1][-1]))
if len(matrix[-1][-1]) != 0:
    print(matrix[-1][-1])
