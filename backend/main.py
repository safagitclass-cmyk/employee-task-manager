from fastapi import FastAPI

app = FastAPI()

employees = []
tasks = []

@app.get("/")
def home():
    return {"message": "Employee Task Manager"}

@app.get("/employees")
def get_employees():
    return employees

@app.post("/employees")
def add_employee(name: str):
    employee = {
        "id": len(employees) + 1,
        "name": name
    }
    employees.append(employee)
    return employee

@app.post("/tasks")
def assign_task(employee_id: int, task_name: str):
    task = {
        "id": len(tasks) + 1,
        "employee_id": employee_id,
        "task_name": task_name,
        "status": "Pending"
    }
    tasks.append(task)
    return task

@app.get("/tasks")
def get_tasks():
    return tasks

@app.put("/tasks/{task_id}")
def update_task(task_id: int):
    for task in tasks:
        if task["id"] == task_id:
            task["status"] = "Completed"
            return task
    return {"message": "Task not found"}

@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    for task in tasks:
        if task["id"] == task_id:
            tasks.remove(task)
            return {"message": "Task deleted"}
    return {"message": "Task not found"}