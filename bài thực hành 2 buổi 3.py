# Bai2.py
# 1. Nhập vào Họ Tên đầy đủ
fullname = input("Nhập Họ tên đầy đủ: ")

# 2. Nhập vào Năm sinh
birth_year = input("Nhập Năm sinh: ")

# 3. Tách lấy từ cuối cùng (Tên)
# split() mặc định tách theo khoảng trắng, [-1] giúp lấy từ cuối cùng trong danh sách
name = fullname.split()[-1]

# Lấy 3 chữ cái đầu của Tên và chuyển thành viết hoa bằng upper()
# (Nếu tên ngắn hơn 3 ký tự, cú pháp slicing [0:3] sẽ tự động lấy toàn bộ tên)
name_code = name[0:3].upper()

# Tạo mã ưu đãi theo quy tắc bằng F-string
promo_code = f"{name_code}-{birth_year}-VIP"

# In kết quả ra màn hình
print(f"Mã ưu đãi phát sinh: {promo_code}")
