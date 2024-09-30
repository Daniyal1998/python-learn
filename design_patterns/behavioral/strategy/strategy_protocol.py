import random
import typing


class OrderingStrategy(typing.Protocol):
    def order_items(self, items: typing.Sequence[typing.Any]) -> typing.List:  # type: ignore
        """returns an ordered list of items"""


class FIFOStrategy:
    """First in First out ordering of items"""

    def order_items(self, items: typing.Sequence[typing.Any]) -> typing.List:
        return [item for item in items]


class FILOStrategy:
    """First in Last out ordering of items"""

    def order_items(self, items: typing.Sequence[typing.Any]) -> typing.List:
        return list(reversed(items))


class RandomStrategy:
    """Random ordering of items"""

    def order_items(self, items: typing.Sequence[typing.Any]) -> typing.List:
        return random.sample(items, len(items))


class ItemProcessing:
    def __init__(self) -> None:
        self.items: list = []

    def add_item(self, item: typing.Any) -> None:
        self.items.append(item)

    def process_items(self, processing_strategy: OrderingStrategy):
        # create the ordered list
        item_list = processing_strategy.order_items(self.items)

        # if it's empty, don't do anything
        if not item_list:
            print("There are no items to process!!")
            return

        # go through the items in the list
        for item in item_list:
            print(item, end=" --> ")
        print("None")
