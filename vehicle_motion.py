from sympy import *

t = symbols('t')

s = t**3 - 6*t**2 + 9*t + 5

print("Displacement Function:")
print(s)

velocity = diff(s, t)
print("\nVelocity:")
print(velocity)

acceleration = diff(velocity, t)
print("\nAcceleration:")
print(acceleration)

rest_time = solve(velocity, t)

print("\nVehicle at Rest at:")
print(rest_time)

displacement = integrate(s, (t, 0, 3))

print("\nDisplacement from t=0 to t=3:")
print(displacement)
