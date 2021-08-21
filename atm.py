#defining class
class atm(object):
    def __init__(self,name, pinNo, atmCardNo, bal):
      self.name = name
      self.pinNo = pinNo
      self.atmCardNo = atmCardNo
      self.bal = bal

    #fetch the bal
    def balenq(self):
       print("Your balance is:", self.bal)

    #withdraw
    def cashWithdrawal(self):
       valWith = int(input("Enter value to withdraw: "))

       #making sure the value withdrawn is lesser than balance  
       if valWith>self.bal:
         print("U can't with an amount more than ur bal dumbo!")
       else:
           #updating bal and withdrawing money
           newVal=self.bal-valWith
           print("Suxesfooli withdrew $",valWith,", current bal is $",newVal)
       
       self.bal = newVal 

#just timepass
name = input("Enter name: ")
pinNo = input("Enter pin no: ")
cardNo = input("Enter card no: ")

#defining user1
user1 = atm(name, pinNo, cardNo, 200000)
#getting his bal
print(user1.balenq())

#taking input to with
que=input("wanna withdraw some money? y/n: ")

#condition to with
if que=='y':
  user1.cashWithdrawal() 
  user1.balenq()
else:
  print("ok then, cu soon, gubei")  
