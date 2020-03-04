"""
Whether the number of array can be equal after altering
rule: each number can multiply 2 and the number of times is not limited
2
1 2

4
1 3 4 8
"""
import sys
import math
def fun():
    n = int(sys.stdin.readline().strip())
    line = sys.stdin.readline().strip()
    input_list = list(map(int, line.split()))
    input_list.sort()
    x_max=max(input_list)
    if all(x_max% num ==0 and x_max//num % 2 ==0 for num in input_list[:-1]): # and math.log(2,x_max/y_min)==1.0 or math.log(2,x_max/y_min) %2.0==0
             print("YES")
    else:
             print("NO")

if __name__ == "__main__":
    fun()