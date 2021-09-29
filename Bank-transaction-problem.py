totalAmount = 0

while True:

    

   str =input ("Enter transaction type and transaction amount in formate D 2000 or W 100: ")

   typeAndAmo = str.split(" ")

   type = typeAndAmo [0]

   amount = int (typeAndAmo [1])

   if type=="D" or type=="d":

      totalAmount += amount

   elif type=="W" or type=="w":

      if amount>totalAmount:

          print ("amount not sufficient in bank")

      else:

          totalAmount -= amount

   else:

      pass

    

   str1 =input ("You want to continue (Y for yes) : ")

   if not (str1 =="Y" or str1 =="y") : 

      break

print("Total amount after withdraw and deposit: ", totalAmount)
