"""
Find the longest increasing subsequence only need to modify a number
The 1st line: n(1 ≤ n ≤ 10^5)
The 2nd line: 1 ≤ a_i ≤ 10^9
Output: The number of longest increasing subsequence
In: 6
7 2 3 1 5 6
Output: 5 - {2 3 1 5 6}

In: 5
10 3 10 5 7
Output: 4 - {3 10 5 7}
"""
import sys
def fun(values):
    i = 1
    record=[]
    while i <= len(values) - 2:
        if(values[i - 1] > values[i] and values[i] < values[i + 1] or  ### through of wave
          values[i-1] < values[i] and values[i] > values[i + 1]):   ### peak of wave
            if values[i + 1] >= values[i - 1]: ######### right > left
                j = i - 1
                while j>=1 and values[j - 1]<=values[j]: # find left the longest subsequence
                    j=j-1

                k=i+2
                while k <= len(values) - 1 and values[k] >= values[k - 1]: # find right longest subsequence
                    k+= 1

                if len(record)==0:record.append((j, k - j))  ####for the subsequence: subscript is j, superscript is k-1
                else:
                    s_index,s_len=record[0]
                    if k-j>s_len: record[0]=(j, k - j)

        i+=1 ################# check each element, rather than check continuous 3 elements

    final_index,final_len=record[0]
    print(final_len)

if __name__ == "__main__":
    n = int(sys.stdin.readline().strip())
    line = sys.stdin.readline().strip()
    values = list(map(int, line.split()))
    fun(values)