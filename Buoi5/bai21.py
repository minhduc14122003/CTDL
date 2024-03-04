def tuple_elementwise_sum(tuple1, tuple2):
    return tuple(x + y for x, y in zip(tuple1, tuple2))

tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
output_tuple = tuple_elementwise_sum(tuple1, tuple2)
print(output_tuple)
