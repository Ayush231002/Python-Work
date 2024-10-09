nm = input("Dear User, Enter your Name:- ")

gender = input("Enter your gender (Male/Female): ").lower()

if gender == "male":
    if len(nm.replace(" ", "")) <= 3:
        print(f"Dear {nm}, your Name is Nice 😊")

    elif 3 < len(nm.replace(" ", "")) <= 5:
        print(f"Dear {nm}, your Name is Good 😊")

    elif 5 < len(nm.replace(" ", "")) <= 8:
        print(f"Dear {nm}, your Name is also Good 😊")

    else:
        dec1 = input(f"Dear {nm}, your Name is quite long 😊 \nWould you like us to recommend a shorter name? (yes/no):- ")
        
        # Recommend name if user agrees
        if dec1.lower() == "yes":
            dec2 = input("What about Kisn, Cku, Ram, Sonu, Monu? \nAre you satisfied with any of these names? (yes/no):- ")
            
            if dec2.lower() == "yes":
                print("\nThanks for Considering 😊")
            else:
                dec3 = input("What about Kitu, Papu, Satu, Jitu? \nAre you satisfied with any of these names? (yes/no):- ")
                
                if dec3.lower() == "yes":
                    print("\nThanks for Considering 😊")
                else:
                    print("Sorry for the misunderstanding, your Name is Awesome! 🤦‍♂️🤒")
        else:
            print("No problem! Your name is great as it is 😊")
            
elif gender == "female":
    if len(nm.replace(" ", "")) <= 3:
        print(f"Dear {nm}, your Name is Nice 😊")

    elif 3 < len(nm.replace(" ", "")) <= 5:
        print(f"Dear {nm}, your Name is Good 😊")

    elif 5 < len(nm.replace(" ", "")) <= 8:
        print(f"Dear {nm}, your Name is also Good 😊")

    else:
        dec1 = input(f"Dear {nm}, your Name is quite long 😊 \nWould you like us to recommend a shorter name? (yes/no):- ")
        
        # Recommend name if user agrees
        if dec1.lower() == "yes":
            dec2 = input("What about:- \nRina \nSita \nRani\nMeena\nAnita  \nAre you satisfied with any of these names? (yes/no):- ")
            
            if dec2.lower() == "yes":
                print("\nThanks for Considering 😊")
            else:
                dec3 = input("What about:- \nKiko \nNaina\nMoni\nNeha \nAre you satisfied with any of these names? (yes/no):- ")
                
                if dec3.lower() == "yes":
                    print("\nThanks for Considering 😊")
                else:
                    print("Sorry for the misunderstanding, your Name is so preety! 🤦‍♂️🤒")
        else:
            print("No problem! Your name is great as it is 😊")
            
    
else:
    print("Invailed gender")
            
    

