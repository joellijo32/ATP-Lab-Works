
database={"password":['reset','Wrong'],
         "contact":['name','Phone Number'],
         "about":["Company","History"]}
faq_responses={"password":{'reset':"Follow The Link Sent To Your Email",
                          'Wrong':"You Have Entered Wrong Password"},
                 "contact":{'name':"Call Our Coustomer Executive ",
                             "Phone Number":"The Phone Number is 156387"},
                  "about":{"Company":"The Company Has Been Created 25 Years Ago",
                           "History":"The Copmany Has A History Of Execellece Of 20 Years,Still One Of The Leading One In the Insdusrty"}
}
faq_follow_up={"password":"Do You What To Reset OR Wrong The Password",
               "contact":"Do you want the name or phone number",
               "about":"Do you want to know about the company or history"}


while True : 
    users_response=input("What Do You Need Help With: ").lower()
    flag=False
    for keyword_1 in database:
        if users_response.find(keyword_1)>=0:
         keyword_2=database[keyword_1]
         for key_2 in keyword_2:
                if users_response.find(key_2)>=0:
                    print(faq_responses[keyword_1][key_2])
                    flag=True
                    break
         if not flag:
                follow_up_response=input(faq_follow_up[keyword_1]).lower()
                for key_2 in keyword_2:
                    if follow_up_response.find(key_2)>=0:
                        print(faq_responses[keyword_1][key_2])
                        flag=True
                        break
        
        
    if not flag:
        print("Couldn't find your answer")
    print("Enter Whether You Want any more help or not (yes or no) : ")
    choice = input().lower()
    if choice == "no" : 
        break