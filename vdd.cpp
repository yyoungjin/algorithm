#include <iostream>
#include <vector>
#include <string>
#include <stack>
#include <queue>
#include <algorithm>
#include <cmath>

using namespace std;

int main () {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int A[100010];
    int B[100010];

    int N, M;
    cin >> N >> M;

    for (int i = 1; i<= N; i++)
    {
        cin >> A[i];
    }

    for (int j = 1; j<=M; j++)
    {
        cin >> B[j];
    }

    int K;

    cin >> K;

    while (K--)
    {
        char c;
        cin >> c;

        if (c == 'U')
        {
            int x, y;

            cin >> x >> y;

            if (x > N)
            {
                x = x%N;
                B[x] = y;
                
            }

            else {
                A[x] = y;
            }
        }

        if (c == 'L')
        {
            int first, second;

            first = 1;
            second = 1;

            for (int i = 2; i<= N; i++)
            {
                if (A[first]> A[i])
                {
                    first = i;
                }
            }

            for (int j = 2; j<= M; j++)
            {
                if (B[second] > B[j])
                {
                    second = j;
                }
            }
            
            cout << first << ' ' << (second + N) << '\n';
        }

    }
}
