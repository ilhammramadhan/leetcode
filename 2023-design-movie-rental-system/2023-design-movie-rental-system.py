from sortedcontainers import SortedList
from collections import defaultdict
from typing import List

class MovieRentingSystem:

    def __init__(self, n: int, entries: List[List[int]]):
        self.prices = {}  # (shop, movie) -> price
        self.unrented = defaultdict(SortedList)  # movie -> SortedList of (price, shop)
        self.rented = SortedList()  # SortedList of (price, shop, movie)

        for shop, movie, price in entries:
            self.prices[(shop, movie)] = price
            self.unrented[movie].add((price, shop))

    def search(self, movie: int) -> List[int]:
        cheapest_shops = self.unrented[movie]
        result = []
        for i in range(min(5, len(cheapest_shops))):
            price, shop = cheapest_shops[i]
            result.append(shop)
        return result

    def rent(self, shop: int, movie: int) -> None:
        price = self.prices[(shop, movie)]
        self.unrented[movie].remove((price, shop))
        self.rented.add((price, shop, movie))

    def drop(self, shop: int, movie: int) -> None:
        price = self.prices[(shop, movie)]
        self.rented.remove((price, shop, movie))
        self.unrented[movie].add((price, shop))

    def report(self) -> List[List[int]]:
        result = []
        for i in range(min(5, len(self.rented))):
            price, shop, movie = self.rented[i]
            result.append([shop, movie])
        return result