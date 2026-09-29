#btvn02
#Nhập thông tin
tong_von_ban_dau = float(input("Nhập tổng vốn ban đầu: "))
tong_gia_tri_ban_ra = float(input("Nhập tổng giá trị bán ra: "))

#Tính toán lợi nhuận
loi_nhuan = tong_gia_tri_ban_ra - tong_von_ban_dau

#Tính toán ROI
roi = ((loi_nhuan / tong_von_ban_dau) * 100)

#In ra kết quả
print("---kết quả---".upper())
print(f"Tổng vốn ban đầu: {tong_von_ban_dau:,} VND")
print(f"Tổng giá trị bán ra: {tong_gia_tri_ban_ra:,} VND")
print(f"Lợi nhuận: {loi_nhuan:,} VND")
print(f"ROI: {roi:,.2f} %")
print("-" * 20)
