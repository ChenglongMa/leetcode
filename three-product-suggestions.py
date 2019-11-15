from typing import List


class Solution:
    def threeProductSuggestions(self, numProducts: int, repository: List, customerQuery: str)->List:
        if not customerQuery or len(customerQuery) < 2:
            return None
        rep = repository[:numProducts]
        res = []
        for product in rep:
            if product[:len(customerQuery)] == customerQuery:
                res.append(product)
        return sorted(res[:3])


if __name__ == "__main__":
    s = Solution()
    print(s.threeProductSuggestions(
        5, ['mobile', 'mouse', 'moneypot', 'moniter', 'mousepad'], 'm'))
    print(s.threeProductSuggestions(
        5, ['mobile', 'mouse', 'moneypot', 'moniter', 'mousepad'], 'mo'))
    print(s.threeProductSuggestions(
        5, ['mobile', 'mouse', 'moneypot', 'moniter', 'mousepad'], 'mou'))
    print(s.threeProductSuggestions(
        5, ['mobile', 'mouse', 'moneypot', 'moniter', 'mousepad'], 'mous'))
    print(s.threeProductSuggestions(
        5, ['mobile', 'mouse', 'moneypot', 'moniter', 'mousepad'], 'mouse'))

    print('mouose'[:2]=='mo')
