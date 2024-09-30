def expanding(l):
    if len(l) < 2:
        return False
    
    prev_diff = abs(l[1] - l[0])
    
    for i in range(2, len(l)):
        diff = abs(l[i] - l[i - 1])
        if diff <= prev_diff:
            return False
        prev_diff = diff
    
    return True