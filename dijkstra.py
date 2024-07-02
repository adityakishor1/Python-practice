def min_path(G, start, end):
	distance = {} 
	prev = {}
	path_str = ''
	visited = set()

	distance[start] = 0
	while True:
		mid = None
		dis_to_mid = float('inf')
		for node in distance:
			if node not in visited and distance[node]<dis_to_mid:
				mid = node
				dis_to_mid = distance[node]

		if mid==None: break
		visited.add(mid)
		for dis, nei in G[mid]:
			if nei not in distance or dis_to_mid+dis<distance[nei]:
				distance[nei] = dis_to_mid+dis
				prev[nei] = mid

	curr = end
	while True:
		if curr not in prev: break
		path_str = ' -> '+prev[curr]+path_str
		curr = prev[curr]
	print path_str+' = '+str(distance[end])
G = {
	'0': [(1, '1'), (12, '2')],
	'1': [(9, '2'), (3, '3')],
	'2': [(5, '4')],
	'3': [(4, '2'), (13, '4'), (15, '5')],
	'4': [(4, '5')],
	'5': []
}

print min_path(G, '0', '5')
