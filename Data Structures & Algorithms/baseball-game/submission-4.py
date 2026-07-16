class Solution:
    def calPoints(self, operations: List[str]) -> int:
        record: list[int] = []
        for op in operations:
            if op == "+":
                first_num = record[-1]
                second_num = record[-2]
                record.append(first_num+second_num)
            elif op == "D":
                record.append(record[-1] * 2)
            elif op == "C":
                record.pop()
            else:
                record.append(int(op))
        return sum(record)
        