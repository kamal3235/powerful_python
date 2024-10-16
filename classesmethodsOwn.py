class CustomerAccount:
    def __init__(self, customer_name):
        self.name = customer_name
        self.invoices = []   # logic?
    # account object created
    #   The add_invoice() method takes an instance of the Invoice class.
    def add_invoice(self, invoice):
        self.invoices.append(invoice)   # logic?

    def total_due(self):
        due = 0
        for invoice in self.invoices:
            due += invoice.amount_due()
        return due

    def unpaid_invoices(self):
        items = []
        for invoice in self.invoices:
            if not invoice.is_fully_paid():
                items.append(invoice)
        return items

    def apply_payment(self, amount):
        unpaid = self.unpaid_invoices()
        while amount > 0:
            invoice = unpaid.pop(0)
            partial = min(amount, invoice.amount_due())
            invoice.add_payment(partial)
            amount -= partial


class Invoice:
    def __init__(self, number: int, customer: str, amount: float):
        self.number = number
        self.customer = customer
        self.amount = amount
        self.total_payments = 0


    def add_payment(self, payment):
        self.total_payments += payment

    def is_fully_paid(self):
        return self.amount == self.total_payments

    def amount_due(self):
        return self.amount - self.total_payments


invoice = Invoice(12, "Mark Smith", 42.50)
print(invoice.number)              # 12
print(invoice.customer)            # "Mark Smith"
print(invoice.amount)              # 42.5
print(invoice.total_payments)      # 0
invoice.add_payment(20)
print(invoice.is_fully_paid())     # False
print(invoice.total_payments)      # 20
print(invoice.amount_due())        # 22.5
invoice.add_payment(22.50)
print(invoice.is_fully_paid())     # True
print(invoice.amount_due())        # 0.0

customer_name = "James Jones"
account = CustomerAccount(customer_name)
print(type(account).__name__)
print(account.name)
account.add_invoice(Invoice(1, customer_name, 20.0))
print(len(account.invoices))
print(account.total_due())
account.add_invoice(Invoice(2, customer_name, 25.0))
print(len(account.invoices))
print(account.total_due())
account.add_invoice(Invoice(3, customer_name, 30.0))
print(len(account.invoices))
print(account.total_due())     # 75.0
unpaid = account.unpaid_invoices()   # create an object
print(len(unpaid))
print(type(unpaid[0]).__name__)
print(unpaid[0].number)
print(unpaid[0].amount)

account.apply_payment(20)
now_unpaid = account.unpaid_invoices()
print(len(now_unpaid))
print(now_unpaid[0].number)
print(account.total_due())
account.apply_payment(10)
print(account.total_due())
print(len(account.unpaid_invoices()))
account.apply_payment(45)
print(len(account.unpaid_invoices()))
