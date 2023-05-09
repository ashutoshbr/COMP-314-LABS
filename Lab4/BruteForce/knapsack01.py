from more_itertools import powerset


class Item:
    def __init__(self, weight: float, value: float) -> None:
        self.weight = weight
        self.value = value
        self.ratio = value // weight

    def __repr__(self) -> str:
        return f"Item({self.weight},{self.value})"


class Knapsack01:
    @staticmethod
    def max_value(item_list: list[Item], max_weight: float) -> float:
        item_list = list(powerset(item_list))  # All combinations
        res_list = item_list[:]  # Make a copy of list
        # Remove set when Knapsack weight exceeds
        for set in item_list:
            weight = 0
            for item in set:
                weight += item.weight
                if weight > max_weight:
                    res_list.remove(set)
                    break
        # Find the max value
        for set in res_list:
            value_list = []
            total_value = 0
            for item in set:
                total_value += item.value
            value_list.append(total_value)
        return max(value_list)
