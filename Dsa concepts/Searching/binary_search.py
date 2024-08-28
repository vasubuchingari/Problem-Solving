def binarySearchAll(nums, search_element):
    low=0
    high=len(nums)-1
    is_found=False
    while low<=high and not is_found:
        mid=(low+high)//2
        if nums[mid]==search_element:
            is_found=True
        elif search_element>nums[mid]:
            low=mid+1
        else:
            high=mid-1
    if is_found==True:
        print(f"the element is found at the index {mid}")
    else:
        print("the element doesnt exist in the list")
        
nums = [1,2,3,4,5,6,7]
search_element = 6
binarySearchAll(nums, search_element)
