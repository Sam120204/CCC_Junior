def sq_pool(n,t):
    trees = [[0, 0]]

    for i in range(t):
        x, y = list(map(int, input().split()))
        trees.append([x, y])

    x_cor = []
    y_cor = []

    for i in range(len(trees)):
        x_cor.append(trees[i][0])
        y_cor.append(trees[i][1])

    ans = 1
    for x in x_cor:
        for y in y_cor:
            sqr_size = min(n - x, n - y)

            for r, c in trees:
                if x < r <= x + sqr_size and y < c <= y + sqr_size:
                    sqr_size = max(r - x - 1, c - y - 1)

            ans = max(ans, sqr_size)

    print(ans)

if __name__ == "__main__":
    n = int(input())
    t = int(input())
    sq_pool(n,t)
