def table(a):
    for i in range(1,11):
        print(int(a) , " X " , int(i) , " = " , int(i)*int(a))

def root(p,q,c):

    
     if c == '+':
        print("Calculation is : ",p+q)
     elif c =='-':
        print("Calculation is : ",p-q)
     elif c == '*':
        print("Calculation is : ",p*q)
     elif c == '/':
        print("Calculation is : ",p/q)
     
    
     else:
        print("invaild")
    
        










n = int(input('Enter the Number: '))

x = int(input("Enter Number 1 : "))
y = int(input("Enter Number 2 : "))
z = input("Enter Operator : ")

try:

 table(n)

 root(x,y,z)

except ZeroDivisionError:
   print("There is an Error")
finally:
   print("Thank you ")


#Filehandling
#method 1  =>

print("File is opeing please wait\n")
print("Your file is \n")
'''
file1 = open('myfile.txt','r')


#statements

filedata = file1.read()

#readline only read one line where as readlines combine all lines into a list.


print(filedata)

file1.close()
'''
#method 2 =>


with open('myfile.txt','r+') as file1:
   #statement
   data=file1.write('Hello This is very secrete file\n Your name \t\t\t\t Mohan Singh \n Your Phone number \t\t\t\t +917703918776 \n')


with open('myfile.txt','r+') as file1:
   #statement
  datafile=file1.read()
  print(datafile)




