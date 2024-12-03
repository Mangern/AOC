#include <stdio.h>
#include <string.h>
#include <stdlib.h>

#define BUFSIZE 1024

char buf[BUFSIZE];
int arr[100];

int issafe(int n) {
    for (int i = 0; i < n; ++i) {
        int prv = -1;
        int cur;
        int safe = 1;
        int sgn = 0;

        for (int j = 0; j < n; ++j) {
            if (j == i) continue;
            if (prv == -1) {
                prv = arr[j];
                continue;
            }
            int d = arr[j] - prv;

            if (abs(d) < 1 || abs(d) > 3) {
                safe = 0;
                break;
            }

            if (sgn < 0 && d > 0) {
                safe = 0;
                break;
            }

            if (sgn > 0 && d < 0) {
                safe = 0;
                break;
            }

            if (sgn == 0) {
                sgn = (d < 0 ? -1 : 1);
            }

            prv = arr[j];
        }

        if (safe) return safe;
    }
    return 0;
}

size_t nbuf;
int main() {
    char *ptr = buf;
    int nread = 0;
    int nsafe = 0;
    while (getline(&ptr, &nbuf, stdin) > 0) {
        ++nread;
        char* nums = strtok(ptr, " ");
        int n = 0;
        arr[n++] = atoi(nums);

        while (nums = strtok(NULL, " "), nums) {
            arr[n++] = atoi(nums);
        }
        nsafe += issafe(n);
    }
    printf("%d\n", nsafe);
    
}
