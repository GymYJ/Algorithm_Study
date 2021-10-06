#include <iostream>
#include <algorithm>
#include <set>

using namespace std;

int arr[500];

int main()
{
    cin.sync_with_stdio(0);
    cin.tie(0);

    int h, w;
    int block = 0;
    cin >> h >> w;

    for (int i = 0; i < w; i++)
    {
        cin >> arr[i];
        block += arr[i];
    }

    set<int> s;

    for (int i = h; i > arr[0]; i--)
    {
        int j = 0;
        while (arr[j] < i && j < w)
        {
            j++;
        }
        if (j == w)
            s.insert(i);
        block += j;
    }

    for (int i = h; i > arr[w - 1]; i--)
    {
        if (s.find(i) != s.end())
            continue;
        int j = w - 1;
        while (arr[j] < i && j >= 0)
        {
            j--;
        }
        block += w - 1 - j;
    }

    cout << h * w - block << '\n';

    return 0;
}
