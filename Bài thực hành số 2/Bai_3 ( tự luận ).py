from collections import Counter

def dem_so_lan_xuat_hien_chu_cai(tu):
    # Chuyển đổi từ về dạng chữ thường để đếm không phân biệt chữ hoa và chữ thường
    tu = tu.lower()
    # Sử dụng Counter để đếm số lần xuất hiện của mỗi chữ cái
    dem = Counter(tu)
    # Trả về kết quả
    return dict(dem)

tu = "Hello Cau Truc Du Lieu"
print(dem_so_lan_xuat_hien_chu_cai(tu)) 
