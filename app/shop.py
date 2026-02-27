from dataclasses import dataclass
from typing import Dict
from datetime import datetime
from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from app.customer import Customer


@dataclass
class Shop:
    name: str
    location: tuple[int, int]
    products: Dict[str, int | float]

    def print_recipe(self, customer: "Customer") -> None:
        cost = 0
        print(f"Date: {datetime.now().strftime('%m/%d/%Y %H:%M:%S')}")
        print(f"Thanks, {customer.name}, for your purchase!")
        print("You have bought:")
        for product, quantity in self.products.items():
            if product in self.products:
                product_cost = self.products[product] * quantity
                cost += product_cost
                print(f"{quantity} {product}s for {product_cost:.2f} dollars")

        print(f"Total cost is {cost:.2f} dollars")
        print("See you again!\n")
