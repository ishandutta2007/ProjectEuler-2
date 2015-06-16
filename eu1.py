# ------------------------ Multiples of 3 and 5 --------------------------- #
#                                                                           #
# If we list all the natural numbers below 10 that are multiples of 3 or 5, #
#   we get 3, 5, 6 and 9. The sum of these multiples is 23.                 #
# ------------------------------------------------------------------------- #

# Find the sum of all the multiples of 3 or 5 below 1000.
MAX = 1000

mult3 = sum([n for n in range(MAX) if n%3 == 0])
mult5 = sum([n for n in range(MAX) if n%5 == 0])
mult15 = sum([n for n in range(MAX) if n%15 == 0])

print (mult3 + mult5 - mult15)
