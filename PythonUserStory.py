import json
import datetime

print("This is your ToDo list helper. It will help you organize your tasks. Please fill in the information bellow")
with open('data.json') as f:
    dict = json.load(f)


def new_task(dict):
    while True:
        user_task = input("What is the task you need to accomplish?   ")
        dict[int(len(dict.keys()) + 1)] = {user_task: ""}
        if user_task.isalpha():
            break
        print("Please enter characters A-Z only")
        
    while True:
        user_deadline = input("What is the deadline for the task mentioned? Please insert in the format MM/DD/YYYY:   ")
        try:
            user_deadline = datetime.datetime.strptime(user_deadline, '%m/%d/%Y')
            dict[int(len(dict.keys()) + 1)] = {"Deadline": user_deadline}
            break
        except ValueError:
            print("Date format should be MM/DD/YYYY")

    while True:
        user_time = input("What is the period of time you need to accomplish it?    ")
        dict[int(len(dict.keys()) + 1)] = {user_time: ""}
        if user_time.isdigit():
            break
        print("You must enter a number (i.e. 0,1,2...")


    y = {user_task: {user_deadline, user_time}}

    with open('data.json', 'w') as f:
        json.dump(dict, f)

def task_modifaction(dict):
    print(dict)
    print(dict.keys())

    question_name = input("Please insert the name of the task you want to modify")
    user_question = ""
    for key in dict[question_name].keys():
        user_question = key
        break
    print("The task is", user_question)

    while True:
        user_answer = input("Please insert the new name of the task?")
        if user_answer.isalpha():
            break
        print("Please enter characters A-Z only")

    user_deadline = input("please input the new deadline")
    user_time = input("please input the new time")
    dict["question_name"] = {user_question: {user_answer, user_deadline, user_time}}

    with open('DataJson.json', 'w') as f:
        json.dump(dict, f)


def see_all_tasks(dict):
    print(dict)

def main():
    while True:
        print("Please choose number from the following:")
        print("1 : Insert new task")
        print("2 : See previously added tasks")
        print("3 : Modify task")

        user_input = int(input())

        if user_input == 1:

            new_task(dict)


        elif user_input == 2:

            see_all_tasks(dict)


        elif user_input == 3:

            task_modifaction(dict)


        else:
            print("Please type as required, inserting the number 1, 2 or 3")
main()
