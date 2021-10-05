#include <iostream>
#include <algorithm>

using namespace std;

int arr[100000];
int dp[100000][2];

int main()
{
    cin.sync_with_stdio(0);
    cin.tie(0);

    int n;
    cin >> n;
    for (int i = 0; i < n; i++)
    {
        cin >> arr[i];
    }

    int answer = -1000;
    dp[0][0] = arr[0];
    for (int i = 1; i < n; i++)
    {
        dp[i][0] = max(dp[i - 1][0] + arr[i], arr[i]);
        dp[i][1] = max(dp[i - 1][0], dp[i - 1][1] + arr[i]);
        answer = max(answer, max(dp[i][0], dp[i][1]));
    }
    cout << answer << '\n';
    return 0;
}
