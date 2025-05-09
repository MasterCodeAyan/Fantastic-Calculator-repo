from math import sqrt

def start_normal_Cal():
    print("Welcome to the fantastic calculator!")
    print("If you want to do advance calculations press 'a' and for normal press 'n'").lower()
    Cal = (input(""))

    if (Cal == "a"):
        adv_cal()

    elif (Cal == "n"):
         N1 = (int(input("Number1: ")))
         N2 = (int(input("Number2: ")))
         O = (input("Enter any Operator: "))
         ncr = 0

         if (O == "+"):

             ncr = N1+N2
             print(f"The sum of number 1 and 2 is {ncr}")
         
         elif (O == "-"):
          ncr = N1-N2
          print(f"The difference of number 1 and 2 is {ncr}")

         elif (O == "*"):
          ncr = N1*N2
          print(f"The product of number 1 and 2 is {ncr}")

         elif (O == "/"):
          ncr = N1/N2
          print(f"The division of number 1 and 2 is {ncr}")


    




    
    
         


def adv_cal():
    print("Welcome to the advance operations!\nHere you can get sqaure,cube and sqaure_root")
    number = int(input("Enter the number: "))
    ad_O = (input("Enter 's' for square 'c' for cube and 'sr' for square_root: "))
    adcr = 0

    if (ad_O == "s"):
        adcr = number*number
        print(f"The square of the number is {adcr}")
        
    if (ad_O == "c"):
        adcr = number*number*number
        print(f"The cube of the number is {adcr}")
        
    if (ad_O == "sr"):
        adcr = sqrt(number)
        print(f"The square_root of the number is {adcr}")
    
    
  





def dir_add_cal(A,B):
   result = A+B
   return result

def dir_sub_cal(A,B):
    reuslt = A-B
    return reuslt

def dir_mul_cal(A,B):
    reuslt = A*B
    return reuslt
 
def dir_div_cal(A,B):
    reuslt = A/B
    return reuslt

def dir_square_cal(A):
    reuslt = A*A
    return reuslt

def dir_cube_cal(A):
    reuslt = A*A*A
    return reuslt
    
def dir_square_root_cal(A):
    reuslt = sqrt(A)
    return reuslt









         


        



