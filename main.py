import string
import random
if __name__=="__main__":
    s1=string.ascii_lowercase
    # print(s1)
    s2=string.ascii_uppercase
    # print(s2)
    s3=string.digits
    # print(s3)
    s4=string.digits
    # print(s4)
    s5=string.punctuation
    # print(s5)
    
    plen=int(input("Enter Password Length\n"))
    s=[]#created an empty list and then extended
    s.extend(list(s1))
    s.extend(list(s2))
    s.extend(list(s3))
    s.extend(list(s4))
    # print(s)
    # random.shuffle(s)#shuffle the list
    # print(s)
    print("your password is:-")   
    print("".join(random.sample(s,plen)))
    # print("".join(s[0:plen]))#concatination












