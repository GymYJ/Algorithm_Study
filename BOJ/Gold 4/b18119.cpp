#include <iostream>
#include <string>

using namespace std;

int arr[10001] = { 0, };

int main() {
    int n, m;
    int remember = 0;

    cin >> n >> m;

    for (int i = 0; i < 26; i++) {
        remember = remember + (1 << i);
    }

    string temp;
    for (int i = 0; i < n; i++) {
        cin >> temp;
        int cur;

        for (int j = 0; j < temp.size(); j++) { // 해당 문자열에 사용된 알파벳을 저장
            cur = temp[j] - 'a';
            arr[i] |= (1 << cur);
        }
    }

    int o;
    char x;

    for (int i = 0; i < m; i++) {
        int count = 0;
        cin >> o >> x;

        remember ^= (1 << (x - 'a'));

        for (int j = 0; j < n; j++) {
            if ((arr[j] & remember) == arr[j])
                count++;
        }
        cout << count << "\n";
    }

    return 0;
}