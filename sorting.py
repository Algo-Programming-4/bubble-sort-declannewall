import random
def bubble(bubble_list):
    length = len(bubble_list)
    for x in range(length):
        for y in range(length-x-1):
            if bubble_list[y] > bubble_list[y+1]:
                keep = bubble_list[y]
                bubble_list[y] = bubble_list[y+1]
                bubble_list[y+1] = keep
    return bubble_list

def main():
    unshorted_list = [53,12,12,8,45,2,1,34,54,21,23,89,45,76,32]
    print(bubble(unshorted_list))
    nums = [random.randint(1,100) for x in range(random.randint(1,100))]
    if bubble(nums) == sorted(nums):
        print("YAY")
    else:
        print(nums)
        print(bubble(nums))
        print(sorted(nums))

if __name__ == "__main__":
    main()