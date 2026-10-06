# Bai1.py
# 1. Yêu cầu nhập một địa chỉ email
email = input("Nhập địa chỉ email cần bảo mật: ")

# 2. Dùng split("@") để tách phần tên đăng nhập và phần tên miền
username, domain = email.split("@")

# 3. Trích xuất 3 ký tự đầu tiên của tên đăng nhập (dùng Slicing [0:3])
username_start = username[0:3]

# 4. Ghép 3 ký tự đầu + chuỗi "***@" + tên miền và in kết quả ra màn hình
masked_email = f"{username_start}***@{domain}"
print(f"Kết quả bảo mật: {masked_email}")
