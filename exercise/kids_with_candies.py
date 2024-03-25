from typing import List


def kids_with_candies(candies: List[int], extraCandies: int) -> List[bool]:
    """
    Determine if each kid can have the greatest number of candies after receiving extra candies.

    Args:
        candies (List[int]): A list of integers representing the number of candies each kid has initially.
        extraCandies (int): An integer representing the number of extra candies you have.

    Returns:
        List[bool]: A list of boolean values indicating whether each kid can have the greatest number of candies
                    after receiving the extra candies. True if they can have the greatest number, False otherwise.
    """
    return [True if (i+extraCandies >= max(candies)) else False for i in candies]