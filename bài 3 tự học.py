# Bài 3
ma_giao_dich = "GD001-5000000-VND"
# Kỹ thuật cắt chuỗi để lấy phần số tiền "5000000"
# Cấu trúc chuỗi: GD001 (0..4), dấu '-' (5), số tiền (6..12)
cac_phan = ma_giao_dich.split("-")
so_tien_str = cac_phan[1]
# Ép kiểu sang số nguyên
so_tien = int(so_tien_str)
# Kiểm tra điều kiện
if so_tien >= 5000000:
    print("Giao dịch cần xác thực OTP")
else:
    print("Giao dịch thành công")
