from ast import arg
from cgitb import reset
from unittest import result
import math

def func1():
    print("I am a function");

def func2(arg1, arg2):
    print(arg1, " ", arg2);

def cube(x):
    return x*x*x;

def power(num, x=1):
    result = 1;
    for i in range(x):
        result = result*num;
    return result;

def sum(a,b):
    return a+b;

def multi_add(*args):
    result = 0;
    for x in args:
        result = result+x;
    return result;

def someFunction():
    global mystr;
    mystr = "def";
    print(mystr);

def ifstates():
    x, y = 10, 100;
    if x < y:
        result = "x is less than y";
    elif x > y:
        result = "x is more than y";
    else:
        result = "x is equal to y";
    
    value = "one";

    match value:
        case "one":
            result += " one";
        case "two":
            result += " two";
        case "three" | "four":
            result += " three and four";
        case _:
            result += " minus one";
    
    return [value, result];

def loops():
    x = 0;
    while(x < 5):
        print(x);
        x += 1;
    for x in range(5, 10):
        print(x);
    
    days = ["Mon","Tue","Wed","Thu","Fri","Sat","Sun"];
    for d in days:
        print(d);
    
    for x in range(5,10):
        if x == 7:
            break;
        if x % 2 == 0:
            continue;
        print(x);
    
    for i,d in enumerate(days):
        print(i, d);

def datatypes():
    myint = 5;
    mfloat = 13.2;
    mystr = "This is a string";
    mybool = True;
    mylist = [0, 1, "two", 3.2, False];
    mytuple = (0, 1, 2);
    mydict = {"one": 1, "two" : 2};

    myint = "abc";
    print(myint);
    print(mylist[2]);
    print(mytuple[1]);
    print(mylist[1:5]);
    print(mylist[1:5:2]);
    print(mylist[::-1]); # reverses the sequence
    print(mydict["one"]);

class Vehicle():
    def __init__(self, bodystyle) -> None:
        self.bodystyle = bodystyle

    def drive(self, speed):
        self.mode = "driving";
        self.speed = speed;

class Car(Vehicle):
    def __init__(self, enginetype, bodystyle="Car") -> None:
        super().__init__(bodystyle);
        self.enginetype = enginetype;
        self.wheels = 4;
        self.doors = 4;
    
    def drive(self, speed):
        super().drive(speed);
        print("Driving my ", self.enginetype, " car at ", self.speed);

class Motorcycle(Vehicle):
    def __init__(self, enginetype, hassidecar, bodystyle="Motorcycle") -> None:
        super().__init__(bodystyle);
        self.enginetype = enginetype;
        self.hassidecar = hassidecar;
        if (hassidecar):
            self.wheels = 3;
        else:
            self.wheels = 3;
        self.doors = 0;
    def drive(self, speed):
        super().drive(speed);
        print("Driving my ", self.enginetype, " Motorcycle at ", self.speed);

def classes():
    car1 = Car("Gas");
    car2 = Car("Electric");
    mc1 = Motorcycle("gas", True);
     
def modules():
    print(math.sqrt(16));
    print(math.pi);

def exceptions():
    try:
        x = 10 / 0;
    except:
        print("Well that didn't work");        

    try: 
        answer = input("What should I divide 10 by: ");
        num = int(answer);
        print(10/num);
    except ZeroDivisionError as e:
        print("You cannot divide by zero!");
    except ValueError as e:
        print("You didn't give me a valid number!\n",e);
    finally:
        print("This code always runs");

def is_palindrome(teststr):
    if teststr == teststr[::-1]:
        return True;
    return False;


def launch():
    run = True;
    while (run):
        teststr = input("Enter string to test for palindrome or 'exit':");
        if teststr == "exit":
            run = False;
            break;
        teststr = teststr.lower();

        newstr = "";
        for x in teststr:
            if x.isalnum():
                newstr += x;
        
        print("Palindrome test: ", is_palindrome(newstr));

def main():
    print("Hello World!");
    print(sum(20,40));
    datatypes();
    print(multi_add(4,5,10,4));

if __name__ == "__main__":
    main()
