import heapq

def dijkstra(graph, start):
  dist = {node: 2009000999 for node in graph}
  dist[start] = 0
  
  pq = [ (0, start)]
  heapq.heapify(pq)
  
  while pq:
    cur_dist, cur_vertex = heapq.heappop(pq)
    
    if dist[cur_vertex] < cur_dist:
      continue
    
    for neighbor, weight in graph[cur_vertex].items():
      d = cur_dist + weight
      if d < dist[neighbor]:
        dist[neighbor] = d
        heapq.heappush(pq, (d, neighbor))
  
  return dist


N = int(input())
lst = list(map(int, input().split()))
M = int(input())
graph = {i: {} for i in range(1, N + 1)}

for i in range(M):
  s, f = list(map(int, input().split()))
  graph[s][f] = lst[s-1]
  graph[f][s] = lst[f-1]


print(dijkstra(graph, 1)[N] if dijkstra(graph, 1)[N] != 2009000999 else -1 )