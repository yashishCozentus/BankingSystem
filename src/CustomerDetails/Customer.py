class Customer:
    def __init__(self, customer_id, name, address, phone_number):
        self.customer_id = customer_id
        self.name = name
        self.address = address
        self.phone_number = phone_number

    def get_customer_info(self):
        return f"Customer ID: {self.customer_id}\n Name: {self.name}\n Address: {self.address}\n Phone Number: {self.phone_number}"


if __name__ == '__main__':
    obj = Customer('123CD','Yashish','BBSR','1234567890')
    res = obj.get_customer_info()
    print(res)