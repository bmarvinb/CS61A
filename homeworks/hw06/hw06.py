
passphrase = '*** PASSPHRASE HERE ***'

def survey(p):
    """
    You do not need to understand this code.
    >>> survey(passphrase)
    '3d2eea56786a3d9e503a4c07dd667867ef3d92bfccd68b2aa0900ead'
    """
    import hashlib
    return hashlib.sha224(p.encode('utf-8')).hexdigest()


# Object Oriented Programming

class Fib(object):
    """A Fibonacci number.

    >>> start = Fib()
    >>> start
    Fib object, value 0
    >>> start.next()
    Fib object, value 1
    >>> start.next().next()
    Fib object, value 1
    >>> start.next().next().next()
    Fib object, value 2
    >>> start.next().next().next().next()
    Fib object, value 3
    >>> start.next().next().next().next().next()
    Fib object, value 5
    >>> start.next().next().next().next().next().next()
    Fib object, value 8
    >>> start.next().next().next().next().next().next() # Ensure start isn't changed
    Fib object, value 8
    """
    def __init__(self, value=0):
        self.value = value
        self.next_value = 1

    def next(self):
        b = Fib()
        b.value = self.next_value
        b.next_value = b.value + self.value
        return b

    def __repr__(self):
        return "Fib object, value " + str(self.value)

class VendingMachine:
    """A vending machine that vends some product for some price.

    >>> v = VendingMachine('candy', 10)
    >>> v.vend()
    'Machine is out of stock.'
    >>> v.deposit(15)
    'Machine is out of stock. Here is your $15.'
    >>> v.restock(2)
    'Current candy stock: 2'
    >>> v.vend()
    'You must deposit $10 more.'
    >>> v.deposit(7)
    'Current balance: $7'
    >>> v.vend()
    'You must deposit $3 more.'
    >>> v.deposit(5)
    'Current balance: $12'
    >>> v.vend()
    'Here is your candy and $2 change.'
    >>> v.deposit(10)
    'Current balance: $10'
    >>> v.vend()
    'Here is your candy.'
    >>> v.deposit(15)
    'Machine is out of stock. Here is your $15.'

    >>> w = VendingMachine('soda', 2)
    >>> w.restock(3)
    'Current soda stock: 3'
    >>> w.restock(3)
    'Current soda stock: 6'
    >>> w.deposit(2)
    'Current balance: $2'
    >>> w.vend()
    'Here is your soda.'
    """
    def __init__(self, item, cost):
        self.item = item
        self.cost = cost
        self.stock = 0
        self.amount_deposited = 0

    def restock(self, amount):
        self.stock += amount
        return 'Current {} stock: {}'.format(self.item, self.stock)

    def deposit(self, amount):
        if self.stock == 0:
            return 'Machine is out of stock. Here is your ${}.'.format(amount)
        self.amount_deposited += amount
        return 'Current balance: ${}'.format(self.amount_deposited)

    def vend(self):
        if self.stock == 0:
            return 'Machine is out of stock.'
        elif self.amount_deposited < self.cost:
            return 'You must deposit ${} more.'.format(self.cost - self.amount_deposited)
        elif self.amount_deposited > self.cost:
            balance = self.amount_deposited - self.cost
            self.amount_deposited = 0
            self.stock -= 1
            return 'Here is your {} and ${} change.'.format(self.item, balance)
        else:
            self.amount_deposited = 0
            self.stock -= 1
            return 'Here is your {}.'.format(self.item)

