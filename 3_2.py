y_vals = [0.740818, 0.670320, 0.606531, 0.548812]  
x_vals = [0.3, 0.4, 0.5, 0.6]  

# P(y) = e^(-y) by Lagrange interpolation
def lagrange_interpolation(x_vals, y_vals):
    def P(y):
        result = 0
        for i in range(len(y_vals)):
            term = x_vals[i]
            for j in range(len(y_vals)):
                if i != j:
                    term *= (y - y_vals[j]) / (y_vals[i] - y_vals[j])
            result += term
        return result
    return P

# Get P(y)
P_y = lagrange_interpolation(x_vals, y_vals)

# f(y) = P(y) - y
def f(y):
    return P_y(y) - y

# solve P(y) = y by Bisection method
def bisection_method(func, p0, p1, max_iter=10):
    i = 0
    while i < max_iter:
        i += 1
        p0_result = func(p0)  
        p1_result = func(p1)  
        
        p2 = (p0 + p1) / 2
        p2_result = func(p2)

        print(f"The {i} time(s) iteration:")
        print(f"p{i} = {p2}")

        if p2_result * p1_result < 0:
            p0 = p2
        elif p2_result * p0_result < 0:
            p1 = p2

    return p2  # If max iterations are exceeded, return the last result

p0 = 0.3
p1 = 0.6

root = bisection_method(f, p0, p1)
print(f"The approximate root is: {root}")
