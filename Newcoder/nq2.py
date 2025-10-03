"""
Find the number of sorted sub-sequence
1st line: the number of numbers, n>=1 and n<=10^5
2st line: the numbers array, a(i)>=1 and a(i)<=10^9
In:6
1 2 3 2 2 1
Out:2

In: 9
1 2 1 2 1 2 1 2 1
Out: 5
"""
import sys
def fun(values):
    """
    use state shift method
    :param values: num arrays
    :return:
    """
    state=0
    cnt=1 #######
    for i in range(len(values)-1):
        if values[i]< values[i+1]: #### exclude"="
            if state == 0:
                state = 1
            elif state == -1:  # state shift, then count number, so there is a previous-sorted sub array
                cnt += 1
                state = 0
        elif values[i]>values[i+1]:
            if state == 0:
                state = -1
            elif state == 1:  # state shift, then count number, so there is a previous-sorted sub array
                cnt += 1
                state = 0
    print(cnt)

def fun2(values):
    """
    use the method for judging the peak or though of wave
    :param values:
    :return:
    """
    cnt=1
    i=1
    while i <= len(values) - 2:
        if (values[i-1] < values[i] and values[i] > values[i + 1] or
                values[i-1] > values[i] and values[i] < values[i + 1]):
            cnt += 1
            if i<=len(values)-4 :i += 2
            else: i+=1   ########ensure judge whether the 2nd last is peak or though
        else:
            i += 1
    print(cnt)

if __name__ == "__main__":
    n = int(sys.stdin.readline().strip())
    line = sys.stdin.readline().strip()
    values = list(map(float, line.split())) ###float
    fun(values)