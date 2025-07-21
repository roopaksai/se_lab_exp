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

def print_results(model, t):
    temp = model.predict(t)
    print(f"\nPredicted temperature at {t}h: {temp:.2f} °C")
    t_peak, T_peak = model.peak_temperature()
    if t_peak is not None:
        print(f"Peak temperature: {T_peak:.2f} °C at {t_peak:.2f} hours")
    else:
        print("No peak temperature (parabola opens upward or is linear)")
    D, direction = model.equation_info()
    print(f"Discriminant: {D:.2f}")
    print(f"Parabola opens {direction}.")

def mode_predefined():
    print("\n--- Predefined Variables ---")
    a, b, c, t = -0.1, 2.5, 15, 12
    model = WeatherModel(a, b, c)
    print_results(model, t)

def mode_keyboard():
    print("\n--- Keyboard Input ---")
    try:
        a = float(input("Enter coefficient a (default -0.1): ") or -0.1)
        b = float(input("Enter coefficient b (default 2.5): ") or 2.5)
        c = float(input("Enter coefficient c (default 15): ") or 15)
        t = float(input("Enter time (0-24 hours, default 12): ") or 12)
    except ValueError:
        print("Invalid input. Using defaults.")
        a, b, c, t = -0.1, 2.5, 15, 12
    model = WeatherModel(a, b, c)
    print_results(model, t)

def mode_single_file():
    print("\n--- Single Input from File ---")
    filename = input("Enter filename (default 'input.txt'): ") or "input.txt"
    try:
        with open(filename, "r") as f:
            line = f.readline()
            a, b, c, t = map(float, line.strip().split())
            model = WeatherModel(a, b, c)
            print_results(model, t)
    except Exception as e:
        print(f"Error reading file: {e}")

def mode_multiple_file():
    print("\n--- Multiple Inputs from File ---")
    filename = input("Enter filename (default 'input.txt'): ") or "input.txt"
    try:
        with open(filename, "r") as f:
            for idx, line in enumerate(f, 1):
                if not line.strip():
                    continue
                try:
                    a, b, c, t = map(float, line.strip().split())
                    print(f"\n--- Case {idx} ---")
                    model = WeatherModel(a, b, c)
                    print_results(model, t)
                except Exception as e:
                    print(f"Error in line {idx}: {e}")
    except Exception as e:
        print(f"Error reading file: {e}")

if __name__ == "__main__":
    print("Weather Modelling Program (Quadratic Equation)")
    print("="*45)
    print("Select mode:")
    print("1. Predefined variables")
    print("2. Keyboard input")
    print("3. Single input from text file")
    print("4. Multiple inputs from text file")
    mode = input("Enter mode (1-4): ").strip()
    if mode == "1":
        mode_predefined()
    elif mode == "2":
        mode_keyboard()
    elif mode == "3":
        mode_single_file()
    elif mode == "4":
        mode_multiple_file()