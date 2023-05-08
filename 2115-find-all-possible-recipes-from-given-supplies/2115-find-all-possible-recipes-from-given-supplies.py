class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        n = len(recipes)
        graph = defaultdict(lambda: [])
        indegrees = defaultdict(lambda: 0)

        for i in range(n):
            for ingredient in ingredients[i]:
                graph[ingredient].append(recipes[i])
                indegrees[recipes[i]] += 1
        
        possibleRecipes = []
        while supplies:
            ingredient = supplies.pop(0)
            
            for neighbor in graph[ingredient]:
                indegrees[neighbor] -= 1
                
                if indegrees[neighbor] == 0:
                    supplies.append(neighbor)
                    possibleRecipes.append(neighbor)

        return possibleRecipes

