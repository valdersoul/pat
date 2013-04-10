#include <stdio.h>
#include <math.h>

int main(void)
{
	int number = 0;
	int count = 0;
	int p1 = 2;
	int p2 = 3;
	int m = 0;
	scanf("%d", &number);
	while( p2 <= number){
		if (p2 - p1 == 2)
		{
			count++;
		}
		p1 = p2;
		p2 = generateP(p2, number);
	}
	printf("%d", count);
	return 0;
}

int generateP ( int num , int n){
    int i = 0;
	for (i = num+1; i < 2*n; i++)
	{
		if (isP(i))
		{
			return i;
		}
	}
}

int isP( int m){
    int n = 0;
    n = sqrt (m);
    int i = 0;
	if (m == 2 || m == 3)
	{
		return 1;
	}
	else
	{
		for (i = 2; i <= n; i++)
		{
			if (m % i == 0)
			{
				return 0;
			}
		}
		if (i == n+1 )
		{
			return 1;
		}
	}
}
