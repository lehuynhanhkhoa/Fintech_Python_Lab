#btvn01

#Nhập thông tin nguoi dùng
X = float(input("Nhập tổng hóa đơn: "))
Y = float(input("Nhập số tiền tip: "))
N = float(input("Nhập số người chia hóa đơn: "))

#Tính toán số tiền cả tip
tong_tien = X + (X * Y / 100)

#Tính toán số tiền mỗi người phải trả
tien_moi_nguoi =  round(tong_tien / N)

#In ra hóa đơn
print("---hóa đơn---".upper())
print(f"Tổng hóa đơn: {X:,} VND")
print(f"Số tiền tip: {Y:,} %")
print(f"Số người chia hóa đơn: {N}")
print(f"Tổng tiền: {tong_tien:,} VND")
print("---cảm ơn quý khách---".upper())
