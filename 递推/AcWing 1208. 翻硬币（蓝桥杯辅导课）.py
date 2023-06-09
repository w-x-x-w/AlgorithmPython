# https://www.acwing.com/problem/content/1210/

'''桌上放着排成一排的若干硬币。我们用 * 表示正面，用 o 表示反面（是小写字母，不是零）。
比如，可能情形是：**oo***oooo
如果同时翻转左边的两个硬币，则变为：oooo***oooo
现在小明的问题是：如果已知了初始状态和要达到的目标状态，每次只能同时翻转相邻的两个硬币,那么对特定的局面，最少要翻动多少次呢？
我们约定：把翻动相邻的两个硬币叫做一步操作。'''

'''输入格式
两行等长的字符串，分别表示初始状态和要达到的目标状态。
输出格式
一个整数，表示最小操作步数
数据范围
输入字符串的长度均不超过100。
数据保证答案一定有解。
输入样例1：
**********
o****o****
输出样例1：
5'''
s=list(input())
e=list(input())
ans=0
def check(x):
    if s[x]=='*':
        s[x]='o'
    else:
        s[x]='*'
for i in range(len(s)-1):
    if s[i]!=e[i]:
        check(i)
        check(i+1)
        ans+=1
print(ans)