import Lab2.bmi as bmi

def test_bmi_under_weight():
    assert bmi.calculate_bmi(1.75,30) == -1

def test_bmi_normal_weight():
    assert bmi.calculate_bmi(1.83,70) == 0
def test_bmi_over_weight():
    assert bmi.calculate_bmi(1.85,100) == 1
