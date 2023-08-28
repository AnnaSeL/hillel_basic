"""Creation of coffe shop with possibility to order coffee, tea and additional drinks, create latte"""
import csv

class Product:
    def __init__(self, name: str, product_type: str, price: float):
        self.name = name
        self.product_type = product_type
        self.price = price

    def __repr__(self):
        return f'{self.product_type.capitalize()}: {self.name}, Ціна: {self.price.__round__()} грн.'


class Store:
    def __init__(self):
        self.products = []

    """Import list of products from given file"""
    def import_productlist(self, filename='inventory.csv'):
        with open(filename, "r", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            for row in reader:
                name = row["Назва"]
                product_type = row["Тип"]
                price = row["Ціна"]
                amount = int(row["Кількість"]) if row["Кількість"] else 5
                price = float(price)
                try:
                    if product_type in ['coffee', 'tea', 'additional']:
                        product = Product(name, product_type, price)
                        self.products.append((product, amount))
                except ValueError as e:
                    print(f"Помилка: {e}")

    """Print list of products of chosen type"""
    def print_products_by_type(self, prod_type: str):
        return [(product, amount) for product, amount in self.products if product.product_type == prod_type]

    """Print total value of all products"""
    def print_total_value(self):
        return sum(product.price * available_amount for product, available_amount in self.products)

    """Sell chosen product"""
    def sell_product(self, name):
        for i, (product, available_amount) in enumerate(self.products):
            if product.name == name and available_amount > 0:
                self.products[i] = (product, available_amount - 1)
                print(f"Продано: {product}")
                return
        return print(f"На жаль, продукту немає.")

    """Create latte from espresso and milk"""
    def create_latte(self):
        espresso = None
        milk = None
        espresso_price = 0
        milk_price = 0
        for i, (product, available_amount) in enumerate(self.products):
            if product.name == "Еспресо" and available_amount > 0:
                espresso = product
                espresso_price = product.price
                self.products[i] = (product, available_amount - 1)
            elif product.name == "Молоко" and available_amount > 0:
                milk = product
                milk_price = product.price
                self.products[i] = (product, available_amount - 1)
        if espresso and milk:
            latte_price = espresso_price + milk_price
            latte = Product("Лате", "coffee", latte_price)
            self.products.append(latte)
            print(f"Створено: {latte}")
            return latte
        else:
            print("Не вистачає продуктів для приготування лате.")
            return None


# usage example
if __name__ == "__main__":
    store1 = Store()
    store1.import_productlist()
    print(store1.print_products_by_type('coffee'))
    print(store1.print_total_value())
    store1.sell_product("Earl Grey")
    print(store1.print_total_value())
    latte = store1.create_latte()
