t_vals = [0, 3, 5, 8, 13]
d_vals = [0, 200, 375, 620, 990]
v_vals = [75, 77, 80, 74, 72]
z_vals = [0, 0, 3, 3, 5, 5, 8, 8, 13, 13]

def f(first,last):
    if first == last:
        return d_vals[int(first/2)]
    if last - first ==1 and first%2 ==0:
        return v_vals[int(first/2)]
    return ((f(first+1, last))-(f(first, last-1)))/(z_vals[last]-z_vals[first])

def H(t):
    tmp =0
    for i in range(1, 10):
        term = 1
        for j in range(i):
            term *= ((t-z_vals[j]))
        # print(f(0, i))
        tmp += f(0, i)*term
    return d_vals[0] + tmp

def H_derivative(H, t, h=1e-5):
    return (H(t + h) - H(t - h)) / (2 * h)


# problem a
t = 10
position_10 = H(t)
print(f"when t = 10 s, position = {position_10} (ft). ")
velocity_10 = H_derivative(H, t)
print(f"when t = 10 s, velocity = {velocity_10} (ft/s).")

# problem b and c
v_limit = 55*5280/3600
iterate_time = 0
v_max = 0
t_target = 0
while iterate_time <= 13:
    v_current = H_derivative(H, iterate_time)
    if v_current > v_max:
        v_max = v_current
        if t_target == 0 and v_current > v_limit:
            t_target = iterate_time
    iterate_time += 0.001
if v_max > v_limit:
    print(f"The car can exceed 55 mi/h, when t = {t_target:.3f} (s). ")
else:
    print("The car can't exceed 55 mi/h. ")
print(f"predicted maximum speed: {v_max} (ft/s).")


