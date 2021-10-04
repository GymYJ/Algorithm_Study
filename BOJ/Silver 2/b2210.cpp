#include <iostream>
#include <algorithm>
#include <set>
#include <map>
#include <string>

using namespace std;

string arr[5][5];
map<string, bool> m;
set<string> s;
int dx[] = {-1, 1, 0, 0};
int dy[] = {0, 0, -1, 1};

void dfs(int x, int y, string now)
{
    if (now.length() == 6)
    {
        s.insert(now);
        m[now] = true;
        return;
    }
    for (int i = 0; i < 4; i++)
    {
        int nx = x + dx[i];
        int ny = y + dy[i];
        if (nx >= 0 && nx < 5 && ny >= 0 && ny < 5)
        {
            string temp = now + arr[nx][ny];
            dfs(nx, ny, temp);
        }
    }
}

int main()
{
    cin.sync_with_stdio(0);
    cin.tie(0);

    for (int i = 0; i < 5; i++)
    {
        for (int j = 0; j < 5; j++)
        {
            cin >> arr[i][j];
        }
    }
    for (int i = 0; i < 5; i++)
    {
        for (int j = 0; j < 5; j++)
        {
            dfs(i, j, arr[i][j]);
        }
    }
    cout << s.size() << '\n';
    // cout << m.size() << '\n';

    return 0;
}
