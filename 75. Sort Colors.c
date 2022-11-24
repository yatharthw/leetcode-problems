void sortColors(int* nums, int n){
    int *dupl = (int *) calloc(n, sizeof(int));
    int *freq = (int *) calloc(3, sizeof(int));
    int i, sum = 0;
    for (i = 0; i < n; i++)
        dupl[i] = nums[i];
    for (i = 0; i < n; i++)
        freq[nums[i]]++;
    for (i = 0; i < 3; i++)
    {
        sum += freq[i];
        freq[i] = sum;
    }
    for (i = n - 1; i >= 0; i--)
    {
        freq[dupl[i]]--;
        nums[freq[dupl[i]]] = dupl[i];
    }
}
