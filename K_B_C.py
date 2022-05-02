print("Welcom To KBC Game")
print("first question per 5000 and second question per 10000 and third question per 30000 Rs milte hai")
question_list = [

    "How many continents are there?",              
    "What is the capital of India?",               
    "NG mei kaun se course padhaya jaata hai?"    

]


options_list = [

    
    ["Four", "Nine", "Seven", "Eight"],
    ["Chandigarh", "Bhopal", "Chennai", "Delhi"],
    ["Software Engineering", "Counseling", "Tourism", "Agriculture"]

]
solution_list = [3, 4, 1]
answer50_50=[("four","seven"),
      ("Bhopal","Delhi"),
      ("software Engineering" ,"Counseling")]

i = 0 
count = 0 
while i < len(question_list):
    print(i+1 , question_list[i])
    j = 0 
    while j < 4 :
        print(j+1,options_list[i][j])
        j+=1
    if count < 1:
        print("do you want to use life line:")
        c = input("enter Yes or No:")
        if c=="yes":
            print(answer50_50[i])
            count+=1
    else:
        print("you have already used life line")
    answer = int(input ("enter your answer:"))
    if solution_list[i] == answer:
        print("your answer is correct")
    else:
        print("Game Over")
        print("thank you for participeting")
        break
    i+=1
