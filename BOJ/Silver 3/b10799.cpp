#include <iostream>
#include <algorithm>
#include <stack>
#include <string>

using namespace std;

int main()
{
    cin.sync_with_stdio(0);
    cin.tie(0);

    stack<char> s;
    string pipe;
    cin >> pipe;

    int answer = 0;
    char before = '\0';
    for (int i = 0; i < pipe.size(); i++)
    {
        if (pipe[i] == '(')
        {
            s.push(pipe[i]);
        }
        else
        {
            s.pop();
            if (before == '(')
            {
                answer += s.size();
            }
            else
            {
                answer++;
            }
        }
        before = pipe[i];
    }

    cout << answer << '\n';

    return 0;
}
