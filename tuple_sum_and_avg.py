list1 = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]
result_sum = ()
result_avg = ()

for t in list1:
    total_sum = sum(t)
    avg = total_sum / len(t)
    
    result_sum = result_sum + (total_sum,)
    result_avg = result_avg + (avg,)

print("Sum of tuples:", result_sum)
print("Average of tuples:", result_avg)
