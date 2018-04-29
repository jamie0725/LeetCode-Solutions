/**
 * Given an array of integers, return indices of the two numbers such that they add up to a specific target.
 * You may assume that each input would have exactly one solution, and you may not use the same element twice.
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* twoSum(int* nums, int numsSize, int target) {
    int *answer = malloc(sizeof(int)*2);
    for(int i = 0; i < numsSize; i++){
        for(int j = i + 1; j < numsSize; j++){
            if (nums[i] + nums[j] == target){
                answer[0] = i;
                answer[1] = j;
                return answer;
            }
        }
    }
    return NULL;
}
