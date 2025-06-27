# Todo List Application

class TaskManager():
    def __init__(self):
        self.tasks = [] # list
        self.task_info = {} # dictionary 

    def GetTaskInfo(self, task):
        if task in self.tasks:
            return self.task_info[task]
    
    def AddTask(self, task, info):
        if task not in self.tasks:
            self.tasks.append(task)
            self.task_info[task] = info
        else:
            print(f"Task already exists!")

    def RemoveTask(self, task):
        if task in self.tasks:
            del self.task_info[task]
            self.tasks.remove(task)
            print(f"Task removed!")
        else:
            print(f"Unknown Task.")

tm = TaskManager()
tm.AddTask("Study", "Finish Chapter 6")
tm.AddTask("Study", "Finish Chapter 6") # Try adding duplicate task
print(tm.GetTaskInfo("Study"))
tm.RemoveTask("Study")
