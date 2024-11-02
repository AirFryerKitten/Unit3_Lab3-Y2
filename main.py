#Jonas York
#U3 L3 
#Merge sort

# Print Statements are commited out feel free to uncommit :3

def merge_sort(num_list):
  if len(num_list) == 1:
    #print(f"BASE CASE: {num_list}\n")

    return num_list

  splitLocation = int(len(num_list)/2)
  left = num_list[:splitLocation]
  right = num_list[splitLocation:]

  #print(f"OG: {num_list}")
  #print(f"L: {left}")
  #print(f"R: {right}\n")

  left = merge_sort(left)
  right = merge_sort(right)

  #print(f"Ready to merge {left} & {right}\n")

  new = []
  leftPoint = 0
  rightPoint = 0

  while leftPoint < len(left) and rightPoint < len(right):
    leftNum = left[leftPoint]
    rightNum = right[rightPoint] 
    if leftNum < rightNum:
     # print(f"Adding left number {leftNum}\n")
      new.append(leftNum)
      leftPoint += 1

    else:
      #print(f"Adding right number {rightNum}\n")
      new.append(rightNum)
      rightPoint += 1 

# This for when one is out range 
  if leftPoint == len(left): 
    while rightPoint < len(right):
      rightNum = right[rightPoint]
      #print(f"Adding right number {rightNum}\n")
      new.append(rightNum)
      rightPoint += 1 

  else:
    while leftPoint < len(left):
      leftNum = left[leftPoint]
      #print(f"Adding left number {leftNum}\n")
      new.append(leftNum)
      leftPoint += 1

  #print(f"New list finished {new}")

  return new


    
def main():
    nums1 = [6,2,5,8,3,4,8]
    nums2 = [1,2,3,4,5,6,7,8]
    nums3 = [8,2,6,0,1,3]

    for num_list in [nums1, nums2, nums3]:
        print(f"\nOriginal: {num_list}")
        new = merge_sort(num_list)
        print(f"Sorted: {new}\n")

if __name__ == "__main__":
    main()