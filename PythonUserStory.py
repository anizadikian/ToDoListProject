import json
import datetime


def new_task():
    with open('data.json') as f:
        dicts_old = json.load(f)  # lets simple call this old dictionary.
    dicts = {}  # the one which should be appended to the old on.
    while True:
        user_task = input("What is the task you need to accomplish?   ")
        if user_task.isalpha():
            dicts[user_task] = {}
            break
        print("Please enter characters A-Z only")

    while True:
        user_deadline = input("What is the deadline for the task mentioned? Please insert in the format MM/DD/YYYY:   ")
        try:
            user_deadline_converted = datetime.datetime.strptime(user_deadline, '%m/%d/%Y')
            dicts[user_task]['Deadline'] = user_deadline
            break
        except ValueError:
            print("Date format should be MM/DD/YYYY")

    while True:
        user_time = input("What is the period of time you need to accomplish it?    ")
        dicts[user_task]['Time'] = user_time
        if user_time.isdigit():
            break
        print("You must enter a number (i.e. 0,1,2...")

    dicts_old['tasks'].append(dicts)
    dicts_new = dicts_old

    with open('data.json', 'w') as f:
        json.dump(dicts_new, f)


def task_modifaction():
    with open('data.json') as f:
        dicts_old = json.load(f)  # lets simple call this old dictionary.

    for i in dicts_old['tasks']:  # make a loop to print out our data
        task_name = next(iter(i.keys()))
        deadline = i[task_name]['Deadline']
        times = i[task_name]['Time']
        print('Task is ', task_name, ', Deadline is ', deadline, ', The period of time you need to accomplish is', times)

    question_name = input("Please insert the name of the task you want to modify:      ")

    print("The task is   ", question_name)

    while True:
        user_answer = input("Please insert the new name of the task?")
        if user_answer.isalpha():
            break
        print("Please enter characters A-Z only")

    user_deadline = input("please input the new deadline:    ")
    user_time = input("please input the new time:     ")

    for i in range(len(dicts_old['tasks'])):  # finding the old record
        if next(iter(dicts_old['tasks'][i].keys())) == question_name:
            dicts_old['tasks'][i] = {
                user_answer: {'Deadline': user_deadline, 'Time': user_time}}  # replacing the old record

    with open('data.json', 'w') as f:
        json.dump(dicts_old, f)


def see_all_tasks():
    with open('data.json') as f:
        dicts_old = json.load(f)  # lets simple call this old dictionary.
    sorted_data = {}  # this is for sorting
    for i in dicts_old['tasks']:
        task_name = next(iter(i.keys()))
        deadline = i[task_name]['Deadline']
        times = i[task_name]['Time']
        sorted_data[
            deadline] = task_name + " " + times  # creating a dict where the keys are the dates and values are the tasks names + the period

    ordered_data = sorted(sorted_data.items(), key=lambda x: datetime.datetime.strptime(x[0], '%m/%d/%Y'),
                          reverse=False)  # sorting based on the dates.
    print(ordered_data)  # printing out the sorted data
    for i in ordered_data:
        print(i[0], " ----", i[1])


def main():
    while True:
        print(
            "This is your ToDo list helper. It will help you organize your tasks. Please fill in the information bellow")
        print("Please choose number from the following:")
        print("1 : Insert new task")
        print("2 : See previously added tasks")
        print("3 : Modify task")

        user_input = int(input())

        if user_input == 1:

            new_task()


        elif user_input == 2:

            see_all_tasks()


        elif user_input == 3:

            task_modifaction()


        else:
            print("Please type as required, inserting the number 1, 2 or 3")


main()
