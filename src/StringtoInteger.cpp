#include <iostream>
#include <string>
#include <map>
#include <set>
#include <vector>

#include <stdio.h>
#include <limits.h>

// #define INT_MAX 0x7fffffff

using namespace std;

int myAtoi(const string &str)
{
    int i = 0;
    const int size = str.size();
    for (; i < size; ++i)
    {
        if (str[i] == ' ' || str[i] == '\t')
            continue;
        else
            break;
    }

    int sign = 1;
    if (str[i] == '+')
        i++;
    else if (str[i] == '-')
    {
        sign = -1;
        i++;
    }

    int num = 0;
    for (; i < size; ++i)
    {
        if (str[i] < '0' || str[i] > '9')
            break;
        if (num > INT_MAX/10 || (num == INT_MAX/10 && (str[i] - '0') > INT_MAX%10))
            return sign == 1 ? INT_MAX : INT_MIN;
        num = num*10 + (str[i] - '0');
    }

	return num * sign;
}

int main(int argc, char const *argv[])
{
	printf("run, max = %d, min = %d\n", INT_MAX, INT_MIN);

	string str = "  012345678999999999999999999999 xxx";
    printf("str = %d\n", myAtoi(str));

	return 0;
}