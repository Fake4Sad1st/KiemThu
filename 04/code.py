import pandas as pd

def credibility(a: int, b: float, c: float) -> str:
    if a < 0 or a > 500 or b < 0.01 or b > 1000.00 or c < 0.00 or c > 100.00:
        return "Đầu vào không hợp lệ"
    if a <= 200 and b >= 500.00 and c <= 50.00:
        return "Không phê duyệt vay"
    if a >= 400 and b <= 120.00 and c >= 90.00:
        return "Cho vay với lãi thấp"
    return "Cho vay với lãi cao"


test_cases = pd.read_csv("testcases.csv", delimiter=",")
print(test_cases)

for (test_id, a, b, c, EO) in test_cases.itertuples(index=False):
    result = credibility(a, b, c)
    if result == EO:
        print(f"Test case {test_id} - Passed")
    else:
        print(f"Test case {test_id} - Failed")
        print(f"- Expected output: {EO}")
        print(f"- Actual output: {result}")
