// rotate in parts
// first rotate the whole array
// then rotate the first half
// then rotate last
void reverse(int *nums, int start, int end)
{
    int temp = 0;
    while (start < end)
    {
        temp = nums[start];
        nums[start] = nums[end];
        nums[end] = temp;
        start++;
        end--;
    }
}
void rotate(int* nums, int n, int k)
{
    k = k % n;
    reverse(nums, 0, n - 1);
    reverse(nums, 0, k - 1);
    reverse(nums, k, n - 1);
}
