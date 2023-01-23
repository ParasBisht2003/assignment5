import random
for i in range(1,11):
    num1=random.randint(0,100)
    num2=random.randint(0,100)
    correctresult=num1*num2
    result=input(f"Question {i} {num1}X{num2}=")
    if(result==correctresult):
        print("Correct answer")
    else:
        print(f"Wrong!The answer is {correctresult}")
