#include <iostream>
#include <string>
#include <map>
#include <set>
#include <vector>

#include <stdio.h>
#include <limits.h>

// #define INT_MAX 0x7fffffff

using namespace std;
/*
1 empty return true
2 第一个和最后一个开始遍历, 直到i >= j
*/
bool isPalindrome(string s)
{
    if (s.empty())
        return true;

    // transform(s.begin(), s.end(), s.begin(), ::tolower);
    for (int i = 0, j = s.size() - 1; i < j; ++i, --j)
    {
        while (!isalnum(s[i]) && i < j) ++i;
        while (!isalnum(s[j]) && i < j) --j;

        const int d = s[i] - s[j];
        if (d != 0 && d != 'a' - 'A' && d != 'A' - 'a')
            return false;
    }

    return true;
}

int main(int argc, char const *argv[])
{
    printf("run, max = %d, min = %d\n", INT_MAX, INT_MIN);

    string s = "0p";
    printf("s = %s\n", isPalindrome(s)==false?"false":"true");

    return 0;
}