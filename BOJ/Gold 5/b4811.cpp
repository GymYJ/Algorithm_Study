#include <iostream>
#include <algorithm>

using namespace std;

long long arr[61][61];

int main()
{
    cin.sync_with_stdio(0);
    cin.tie(0);

    int n;

    while (true)
    {
        cin >> n;
        if (n == 0)
            break;
        for (int i = 1; i <= n; i++)
        {
            arr[0][i] = 1;
        }
        for (int i = 1; i <= n; i++)
        {
            for (int j = i; j <= n; j++)
            {
                arr[i][j] = arr[i - 1][j] + arr[i][j - 1];
            }
        }
        cout << arr[n][n] << '\n';
    }

    return 0;
}
