mark_num = ""

def add_task(list_of_tasks):
    task = input("Enter a task: ")
    list_of_tasks.append(task)

def remove_task(list_of_tasks):
    while True:
        remove_num = input("Which task no. do you want to remove? ")
        if not remove_num.isdigit():
            print("Please enter a number!!!")
            continue
        elif int(remove_num) > len(list_of_tasks) or int(remove_num) <= 0:
            print("Please enter a valid number!!! ")
            continue
        else:
            remove_num = int(remove_num)
            list_of_tasks.remove(list_of_tasks[remove_num - 1])
            break

def mark_done(list_of_tasks):
    global mark_num
    while True:
        mark_num= input("Which task no. do you want to mark as done? ")
        if not mark_num.isdigit():
            print("Please enter a number!!!")
            continue
        elif int(mark_num) > len(list_of_tasks) or int(mark_num) <= 0:
            print("Please enter a valid number!!! ")
            continue
        else:
            mark_num = int(mark_num)
            break

def display(list_of_tasks):
    print()
    print("********** TASKS *********")
    if len(list_of_tasks) <= 0:
        print("There are no tasks to do!!!")
    else:
        task_num = 0
        for task in list_of_tasks:
            task_num += 1
            if task_num == mark_num:
                print(f"{task_num}. {task} ✔️")
            else:
                print(f"{task_num}. {task} ❌")


def main():
    list_of_tasks = []

    while True:
        print()
        print("---------- TO-DO LIST ----------")

        print("a. Add task")
        print("b. Remove task")
        print("c. Mark done")
        print("d. Just display tasks")
        print("e. Quit")

        list_func = input("Enter one of the functions to be performed (a-e): ").lower()
        if list_func not in ("a", "b", "c", "d", "e"):
            print("INVALID INPUT!")
            continue
        elif list_func == "a":
            add_task(list_of_tasks)
            display(list_of_tasks)
        elif list_func == "b":
            remove_task(list_of_tasks)
            display(list_of_tasks)
        elif list_func == "c":
            mark_done(list_of_tasks)
            display(list_of_tasks)
        elif list_func == "d":
            display(list_of_tasks)
        else:
            print("BYE!👋")
            break
    

if __name__ == '__main__':
    main()