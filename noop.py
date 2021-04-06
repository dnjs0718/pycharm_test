def roman_to_num(s):
    symbol = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    result = 0
    for i in range(len(s)):
        if symbol[s[i]] == 5 or symbol[s[i]] == 10:
            if symbol[s[i - 1]] == 1:
                result += symbol[s[i]] - 2 * symbol[s[i - 1]]


        if symbol[s[i]] == 50 or symbol[s[i]] == 100:
            if symbol[s[i - 1]] == 10:
                result += symbol[s[i]] - 2 * symbol[s[i - 1]]

        if symbol[s[i]] == 500 or symbol[s[i]] == 1000:
            if symbol[s[i - 1]] == 100:
                result += symbol[s[i]] - 2 * symbol[s[i - 1]]

        else:
            result += symbol[s[i]]

    return result

print(roman_to_num('MCMXCIV'))