1、打印乘法表

2、二分法求平方根
<!-- 基本思想
n 猜测一个平方根（x/2）
n 如果猜小了，则正确的平方根在猜测数字和原数字之间
n 如果猜大了，则正确的平方根在0和猜测数字之间
v 算法描述
n Input: x
n Output: √x
1. low = 0, high = x
2. guess = (low + high) / 2
3. 如果 guess2 == x，则输出 guess，程序结束
4. 如果 guess2 < x，则 low = guess; 继续执行步骤2
5. 如果 guess2 > x，则 high = guess; 继续执行步骤2 -->

3、素数
<!-- 一个大于1的自然数，除了1和它本身外，不能被其他自然数整除；
否则称为合数 -->

4、回文数
<!-- v 一个正数如果顺着和反过来都是一样的（如13431，反过来也是
13431），就称为回文数
v 判断一个数 num 是否为回文数
v 算法
n 求 num 的逆序 num'
n 如果 num == num'，则 num 为回文数
n 否则 num 非回文数 -->