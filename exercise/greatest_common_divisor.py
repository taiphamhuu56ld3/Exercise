
def gcdOfStrings(str1: str, str2: str) -> str:
    """
    Returns the greatest common divisor of two strings.

    Given two strings `str1` and `str2`, this function computes the greatest common divisor
    (GCD) of their lengths and returns the substring that divides both `str1` and `str2`.

    Args:
        str1 (str): The first input string.
        str2 (str): The second input string.

    Returns:
        str: The greatest common divisor substring of `str1` and `str2`, or an empty string if
        no such substring exists.

    Example:
        >>> gcdOfStrings("ABCABC", "ABC")\n
        >>> result: 'ABC'\n
        >>> gcdOfStrings("ABABAB", "ABAB")\n
        >>> result: 'AB'\n
        >>> gcdOfStrings("LEET", "CODE")\n
        >>> result: ''
    """
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