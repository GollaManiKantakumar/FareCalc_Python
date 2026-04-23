class User:
    def __init__(self, acc_no, name, password):
        self.acc_no = acc_no
        self.name = name
        self.password = password
        self.transactions = []