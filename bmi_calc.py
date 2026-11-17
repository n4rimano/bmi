def bmi(data: tuple)-> None | float:
    weight, height = data  # Unpacking
    if(height < 1.0 or height > 2.5 or weight < 20 or weight > 200):
        return None

    return round(weight / height**2, 1)

