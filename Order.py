

order=[]   # An Empty list that accepts all your order


#function starts with def then def name then ()             

def diner_waitress():                       #note: Indentions are important in python, always in indent stuff when a line of code ends with a colon
    print("Hello my name is Anderson, Ill be your waiter, what will you have?")                                     #This is how you print a sentence
    
    while True:                                                           #this is an Iterative loop where as it will always loop forever,
                                                                        #it will only stop if you give it a false value or a break function

        NewOrder=str(input("Menu Item: "))                      #For the user to input the value you will need a storage, 
                                                                #ours is called NewOrder, then input, then what you want to say for that 
                                                                
        if NewOrder == "that's all":                               #conditional statement to break out of a loop
            break                                                      #if the statement is true then it breaks out the loop

        order.append(NewOrder)                              #This adds your new orderto the list you have Listname.append(variable name)

    print("You've Ordered")
    print(order)                    #this prints out all you ordered

diner_waitress()            #you need to call the function to execute it
