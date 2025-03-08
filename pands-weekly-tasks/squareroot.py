def sqrt():
    num = float(input("Please enter a positive number higher than 0: "))
    while num <= 0:
        num = float(input("Please enter a positive number higher than 0: "))
        if num > 0:
            break
    approx = 0.5 * num
    better = 0.5 * (approx + num/approx)
    while better != approx:
        approx = better
        better = 0.5 * (approx + num/approx)
    print("The square root of", num, "is approx.", round(better, 2))
sqrt()

# References:
# https://en.wikipedia.org/wiki/Newton%27s_method