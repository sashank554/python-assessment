def pivot_index(nums):
    total_sum = sum(nums)
    left_sum = 0

    for i, num in enumerate(nums):
        # Check if left sum equals right sum
        if left_sum == (total_sum - left_sum - num):
            return i
        left_sum += num

    return -1  # Return -1 if no pivot index is found

# Example usage
nums = [1, 7, 3, 6, 5, 6]
result = pivot_index(nums)
print(f"Pivot index: {result}")

