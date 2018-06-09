""" On^2 brute force method """
##def twoSum(nums, target):
##        """
##        :type nums: List[int]
##        :type target: int
##        :rtype: List[int]
##        """
##        test = 0
##        length = len(nums)
##        for i in range(0,length):
##            for j in range(1 + i,length):
##                    test = nums[i] + nums[j]
##                    if test == target:
##                            return i ,j
 




""" O N using dictionary """

def twoSum(nums, target):
    """ Convert nums to dictionary """
    """ So that we can get keys and value pairs """

    dic = dict(enumerate(nums))

    for keys, values in dic.items():

        x = target - values

        if (x in dic.values() and list(dic.values()).index(x) != keys):
            return  list(dic.values()).index(x),keys
        

test = [2,5,5,11]
target = 10

print(twoSum(test,target))
