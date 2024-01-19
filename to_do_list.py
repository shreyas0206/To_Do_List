tasks = []

def add_task():
    task = input('Enter a new task: ')
    tasks.append(task)
    print('\n','Task Added Successfully'.center(30,'='))

def view_task():
    if len(tasks) == 0:
        print('No tasks.')
    else:
        print('\n','List of Tasks.'.center(30,'='))
        for i, task in enumerate(tasks):
            print(f'{i+1}',task)

            
def delete_task():
    if len(tasks) == 0:
        print('\n','No tasks.'.center(20,'='))
    else:
        print('\n','List of Tasks.'.center(30,'='))
        for i , task in enumerate(tasks):
            print(f'{i+1}',task)
        choise = int(input('Enter Task Number To Delete Task: '))
        if 0<choise<=len(tasks):
            del tasks[choise - 1]
            print('\n','Task Deleted Successfully'.center(30,'='))
        else:
            print('\n','Invalid Task Number'.center(20,'='))
        

while True:
    print('\n====| TO DO LIST APPLICATION |=====')
    print('         1    Add Task')
    print('         2    View Task')
    print('         3    Delete Task')
    print('         4    Exit')

    choise = input('Enter Your Choise: ')
    if choise == '1':
        add_task()
    elif choise == '2':
        view_task()
    elif choise == '3':
        delete_task()
    elif choise == '4':
        print('THANK YOU'.center(20,'='))
        break
    else:
        print("Invalid input. Please try again.")
