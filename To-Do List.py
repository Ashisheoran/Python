from dotenv import load_dotenv 
from sqlalchemy import create_engine , text ,Column,String, Integer,TIMESTAMP,func ,Enum
from sqlalchemy.orm import declarative_base , sessionmaker
import enum , os

Base = declarative_base()

class TaskState(enum.Enum):
    pending = "pending"
    ongoing = "ongoing"
    fullfilled = "fullfilled"

class Task(Base):
    __tablename__ = "tasks"
    task_id = Column(Integer,primary_key=True,autoincrement=True)
    task_category = Column(String(200),nullable=False)
    task_description = Column(String(300),nullable=False)
    created_at = Column(TIMESTAMP,server_default=func.now())
    state = Column(Enum(TaskState),default=TaskState.pending)

load_dotenv()
try:
    engine = create_engine(os.getenv("DATABASE_URL"))
    Session = sessionmaker(bind=engine)
    print("Database connected")

    try:
        session = Session()
        Base.metadata.create_all(engine)
        print("table created")
    except Exception as e:
        print(f"Table not created and error occur: {e}")
        
except Exception as e:
    print(e)

# CRUD operations
def add_task(category,description,state=TaskState.pending):
    new_task = Task(task_category=category,task_description = description,state = state)
    session.add(new_task)
    session.commit()
    return f"Task Added Successfully"

def view_all_tasks():
    tasks = session.query(Task).all()
    print("All tasks :")
    for task in tasks:
        print(f"{task.task_id}. {task.task_category} - {task.task_description}  (created at {task.created_at})")
    return view_all_tasks

def view_tasks_by_state(state):
    tasks = session.query(Task).filter(Task.state==state).all()
    print(f"task in state: {state} is")
    for task in tasks:
        print(f" {task.task_id}. {task.task_category} - {task.task_description}  (created at {task.created_at})")

def update_task_state(task_id,new_state):
    task = session.query(Task).filter_by(task_id = task_id).first()
    if task:
        task.state = new_state
        session.commit()
        return f"{task_id} Task Updated"
    else:
        return f"{task_id} task not found"
    
def delete_task(task_id):
    task = session.query(Task).filter_by(task_id=task_id).first()
    if task:
        session.delete(task)
        session.commit()    
        print(f"task with id {task_id} deleted")
    else:
        print(f"task with id {task_id} not found")



def main():
    while True:
        print("\n------ TO-DO LIST MANAGER ------")
        print("1. Add Task")
        print("2. View All Tasks")
        print("3. View Tasks by State")
        print("4. Update Task State")
        print("5. Delete Task")
        print("6. Exit")

        choice = input("Enter Your Choice: ")

        match choice:
            case '1':
                category = input("Enter Task Category: ")
                description = input("Enter Task Description: ")
                state_input = input("Enter Task state (pending/ongoing/fullfilled)") 
                if state_input not in TaskState.__members__:
                    print("Invalid State")
                    continue
                print(add_task(category,description,TaskState[state_input]))
            
            case '2':
                result = view_all_tasks()
                print(result())
            
            case '3':
                state_input = input("Enter Task State(pending/ongoing/fullfilled): ")
                if state_input not in TaskState.__members__:
                    print("Invalid State")
                    continue
                print(view_tasks_by_state(state_input))
            
            case '4':
                try:
                    task_id = int(input("Enter Task Id to Update State:"))
                    new_state_input = input("Enter New State for task (pending/ongoing/fullfilled): ")
                    if new_state_input not in TaskState.__members__:
                        print("Invalid State")
                        continue
                    print(update_task_state(task_id,new_state_input))
                except ValueError:
                    print("invalid Input Task Id")
            case '5':
                try:
                    task_id_input = int(input("Enter Task Id to Delete: "))
                    print(delete_task(task_id_input))
                except ValueError:
                    print("Invalid Input Task id")

            case '6':
                print("Exiting To-Do list Manager")
                break

            case _:
                print("Invalid Choice.... Try Again")
                


if __name__ == "__main__":
    main()
