class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        arr_len = len(arr)
        for i in range(0, arr_len):
            max_right = 0
            for j in range (i+1, arr_len):
                if arr[j] > max_right:
                    max_right = arr[j]
            arr[i] = max_right

        arr[arr_len-1] = - 1
        return arr