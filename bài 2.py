# Nhập thông tin từ người dùng
ten_san_pham = input("Nhập tên sản phẩm: ")
so_luong = int(input("Nhập số lượng: "))
don_gia = float(input("Nhập đơn giá: "))

# Tính toán các giá trị hóa đơn
tong_tien_hang = so_luong * don_gia
thue_vat = 0.08 * tong_tien_hang  # 8% Tổng tiền hàng
tong_thanh_toan = tong_tien_hang + thue_vat

# In hóa đơn bán hàng định dạng dấu phân cách hàng nghìn
print("\n" + "="* 30)
print("HÓA ĐƠN BÁN HÀNG")
print("="* 30)
print(f"Tên sản phẩm: {ten_san_pham}")
print(f"Số lượng: {so_luong}")
print(f"Đơn giá: {don_gia:,.0f} VND")
print("-" * 30)
print(f"Tổng tiền hàng: {tong_tien_hang:,.0f} VND")
print(f"Thuế VAT (8%): {thue_vat:,.0f} VND")
print(f"Tổng thanh toán: {tong_thanh_toan:,.0f} VND")
print("="* 30)
