# -*- coding: utf-8 -*-
"""
Created on Mon Aug 28 15:17:09 2023

@author: KIIT
"""

def getTotalExecutionTime(n, logs):
    stack = []  
    result = [0] * n  

    prev_time = 0

    for log in logs:
        parts = log.split(":")
        function_id, action, timestamp = int(parts[0]), parts[1], int(parts[2])

        if action == "start":
            if stack:
                result[stack[-1]] += timestamp - prev_time
            stack.append(function_id)
            prev_time = timestamp
        else:
            result[stack.pop()] += timestamp - prev_time + 1
            prev_time = timestamp + 1

    return result


n = 3
logs = ["0:start:0", "1:start:3", "1:end:6", "2:start:8", "2:end:10", "0:end:12"]

# Get the exclusive times
exclusive_times = getTotalExecutionTime(n, logs)

# Print the result
print(exclusive_times)
