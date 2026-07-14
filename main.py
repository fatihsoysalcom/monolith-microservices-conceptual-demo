# main.py

# --- Monolithic Application Concept ---
# A single application handles all business domains (e.g., users, products, orders).
# All logic and data management are tightly coupled within one codebase.
class MonolithicApplication:
    def __init__(self):
        print("Initializing Monolithic Application...")
        self.users = {}
        self.products = {}
        self.orders = {}

    def create_user(self, user_id, name):
        # Monolith handles user logic directly
        print(f"[Monolith] Creating user: {name} ({user_id})")
        self.users[user_id] = {"name": name, "status": "active"}
        return self.users[user_id]

    def add_product(self, product_id, name, price):
        # Monolith handles product creation directly
        print(f"[Monolith] Adding product: {name} ({product_id}) at ${price}")
        self.products[product_id] = {"name": name, "price": price, "stock": 100}
        return self.products[product_id]

    def place_order(self, user_id, product_id, quantity):
        # Monolith handles order logic, accessing user and product data directly within the same app
        print(f"[Monolith] Placing order for user {user_id}, product {product_id}, qty {quantity}")
        if user_id not in self.users:
            return {"error": "User not found"}
        if product_id not in self.products:
            return {"error": "Product not found"}

        order_id = f"ORD-{len(self.orders) + 1}"
        self.orders[order_id] = {"user_id": user_id, "product_id": product_id, "quantity": quantity, "status": "pending"}
        return self.orders[order_id]

# --- Microservices Architecture Concept ---
# Each "service" is conceptually independent, focusing on a single business capability.
# In a real microservices setup, these would be separate deployable units,
# communicating over a network (e.g., HTTP, message queues). Here, they are separate
# classes within the same file to demonstrate conceptual separation and independent responsibility.

class UserService:
    def __init__(self):
        print("  [UserService] Initializing...")
        self.users = {} # Each service has its own data store (conceptually)

    def create_user(self, user_id, name):
        print(f"  [UserService] Creating user: {name} ({user_id})")
        self.users[user_id] = {"name": name, "status": "active"}
        return self.users[user_id]

class ProductService:
    def __init__(self):
        print("  [ProductService] Initializing...")
        self.products = {} # Each service has its own data store (conceptually)

    def add_product(self, product_id, name, price):
        print(f"  [ProductService] Adding product: {name} ({product_id}) at ${price}")
        self.products[product_id] = {"name": name, "price": price, "stock": 100}
        return self.products[product_id]

class OrderService:
    def __init__(self):
        print("  [OrderService] Initializing...")
        self.orders = {} # Each service has its own data store (conceptually)

    def place_order(self, user_id, product_id, quantity):
        # In a real microservices setup, this service would call UserService and ProductService
        # via network requests to validate user/product existence and get details.
        # For this conceptual demo, we'll simulate success if IDs are provided.
        print(f"  [OrderService] Placing order for user {user_id}, product {product_id}, qty {quantity}")
        
        order_id = f"MS-ORD-{len(self.orders) + 1}"
        self.orders[order_id] = {"user_id": user_id, "product_id": product_id, "quantity": quantity, "status": "pending"}
        return self.orders[order_id]

# --- Demonstration ---
if __name__ == "__main__":
    print("\n--- Demonstrating Monolithic Application ---")
    mono_app = MonolithicApplication()
    mono_app.add_product("P101", "Laptop", 1200)
    mono_app.create_user("U001", "Alice")
    mono_app.place_order("U001", "P101", 1)
    print("-" * 40)

    print("\n--- Demonstrating Microservices Architecture (Conceptual) ---")
    user_service = UserService()
    product_service = ProductService()
    order_service = OrderService()

    user_service.create_user("U002", "Bob")
    product_service.add_product("P102", "Mouse", 25)
    # Order service conceptually interacts with other services for data, but in this single-file demo,
    # we simulate the call without actual network communication.
    order_service.place_order("U002", "P102", 2)
    print("-" * 40)

    print("\nKey takeaway: Microservices break down a large application into smaller, independent, and focused services.")
    print("Each service manages its own domain and can be developed, deployed, and scaled independently.")
    print("This example simulates this conceptual separation within a single file.")
