# 그래프에서 정점끼리의 최단경로를 구하는 문제
# 하나의 정점에서 다른 모든 정점까지의 최단 경로를 구하는 문제
# single source shortest path problem

import sys

def dijkstra(K, V, graph):
    """
    첫 정점을 기준으로 연결되어 있는 정점들을 추가해가며, 최단 거리를 갱신하는 것.
    정점을 잇기 전까지는 시작점을 제외한 정점들은 모두 무한대 값을 가짐.

    정점 A에서 B로 이어지면,
    정점 B가 가지는 최단 거리는 시작점부터 정점 A까지의 최단거리
    +
    점 A와 점 B 간선의 가중치와 기존에 가지고 있던 정점 B의 최단 거리 중 작은 값이 최단거리
    """
    # INF는 시스템의 맥스사이즈를 가져와서 Infinity를 뜻한다.
    INF = sys.maxsize
    # s는 해당 노드를 방문 했는지 여부를 저장하는 변수이다.
    s = [False] * V
    # memoization : 컴퓨터 프로그램이 동일한 계산을 반복해야 할 때, 이전에 계산한 값을 메모리에
    # 저장함으로써 동일한 계산의 반복 수행을 제거하여 프로그램 실행 속도를 빠르게 하는 기술이다.
    # 동적 계획법의 핵심이 되는 기술이다.
    # 동적 계획법 : 복잡한 문제를 간단한 여러 개의 문제로 나누어 푸는 방법을 말한다.
    # 이것은 부분 문제 반복과 최적 부분 구조를 가지고 있는 알고리즘을 일반적인 방법에 비해
    # 더욱 적은 시간 내에 풀 때 사용한다.
    #
    # dist(거리)는 memoization을 위한 array이다. d[i]는 정점 K에서 i가지 가는 최소한의
    # 거리가 저장되어 있다.
    dist = [INF] * V
    dist[K - 1] = 0

    while True:
        m = INF
        N = -1

        # 방문하지 않은 노드 중 dist 값이 가장 작은 값을 선택해 그 노드의 번호를 N에 저장한다.
        # 즉, 방문하지 않은 노드 중 K 정점과 가장 가까운 노드를 선택한다.
        for j in range(V):
            if not s[j] and m > dist[j]:
                m = dist[j]
                N = j

        # 방문하지 않은 노드 중 현재 K 정점과 가장 가까운 노드와의 거리가 INF 라는 뜻은
        # 방문하지 않은 남아있는 모든 노드가 A에서 도달할 수 없는 노드라는 의미
        # 반복문을 빠져나간다.

        if m == INF:
            break;

        # N번 노드를 '방문'한다.
        # '방문'한다는 의미는 모든 노드를 탐색하며 N번 노드를 통해서 가면 더 빨리 갈 수 있는
        # 노드가 있는지 확인하고, 더 빨리 갈 수 있다면 해당 노드(노드 번호 j)의
        # dist[j]를 업데이트 해준다.
        s[N] = True

        for j in range(V):
            if s[j]: continue
            via = dist[N] + graph[N][j]
            if dist[j] > via:
                dist[j] = via

    return dist

if __name__ == "__main__":
    V, E = map(int, input().split())
    K = int(input())
    INF = sys.maxsize
    graph = [[INF] * V for _ in range(V)]

    for _ in range(E):
        u, v, w = map(int, input().split())
        graph[u - 1][v - 1] = w

    for dist in dijkstra(K, V, graph):
        print(dist if dist != INF else "INF")

    print(dijkstra.__doc__)
