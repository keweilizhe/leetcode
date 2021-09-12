#include <iostream>
#include <string>
#include <map>
#include <set>
#include <vector>

#include <stdio.h>
#include <limits.h>


using namespace std;

/*
如果匹配到第一个相同,则向后比较, 如果没有匹配并且到达最后,-1
否则,下一个字符匹配
*/
int strStr(string haystack, string needle) 
{
    if (needle.empty())
        return 0;

    int size = haystack.size();
    for (int i = 0; i < size; ++i)
    {
        if (size - i < needle.size())
            return -1;
        for (int j = 0; j < needle.size(); ++j)
        {
            if (haystack[i+j] != needle[j])
                break;
            if (j == needle.size() - 1)
                return i;
        }
    }

    return -1;
}

int main(int argc, char const *argv[])
{
    printf("run, max = %d, min = %d\n", INT_MAX, INT_MIN);

    string str = "  012345678999999999999999999999 xxx";
    // printf("str = %d\n", myAtoi(str));

    return 0;
}