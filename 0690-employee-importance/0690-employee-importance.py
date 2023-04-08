"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        self.employees_id = {}
        for employee in employees:
            self.employees_id[employee.id] = employee

        def totalImportance(employee):
            sub_importance = 0
            for subordinate_id in employee.subordinates:
                subordinate = self.employees_id[subordinate_id]
                sub_importance += totalImportance(subordinate)
            
            return sub_importance + employee.importance

        return totalImportance(self.employees_id[id])
