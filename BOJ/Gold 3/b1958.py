import sys

s1 = '0' + sys.stdin.readline().strip()
s2 = '0' + sys.stdin.readline().strip()
s3 = '0' + sys.stdin.readline().strip()
len1 = len(s1)
len2 = len(s2)
len3 = len(s3)
matrix = [[[0 for _ in range(len3)] for _ in range(len2)] for _ in range(len1)]
for i in range(1, len1):
    for j in range(1, len2):
        for k in range(1, len3):
            if s1[i] == s2[j] and s2[j] == s3[k]:
                matrix[i][j][k] = matrix[i - 1][j - 1][k - 1] + 1
            else:
                matrix[i][j][k] = max(matrix[i - 1][j][k], matrix[i][j - 1][k], matrix[i][j][k - 1])
print(matrix[len1 - 1][len2 - 1][len3 - 1])
