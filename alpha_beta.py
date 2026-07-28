import math

def alpha_beta(depth, nodeIndex, maximizingPlayer,
               values, alpha, beta, maxDepth):

    # Leaf node
    if depth == maxDepth:
        return values[nodeIndex]

    if maximizingPlayer:
        best = -math.inf

        for i in range(2):
            value = alpha_beta(depth + 1,
                               nodeIndex * 2 + i,
                               False,
                               values,
                               alpha,
                               beta,
                               maxDepth)

            best = max(best, value)
            alpha = max(alpha, best)

            if beta <= alpha:
                break      # Beta Pruning

        return best

    else:
        best = math.inf

        for i in range(2):
            value = alpha_beta(depth + 1,
                               nodeIndex * 2 + i,
                               True,
                               values,
                               alpha,
                               beta,
                               maxDepth)

            best = min(best, value)
            beta = min(beta, best)

            if beta <= alpha:
                break      # Alpha Pruning

        return best


values = [3, 5, 6, 9, 1, 2, 0, -1]

maxDepth = 3

result = alpha_beta(
    0,
    0,
    True,
    values,
    -math.inf,
    math.inf,
    maxDepth
)

print("Optimal Value:", result)