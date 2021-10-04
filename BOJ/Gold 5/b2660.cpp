#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

int arr[51][51];
int n;

int main()
{
    cin.sync_with_stdio(0);
    cin.tie(0);

    cin >> n;
    int a, b;
    while (true)
    {
        cin >> a >> b;
        if (a == -1 && b == -1)
            break;
        arr[a][b] = 1;
        arr[b][a] = 1;
    }

    for (int i = 1; i <= n; i++)
    {
        arr[i][i] = 1;
    }

    for (int k = 1; k <= n; k++)
    {
        for (int i = 1; i <= n; i++)
        {
            for (int j = 1; j <= n; j++)
            {
                if (arr[i][k] != 0 && arr[k][j] != 0)
                {
                    if (arr[i][j] == 0)
                    {
                        arr[i][j] = arr[i][k] + arr[k][j];
                    }
                    else
                    {
                        arr[i][j] = min(arr[i][j], arr[i][k] + arr[k][j]);
                    }
                    arr[j][i] = arr[i][j];
                }
            }
        }
    }

    vector<int> v;
    for (int i = 1; i <= n; i++)
    {
        int score = *max_element(arr[i] + 1, arr[i] + n + 1);
        v.push_back(score);
    }

    int min_value = *min_element(v.begin(), v.end());
    vector<int> candidate;
    for (int i = 0; i < n; i++)
    {
        if (v[i] == min_value)
            candidate.push_back(i + 1);
    }
    cout << min_value << " " << candidate.size() << "\n";
    for (auto i : candidate)
    {
        cout << i << ' ';
    }

    return 0;
}