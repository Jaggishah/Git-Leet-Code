nums= [1,2,3]
res=[]
subset=[]
def dfs(i):
    if i >= len(nums):
        res.append(subset.copy())
        return

    subset.append(nums[i])
    dfs(i+1)
    print("--->",res)
    # print("append:",i,subset,nums[i])
    subset.pop()
    # print("popbefore:",i,subset,nums[i])
    print(res)
    dfs(i+1)
    # print("pop:",i,subset,nums[i])



dfs(0)
print(res)