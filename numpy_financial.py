import numpy_financial as npf
import matplotlib.pyplot as plt
import numpy as np

# fv() function in action, which stands for future value.

fv = npf.fv(rate=0.08, nper=5, pmt=0, pv=-1000)

print(f"fv {fv}")

# pv() function is used to calculate  the present value of an investment.
# For example, let's calculate the present value of an investment,
# that needs to total 1000 in 8 years, with an annual interest rate of 10%:
pv = npf.pv(rate=0.10, nper=8, pmt=0, fv=1000)

print(f"fv {pv}")
# Fill in the blanks to calculate the amount you need to invest annually for 15 years at an interest rate of 7%,
# to result in a total amount of 150000.


pv1 = npf.pv(rate=0.07, nper=15, pmt=0, fv=150000)
print(f"fv1 {pv1}")

# The pmt() function is used to compute the payment against loan principal plus interest.
# Let's say we want to calculate how much we have to pay monthly to pay back a loan of 100,000 in 5 years.
# The yearly interest rate is 7%, and is calculated monthly.

pmt = npf.pmt(rate=0.07 / 12, nper=5 * 12, pv=100000, fv=0)
print(f"pmt {pmt}")

# the pmt() function can be used to return the periodic deposit one must make to achieve a specified
# future balance with a given interest rate.
# The code will return the monthly deposits needed to achieve 50000 in 5 years

pmt1 = npf.pmt(rate=0.10 / 12, nper=5 * 12, pv=0, fv=50000)
print(f"pmt1 {pmt1}")

# Fill in the blanks to calculate how much you need to save annually, to result in 100K savings in 30 years.
# The interest rate is 3%.

pmt2 = npf.pmt(rate=0.03, nper=30, pv=0, fv=100000)
print(f"pmt2 {pmt2}")

# an irr() function, used to calculate the IRR (Internal Rate of Return).
# Let's assume we invested 5000 and got the following payments back: 500, 700, 1000, 3000.

# To calculate the IRR, we first need to declare an array with the values, with the first value being
# our initial investment:

Cashflow = [-5000, 500, 700, 1000, 3000]
irr = npf.irr(Cashflow)

print(f"the internal rate of return:{irr}")
# This will calculate the internal rate of return.


# Let's use the irr() function to compare two investment opportunities and decide which one is better.

# Option 1:
# Requires 50K in investment
# Will pay 10K, 25K, 25K, 35K, 42K each year for the next 5 years.

# Option 2:
# Requires 30K in investment
# Will pay 10K, 13K, 18K, 25K, 20K each year for the next 5 years.

# Let's calculate the IRR for each investment and compare:

cf1 = [-50000, 10000, 25000, 25000, 35000, 42000]
cf2 = [-30000, 10000, 13000, 18000, 25000, 20000]

option1 = npf.irr(cf1)
option2 = npf.irr(cf2)

print(f"Option1:{option1}")
print(f"Option2:{option2}")

# You invested a value of 1, and got back a value of 1.
# So the return on your investment is 0 because you did not gain anything.
cf = [-1, 1]
return_of_investment = npf.irr(cf)
print(f"return {return_of_investment}")

# The savefig() function is used to save the chart as an image, so it can be displayed in our Code Playground
rev = [18000, 25000, 20000, 45000, 19500]

plt.plot(rev)

plt.savefig("plot.jpg")

# The plot() function can also take values for both the x and y axis.
# Let's add the month names on the horizontal axis:

rev = [18000, 25000, 20000, 45000, 19500]
month = ["january", "february", "march", "april", "may"]

plt.plot(month, rev)

plt.savefig("plot2.jpg")

# What is the output of this code?
# print(npf.fv(rate=0, nper=3, pmt=0, pv=-100))

# Fill in the blanks to calculate and output the IRR of an investment of 5000,
# which returns the following amounts annually: 2000, 4000, 3000.

arr = [-5000, 2000, 4000, 3000]

irr2 = npf.irr(arr)

print(f"irr2: {irr2}")

# calculate the monthly deposits required to achieve $50 K in 5 years,
# with an annual interest rate of 10 %.

monthly = npf.pmt(rate=0.10 / 12, nper=5 * 12, pv=0, fv=50000)
print(f"monthly {monthly}")

# The Numpy sqrt function calculates the square root
# of each value in an array and returns a new array with the result.


rev2 = [18000, 25000, 20000, 45000, 32000]

rev2 = np.sqrt(rev2)

plt.plot(rev2)

plt.savefig("plot3.jpg")
