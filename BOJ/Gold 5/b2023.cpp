#include <iostream>
#include <algorithm>
#include <cmath>

using namespace std;

int is_prime(int n, int k)
{
    int divide = k / 10;
    while (divide > 0)
    {
        int num = n / divide;
        if (num == 1)
            return divide;
        for (int i = 2; i <= sqrt(num); i++)
        {
            if (num % i == 0)
                return divide;
        }
        divide /= 10;
    }
    return 0;
}

int main()
{
    cin.sync_with_stdio(0);
    cin.tie(0);

    int n;
    cin >> n;
    int k = pow(10, n);
    int now = k / 10;

    while (now < k)
    {
        int result = is_prime(now, k);
        if (result == 0)
        {
            cout << now << '\n';
            now += 1;
        }
        else
            now += result;
    }

    return 0;
}
