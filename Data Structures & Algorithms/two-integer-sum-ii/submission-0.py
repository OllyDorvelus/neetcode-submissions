class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        val_to_index_map: dict[int,int] = {}

        for i, n in enumerate(numbers):
            diff = target - n
            if diff in val_to_index_map:
                return [val_to_index_map[diff] + 1, i + 1]
            val_to_index_map[n] = i
        return []