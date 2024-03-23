import datetime
from application.salary import calculate_salary
from application.db.people import get_employees

def main():
    current_date = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print(f'Текущая дата: {current_date}')
    calculate_salary()
    get_employees()

if __name__ == '__main__':
    main()
