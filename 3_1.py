from math import factorial, cos, sin

def p1(x):
    return y0*((x-x1)/(x0-x1)) + y1*((x-x0)/(x1-x0))

def p2(x):
    return y0*(((x-x1)*(x-x2))/((x0-x1)*(x0-x2))) + y1*(((x-x0)*(x-x2))/((x1-x0)*(x1-x2))) + y2*(((x-x0)*(x-x1))/((x2-x0)*(x2-x1)))

def p3(x):
    return y0*(((x-x1)*(x-x2)*(x-x3))/((x0-x1)*(x0-x2)*(x0-x3))) + y1*(((x-x0)*(x-x2)*(x-x3))/((x1-x0)*(x1-x2)*(x1-x3))) + y2*(((x-x0)*(x-x1)*(x-x3))/((x2-x0)*(x2-x1)*(x2-x3))) + y3*(((x-x0)*(x-x1)*(x-x2))/((x3-x0)*(x3-x1)*(x3-x2)))

def lagrange_error_bound(x, x_vals, degree):
    n = degree + 1
    # 找到插值點範圍內 (n+1) 階導數的最大值
    max_derivative = 1  # cos(x) 的導數最大值為 1 或 -1
    
    # 計算 |(x-x0)(x-x1)...(x-xn)|
    product_term = 1
    for i in range(n):
        product_term *= (x - x_vals[i])
    
    # 誤差界限公式
    error_bound = abs(max_derivative / factorial(n) * product_term)
    return error_bound

x0, y0 = 0.698, 0.7661
x1, y1 = 0.733, 0.7432
x2, y2 = 0.768, 0.7193
x3, y3 = 0.803, 0.6946
x_ans, y_ans = 0.750, 0.7317
x_vals = [x0, x1, x2, x3]

result_1 = p1(x_ans)
error_bound_1 = lagrange_error_bound(x_ans, x_vals, 1)
print(f"# degree one result: {result_1}")
print(f"  error bound: {error_bound_1}\n")

result_2 = p2(x_ans)
error_bound_2 =  lagrange_error_bound(x_ans, x_vals, 2)
print(f"# degree two result: {result_2}")
print(f"  error bound: {error_bound_2}\n")

result_3 = p3(x_ans)
error_bound_3 =  lagrange_error_bound(x_ans, x_vals, 3)
print(f"# degree three result: {result_3}")
print(f"  error bound: {error_bound_3}\n")

print("""It is not possible to obtain the solution for the degree-four interpolation because 
the problem provides only four reference points, whereas five are required for its 
implementation.""")
