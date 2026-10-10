# Bài 1
def phan_loai_khach_hang(diem_credit):
    """Phân hạng rủi ro tín dụng dựa trên điểm credit score."""
    if 750 <= diem_credit <= 850:
        return "Rủi ro Thấp - Duyệt tự động"
    elif 600 <= diem_credit < 750:
        return "Rủi ro Trung bình - Cần thẩm định"
    elif 300 <= diem_credit < 600:
        return "Rủi ro Cao - Từ chối cấp tín dụng"
    else:
        return "Điểm tín dụng không hợp lệ"
# Ví dụ kiểm tra thử
diem_test = 720
ket_qua = phan_loai_khach_hang(diem_test)
print(f"Điểm {diem_test}: {ket_qua}")
