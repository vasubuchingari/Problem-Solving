def linearSearchAll(nums, search_element):
    indices = []
    for i in range(len(nums)):
        if nums[i] == search_element:
            indices.append(i)
    if indices:
        print(f"The element {search_element} is found at indices {indices}")
        return indices
    else:
        print("Element not found")
        return []

nums = [7, 6, 5, 7, 7, 7, 7, 2, 7]
search_element = 7
linearSearchAll(nums, search_element)
