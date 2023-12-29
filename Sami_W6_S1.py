import os
import datetime
from abc import ABC, abstractmethod


# 1.Task Management Class (TaskManagement):
class TaskManagement:
    def __init__(self,):
        self.taskList = []
#   This class serves as the core of the task management system.
# It contains a list (taskList) to store tasks.
# It provides methods to add and display tasks.


#   This class is responsible for creating and adding tasks to the TaskManagement instance.
#   It uses the PersonalTask and WorkTask classes to create specific types of tasks.
#    It enforces proper task type (Personal or Work).
    def createTask(self):
        taskType = input("Task Type (Personal or Work): ")
        taskId = input("Task ID: ")
        taskname = input("Task Name: ")
        deadline = input("Deadline: ")
        color = input("Color: ")
        priority = input("Priority: ")
        task = Task(taskType, taskId, taskname, deadline, color, priority)
        self.addTask(task)
        print("Task created successfully.")

    def addTask(self, task):
        self.taskList.append(task)


# 3.Task Editing Class (TaskEditing):
class TaskEditing(TaskManagement):
    def __init__(self, status, priority, deadline):
        super().__init__()
#   This class handles various editing operations on tasks.
#   Students will learn how to modify task attributes such as status, priority, and deadline.
#   They will also learn about searching for tasks and removing tasks from the list.
    def searchTask(self):
        taskname = input("Enter task name to search: ")
        searchTask = TaskEditing()
        found_Task = searchTask.searchTask(taskname)
        if foundTask:
            print("Task found:")
            print(f"Task Type: {foundTask.taskType}")
            print(f"Task ID: {foundTask.taskId}")
            print(f"Task Name: {foundTask.taskname}")
            print(f"Deadline: {foundTask.deadline}")
            print(f"Color: {foundTask.color}")
            print(f"Priority: {foundTask.priority}")
            print("Status: Completed" if foundTask.completed else "Status: Incomplete")
        else:
            print("Task not found.")

    def removeTask(self):
        taskId = input("Enter task ID to remove: ")
        removeTask = TaskEditing()
        removeTask.removeTask(taskId)
        print("Task removed successfully.")




#  4.Task Tracking Class (TaskTracking):
class TaskTracking(TaskManagement):
    def __init__(self):
        super().__init__()
#   This class allows tracking task statuses.
#   Students will learn how to retrieve the status of a task and mark tasks as completed.
    def displayTask(self):
        displayTask = TaskTracking()
        displayTask.displayTask()


        # for task in self.taskList:
        #     print(f"Task Type: {task.tasktype}")
        #     print(f"Task ID: {task.taskId}")
        #     print(f"Task Name: {task.taskname}")
        #     print(f"Deadline: {task.deadline}")
        #     print(f"Color: {task.color}")
        #     print(f"Priority: {task.priority}")
        #     if task.completed:
        #         print("Status: Completed")
        #     else:
        #         print("Status: Incomplete")
        #     print("\n")

    def completeTask(self):
        taskId = input("Enter task ID to mark as completed: ")
        completeTask = TaskTracking()
        completeTask.completeTask(taskId)
        print("Task marked as completed.")



#TaskManagement.displayTask()

# 5.Abstract Base Class (Task):
class Task(ABC):
    def __init__(self,tasktype, taskId, taskname, deadline, color, priority):
#   An abstract base class defines the common structure for PersonalTask and WorkTask subclasses.
#   It introduces the concept of abstract methods and demonstrates inheritance.
        self.tasktype = tasktype
        self.taskId = taskId
        self.taskname = taskname
        self.deadline = self.handle_special_keywords(deadline)
        self.color = color
        self.priority = priority


@abstractmethod
def mark_as_completed(self):
    pass


def handle_special_keywords(self, deadline):
    SPECIAL_KEYWORDS = {
        "today": datetime.date.today(),
        "tomorrow": datetime.date.today() + datetime.timedelta(days=1),
        "next week": datetime.date.today() + datetime.timedelta(weeks=1)
    }




#  6.PersonalTask and WorkTask Classes:
class PersonalTask(Task):
    def __init__(self, taskType, taskId, taskname, deadline, color, priority):
        super().__init__(taskType, taskId, taskname, deadline, color, priority)
        self.completed = False  # Varsayılan olarak tamamlanmamış

    def mark_as_completed(self):
        self.completed = True

class WorkTask(Task):
    def __init__(self, taskType, taskId, taskname, deadline, color, priority):
        super().__init__(taskType, taskId, taskname, deadline, color, priority)
        self.completed = False  # Varsayılan olarak tamamlanmamış

    def mark_as_completed(self):
        self.completed = True

#   These are subclasses of the ‘Task’ class, representing personal and work-related tasks.
#   Students will understand how to override methods and use class-specific attributes.
#   They will see how to implement interfaces/abstract classes (‘Priorization’).

ptask1 = PersonalTask(1, "reading", "Today", "Blue", None)
ptask2 = PersonalTask(2, "exercise", "Tomorrow", "Green", None)
ptask1 = WorkTask(1, "meeting", "20/12/2023", "Red", None)


ptask1 = PersonalTask("Personal", ptask1.taskId, ptask1.taskName, ptask1.deadline, ptask1.color, priority=None)
ptask2 = PersonalTask("Personal", ptask2.taskId, ptask2.taskName, ptask2.deadline, ptask2.color, priority=None)
ptask1 = WorkTask("Work", wtask1.taskId, wtask1.taskName, wtask1.deadline, wtask1.color, priority=None)


#  7.Special Keywords Dictionary (SPECIAL_KEYWORDS):


#   A dictionary is used to handle special keywords like "today," "tomorrow," and "next week" for deadlines.
#   Students will learn about dictionary usage and date manipulation.
'''

while(True):
    try:
        print("---------------> TODO <--------------")
        print("1 - CREATE TASK")
        print("2 - ADD TASK 2")
        print("3 - SEARCH TASK")
        print("4 - REMOVE TASK")
        print("5 - DISPLAY TASK")
        print("6 - COMPLETE TASK")
        print("0 - CIKIS")



        secim=input("Lutfen yapmak istediginiz secimin kodunu girin : ", )
        os.system('cls')
        if secim=="1":  #create task
            createTask.TaskScheduling(TaskManagement)
        elif secim=="2":
            addTask.TaskScheduling(TaskManagement)
        elif secim=="3":
            searchTask.TaskEditing()
        elif secim=="4":
            removeTask.TaskEditing()
        elif secim=="5":
            displayTask.TaskTracking()
        elif secim=="6":
            completeTask.TaskTracking()
        elif secim=="0":
            break
        else:
            print("Geçersiz seçim. Lütfen tekrar deneyin.")
    except Exception as e:
        print("Bir hata oluştu:", str(e))

# 2.Task Scheduling Class (TaskScheduling):
class TaskScheduling(TaskManagement):
    def __init__(self):
        super().__init__()
'''
while True:
    try:
        print("---------------> TODO <--------------")
        print("1 - CREATE TASK")
        print("2 - ADD TASK")
        print("3 - SEARCH TASK")
        print("4 - REMOVE TASK")
        print("5 - DISPLAY TASK")
        print("6 - COMPLETE TASK")
        print("0 - CIKIS")

        secim = input("Lutfen yapmak istediginiz secimin kodunu girin: ")
        os.system('cls')
        if secim == "1":
            taskType = input("Task Type (Personal or Work): ")
            taskId = input("Task ID: ")
            taskname = input("Task Name: ")
            deadline = input("Deadline: ")
            color = input("Color: ")
            priority = input("Priority: ")
            TaskManagement.createTask(taskType, taskId, taskname, deadline, color, priority)
        elif secim == "2":
            addTask = TaskManagement()
            taskId = input("Enter task ID to mark as completed: ")
            addTask.addTask(task)
        elif secim == "3":
            searchTask = TaskManagement()
            taskname = input("Enter task name to search: ")
            foundTask = searchTask.searchTask(taskname)
            if foundTask:
                print("Task found:")
                print(f"Task Type: {foundTask.taskType}")
                print(f"Task ID: {foundTask.taskId}")
                print(f"Task Name: {foundTask.taskname}")
                print(f"Deadline: {foundTask.deadline}")
                print(f"Color: {foundTask.color}")
                print(f"Priority: {foundTask.priority}")
                print("Status: Completed" if foundTask.completed else "Status: Incomplete")
            else:
                print("Task not found.")
        elif secim == "4":
            removeTask = TaskManagement()
            taskId = input("Enter task ID to remove: ")
            removeTask.removeTask(taskId)
        elif secim == "5":
            displayTask = TaskManagement()
            displayTask.displayTask()
        elif secim == "6":
            completeTask = TaskManagement()
            taskId = input("Enter task ID to mark as completed: ")
            completeTask.completeTask(taskId)
        elif secim == "0":
            break
        else:
            print("Geçersiz seçim. Lütfen tekrar deneyin.")
    except Exception as e:
        print("Bir hata oluştu:", str(e))