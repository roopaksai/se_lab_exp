"""
Basic Weather Prediction Model using Quadratic Equation
T(t) = a*t^2 + b*t + c
Where:
- T = Temperature (°C)
- t = Time (hours from midnight)
- a, b, c = Coefficients with default values
"""

import math


class WeatherPredictionModel:
    def __init__(self, a=-0.1, b=2.5, c=15):
        """
        Initialize the quadratic weather model
        
        Default coefficients:
        - a = -0.1 (negative for parabola opening downward - realistic daily temp curve)
        - b = 2.5 (positive slope at start of day)
        - c = 15 (base temperature at midnight in °C)
        """
        self.a = a  # Quadratic coefficient
        self.b = b  # Linear coefficient  
        self.c = c  # Constant term (base temperature)
        
        print(f"Weather Model Initialized:")
        print(f"Equation: T(t) = {self.a}*t² + {self.b}*t + {self.c}")
        print(f"Where t is time (hours from midnight), T is temperature (°C)")
    
    def predict_temperature(self, time_hours):
        """
        Predict temperature at given time using quadratic equation
        
        Args:
            time_hours: Time in hours from midnight (0-24)
        
        Returns:
            temperature: Predicted temperature in Celsius
        """
        # Ensure time is within 0-24 hour range
        time_hours = time_hours % 24
        
        # Calculate temperature using quadratic formula
        temperature = self.a * (time_hours ** 2) + self.b * time_hours + self.c
        
        return temperature
    
    def get_daily_predictions(self):
        """
        Get temperature predictions for every hour of the day
        """
        predictions = []
        
        print(f"\nDaily Temperature Predictions:")
        print(f"{'Time':>6} | {'Temperature':>11}")
        print("-" * 20)
        
        for hour in range(24):
            temp = self.predict_temperature(hour)
            predictions.append((hour, temp))
            
            # Format time display
            if hour == 0:
                time_str = "12 AM"
            elif hour < 12:
                time_str = f"{hour} AM"
            elif hour == 12:
                time_str = "12 PM"
            else:
                time_str = f"{hour-12} PM"
            
            print(f"{time_str:>6} | {temp:>8.2f} °C")
        
        return predictions
    
    def find_peak_temperature_time(self):
        """
        Find the time when temperature is maximum using calculus
        For quadratic ax² + bx + c, maximum occurs at x = -b/(2a)
        """
        if self.a >= 0:
            print("Warning: With positive 'a' coefficient, temperature increases indefinitely")
            return None
        
        peak_time = -self.b / (2 * self.a)
        peak_temp = self.predict_temperature(peak_time)
        
        # Convert to readable time format
        hours = int(peak_time)
        minutes = int((peak_time - hours) * 60)
        
        if hours < 12:
            time_str = f"{hours}:{minutes:02d} AM"
        elif hours == 12:
            time_str = f"{hours}:{minutes:02d} PM"
        else:
            time_str = f"{hours-12}:{minutes:02d} PM"
        
        print(f"\nPeak Temperature Analysis:")
        print(f"Maximum temperature occurs at: {time_str} ({peak_time:.2f} hours)")
        print(f"Peak temperature: {peak_temp:.2f} °C")
        
        return peak_time, peak_temp
    
    def analyze_equation(self):
        """
        Analyze the quadratic equation properties
        """
        print(f"\nQuadratic Equation Analysis:")
        print(f"T(t) = {self.a}*t² + {self.b}*t + {self.c}")
        print("-" * 35)
        
        # Coefficient analysis
        print(f"Coefficient 'a' = {self.a}")
        if self.a > 0:
            print("  → Parabola opens upward (temperature increases with time²)")
        elif self.a < 0:
            print("  → Parabola opens downward (realistic daily temperature curve)")
        else:
            print("  → Linear relationship (no quadratic effect)")
        
        print(f"\nCoefficient 'b' = {self.b}")
        if self.b > 0:
            print("  → Positive initial slope (temperature rises in early hours)")
        elif self.b < 0:
            print("  → Negative initial slope (temperature falls in early hours)")
        else:
            print("  → No linear effect")
        
        print(f"\nCoefficient 'c' = {self.c}")
        print(f"  → Base temperature at midnight: {self.c} °C")
        
        # Calculate discriminant for analysis
        discriminant = self.b**2 - 4*self.a*self.c
        print(f"\nDiscriminant (b² - 4ac) = {discriminant:.2f}")
        
        if discriminant > 0:
            print("  → Equation has two real roots (temperature crosses zero twice)")
        elif discriminant == 0:
            print("  → Equation has one real root (temperature touches zero once)")
        else:
            print("  → Equation has no real roots (temperature never reaches zero)")


def demonstrate_model():
    """
    Demonstrate the weather prediction model with different scenarios
    """
    print("Weather Prediction Model Demonstration")
    print("="*45)
    
    # Scenario 1: Default coefficients (typical day)
    print("\nScenario 1: Typical Day (Default Coefficients)")
    print("-" * 50)
    model1 = WeatherPredictionModel()
    
    # Show some specific time predictions
    test_times = [0, 6, 12, 18, 24]
    print(f"\nSample Predictions:")
    for hour in test_times:
        temp = model1.predict_temperature(hour)
        if hour == 0 or hour == 24:
            time_label = "Midnight"
        elif hour == 6:
            time_label = "6 AM"
        elif hour == 12:
            time_label = "Noon"
        elif hour == 18:
            time_label = "6 PM"
        
        print(f"{time_label:>10}: {temp:6.2f} °C")
    
    # Find peak temperature
    model1.find_peak_temperature_time()
    
    # Analyze equation
    model1.analyze_equation()
    
    # Scenario 2: Hot summer day
    print(f"\n{'='*60}")
    print("Scenario 2: Hot Summer Day")
    print("-" * 30)
    model2 = WeatherPredictionModel(a=-0.08, b=3.0, c=22)
    
    peak_time, peak_temp = model2.find_peak_temperature_time()
    
    # Scenario 3: Cold winter day
    print(f"\n{'='*60}")
    print("Scenario 3: Cold Winter Day")
    print("-" * 30)
    model3 = WeatherPredictionModel(a=-0.05, b=1.5, c=2)
    
    peak_time, peak_temp = model3.find_peak_temperature_time()


def interactive_prediction():
    """
    Interactive temperature prediction
    """
    print(f"\n{'='*50}")
    print("INTERACTIVE TEMPERATURE PREDICTION")
    print("="*50)
    
    try:
        print("Enter coefficients for T(t) = a*t² + b*t + c")
        print("(Press Enter to use default values)")
        
        a_input = input("Enter coefficient 'a' (default -0.1): ").strip()
        a = float(a_input) if a_input else -0.1
        
        b_input = input("Enter coefficient 'b' (default 2.5): ").strip()
        b = float(b_input) if b_input else 2.5
        
        c_input = input("Enter coefficient 'c' (default 15): ").strip()
        c = float(c_input) if c_input else 15
        
        # Create model with custom coefficients
        print(f"\nCreating model with a={a}, b={b}, c={c}")
        model = WeatherPredictionModel(a, b, c)
        
        # Get time input
        time_input = input("\nEnter time (0-24 hours from midnight, default 12): ").strip()
        time_hours = float(time_input) if time_input else 12
        
        # Predict temperature
        predicted_temp = model.predict_temperature(time_hours)
        
        print(f"\nPREDICTION RESULT:")
        print("-" * 20)
        print(f"Time: {time_hours} hours from midnight")
        print(f"Predicted Temperature: {predicted_temp:.2f} °C")
        
        # Show analysis
        model.find_peak_temperature_time()
        
    except (ValueError, KeyboardInterrupt):
        print("\nUsing default values...")
        model = WeatherPredictionModel()
        temp = model.predict_temperature(12)
        print(f"Temperature at noon: {temp:.2f} °C")


def main():
    """
    Main function to run the weather prediction model
    """
    print("Basic Weather Prediction Model")
    print("Using Quadratic Equation: T(t) = a*t² + b*t + c")
    print("="*55)
    
    # Run demonstration
    demonstrate_model()
    
    # Interactive section
    interactive_prediction()
    
    print(f"\nThank you for using the Weather Prediction Model!")


if __name__ == "__main__":
    main()
