import math
import sys

def calcEOQ(d, c, k, h):
  q = math.sqrt((2*d*k)/h)
  tac = ((q/2)*h)+((d*k)/q)+(d*c)
  t = (q/d)*52
  eoq = (q, tac, t)
  return eoq

#def validateDate()

def newBrand(x):
  #data validation (positive + integer)
  
  d = float(input("How many pounds of coffee per year do you need to stock (D)?\n"))
  while d <= 0:
    d = float(input("Negative values are not accepted. Please provide a positive value:\n"))

  c = float(input("What is your unit cost (C)?\n"))
  while c <= 0:
    c = float(input("Negative values are not accepted. Please provide a positive value:\n"))

  k = float(input("What is your order cost (K)?\n"))
  while k <= 0:
    k = float(input("Negative values are not accepted. Please provide a positive value:\n"))

  h = float(input("What is your holding cost (h)?\n"))
  while h <= 0:
    h = float(input("Negative values are not accepted. Please provide a positive value:\n"))

  brand = [x, d, c, k, h]
  eoq = calcEOQ(d, c, k, h)
  for i in eoq:
    brand.append(i)
  return brand

def main():
  x = str(input("Welcome to the EOQ Calculator prepared by Jack Hotaling\nEnter q to quit and display the results or the name of the coffee to continue\n"))
  totalQ = 0

  #store brands:
  brandList = []

  while x != 'q':
    newB = newBrand(x)
    brandList.append(newB)
    totalQ += newB[5]
    x = str(input("Enter q to quit and display the results or the name of the coffee\n"))
  else:
    print('**********\n\nThe Results of EOQ Calculation\n\n**********\nBrand\t\tQuantity(lbs)\tTotal Cost($)\tCycle Length (in weeks)')
    for B in brandList:
      print("{0}\t\t{1:.2f}\t\t\t{2:.2f}\t\t\t{3:.2f}".format((B[0]),(B[5]),(B[6]),(B[7])))

    print("\nIf you purchase all of the coffee, you will need space to hold {0} lbs. of cofffee.".format(totalQ))
    if input(): sys.exit()

main()

if __name__ == "__main()__":
  main()