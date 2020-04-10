import json # To read and write lists to a file
import math
import sys

mainmenu = "\nMain Menu\nA)dd calculations to an existing file\nL)oad a file and view results\nP)rint current results\nR)eset and perform new EOQ calculations\nS)ave current calculations to a file\nQ)uit:\n"
question = "\nEnter q to quit and display the results, or enter the name of a coffee\n"
nofile = "\nThe file doesn't exists\n"
nocalc = "\nThere are no calculations to display\nLoad a file or perform new calculations\n"

def validate(vString):
    """ This function validates the inputs to be non-negative numeric values"""
    while True: 
        try: 
            if int(float(vString)) >= 0:
                vString = int(float(vString))
                break
            else: 
                vString = input("Negative values are not accepted. Please provide a positive value:\n")
        except ValueError:
            vString = input("Non-numeric values are not accepted. Please provide a numeric value:\n")
    return vString

def getParam():
    
    d = float(validate(input("How many pounds of coffee per year do you need to stock (D)?\n")))
    c = float(validate(input("What is your unit cost (C)?\n")))
    k = float(validate(input("What is your order cost (K)?\n")))
    h = float(validate(input("What is your holding cost (h)?\n")))
    return d, c, k, h
        
def printResults(dataList):

    """ This function displays the results for each data in the dataList, it displays all four variables"""     

    print('**********\n\nThe Results of EOQ Calculation\n\n**********\nBrand\t\tQuantity(lbs)\tTotal Cost($)\tCycle Length (in weeks)')
    for B in dataList:
      print("{0}\t\t{1:.2f}\t\t\t{2:.2f}\t\t\t{3:.2f}".format((B[0]),(B[5]),(B[6]),(B[7])))
      totalQ += B[5]
    print("\nIf you purchase all of the coffee, you will need space to hold {0} lbs. of cofffee.".format(totalQ))
    print("\n")
    #total_b = total_c = total_d = 0
    
    #print("*********\n\nThe Results of Totals\n\n*********")
    #print("{0:15}{1:20}{2:20}{3:20}".format("A", "B", "C", "D"))
    
    #for row in dataList:
        #print("{0:15}{1:<20.2f}{2:<20.2f}{3:<20.2f}".format(row[0], row[1], row[2], row[3]))    
        #total_b += row[1]
        #total_c += row[2]
        #total_d += row[3]
        
    #print("*********\n\n")        
    #print("""The total B is \u03A3(B) = ${0:.2f}.  
#The total C is \u03A3(C) = ${1:.2f}. 
#The total D is \u03A3(D) = ${2:.2f}.""".format(total_b, total_c, total_d))

def calcEOQ(d, c, k, h):
    q = math.sqrt((2*d*k)/h)
    tac = ((q/2)*h)+((d*k)/q)+(d*c)
    t = (q/d)*52
    return q, tac, t
    
def askData(dataList):    
    print(question)
    coffeeName = input()
    while (coffeeName.lower() !="q"):
        d, c, k, h = getParam()                            # Call getParam and unpack the results to three variables (b, c, d). No calculations here to make itsimple. 
        q, tac, t = calcEOQ(d, c, k, h)
        dataList.append([coffeeName, d, c, k, h, q, tac, t])                   # Add a new data point (a, b, c, d) to data list
        print(question)
        coffeeName = input()        
    printResults(dataList)    
      
def load_data(filename='dataListJSON'):#remove defaults!?
    """ Load the elements stored in the text file named filename. """
    # Open file to read
    dataList = []
    with open (filename, 'r') as fp:
        dataList = json.load(fp)    
    return dataList
        

def store_data(dataList, filename='dataListJSON'):#remove defaults!?
    """ Allows the user to store data in a list to the text file named filename. """
    with open(filename, 'w') as fp:
        json.dump(dataList, fp)
                
def main():
    print("Welcome to the EOQ Calculator prepared by Jack Hotaling\n\n")
    done = False
    while not done:
        cmd = input(mainmenu)
        if cmd.lower() == 'r':
            dataList = []
            askData(dataList)
        elif cmd.lower() == 'a':
            try:
                askData(dataList)
            except UnboundLocalError: 
                print(nocalc)
        elif cmd.lower() == 's':
            try:
                filename= input('Enter file name: ')
                if filename: store_data(dataList, filename)
                else: print("Please enter a file name") # LOOP?!
                #store_data(dataList)               
            except UnboundLocalError: 
                print(nocalc)
                input("Hit enter to go to the main menu")
            except: pass
        elif cmd.lower() == 'p':
            try:
                printResults(dataList)
            except UnboundLocalError: 
                print(nocalc)
                input("Hit enter to go to the main menu")
            except: pass
        elif cmd.lower() == 'l':
            while True:  
                try:
                    filename = input('Enter a file name: ')
                    if filename: dataList = load_data(filename)
                    else: #dataList = load_data()
                        print('Please provide a valid file name\n') # necessary??
                    if dataList: 
                        printResults(dataList)
                        break
                except FileNotFoundError:
                    print("Please provide a valid filename\n")    
        elif cmd.lower() == 'q':
            done = True

if __name__ == '__main__':
    main()