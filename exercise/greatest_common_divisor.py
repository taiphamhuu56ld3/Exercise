
def gcdOfStrings(str1: str, str2: str) -> str:
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a
    len1, len2 = len(str1), len(str2)
    divisor_length = gcd(len1, len2)

    divisor = str1[:divisor_length]
    if str1 == divisor * (len1 // divisor_length) and str2 == divisor * (len2 // divisor_length):
        return divisor
    else:
        return ""