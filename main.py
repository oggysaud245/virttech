from cart import Cart
from placeorder import PlaceOrder
from products import Products
from user import User

tshirt = Products("Tshirt", 500)  # Tshirt as a product
tshirt.description = "Tshirt description"  # Tshirt description

shoe = Products("Shoe", 1500)  # Shoe as a product
shoe.description = "Shoe description"  # Shoe description

sweater = Products("Sweater", 800)  # sweater as a product
sweater.description = "Sweater description"  # sweater description

cap = Products("Cap", 200)      # Cap as a product
cap.description = "Cap description"  # Cap description


adminUser = User("Ramesh Saud", "541235411")  # adminUser as an admin and details
adminUser.address = "Kathmandu"
adminUser.isAdmin = True

customer1 = User("Hari Prasad", "12346789")  # customer 1 and details
customer1.address = "Lalitpur"
customer1.shippingAddress = "Baneshwor, Kathmandu"
customer1.email = "haripd@gmail.com"

item1 = PlaceOrder(tshirt, 2)
item2 = PlaceOrder(shoe, 3)
item3 = PlaceOrder(sweater, 1)

customer1Cart = Cart(customer1)

customer1Cart.addProduct(item1)
customer1Cart.addProduct(item2)
customer1Cart.calDiscount()
print(customer1Cart.invoice)

print(f"\n\n**Making Premium User\n")
adminUser.makePremium(customer1)
customer1Cart.addProduct(item3)
customer1Cart.addProduct(PlaceOrder(cap, 1))
customer1Cart.calDiscount()
print(customer1Cart.invoice)
