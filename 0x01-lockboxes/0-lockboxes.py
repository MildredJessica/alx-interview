#!/usr/bin/python3
"""Function to unlock boxes"""


def canUnlockAll(boxes):
    unlocked = [0]
    for id, box in enumerate(boxes):
        if not box:
            continue
        for key in box:
            if key < len(boxes) and key not in unlocked and key != id:
                unlocked.append(key)
    if len(unlocked) == len(boxes):
        return True
    return False
