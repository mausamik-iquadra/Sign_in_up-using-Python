#code by Mausami 

#Test cases for account creation

#TEST CASES
## if account already exists -- no entry added 
## login if account exists
## if account doesn't exist -- signup (before sign up check for all validation cases )
## if account doesn't exist -- but username doesn't follow test cases -- account cannot be created -- try creating again 


#Username test cases 
## Lower ## Upper ## len > 6 ## Digits 


import mysql.connector as sql
from mysql.connector import Error
from mysql.connector import errorcode
import re

try:
#connect to mysql using the connect() with following parameters(own mysql credentials ) 
    connection = sql.connect(host='localhost',database='testpython',user='root', password='1234')
    print("Connection established")

# error handling  
except sql.Error as e :
    if e.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Username / Password Incorrect ")
    elif e.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database does not exist ")
    else :
        print(e)

curs = connection.cursor()

#function for signup 

def signup(u,p):
    curs.execute('Select * from users where name = %s  and password = %s ', (u,p))
    acc = curs.fetchone()
    
    # if account already exits 
    if acc:
        print('Account exists already')
    
    else :
    # if account doesn't exist --> create account 
        query = ("insert into users(name  , password) values('{}','{}')".format(u,p))
        curs.execute(query)
        connection.commit()
        print(" Created your account succesfully !")


# function for signin / login 

def signin(u,p):
    curs.execute('Select * from users where name =%s and  password = %s ', (u,p))
    account  = curs.fetchone()
    #check if account exists 
    if not account:
        print("Account doesn't exist , create one !")
    else:
        print("Logged in successfully ! ")

# to validate username 
class Authenticate(object):
    def __init__(self, username = ''):
        self.username = username

    def __lower(self):
        lower = any(c.islower() for c in self.username)
        return lower

    def __upper(self):
        upper = any(c.isupper() for c in self.username)
        return upper

    def __digit(self):
        digit = any(c.isdigit() for c in  self.username)
        return digit

    def validate(self):
        lower = self.__lower()
        upper = self.__upper()
        digit = self.__digit()

        length = len(self.username)

        report =  lower and upper and digit and length >= 6

        if report:
            print("Username passed all checks ")
            return True

        elif not lower:
            print("You didnt use Lower case letter")
            return False

        elif not upper:
            print("You didnt use Upper case letter")
            return False

        elif length <6:
            print("Username should Atleast have 6 character")
            return False

        elif not digit:
            print("You didnt use Digit")
            return False
        else:
            pass


# Driver code 
print("Enter Username : ")
user_name = input()
print("Enter Password : ")
pas = input() 

v = Authenticate(user_name)


print("Do you already have account ? (Y/ N) ")
print("Account Yes ? Press 1 : ")
print("Don't have account ? Press 2 :  ")
inp = input(">")
if inp == '1':
    
    signin(user_name,  pas)
else :
    
    if(v.validate() == True):
        signup(user_name , pas)




