# ============================================================
# Bài 1: Hàm Niên kim Trả góp
# Tính số tiền trả góp hàng tháng và tổng lãi phải trả
# ============================================================

def calculate_emi(principal: float, annual_rate: float, months: int) -> tuple[float, float]:
    """
    Tính số tiền trả góp hàng tháng và tổng lãi phải trả.

   (r = lãi suất tháng):
        EMI = P × [r(1+r)^n] / [(1+r)^n − 1]

    Tham số:
        principal (float): Số tiền vay gốc (VNĐ)
        annual_rate (float): Lãi suất năm (ví dụ 0.12 = 12%)
        months (int): Số tháng vay

    Trả về:
        tuple: (emi_hang_thang, tong_lai)
    """
    # 1. Kiểm tra tính hợp lệ của dữ liệu đầu vào
    if principal <= 0 or annual_rate < 0 or months <= 0:
        return 0.0, 0.0

    # 2. Tính lãi suất tháng
    r = annual_rate / 12

    # 3. Tính (1 + r)^n
    power = (1 + r) ** months

    # 4. Tính EMI
    emi = principal * (r * power) / (power - 1)

    # 5. Tính tổng lãi phải trả
    total_payment = emi * months
    total_interest = total_payment - principal

    return emi, total_interest


# ==================== TEST CASE ====================
if __name__ == "__main__":
    # Test case theo yêu cầu đề bài
    goc = 1_000_000_000          # 1 tỷ
    lai_suat_nam = 0.12          # 12%/năm
    thoi_han = 12                # 12 tháng

    emi, tong_lai = calculate_emi(goc, lai_suat_nam, thoi_han)

    print("--- KẾT QUẢ TÍNH EMI ---")
    print(f"Số tiền vay gốc   : {goc:,.0f} VNĐ")
    print(f"Lãi suất năm      : {lai_suat_nam * 100}%")
    print(f"Thời hạn          : {thoi_han} tháng")
    print(f"Trả mỗi tháng     : {emi:,.0f} VNĐ")
    print(f"Tổng lãi phải trả : {tong_lai:,.0f} VNĐ")
