"""
description of the code goes here
"""

error_limit = 0.0067  # equivalent to 1*(e^-5)


def f(x):
    return 3 * (x ** 2)


def definite_integral(lower, upper):
    return (upper ** 3) - (lower ** 3)


def get_rounded_n_to_nearest_100(n):
    reminder = n % 100
    res = int(n / 100)

    if reminder < 50:
        return res * 100
    else:
        return int((res + 1) * 100)


def trapezoid_integral(lower, upper, n):
    delta_x = float((upper - lower) / n)
    result = 0
    f_1 = lower
    for a in range(lower, n+1):
        f_2 = f_1 + delta_x
        result = result + (((f(f_1) + f(f_2)) / 2) * delta_x)
        f_1 = f_2

    return result


lower_bound = int(input('Enter lower bound: '))
upper_bound = int(input('Enter upper bound: '))
no_of_poly = int(input('Enter number of Polygons for approximate area: '))

approx_area = trapezoid_integral(lower_bound, upper_bound, no_of_poly)
definite_area = definite_integral(lower_bound, upper_bound)

print("The APPROXIMATE area of the circle is %f" % approx_area)
print("The DEFINITE area of the circle is %f" % definite_area)
print("ERROR is %f" % (approx_area - definite_area))

while abs(approx_area - definite_area) > error_limit:
    approx_area = trapezoid_integral(lower_bound, upper_bound, no_of_poly)
    no_of_poly += 1

print("Number of polygons that gives an error less than 1e-5 is %d" % get_rounded_n_to_nearest_100(no_of_poly))
# print("New ERROR is %f" % (approx_area - definite_area))
