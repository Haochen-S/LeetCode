

public class Find_First_and_Last_Position_of_Element_in_Sorted_Array_34 {
    
}

class Solution {
    public int[] searchRange(int[] nums, int target) {
        int startIndex = -1;
        int endIndex = -1;
        int length = nums.length;
        int index = (int)Math.ceil(length / 2);
        int indexOfTarget;

        while (true) {
            if (nums[index] == target) {
                indexOfTarget = index;
                break;
            }
            if (index <= 0 || index >= length) {
                return new int[] {startIndex, endIndex};
            }
            if (nums[index] > target) {
                index = (int)Math.ceil(index / 2);
                continue;
            }
            
            if (nums[index] < target) {
                index += (int)Math.ceil((length - index) / 2);
                continue;
            }
        }

        index = (int)Math.ceil(indexOfTarget / 2);
        while (true) {
            if (index == 0) {
                if (nums[0] == target) {
                    startIndex = 0;
                }
                break;
            }
            if (index == indexOfTarget) {
                if (nums[indexOfTarget] == target) {
                    startIndex = indexOfTarget;
                }
                break;
            }
            if (nums[index] == target) {
                if (nums[index - 1] != target) {
                    startIndex = index;
                    break;
                }
                index = (int)Math.ceil(index / 2);
            } else {
                if (nums[index + 1] == target) {
                    startIndex = index + 1;
                    break;
                }
                index += (int)Math.ceil((indexOfTarget - index) / 2); 
            }
        }
        index = indexOfTarget + (int)Math.ceil((length - indexOfTarget) / 2); 
        while (true) {
            if (index == length - 1) {
                if (nums[length - 1] == target) {
                    endIndex = length - 1;
                }
                break;
            }
            if (index == indexOfTarget) {
                if (nums[indexOfTarget] == target) {
                    endIndex = indexOfTarget;
                }
                break;
            }
            if (nums[index] == target) {
                if (nums[index + 1] != target) {
                    endIndex = index;
                    break;
                }
                index += (int)Math.ceil((length - index) / 2);
            } else {
                if (nums[index - 1] == target) {
                    endIndex = index + 1;
                    break;
                }
                index += indexOfTarget + (int)Math.ceil((index - indexOfTarget) / 2); 
            }
        }

        return new int[] {startIndex, endIndex};
    }
}