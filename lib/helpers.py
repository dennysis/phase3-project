def calculate_bmi(weight, height):
    if height > 0:
        return weight / (height ** 2)
    return None
