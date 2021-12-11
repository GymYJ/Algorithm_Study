#include <iostream>
#include <algorithm>
#include <string>

using namespace std;

int main()
{
    cin.sync_with_stdio(0);
    cin.tie(0);

    string n, origin;

    cin >> n;
    origin = n;

    long long answer = stoi(n);

    n = n.substr(n.size() - 1, n.size()) + n.substr(0, n.size() - 1);
    while (origin != n){
        answer += stoi(n);
        n = n.substr(n.size() - 1, n.size()) + n.substr(0, n.size() - 1);
    }
    cout << answer << '\n';

    return 0;
}
