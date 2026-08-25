new_tasks = ['task_001', 'task_011', 'task_007', 'task_015', 'task_005']
completed_tasks = ['task_002', 'task_012', 'task_006'] 

val = new_tasks.pop(-1)
completed_tasks.append(val) 
new_tasks.remove('task_007')

def last_task():
    print(new_tasks.pop(-1))

last_task()