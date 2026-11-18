# Copyright (C) 2026 Nariman Seyfulayev
# SPDX-License-Identifier: GPL-3.0-only


from constants import LB, INCH, FOOT

# Convert pounds to Kg
def lb_to_kg(lb: float)-> float:
    return round(lb * LB, 2)

# Convert feet and inches to meters
def ft_and_inch_to_m(ft_inch: tuple)-> float:
    return round(ft_inch[0] * FOOT + ft_inch[1] * INCH, 2)

