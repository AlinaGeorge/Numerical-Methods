def f(y):
    return y  # dy/dt = y (example ODE)

def euler_method(y0, t0, t_end, h):
    y = y0
    t = t0
    while t <= t_end:
        print(f"t = {t:.2f}, y = {y:.4f}")
        y += h * f(y)
        t += h

# Initial conditions and step size
y0 = 1
t0 = 0
t_end = 5
h = 1

euler_method(y0, t0, t_end, h)
