import json
print("This is your ToDo list helper. It will help you organize your tasks. Please fill in the information bellow")
with open('my_dict.json') as f:
dict = json.load(f)

    def new_task():

        user_task = input("what is your task?")
        dict[int(len(dict.keys()) + 1)] = {user_task: ""}

        user_deadline = input("what is the deadline:")
        dict[int(len(dict.keys()) + 1)] = {user_deadline: ""}

        user_time = input("what is the time:")
        dict[int(len(dict.keys()) + 1)] = {user_time: ""}

        with open('my_dict.json', 'w') as f:
            json.dump(dict, f)

        return new_task()

    def task_modifaction():

       with open('DataJson.json') as f:
       dict = json.load(f)

       print(dict)
       print(dict.keys())

       question_name = input('name of the task ? ')
       user_question = ""
       for key in dict[question_name].keys():
       user_question = key
       break
       print("The task is", user_question)
       
    user_answer = input("Please Insert your answer?")
    user_deadline = input("please input the new deadline")
    user_time = input("please input the new time")
      dict[question_name] = {user_question: user_answer, user_deadline}

    with open('DataJson.json', 'w') as f:
        json.dump(dict, f)

       return task_modifaction()

def see_all_tasks():
    with open("DataJson.json") as data:
        data_dict = json.load(data)

        for object in DataJson.json:
            print(object)

    def main():

    while True:
        print("Please choose number from the following:")
        print("1 : Insert new task")
        print("2 : See previously added tasks")
        print("3 : Modify task")

        user_input= int(input())


        if user_input == 1:

            return new_task()

        elif user_input == 2:

            return see_all_tasks()

        elif user_input == 3:

        return task_modifaction()

        else :
            print("Please type as required")
            exit

main()
