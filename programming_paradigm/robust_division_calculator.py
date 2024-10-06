def safe_divide(numerator, denominator):
    try:
        # Attempt to convert inputs to floats
        num = float(numerator)
        denom = float(denominator)
        
        # Perform the division
        result = num / denom
        return result
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."
    except ValueError:
        return "Error: Please enter numeric values only."