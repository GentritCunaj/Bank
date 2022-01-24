import random
import mysql.connector as mysql





class Bank:
    def __init__(self,balance=20000,name=""):
        self.balance = balance
        self.name = str(input("Whats your name?"))

    def display(self):
        print("\n Your Balance is=",self.balance)

    def deposit(self):
        amount = float(input("How much would you want to deposit"))
        self.balance += amount
        print("\n Amount Deposited",amount)

    def withdraw(self):
        amount = float(input("How much would you want to withdraw"))
        if self.balance >= amount:
            self.balance -= amount
            print("\n Amount Withdrawin",amount)
        else:
            print("\n Insufficient funds")

    def loan_allowances(self):
        global pay,amount
        pay = 0
        while True:
            try:
                pay = float(input("How much do you make a year"))
                if pay == float or int:
                    break
            except Exception as e:
                print(e)
        range = 0
        if pay <= 50000:
            range = 50000
        if 50001 <= pay <= 80000 :
            range = 80000
        if 80001 <= pay:
            range = 100000

        while True:
            try:
                amount = float(input("How much would you like to loan"))
                if amount < range:
                    self.balance+= amount
                    break
                print("This value over exceeds our allowance")
            except Exception as e:
                print(e)

    def monthly_function(self):
        global pay,amount
        hm_months = int(input("How many months you want to check for"))
        for i in range(hm_months):
            self.balance += (pay // 12) + (random.randrange(3000, 4000) - 105 / 100 * amount // 12)
        return self.balance


s = Bank()
s.display()
s.loan_allowances()
s.monthly_function()
s.display()



db = mysql.connect(
    host="localhost",
    user = "root",
    passwd="1234",
    database="bank1"
)

cursor = db.cursor()
# cursor.execute("CREATE TABLE ClientBank (name VARCHAR(50), balance int)")
sql = "INSERT INTO ClientBank (name,balance) VALUES (%s,%s)"
val = (s.name,s.balance)
cursor.execute(sql,val)
db.commit()

cursor.execute("SELECT * FROM ClientBank")

for database in cursor:
    print(database)