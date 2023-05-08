class Item:
    def __init__(self, weight: float, value: float) -> None:
        self.weight = weight
        self.value = value
        self.ratio = value // weight

    def __repr__(self) -> str:
        return f"Item({self.weight},{self.value})"


class Knapsack:
    @staticmethod
    def max_value(item_list: list[Item], max_weight: float) -> float:
        knapsack = []
        item_list.sort(key=lambda x: x.ratio, reverse=True)
        for item in item_list:
            if max_weight == 0:
                return sum(knapsack)
            elif item.weight <= max_weight:
                knapsack.append(item.value)
                max_weight -= item.weight
            elif item.weight > max_weight:
                knapsack.append(max_weight / item.weight * item.value)
                max_weight = 0
        return sum(knapsack)
