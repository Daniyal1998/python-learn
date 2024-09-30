import typing

from strategy_protocol import ItemProcessing, FILOStrategy


class BlackHoleStrategy:
    def order_items(self, items: typing.Sequence[typing.Any]) -> typing.List:
        return []


def main():
    # create the application
    app = ItemProcessing()

    # create a few items
    app.add_item("Air Pods")
    app.add_item("Paint Brush")
    app.add_item("Gloves")

    # process items
    app.process_items(BlackHoleStrategy())  # type: ignore
    app.process_items(FILOStrategy())


if __name__ == "__main__":
    main()
