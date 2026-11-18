# Copyright (C) 2026 Nariman Seyfulayev
# SPDX-License-Identifier: GPL-3.0-only


# Importing functions from local module
from prompt import prompt_unit_system, prompt_weight_height, prompt_lb_ft_inch
from converter import lb_to_kg, ft_and_inch_to_m
from bmi_calc import bmi



def main():
    if prompt_unit_system():
        data = prompt_weight_height()
        return bmi(data)
    else:
        data = prompt_lb_ft_inch()
        weight = lb_to_kg(data[0])
        height = ft_and_inch_to_m(data[1:3])
        data = (weight, height)
        return bmi(data)

if __name__ == "__main__":
    result = main()
    print(result)

