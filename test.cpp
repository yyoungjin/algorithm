#include <stdio.h>

int main() {
    int n = 0, q = 0;
    int c, x, y, d;
    int a[200001] = {0};

    scanf("%d %d", &n, &q);
    for(int i = 1; i <= n - 1; i++) {
        scanf("%d", &a[i]);
        a[i] ^= a[i - 1];
    }
    
    while(q--) {
        scanf(" %d", &c);
        if(c == 1) {
            scanf("%d %d %d", &x, &y, &d);
            printf("%d\n", a[x - 1] ^ a[y - 1] ^ d);
        } else {
            scanf("%d %d", &x, &y);
            printf("%d\n", a[x - 1] ^ a[y - 1]);
        }
    }
    return 0;
}