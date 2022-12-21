class Solution:
    def average(self, salary: List[int]) -> float:
        edge_salary = max(salary) + min(salary)
        return (sum(salary)-edge_salary) / (len(salary)-2)