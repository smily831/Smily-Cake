"""
create table Customers(
    id int primary key auto_increment,
    name varchar(256),
    phone varchar(10),
    quantity varchar(10),
    flavour varchar(256),
    price varchar(10),
    createdOn datetime DEFAULT CURRENT_TIMESTAMP
    type int DEFAULT 1
 );
"""


class customers:

    # Constructor
    def __init__(self, id=None, name=None, phone=None, quantity=None, flavour=None, price=None, created_on=None, type=1):
        self.id = id
        self.name = name
        self.phone = phone
        self.quantity = quantity
        self.flavour = flavour
        self.price = price
        self.created_on = created_on
        self.type = type

    def insert_sql(self):
        return "insert into customers (name, phone, quantity, flavour, price) values('{name}', '{phone}', '{quantity}', '{flavour}', '{price}');".format_map(vars(self))

    def update_sql(self):
        return""

    def delete_sql(self):
        return"delete from customers where id = {}".format(self.id)

    def select_sql(self):
        return""

c1 = customers()
print(vars(c1))
