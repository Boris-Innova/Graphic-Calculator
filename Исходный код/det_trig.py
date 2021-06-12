from math import *

"""Переопределение тригонометрических формул, перевод из радиан в градусы."""

# Синус
old_sin = sin
def sin(deg):
	return round(old_sin(radians(deg)), 6)

# Косинус
old_cos = cos
def cos(deg):
	return round(old_cos(radians(deg)), 6)

# Тангенс
old_tan = tan
def tan(deg):
	return round(old_tan(radians(deg)), 6)

# Арксинус
old_asin = asin
def asin(number):
	return round(degrees(old_asin(number)), 6)

# Арккосинус
old_acos = acos
def acos(number):
	return round(degrees(old_acos(number)), 6)

# Арктангенс
old_atan = atan
def atan(number):
	return round(degrees(old_atan(number)), 6)
