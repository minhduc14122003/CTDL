def common_elements(tuple1, tuple2):
    #Khai báo một hàm có tên là common_elements nhận hai tham số là tuple1 và tuple2.
    return tuple(set(tuple1) & set(tuple2))
tuple1 = (1,2,3,4,5)
tuple2 = (4,5,6,7,8)
#Tạo hai tuple, tuple1 và tuple2, mỗi cái chứa một dãy số nguyên.
output_tuple = common_elements(tuple1, tuple2)
print(output_tuple)
#Gọi hàm common_elements với tuple1 và tuple2 làm đối số và lưu kết quả vào output_tuple.
#In kết quả ra màn hình.