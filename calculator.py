def add(a,b):
    sum=a+b;
    return sum;
def sub(a,b):
    sum=a-b;
    return sum;
def mul(a,b):
    sum=a*b;
    return sum;
def div(a,b):
    sum=a/b;
    return sum;
a=int(input("Enter A value "))
b=int(input("Enter B value "))
print("The sum is ",add(a,b))
print("The sub is ",sub(a,b))
print("The mul is ",mul(a,b))
print("The div is ",div(a,b))