# import os
# os.remove("todo.db")


from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date
from datetime import datetime, timedelta
from sqlalchemy.orm import sessionmaker
from sqlalchemy import desc, asc

engine = create_engine('sqlite:///todo.db?check_same_thread=False')
Base = declarative_base()


class Table(Base):
    __tablename__ = 'task'
    id = Column(Integer, primary_key=True)  # this is the primary key
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

# datetime.today()  # return current date and time.
# datetime.today().date()  # current date without time
# datetime.today().time()  # current time without date
#
# datetime.strptime(date_string, format)  # return a datetime corresponding to date_string, parsed according to format.
# # Format example: '%Y-%m-%d' - '2020-04-24'
#
# today = datetime.today()
# today.day  # the day of a current month.
# today.strftime('%b')  # the short name of the current month. I.e 'Apr'
# today.weekday()  # return the day of the week as an integer, where Monday is 0 and Sunday is 6.
#
# yesterday = today - timedelta(
#     days=1)  # a timedelta object represents a duration, the difference between two dates or times.
# day_after_tomorrow = today + timedelta(days=2)
#
# from datetime import datetime
#
# today = datetime.today()
# rows = session.query(Table).filter(Table.date == today).all()

class Menu:
    def __init__(self):
        self.menu_message = '''1) Today's tasks\n2) Week's tasks\n3) All tasks\n4) Add task\n0) Exit  '''
        self.new_task = ""
        self.quick_list = False
        self.today = datetime.today()
        self.new_deadline = ""
        self.week_after = self.today + timedelta(days=7)

    def today_task(self):
        print(f'Today: {self.today.day} {self.today.strftime("%b")}')
        rows = session.query(Table).filter(Table.deadline == self.today.date()).all()
        if len(rows) <= 0:
            print("Nothing to do!")
        else:
            for i in range(len(rows)):
                print(str(i + 1) + '. ' + rows[i].task)
        print()

    def week_task(self):
        for j in range(7):
            deadline = self.today + timedelta(days=j)
            rows = session.query(Table).filter(Table.deadline == deadline.date()).all()
            count = 1
            print(datetime.strftime(deadline, '%A %d %b:'))
            if len(rows) <= 0:
                print("Nothing to do!")
            for i in range(len(rows)):
                print(str(count) + '. ' + rows[i].task)
                count += 1
            print()

    def all_task(self):
        rows = session.query(Table).order_by(asc(Table.deadline)).all()
        if len(rows) <= 0:
            print("Nothing to do!")
        else:
            print("All tasks:")
            count = 1
            for i in range(len(rows)):
                print(f'{count}. {rows[i].task}. {rows[i].deadline.strftime("%d %b")}')
                count += 1
        print()

    def add_task(self):
        self.new_task = input("Enter task\n")
        self.new_deadline = input("Enter deadline\n")
        new_row = Table(task=self.new_task, deadline=datetime.strptime(self.new_deadline, '%Y-%m-%d').date())
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
                self.week_task()
            elif user_choice == '3':
                self.all_task()
            elif user_choice == '4':
                self.add_task()
            elif user_choice == '0':
                self.exit_list()


new_list = Menu()
new_list.main_loop()
