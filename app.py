def checkHeight(red_shirts,blue_shirts):
    for idx,val in enumerate(red_shirts):
        if highest_player == "RED":
            print([red_shirts[idx],blue_shirts[idx]])
            if(red_shirts[idx] < blue_shirts[idx]):
                return False
        if highest_player == "BLUE":
            print([blue_shirts[idx],red_shirts[idx]])
            if(blue_shirts[idx] < red_shirts[idx]):
                return False
    return True
    

red_shirts = [5,8,1,5,4]
blue_shirts = [6,9,2,4,5]

red_shirts.sort()
red_shirts.reverse()

blue_shirts.sort()
blue_shirts.reverse()

if red_shirts[0] > blue_shirts[0]:
    highest_player = "RED"
else:
    highest_player = "BLUE"

a = checkHeight(red_shirts,blue_shirts)
print(a)


############################################################################################################################################
## Time Complexity= O(nlogn)
## Explanation: It is due to sorting of the two lists.
## Space Complexity = O(1)
## Explanation= As we are returning only True or False.
############################################################################################################################################
