class Solution(object):
    def romanToInt(self, s):
        
        roman_values = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        
        total = 0
        prev_value = 0

        # Traverse the string from right to left
        for char in reversed(s):
            current_value = roman_values[char]

            # If the current value is less than the previous value, subtract it
            if current_value < prev_value:
                total -= current_value
            else:
                total += current_value

            # Update previous value for the next iteration
            prev_value = current_value

        return total
