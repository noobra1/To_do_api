import requests

BASE_URL = "https://jsonplaceholder.typicode.com/todos"

def get_all_todos():
    try:
        params = {"_limit": 5}
        response = requests.get(BASE_URL, params=params)
        response.raise_for_status()
        
        print("--- Current To-Do Tasks (First 5) ---")
        for todo in response.json():
            status = "Completed" if todo['completed'] else "Pending"
            print(f"- ID {todo['id']}: {todo['title']} [{status}]")
        print("-" * 35)

    except Exception as err:
        print(f"Error fetching tasks: {err}")

def add_new_todo(title, user_id):
    try:
        new_task_payload = {
            "title": title,
            "completed": False,
            "userId": user_id
        }
        response = requests.post(BASE_URL, json=new_task_payload)
        response.raise_for_status()
        
        created_task = response.json()
        print("\n--- Successfully Added New Task ---")
        print(f"New Task ID: {created_task['id']} | Title: {created_task['title']}")
        
    except Exception as err:
        print(f"Error adding task: {err}")

def update_task(task_id):
    try:
        url = f"{BASE_URL}/{task_id}"
        update_payload = {
            "title": "My updated and completed task",
            "completed": True,
            "userId": 1
        }
        response = requests.put(url, json=update_payload)
        response.raise_for_status()

        updated_task = response.json()
        print("\n--- Successfully Updated Task ---")
        print(f"Updated Task ID: {updated_task['id']} | Completed: {updated_task['completed']}")

    except Exception as err:
        print(f"Error updating task {task_id}: {err}")

def delete_task(task_id):
    try:
        url = f"{BASE_URL}/{task_id}"
        response = requests.delete(url)
        response.raise_for_status()
        if response.status_code == 200:
            print("\n--- 🗑️ Successfully Deleted Task ---")
            print(f"Task with ID {task_id} has been deleted.")

    except Exception as err:
        print(f"Error deleting task {task_id}: {err}")

if __name__ == "__main__":
    get_all_todos()
    add_new_todo(title="Learn about POST requests", user_id=1)
    update_task(task_id=5)
    delete_task(task_id=10)
