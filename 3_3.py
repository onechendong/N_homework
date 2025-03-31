import numpy as np
import scipy.interpolate as interp
from scipy.optimize import fsolve

t = np.array([0, 3, 5, 8, 13])  
d = np.array([0, 200, 375, 620, 990])  
v = np.array([75, 77, 80, 74, 72]) 

# Hermite interpolating polynomial
hermite_poly = interp.CubicHermiteSpline(t, d, v)

velocity_func = hermite_poly.derivative()
acceleration_func = velocity_func.derivative()

critical_times = fsolve(acceleration_func, np.mean(t)) 
valid_critical_times = [t_c for t_c in critical_times if t[0] <= t_c <= t[-1]]
critical_speeds = [velocity_func(t_c) for t_c in valid_critical_times]

# max speed
max_speed = max(critical_speeds) if critical_speeds else max(v)
max_speed_mph = max_speed * 0.681818  # Convert to mi/h

# position and speed at t = 10
t_pred = 10
d_pred = hermite_poly(t_pred)  
v_pred = velocity_func(t_pred)  
v_pred_mph = v_pred * 0.681818  

# check if speed exceeds 55 mi/h
time_range = np.linspace(min(t), max(t), 100)
speed_values = velocity_func(time_range) * 0.681818 

over_speed_times = time_range[speed_values > 55]
first_exceed_time = over_speed_times[0] if len(over_speed_times) > 0 else None

# Print results
print(f"Predicted position at t=10: {d_pred:.2f} feet")
print(f"Predicted speed at t=10: {v_pred:.2f} ft/s ({v_pred_mph:.2f} mi/h)")
if first_exceed_time:
    print(f"First time car exceeds 55 mi/h: {first_exceed_time:.2f} s")
else:
    print("Car never exceeds 55 mi/h")
print(f"Predicted maximum speed: {max_speed:.2f} ft/s ({max_speed_mph:.2f} mi/h)")
