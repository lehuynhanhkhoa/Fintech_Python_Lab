# Bài 4
"""Script tính tổng số tiền nhận được sau thời gian gửi tiết kiệm theo lãi đơn."""
# Khai báo thông tin đầu vào
so_tien_goc = float(222222222)  # 222222222 VNĐ
lai_suat_nam = float(0.06)  # Lãi suất 6%/năm
thoi_gian = float(2)  # Thời gian gửi 2 năm
# Tính tổng tiền theo công thức lãi đơn
tong_tien = so_tien_goc * (1 + lai_suat_nam * thoi_gian)
# In kết quả
print(f"Số tiền gốc: {so_tien_goc:,.0f} VNĐ")
print(f"Lãi suất/năm: {lai_suat_nam * 100}%")
print(f"Thời gian gửi: {thoi_gian} năm")
print(f"Tổng số tiền nhận được: {tong_tien:,.0f} VNĐ")
