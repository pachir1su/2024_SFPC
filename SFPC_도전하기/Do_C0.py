# Do_C0
import math

grapes = [15, 25, 9, 7, 17, 26, 32, 19, 8, 31]

BOX_CAPACITY = 9
TOTAL_BOXES = 19

full_boxes = [count // BOX_CAPACITY for count in grapes]
remainders = [count % BOX_CAPACITY for count in grapes]

used_boxes = sum(full_boxes)
total_grapes = sum([boxes * BOX_CAPACITY for boxes in full_boxes])

remaining_boxes = TOTAL_BOXES - used_boxes

if remaining_boxes > 0:
    remainders.sort(reverse=True)
    total_grapes += sum(remainders[:remaining_boxes])

print(total_grapes)