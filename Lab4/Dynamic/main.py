def dynamic_kp(values: int, weights: int, capacity: int) -> int:
    assert len(values) == len(weights), "values and weights must have same size"
    length = len(values)
    K = [[0 for _ in range(capacity + 1)] for _ in range(length + 1)]

    for i in range(length + 1):
        for j in range(capacity + 1):
            if i == 0 or weights == 0:
                K[i][j] = 0
            elif weights[i - 1] <= j:
                K[i][j] = max(values[i - 1] + K[i - 1][j - weights[i - 1]], K[i - 1][j])
            else:
                K[i][j] = K[i - 1][j]

    return K[length][capacity]
