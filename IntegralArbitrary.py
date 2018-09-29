"""
Create Python program to numerically compute the integral (area) of an
arbitrary function. For your program use 3(x)^2.
Integrate is limited to the range from 1.0 to 5.0.

Define a function in a separate def where you can create the function to be
integrated, f(x).
Define a function that can take in the bounds (upper and lower) and the
number of polygons (n) from the command line, then compute the integral
using simple numeric approximation (Trapezoid Rule).
Return the approximate area as well as the error (error found by computing
the integral by hand and subtract this result from your approximate result).
"""

error_limit = 0.0067  # equivalent to 1*(e^-5)


def f(x):
    return 3 * (x ** 2)


def definite_integral(lower, upper):
    return (upper ** 3) - (lower ** 3)


"""
get_rounded_n_to_nearest_100(n)
This method will round n to nearest 100.
If n = 25, return 0
If n = 55, return 100
If n = 125, return 100
If n = 155, return 200
"""


def get_rounded_n_to_nearest_100(n):
    reminder = n % 100
    res = int(n / 100)

    # if res == 0 and reminder < 50:
    #    res += 1

    if reminder < 50:
        return res * 100
    else:
        return int((res + 1) * 100)


def trapezoid_integral(lower, upper, n):
    delta_x = float((upper - lower) / n)
    result = 0
    f_1 = lower
    for a in range(1, n+1):
        f_2 = f_1 + delta_x
        result = result + (((f(f_1) + f(f_2)) / 2) * delta_x)
        f_1 = f_2

    return result


success = False

while not success:  # to make sure lower and upper bound is in range of 1 and 5
    lower_bound = float(input('Enter lower bound: '))
    upper_bound = float(input('Enter upper bound: '))

    if (lower_bound < upper_bound) and (1 <= lower_bound < 5) and (1 < upper_bound <= 5):
        success = True
    else:
        success = False
        print("Lower and Upper bound input wrong, please keep the range between 1 and 5")

# lower_bound = int(input('Enter lower bound: '))
# upper_bound = int(input('Enter upper bound: '))
no_of_poly = int(input('Enter number of Polygons for approximate area: '))

approx_area = trapezoid_integral(lower_bound, upper_bound, no_of_poly)
definite_area = definite_integral(lower_bound, upper_bound)

print("======================< OUTPUT SUMMARY >========================")
print("The APPROXIMATE area of the circle is %f" % approx_area)
print("The DEFINITE area of the circle is %f" % definite_area)
print("ERROR is %f" % (approx_area - definite_area))

while abs(approx_area - definite_area) > error_limit:
    no_of_poly += 1
    approx_area = trapezoid_integral(lower_bound, upper_bound, no_of_poly)

print("Number of polygons that gives an error less than 1e-5 is %d" % no_of_poly)
print("And rounded to nearest hundred is %d" % get_rounded_n_to_nearest_100(no_of_poly))
# print("New ERROR is %f" % (approx_area - definite_area))
print("======================<<<<<<<<<>>>>>>>>>========================")
