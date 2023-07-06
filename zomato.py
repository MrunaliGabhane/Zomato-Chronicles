class ZomatoChronicles:
    def __init__(self):
        self.menu_mastery = []
        self.orders = []

    def display_menu(self):
        if not self.menu_mastery:
            print("No dishes available in the Zomato menu.")
        else:
            print("Zomato Menu:")
            print("ID  |  Name  |  Price  | Stock | Availability")
            for dish in self.menu_mastery:
                print(f"{dish['id']:3} | {dish['name']:6} | {dish['price']:7.2f} | {dish['stock']}     | {dish['availability']}")

    def add_dish(self):
        dish = {}
        dish["id"] = int(input("Enter the Dish ID: "))
        dish["name"] = input("Enter the Dish name: ")
        dish["price"] = float(input("Enter the Dish price: "))
        dish["stock"] = int(input("Enter the Dish stock: "))
        dish['availability'] = 'no' if dish["stock"] <= 0 else 'yes'
        self.menu_mastery.append(dish)
        print("Dish added successfully.")

    def remove_dish(self):
        dish_id = int(input("Enter the dish ID to remove: "))
        for dish in self.menu_mastery:
            if dish["id"] == dish_id:
                self.menu_mastery.remove(dish)
                print("Dish removed successfully.")
                return
        print("Dish not found.")

    def update_dish_stock(self):
        dish_id = int(input("Enter the dish ID to update: "))
        for dish in self.menu_mastery:
            if dish["id"] == dish_id:
                dish["stock"] = int(input("Enter the updated stock: "))
                dish["availability"] = "no" if dish["stock"] <= 0 else "yes"
                print("Dish stock updated successfully.")
                return
        print("Dish not found.")

    def take_new_order(self):
        customer_name = input("Enter customer name: ")
        dish_ids = input("Enter dish IDs (separated by commas): ").split(",")
        dish_ids = [int(dish_id.strip()) for dish_id in dish_ids]

        for dish_id in dish_ids:
            dish_available = False
            for dish in self.menu_mastery:
                if dish["id"] == dish_id and dish["availability"] == "yes" and dish["stock"] > 0:
                    dish_available = True
                    dish["stock"] -= 1
                    dish["availability"] = "no" if dish["stock"] <= 0 else "yes"
                    break

            if not dish_available:
                print(f"Dish with ID {dish_id} is not available.")
                return

        order_id = len(self.orders) + 1
        order_bill = sum([dish["price"] for dish in self.menu_mastery if dish["id"] in dish_ids])

        order = {
            "order_id": order_id,
            "customer_name": customer_name,
            "dish_ids": dish_ids,
            "status": "received",
            "order_bill": order_bill
        }

        self.orders.append(order)
        print(f"Order placed successfully. Order ID is {order_id}.")

    def update_order_status(self):
        order_id = int(input("Enter the order ID to update status: "))
        status = input("Enter the new status: ")

        for order in self.orders:
            if order["order_id"] == order_id:
                order["status"] = status
                print("Order status updated.")
                return

        print("Order not found.")

    def review_orders(self):
        for order in self.orders:
            print(f"Order ID: {order['order_id']}")
            print(f"Customer Name: {order['customer_name']}")
            print(f"Dish IDs: {order['dish_ids']}")
            print(f"Status: {order['status']}")
            print(f"Order Bill: {order['order_bill']}")
            print("-------------------------")

    def run(self):
        while True:
            print("\n===== Zomato Chronicles: The Great Food Fiasco =====")
            print("1. Display Menu")
            print("2. Add Dish to Menu")
            print("3. Remove Dish from Menu")
            print("4. Update Dish stock")
            print("5. Take New Order")
            print("6. Update Order Status")
            print("7. Review Orders")
            print("8. Exit")
            choice = input("Enter your choice (1-8): ")

            if choice == '1':
                self.display_menu()
            elif choice == '2':
                self.add_dish()
            elif choice == '3':
                self.remove_dish()
            elif choice == '4':
                self.update_dish_stock()
            elif choice == '5':
                self.take_new_order()
            elif choice == '6':
                self.update_order_status()
            elif choice == '7':
                self.review_orders()
            elif choice == '8':
                print("Thank you for using Zomato Chronicles. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")


if __name__ == '__main__':
    zomato = ZomatoChronicles()
    zomato.run()
