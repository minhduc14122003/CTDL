from collections import Counter

def dem_so_lan_xuat_hien_tu(file_path):
    # Mở file và đọc nội dung
    with open(file_path, 'r') as f:
        noi_dung = f.read()

    # Chuyển đổi nội dung về dạng chữ thường
    noi_dung = noi_dung.lower()

    # Tách nội dung thành từng từ
    tu = noi_dung.split()

    # Sử dụng Counter để đếm số lần xuất hiện của mỗi từ
    dem = Counter(tu)

    # Trả về kết quả
    return dict(dem)

file_path = "C:\Users\ADMIN\Downloads\P1_data.txt"
print(dem_so_lan_xuat_hien_tu(file_path))
