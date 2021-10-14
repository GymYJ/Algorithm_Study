#include <iostream>
#include <algorithm>
#include <set>
#include <cmath>

using namespace std;

set<pair<int, int>> se;
int n;
double rate[4];
int dx[4] = {0, 0, 1, -1};
int dy[4] = {1, -1, 0, 0};
double answer;

void dfs(int x, int y, int count, double sum)
{
    if (count == n)
    {
        answer += sum;
        return;
    }
    for (int i=0; i<4; i++){
        if (rate[i] == 0)
            continue;
        if (se.find(make_pair(x + dx[i], y + dy[i])) == se.end()){
            se.insert(make_pair(x + dx[i], y + dy[i]));
            dfs(x + dx[i], y + dy[i], count + 1, sum*rate[i]);
            se.erase(se.find(make_pair(x + dx[i], y + dy[i])));
        }
    }
}

int main()
{
    cin.sync_with_stdio(0);
    cin.tie(0);
    cout.precision(9);

    cin >> n;
    double temp;
    for (int i=0; i<4; i++){
        cin >> temp;
        rate[i] = temp / 100;
    }
    se.insert(make_pair(0, 0));
    dfs(0, 0, 0, 1);
    cout << answer << '\n';
    return 0;
}
