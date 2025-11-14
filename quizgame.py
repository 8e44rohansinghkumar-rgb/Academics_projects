questions=( ("what is my name?")
           ,("what is your name?")
           ,("what is his name?")
           ,("name the most dangerous animal?")
           ,("name the tallest animal?"))
options=(("A. rohan","B. rahul","C. adarsh","D. srikar"),
         ("A. nishant","B. pulkit","C. sahil","D. piyush"),
         ("A. pranav","B. rayan","C. ryan","D. adi"),
         ("A. tiger","B. lion","C. rabit","D. kangaroo"),
         ("A. giraffee","B. leopard","C. elephant","D. T-rex"))
answers=(("A","B","B","A","D"))
guesses=[]
score=0
question_num=0

for question in questions:
    print("---------------------")
    print(question)
    for option in options[question_num]:
      print(option)
    guess=input("enter your option A,B,C,D").upper()
    guesses.append(guess)
      
    if guess==answers[question_num]:
      score+=1
      print("CORRECT!")
    else:
      print("WRONG!")
      print(f"correct answer is: {answers[question_num]}")
    question_num+=1