def min_boxes_sequential(n, m, weights) :
    box_count = 1
    current_weight = 0

    for weight in weights:
        if current_weight + weight <= m:
            current_weight += weight
        else:
            box_count += 1
            current_weight = weight

    return box_count

if __name__ == "__main__" :
    import sys
    input_data = sys.stdin.read().split()
    n = int(input_data[0])
    m = int(input_data[1])
    weights = list(map(int, input_data[2:]))

    result = min_boxes_sequential(n, m, weights)
    print(result)