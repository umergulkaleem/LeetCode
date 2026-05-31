class FoodRatings:

    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.food_to_cuisine = {}
        self.food_to_rating = {}
        self.cuisine_heap = {}

        for f,c,r in zip(foods,cuisines,ratings):
            self.food_to_rating[f] =r
            self.food_to_cuisine[f] = c

            if c not in self.cuisine_heap:
                self.cuisine_heap[c] = []

            heapq.heappush(self.cuisine_heap[c], (-r, f))

    def changeRating(self, food: str, newRating: int) -> None:
        c = self.food_to_cuisine[food]
        self.food_to_rating[food] = newRating
        heapq.heappush(self.cuisine_heap[c], (-newRating, food))

    def highestRated(self, cuisine: str) -> str:
        heap = self.cuisine_heap[cuisine]

        while True:
            rating, food = heap[0]
            if -rating == self.food_to_rating[food]:
                return food
            heapq.heappop(heap)
        


# Your FoodRatings object will be instantiated and called as such:
# obj = FoodRatings(foods, cuisines, ratings)
# obj.changeRating(food,newRating)
# param_2 = obj.highestRated(cuisine)