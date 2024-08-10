#!/usr/bin/python3
"""
Solution to lockboxes problem
"""

def canUnlockAll(boxes):
    if not isinstance(boxes, list) or len(boxes) == 0:
        return False
    
    n = len(boxes)
    opened_boxes = set([0])  # Start with box 0
    stack = [0]  # Stack to keep track of boxes to explore
    
    while stack:
        current_box = stack.pop()
        for key in boxes[current_box]:
            if key < n and key not in opened_boxes:
                opened_boxes.add(key)
                stack.append(key)
    
    return len(opened_boxes) == n
