'''
Calculate the sum of two integers a and b, but you are not allowed to use the operator + and -.
'''

'''
class Solution {
    public int getSum(int a, int b) {
        
        while(b != 0){
            int carry = a & b;
            a = a ^ b;
            b = carry << 1;
        }
        
        return a;
    }
}

使用 &(And) 计算 carry
使用 ^(异或) 计算值
b 代表 carry 左移位运算
'''