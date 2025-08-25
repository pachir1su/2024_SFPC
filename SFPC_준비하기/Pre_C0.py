def min_boxes_for_gifts(gift_weights, box_capacity):
    sorted_weights = sorted(gift_weights, reverse=True)
    
    boxes = []

    for weight in sorted_weights:
        placed = False
        for i in range(len(boxes)):
            if boxes[i] + weight <= box_capacity:
                boxes[i] += weight
                placed = True
                break
        if not placed:
            boxes.append(weight)
    
    return len(boxes)

gift_weights = [13, 26, 31, 5, 8, 6, 7, 15, 40, 32]
box_capacity = 40

answer = min_boxes_for_gifts(gift_weights, box_capacity)
print(answer)