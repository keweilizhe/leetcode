#include <iostream>
#include <string>
#include <map>
#include <set>
#include <vector>

#include <stdio.h>
#include <limits.h>


using namespace std;

/*
ay you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete at most k transactions.

Note:
You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).
*/

class Solution {
public:
    int maxProfit(int k, vector<int>& prices) {
        // todo 对这个动态规划理解不方便, 期待以后对动态规划有更深入的了解后再看待这个问题
    }
};

int main(int argc, char const *argv[])
{
    int k = 2;
    int a[] = [];
    vector<int> prices(a, a + sizeof(a)/sizeof(int));

    Solution s;
    printf("max profit = %d\n", s.maxProfit(k, prices));

    return 0;
}