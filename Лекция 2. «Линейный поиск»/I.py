def input_read():
    n, m, k = [int(x) for x in input().split()]
    mines = [[int(x) - 1 for x in input().split()] for _ in range(k)]
    return n, m, k, mines


def render_field(n, m, k, mines):
    field = [[0] * m for _ in range(n)]
    neibs_x = [0, -1, -1, -1, 0, 1, 1, 1]
    neibs_y = [-1, -1, 0, 1, 1, 1, 0, -1]
    for x, y in mines:
        field[x][y] = '*'
        for k in range(8):
            neib_x = x + neibs_x[k]
            neib_y = y + neibs_y[k]
            if neib_x < 0 or neib_x >= n:
                continue
            if neib_y < 0 or neib_y >= m:
                continue
            if field[neib_x][neib_y] == '*':
                continue
            field[neib_x][neib_y] += 1
    return field


def main():
    field = render_field(*input_read())
    for line in field:
        print(*line)


if __name__ == '__main__':
    main()
