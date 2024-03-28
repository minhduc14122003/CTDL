from collections import deque

def max_in_sliding_window(num_list, k):
    dq = deque()
    max_values = []

    for i in range(len(num_list)):
        while dq and dq[0] < i - k + 1:
            dq.popleft()

        while dq and num_list[dq[-1]] < num_list[i]:
            dq.pop()

        dq.append(i)

        if i >= k - 1:
            max_values.append(num_list[dq[0]])

    return max_values

num_list = [3, 4, 5, 1, -44 , 5 ,10, 12 ,33, 1]
print(max_in_sliding_window(num_list, 3))  # Output: [5, 5, 5, 5, 10, 12, 33, 33]
