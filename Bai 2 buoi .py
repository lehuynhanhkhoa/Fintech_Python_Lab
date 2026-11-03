# ============================================================
# Bài 2: Hàm chấm điểm tín dụng tự động (Credit Scoring)
# Xếp hạng tín dụng dựa trên thu nhập, lịch sử tín dụng và nợ xấu
# ============================================================

def credit_score(income: float, credit_history_years: int, has_bad_debt: bool = False) -> str:
    """
    Chấm điểm tín dụng tự động dựa trên thu nhập, lịch sử tín dụng và nợ xấu.

    Logic nghiệp vụ:
        1. Có nợ xấu (has_bad_debt == True)               → "Reject"
        2. Thu nhập < 10.000.000 hoặc lịch sử < 1 năm     → "High Risk"
        3. Thu nhập ≥ 20.000.000 và lịch sử ≥ 3 năm       → "VIP"
        4. Các trường hợp còn lại                         → "Standard"

    Tham số:
        income (float): Thu nhập hàng tháng (VNĐ)
        credit_history_years (int): Số năm có lịch sử tín dụng
        has_bad_debt (bool): Có nợ xấu hay không (mặc định False)

    Trả về:
        str: Kết quả xếp hạng ("Reject" | "High Risk" | "VIP" | "Standard")
    """
    # Ưu tiên cao nhất: có nợ xấu → từ chối ngay
    if has_bad_debt:
        return "Reject"

    # Rủi ro cao
    if income < 10_000_000 or credit_history_years < 1:
        return "High Risk"

    # Khách VIP
    if income >= 20_000_000 and credit_history_years >= 3:
        return "VIP"

    # Mặc định
    return "Standard"


# ==================== TEST CASE ====================
if __name__ == "__main__":
    print("--- Kết quả chấm điểm tín dụng ---")

    # Các test case minh họa
    test_cases = [
        (8_000_000, 2, False),           # High Risk
        (25_000_000, 4, False),          # VIP
        (15_000_000, 2, False),          # Standard
        (30_000_000, 5, True),           # Reject
        (5_000_000, 0, False),           # High Risk
        (22_000_000, 3, False),          # VIP
    ]

    for income, years, bad_debt in test_cases:
        result = credit_score(income, years, bad_debt)
        print(f"Thu nhập: {income:>12,} | Lịch sử: {years} năm | Nợ xấu: {bad_debt} → {result}")
