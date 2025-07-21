"""
Weather Modelling Program using Quadratic Equation

T(t) = a*t^2 + b*t + c
Where:
- T = Temperature (°C)
- t = Time (hours from midnight)
- a, b, c = Coefficients
"""

class WeatherModel:
    def __init__(self, a=-0.1, b=2.5, c=15):
        self.a = a
        self.b = b
        self.c = c

    def predict(self, t):
        """Predict temperature at time t (hours from midnight)."""
        t = t % 24
        return self.a * t**2 + self.b * t + self.c

    def peak_temperature(self):
        """Return (time, temperature) of peak temperature in the day."""
        if self.a >= 0:
            return None, None
        t_peak = -self.b / (2 * self.a)
        T_peak = self.predict(t_peak)
        return t_peak, T_peak

    def equation_info(self):
        """Return discriminant and parabola direction."""
        D = self.b**2 - 4*self.a*self.c
        direction = "downward" if self.a < 0 else "upward" if self.a > 0 else "linear"
        return D, direction

if __name__ == "__main__":
    print("Weather Modelling Program (Quadratic Equation)")
    print("="*45)
    try:
        a = float(input("Enter coefficient a (default -0.1): ") or -0.1)
        b = float(input("Enter coefficient b (default 2.5): ") or 2.5)
        c = float(input("Enter coefficient c (default 15): ") or 15)
    except ValueError:
        print("Invalid input. Using default coefficients.")
        a, b, c = -0.1, 2.5, 15

    model = WeatherModel(a, b, c)
    try:
        t = float(input("Enter time (0-24 hours, default 12): ") or 12)
    except ValueError:
        t = 12

    temp = model.predict(t)
    print(f"\nPredicted temperature at {t}h: {temp:.2f} °C")

    t_peak, T_peak = model.peak_temperature()
    if t_peak is not None:
        print(f"Peak temperature: {T_peak:.2f} °C at {t_peak:.2f} hours")
    else:
        print("No peak temperature (parabola opens upward or is linear)")

    D, direction = model.equation_info()
    print(f"Discriminant: {D:.2f}")
    print(f"Parabola opens