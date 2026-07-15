from client import PgDogDbBalancerClient
client = PgDogDbBalancerClient()
print(client.get_route("SELECT * FROM products;"))