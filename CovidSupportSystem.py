print("Welcome to the covid 19 support service.Please select an option below:\n")
print()
print("1.Statistics\n""2.Prevention\n""3.Symptoms\n""4.Treatment\n""5.Report case\n""6.Exit\n")

USA = 1700000
SA = 27403
China = 82995


choice = input("Enter choice (1/2/3/4/5/6): ")

#loop for as long option is not 6

while choice != "6":

        

        if choice == '1':
                print("\nCurrent in SA there are "+ str(SA) +" confirmed casses\n"
                "Current in USA there are "+ str(USA) +" confirmed casses\n"
                "Current in China there are "+ str(China) +" confirmed casses\n")

                option = input("would you like to see the confirmed casses for a random country? y/n:")
    
                if option == "y":
                        print("To select a random country, type a number from 0 to 9: ")
                        number = input("Enter number str(0, 9): ")

                        if number == "0":
                                print("Spain has 4567 confirmed casses\n")
                        elif number == "1":
                                print("Russia has 72 confirmed casses\n")
                        elif number == "2":
                                print("Uganda as 900 confirmed casses\n")
                        elif number == "3":
                                print("Spain has 4567 confirmed casses\n")
                        elif number == "4":
                                print("Ghana has 12 confirmed casses\n")
                        elif number == "5":
                                print("Botswane has 23 confirmed casses\n")
                        elif number == "6":
                                print("Gabon has 1000 confirmed casses\n")
                        elif number == "7":
                                print("Austsralia has 7155 confirmed casses\n")
                        elif number == "8":
                                print("Ghana has 12 confirmed casses\n")
                        elif number == "9":
                                print("Botswane has 23 confirmed casses\n")
                        else:
                                exit()
                        choice = input("Enter choice (1/2/3/4/5/6): ")

                else:
                        exit()

        elif choice == "2":
                print("\nTo prevent the spread of COVID-19:\n"
                "Clean your hands often. Use soap and water, or an alcohol-based hand rub.\n"
                "Maintain a safe distance from anyone who is coughing or sneezing.\n"
                "Don't touch your eyes, nose or mouth.\n""Cover your nose and mouth with your bent elbow or a tissue when you cough or sneeze.\n"
                "Stay home if you feel unwell.\n""If you have a fever, cough and difficulty breathing, seek medical attention. call in advance\n"
                "Follow the direction of your local health authority\n")

                choice = input("Enter choice (1/2/3/4/5/6): ")


        elif choice == '3':
                print("\nMost common symtoms:\n""fever\n""dry cough\n""tirednes\n\n"
                "Less common symptoms:\n""aches and pains\n""sore throat\n""diarrhoea\n"
                "conjunctivitis\n""headache\n""loss of taste or smell\n"
                "a rash on skin, or discolouration of fingers or toes\n\n""Serious symptoms:\n"
                "difficulty breathing or shortness of breath\n""chest pain or pressure\n"
                "loss of speech or movement")

                choice = input("Enter choice (1/2/3/4/5/6): ")


        elif choice == '4':
                print("\nIf you feel sick you should rest, drink plent of fluid, and eat nutritious food. Stay in a separate room from other family members, and use a dedicated bathroom if possible. clean and disinfect\n"
                "frequently touched surfaces")

                choice = input("Enter choice (1/2/3/4/5/6): ")

        
        elif choice == '5':
                sypmtos = input("\nDo you have any of the symptoms? y/n:")
                if sypmtos == 'y':
                        temp = input("Is your temperature above 38.5\xb0C? y/n:")
                        if temp == 'y':
                                country = input("In which country are you? y/n:\n1.SA\n2.USA\n3.China\nEnter option(1/2/3): ")
                                if country == '1':
                                        SA += 1
                                elif country == "2":
                                        USA += 1
                                elif country == "3":
                                        China += 1
                                
                                print('you have COVID 19 please see Treament')

                choice = input("Enter choice (1/2/3/4/5/6): ")

