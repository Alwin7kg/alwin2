#include <stdio.h>
#include <bits/stdc.h>
using namespace std;
string addBitStrings(string str1, string str2)
{
string ans = "";
int i = str1.size()-1;
int j = str2.size()-1;
int carry = 0;
while (i>=0 || j>=0 || carry){
carry += ((i>=0)?(str1[i--] - '0'):(0));
carry += ((j>=0)?(str1[j--] - '0'):(0));
ans = char('0'+(carry % 2)) + ans;
carry = carry/2;
}
return ans;

int main()
{
int decimal_num, binary_num = 0, i=1,remainder;
printf("Enter a decimal number: ");
scanf("%d", &decimal_num);
while(decimal_num!=0)
{
remainder = decimal_num % 2;
decimal_num /= 2;
binary_num += remainder*i;
i*=10;
}
printf("Binary number: %d\n",binary_num);
return 0;
}

