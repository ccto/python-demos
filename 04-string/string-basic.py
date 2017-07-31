a="Hello,world！"

len(a)

a="a"+"b"

a*3

b="He"

b in a #判断一个字符串是否是另一个字符串的子串

for char in a:
    print(char)

# 编写 vowels_count 函数，计算一个字符串中元音字母
# （aeiou或AEIOU）的数目

def vowels_count(input_str):
    ret=0
    for c in input_str:
        if c in "aeiouAEIOU":
            ret=ret+1
    
    return ret

# 字符串中每个字符都有一个索引值（下标）
# v 索引从0（前向）或-1（后向）开始