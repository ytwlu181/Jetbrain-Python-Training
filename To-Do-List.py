from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date
from datetime import datetime
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///todo.db?check_same_thread=False')
Base = declarative_base()


class Table(Base):
    __tablename__ = 'task'
    id = Column(Integer, primary_key=True) # this is the primary key
    task = Column(String, default='default_value')
    deadline = Column(Date, default=datetime.today())

    def __repr__(self):
        return self.task


Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

# new_row = Table(task='This is nothing!',
#                 deadline=datetime.strptime('01-24-2020', '%m-%d-%Y').date())
# session.add(new_row)
# session.commit()

# rows = session.query(Table).all()

# print(len(rows))
# first_row = rows[0]  # In case rows list is not empty

# print(first_row.task)  # Will print value of the string_field
# print(first_row.id)  # Will print the id of the row.
# print(first_row)  # Will print the string that was returned by __repr__ method

class Menu:
    def __init__(self):
        self.menu_message= '''1) Today's tasks\n2) Add task\n0) Exit
            '''
        self.new_task = ""
        self.quick_list = False

    def today_task(self):
        print("Today:")
        rows = session.query(Table).all()
        if len(rows)<=0:
            print("Nothing to do!")
        else:
            for i in range(len(rows)):
                print(str(rows[i].id) + '. ' +rows[i].task)

            print()

    def add_task(self):
        self.new_task = input("Enter task\n")
        new_row = Table(task=self.new_task)
        session.add(new_row)
        session.commit()
        print("The task has been added!\n")

    def exit_list(self):
        print("Bye!")
        self.quick_list = True

    def main_loop(self):
        while not self.quick_list:
            print(self.menu_message)
            user_choice = input()
            print()
            if user_choice == '1':
                self.today_task()
            elif user_choice == '2':
                self.add_task()
            else:
                self.exit_list()

new_list = Menu()
new_list.main_loop()
