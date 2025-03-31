x0, y0 = 0.698, 0.7661
x1, y1 = 0.733, 0.7432
x2, y2 = 0.768, 0.7193
x3, y3 = 0.803, 0.6946
x_ans, y_ans = 0.750, 0.7317

# degree one
def p1(x):
    return y0*((x-x1)/(x0-x1)) + y1*((x-x0)/(x1-x0))
# degree two 
def p2(x):
    return y0*(((x-x1)*(x-x2))/((x0-x1)*(x0-x2))) + y1*(((x-x0)*(x-x2))/((x1-x0)*(x1-x2))) + y2*(((x-x0)*(x-x1))/((x2-x0)*(x2-x1)))
# degree three
def p3(x):
    return y0*(((x-x1)*(x-x2)*(x-x3))/((x0-x1)*(x0-x2)*(x0-x3))) + y1*(((x-x0)*(x-x2)*(x-x3))/((x1-x0)*(x1-x2)*(x1-x3))) + y2*(((x-x0)*(x-x1)*(x-x3))/((x2-x0)*(x2-x1)*(x2-x3))) + y3*(((x-x0)*(x-x1)*(x-x2))/((x3-x0)*(x3-x1)*(x3-x2)))
# error value
def err(y):
    return (abs(y-y_ans)/y_ans) * 100

result_1 = p1(x_ans)
error_1 = err(result_1)
print(f"# degree one result: {result_1}")
print(f"  error: {error_1} %\n")
result_2 = p2(x_ans)
error_2 = err(result_2)
print(f"# degree two result: {result_2}")
print(f"  error: {error_2} %\n")
result_3 = p3(x_ans)
error_3 = err(result_3)
print(f"# degree three result: {result_3}")
print(f"  error: {error_3} %\n")

print("""It is not possible to obtain the solution for the degree-four interpolation because 
the problem provides only four reference points, whereas five are required for its 
implementation.""")
