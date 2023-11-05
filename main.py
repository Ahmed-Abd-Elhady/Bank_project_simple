import json
import os
import subprocess
import time
import re
print("1 : GImee money")#give him money
print("------------------------------")#give friend money
print("2 : Give your Friend money")
print("------------------------------")#input money
print("3 : Enter money\n")
def clear_screen():


    os.system('cls' if os.name == 'nt' else 'clear')
try:
    user_input = input("Your select sir : \n")#the input select number
    if user_input > '3':
        clear_screen()
        print("You have 3 choice only\n")
        time.sleep(1)
        subprocess.run(['python', 'main.py'], check=True)
    int(user_input) + 1
except ValueError:
    clear_screen()
    print("Invalid input. Please enter a valid int value.")






user_input = user_input
user_friends = ['Ali' , 'Ahmed' , 'Alla' , "Kngako"]



file_path = "data.json"
try:
    with open(file_path, "r") as file:
        money_in_bank = json.load(file)
except FileNotFoundError:
    money_in_bank = 5000  # Set a default value if the file doesn't exist
    print(f"File '{file_path}' not found. so we created one UwU")

money_in_bank = money_in_bank['money_in_bank']['user']





try:
    with open(file_path, "r") as file:
        user_access_users = json.load(file)
except FileNotFoundError:
    print(f"File '{file_path}' not found.")

user_access_users = user_access_users['user_access_users']


try:
    with open(file_path, "r") as file:
        user_friends_money_in_bank = json.load(file)
except FileNotFoundError:
    print(f"file '{file_path } not found")





user_friends_money_in_bank = user_friends_money_in_bank['user_friends_money_in_bank']








class CustomBreak(Exception):
    pass






try:




    if (user_input == '1'):
        clear_screen()
        print(f"your money in bank is : ${money_in_bank}\n")
        money_out_count = int(input("How much do you want to take? : "))
        if  int(money_out_count) > money_in_bank:
            clear_screen()
            print("You Don't Have This Number Of Money Sir !\n")
            time.sleep(1)
            raise CustomBreak
        clear_screen()
        new_money_req = int(money_in_bank) - int(money_out_count)
        '''
        with open("user.txt", "w") as file:
            file.write("money_in_bank = " + str(new_money_req))
        with open("user.txt", "r") as file:
            first_line = file.readline()
            integers = [int(match) for match in re.findall(r'\d+', first_line)]
            integers = int(integers[0])
            money_in_bank = int(integers)
        '''
        with open(file_path, "r") as file:
            data = json.load(file)

            user_main = 'user'
            new_balance = new_money_req

            if user_main in data['money_in_bank']:
                data['money_in_bank'][user_main] = new_balance
                print(f"Updated balance for {user_main}: {new_balance}")
            else:
                print(f"User {user_main} not found in the database.")
            with open(file_path, "w") as file:
                json.dump( data , file, indent=4)



        print(f'You now have in your bank : {new_money_req}\n')
    elif(user_input == '2'):
        clear_screen()
        print(f"your money in bank is : ${money_in_bank}\n")
        print(f"You have {len(user_friends)} Freinds names is : {", ".join(user_friends)}\n ")
        print(user_access_users)
        friend_req_name = input("Tell me who you want to send money to ? :\n ")
        
        clear_screen()













        if not friend_req_name != user_friends :
            print("You don't have access to this user\n")
            time.sleep(1)
            subprocess.run(['python', 'main.py'], check=True)
            raise CustomBreak
        
        for i in user_friends:
            if i == friend_req_name:
                for z in user_access_users:
                    if (friend_req_name == z):
                        print(f"Systeam say you Have {user_access_users[z]} access\n") 
                        #print(f"The Z is  : {user_access_users[z]} ")
                        
                        if not user_access_users[z] != 'No':
                            clear_screen()
                            print("You don't have access to this user\n")
                            raise CustomBreak
                        print(f"your money in bank is : ${money_in_bank}\n")
                        print(f"Your friend {friend_req_name} have ${user_friends_money_in_bank[z]}\n")
                        money_out_count = input("How mutch do you want to transfare ? : \n")
                        if  int(money_out_count) > money_in_bank:
                            clear_screen()
                            print("You Don't Have This Number Of Money Sir !\n")
                            time.sleep(1)
                            subprocess.run(['python', 'main.py'], check=True)
                            raise CustomBreak
                        clear_screen()
                        user_friends_money_in_bank[z] = int(user_friends_money_in_bank[z]) + int(money_out_count)
                        money_negtive_main_user =  int(money_in_bank) - int(money_out_count)


                        with open(file_path, "r") as file:
                            data = json.load(file)

                        user_main = friend_req_name
                        new_balance = user_friends_money_in_bank[z]

                        if user_main in data['user_friends_money_in_bank']:
                            data['user_friends_money_in_bank'][user_main] = new_balance
                            print(f"Updated balance for {user_main}: {new_balance} \n")
                        else:
                            print(f"User {user_main} not found in the database.")
                        with open(file_path, "w") as file:
                                json.dump( data , file, indent=4)











                        print(f"Your friend {friend_req_name} $money is : {user_friends_money_in_bank[z]} \n")

                        with open(file_path, "r") as file:
                            data = json.load(file)

                        user_main = 'user'
                        new_balance = money_negtive_main_user

                        if user_main in data['money_in_bank']:
                            data['money_in_bank'][user_main] = new_balance
                            print(f"Updated balance for {user_main}: {new_balance}\n")
                        else:
                            print(f"User {user_main} not found in the database.\n")

                        with open(file_path, "w") as file:
                            json.dump( data , file, indent=4)

                    # with open(file_path, "w") as file:
                            #json.dump(data, file, indent=4)



                        






                        print(f"Your bank money is : ${money_in_bank} " )




    if (user_input == '3'):
        clear_screen()
        print(f"your money in bank is : ${money_in_bank}\n")
        money_add_count = int(input("How much do you want to add? : "))
        clear_screen()
        new_money_req = int(money_in_bank) + int(money_add_count)
        '''
        with open("user.txt", "w") as file:
            file.write("money_in_bank = " + str(new_money_req))
        with open("user.txt", "r") as file:
            first_line = file.readline()
            integers = [int(match) for match in re.findall(r'\d+', first_line)]
            integers = int(integers[0])
            money_in_bank = int(integers)
        '''
        with open(file_path, "r") as file:
            data = json.load(file)

            user_main = 'user'
            new_balance = new_money_req

            if user_main in data['money_in_bank']:
                data['money_in_bank'][user_main] = new_balance
                print(f"Updated balance for {user_main}: {new_balance}")
            else:
                print(f"User {user_main} not found in the database.")
            with open(file_path, "w") as file:
                json.dump( data , file, indent=4)



        print(f'You now have in your bank : {new_money_req}\n')

        #money_out_count = input("How mutch do you want to Give your Friend ? : ")
        
except CustomBreak:
    print("Stop the Transfer!!! Contact the support www.banksupport.com\n")
except ValueError:
    print("Invalid input. Please enter a valid int value.")





