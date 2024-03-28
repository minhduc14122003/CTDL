from collections import Counter

def giao_cua_hai_danh_sach(nums1, nums2):
    counts = Counter(nums1)
    giao = []

    for num in nums2:
        if counts[num] > 0:
            giao.append(num)
            counts[num] -= 1

    return giao

nums1 = [1,2,2,1]
nums2 = [2,2]
print(giao_cua_hai_danh_sach(nums1, nums2))  # Kết quả: [2, 2]

nums1 = [4,9,5]
nums2 = [9,4,9,8,4]
print(giao_cua_hai_danh_sach(nums1, nums2))  # Kết quả: [9, 4]
