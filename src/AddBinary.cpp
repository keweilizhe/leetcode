#include <iostream>
#include <string>
#include <map>
#include <set>
#include <vector>
#include <algorithm>

#include <stdio.h>
#include <limits.h>


using namespace std;

/*
Given two binary strings, return their sum (also a binary string).
For example,
a = "11"
b = "1"

边界情况
特殊情况
一般情况 从后往前遍历,

当前值取决于 3个条件, a[i], b[i], 进位值, 
短字符串遍历完后,
*/

int sumOne(int a, int b, int& flag, int& result)
{
    result = a + b + flag;
    switch(result)
    {
        case 0:
            flag = 0;
            result = 0;
            break;
        case 1:
            flag = 0;
            result = 1;
            break;
        case 2:
            flag = 1;
            result = 0;
            break;
        case 3:
            flag = 1;
            result = 1;
            break;
        default :
            return -1;
    }

    return 0;
}

string addBinary(string a, string b)
{
    if( a.empty())
        return b;
    if (b.empty())
        return a;

    int lsize = a.size() > b.size() ? a.size() : b.size();
    int ssize = a.size() <= b.size() ? a.size() : b.size();

    const string& lstr = a.size() > b.size() ? a : b;
    const string& sstr = a.size() <= b.size() ? a : b;

    int flag = 0;
    string c;
    for (int i = 0; i < lsize; ++i)
    {
        int lint = lstr[lsize - i - 1] - '0';
        int sint = 0;
        if (i < ssize)
        {
            sint = sstr[ssize - i - 1] - '0';
        }

        int result = 0;
        sumOne(lint, sint, flag, result);
        c.push_back(result + '0');
    }
    if (flag)
        c.push_back('1');

    reverse(c.begin(), c.end());

    return c;
}

int main(int argc, char const *argv[])
{
    // printf("run, max = %d, min = %d\n", INT_MAX, INT_MIN);

    string str1 = "1";
    string str2 = "1";
    printf("a = %s\n", str1.c_str());
    printf("b = %s\n", str2.c_str());
    printf("c = %s\n", addBinary(str1, str2).c_str());

    return 0;
}