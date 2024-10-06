def safe_divide(numerator, denominator):
    try:
        # Attempt to convert inputs to floats
        num = float(numerator)
        denom = float(denominator)
        
        # Perform the division
        result = num / denom
        return result
    except ZeroDivisionError:
        return "Error: Division by zero is not allowed."
    except ValueError:
        return "Error: Non-numeric input provided."