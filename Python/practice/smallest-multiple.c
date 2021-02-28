#include <stdio.h>

int main(void) {
	int num = 0;
	while (num % 20 == 0 && num % 19 == 0 && num % 18 == 0 && num % 17 == 0 && num % 15 == 0 && num % 12 == 0 && num % 11 == 0 && num % 12 == 0 && num % 13 == 0 && num % 14 == 0) {
		printf("The number is : %d ", num);
		num = num + 1;

	}
	return 0;
}

