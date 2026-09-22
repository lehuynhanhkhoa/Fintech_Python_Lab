# 1. Nhập thông tin từ người dùng
ho_ten = input("Nhập họ tên khách hàng: ")
so_dien_thoai = input("Nhập số điện thoại: ")
cccd = input("Nhập số Căn cước công dân (CCCD): ")
so_tien_nap = float(input("Nhập số tiền nạp ban đầu (VND): "))

# 2. Định nghĩa phí mở ví và tính số dư thực tế
phi_mo_vi = 50000
so_du_kha_dung = so_tien_nap - phi_mo_vi

# 3. Xử lý chuỗi theo yêu cầu bài toán
ho_ten_hoa = ho_ten.upper()  # In hoa toàn bộ họ tên
b_so_cuoi_cccd = cccd[-4:]   # Cắt lấy 4 số cuối của CCCD

# 4. In biên lai khởi tạo ví (sử dụng định dạng phân cách hàng nghìn)
print("\n" + "="*35)
print("=== BIÊN LAI KHỞI TẠO VÍ ĐIỆN TỬ ===")
print(f"Họ tên khách hàng: {ho_ten_hoa}")
print(f"4 số cuối CCCD: {b_so_cuoi_cccd}")
print(f"Số tiền nạp: {so_tien_nap:,.0f} VND")
print(f"Phí mở ví: {phi_mo_vi:,.0f} VND")
print(f"Số dư khả dụng thực tế: {so_du_kha_dung:,.0f} VND")
print("="*35)
