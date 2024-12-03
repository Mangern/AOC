#include <stdio.h>
#include <string.h>
#include <stdlib.h>

#define BUFSIZE 1024

size_t n;
char buf[BUFSIZE];

int main() {
    char *ptr = buf;
    int nread = 0;
    int nsafe = 0;
    while (getline(&ptr, &n, stdin) > 0) {
        ++nread;
        char* nums = strtok(ptr, " ");
        int prev = atoi(nums);
        int cur;

        int diffs[3];
        int dptr = 0;

        int safe = 1;
        int i;

        while (nums = strtok(NULL, " "), nums) {
            cur = atoi(nums);
            int diff = cur - prev;

            if (abs(diff) < 1 || abs(diff) > 3) {
                safe = 0;
                break;
            }

            for (i = 0; i < dptr; ++i) {
                if (diffs[i] == diff) {
                    break;
                }
            }

            if (i == dptr) {
                if (dptr == 3) {
                    safe = 0;
                    break;
                }
                diffs[i] = diff;
                ++dptr;
            }
            prev = cur;
        }

        if (!safe) continue;

        for (int i = 1; i < dptr; ++i) {
            if ((diffs[i] > 0 && diffs[i-1] < 0) 
                || (diffs[i] < 0 && diffs[i-1] > 0)) {
                safe = 0;
                break;
            }
        }
        nsafe += safe;
    }
    printf("%d\n", nsafe);
    
}
