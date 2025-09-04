def digit_to_words(num):
    digit_map = {
        '0': 'zero',
        '1': 'one',
        '2': 'two',
        '3': 'three',
        '4': 'four',
        '5': 'five',
        '6': 'six',
        '7': 'seven',
        '8': 'eight',
        '9': 'nine'
    }
    
    num_str = str(num)
    words = [digit_map[digit] for digit in num_str]
    return ' '.join(words)
print(digit_to_words(123))