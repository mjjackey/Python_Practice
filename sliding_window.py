from collections import deque

from collections import deque


def max_sliding_window1(nums, k):
    if not nums or k <= 0:
        return []
    n = len(nums)
    if k == 1:
        return nums

    max_values = []
    window = nums[:k]
    current_max = max(window)
    max_values.append(current_max)

    for i in range(1, n - k + 1):
        # 移除窗口的左端元素
        if nums[i - 1] == current_max:
            # 如果移除的元素是当前最大值，则需要重新计算最大值
            current_max = max(nums[i:i + k])
        else:
            # 如果移除的元素不是当前最大值，则只需要比较新加入的元素
            current_max = max(current_max, nums[i + k - 1])

        max_values.append(current_max)

    return max_values



def max_sliding_window2(nums, k):
    if not nums or k <= 0:
        return []
    n = len(nums)
    if k == 1:
        return nums

    max_values = []
    dq = deque()  # dq 用于存储索引

    for i in range(n):
        # 移除窗口外的元素
        if dq and dq[0] < i - k + 1:
            dq.popleft()

        # 移除比当前元素小的队尾元素
        while dq and nums[dq[-1]] < nums[i]:
            dq.pop()

        # 将当前元素的索引加入队列
        dq.append(i)

        # 当窗口到达大小 k 时，开始记录最大值
        if i >= k - 1:
            max_values.append(nums[dq[0]])

    return max_values


if __name__=="__main__":
    # 示例
    nums = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3
    print(max_sliding_window1(nums, k))  # 输出: [3, 3, 5, 5, 6, 7]
    print(max_sliding_window2(nums, k))
