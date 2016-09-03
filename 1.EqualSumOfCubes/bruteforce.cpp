#include <stdio.h>
#include <math.h>

int main()
{
	int a, b, c, d;
	int MAX = 100;

	for(a = 0; a <= MAX; a++){
		for(b = 0; b <= MAX; b++){
			for( c = 0; c <= MAX; c++){
				for( d = 0; d <= MAX; d++){
					if( pow(a, 3) + pow(b, 3) == pow(c, 3) + pow(d, 3)){
						printf("%d %d %d %d \n", a, b, c, d);
						break;
					}
				}
			}
		}
	}
}