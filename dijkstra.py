import heapq

def main():
    n, c = [int(n) for n in input().split()]
    grid = [[int(num) for num in input().split()] for _ in range(n)]

    def valid(i, j):
        return 0 <= i < n and 0 <= j < c 

    neighbours = ((1,0), (0,1), (-1, 0), (0,-1))
        
    dist = [[float('inf')] * c for _ in range(n)]
    dist[0][0] = grid[0][0]

    pq = []
    heapq.heappush(pq, (grid[0][0], 0, 0))

    while pq:
        cost, i, j = heapq.heappop(pq)
        for dx, dy in neighbours:
            if valid(i+dx, j+dy):
                nx, ny = i+dx, j+dy
                newCost = cost + grid[nx][ny]
                if newCost < dist[nx][ny]:
                    dist[nx][ny] = newCost
                    heapq.heappush(pq, (newCost, nx, ny))
    print(">>> Shortest paths: ", dist)
    return dist[-1][-1]

if __name__ == "__main__":
    print(main())
