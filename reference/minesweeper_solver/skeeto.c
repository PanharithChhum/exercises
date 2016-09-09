//gcc -g -std=c99 -Wall -Wextra -o skeeto skeeto.c


#include <stdio.h>
#include <stdint.h>
#include <string.h>

#define MAX_SIZE 256
static char grid[MAX_SIZE][MAX_SIZE];

static int
count_or_assign(int x, int y, char c, char a)
{
    static const uint16_t dirs[] = {
        0xffff, 0xff00, 0xff01, 0x00ff, 0x0001, 0x01ff, 0x0100, 0x0101
    };
    unsigned count = 0;
    for (unsigned i = 0; i < 8; i++) {
        int8_t dx = dirs[i] & 0xff;
        int8_t dy = dirs[i] >> 8;
        if (x + dx >= 0 && y + dy >= 0) {
            if (grid[y + dy][x + dx] == c) {
                count++;
                if (a)
                    grid[y + dy][x + dx] = a;
            }
        }
    }
    return count;
}

static int
deduce(int x, int y)
{
    char c = grid[y][x];
    if (c >= '0' && c <= '9') {
        int n = c - '0';
        int unknown = count_or_assign(x, y, '?', 0);
        int bombs = count_or_assign(x, y, '*', 0);
        if (unknown == n - bombs)
            return count_or_assign(x, y, '?', '*');
        if (bombs == n)
            return count_or_assign(x, y, '?', 'S');
    }
    return 0;
}

int
main(void)
{
    int height = 0;
    while (fgets(grid[height], sizeof(grid[0]), stdin))
        height++;

    int changes;
    do {
        changes = 0;
        for (int y = 0; y < height; y++)
            for (int x = 0; x < MAX_SIZE; x++)
                changes += deduce(x, y);
    } while (changes);

    for (int y = 0; y < height; y++)
        for (int x = 0; x < MAX_SIZE - 1; x++)
            if (grid[y][x] == 'S')
                printf("%d %d\n", y, x);
    return 0;
}