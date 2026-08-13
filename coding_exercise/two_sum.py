nums = [7,9,3,45,8,61,23,45,43,17,1,11]
target = 10

for i in range(len(nums)):
    for j in range(i+1, len(nums)):
       if nums[i] + nums[j] == target:
           print("Index: ",[i, j],"Element: ",nums[i],"+",nums[j])