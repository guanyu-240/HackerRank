def product(fracs):
    t = reduce(lambda x,y: x*y, fracs, Fraction(1,1))
    return t.numerator, t.denominator
