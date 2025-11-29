import Lab2.bmi as bmi

def test_bmi_under_weight():
    assert bmi.bmi_category(17.0) == "Under Weight"

def test_bmi_normal_weight():
    assert bmi.bmi_category(22.0) == "Normal Weight"

def test_bmi_over_weight():
    assert bmi.bmi_category(27.0) == "Over Weight"
