def majorityElement(nums: list[int]) -> int:
    candidate = None
    count = 0
    
    for num in nums:
        # Pick a new candidate when count resets to zero
        if count == 0:
            candidate = num
            
        # Increment if same as candidate, decrement if different
        count += 1 if num == candidate else -1
        
    return candidate