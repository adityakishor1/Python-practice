class Solution(object):
    def findAllRecipes(self, recipes, ingredients, supplies):
        N = len(recipes)
        adj = collections.defaultdict(list)
        inbounds = collections.Counter()
        q = collections.deque(supplies)
        recipeSet = set(recipes)
        ans = []
        
        for i, recipe in enumerate(recipes):
            for ingredient in ingredients[i]:
                adj[ingredient].append(recipe)
                inbounds[recipe] += 1
        
        while q:
            node = q.popleft()
            
            if node in recipeSet: ans.append(node)
            
            for nei in adj[node]:
                inbounds[nei] -= 1
                if inbounds[nei]==0: q.append(nei)
        
        return ans
