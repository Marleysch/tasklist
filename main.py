#Marley Schneider, Rene Trujillo
#10/16/23
#Program that keeps an ordered tasklist with the ability to search by date
import check_input
import task
import tasklist as ts

def main_menu():
  # Get an integer input from the user within the specified range (1-5)
  user_input = check_input.get_int_range('\n 1. Display current task \n 2. Display all tasks\n 3. Mark current task complete\n 4. Add new task\n 5. Search by date\n 6. Save and quit\n Enter choice:', 1,5)
  print()

  return user_input

# Function to get a due date from the user
def get_date():
  print('Enter due date')
  # Get the month, day, and year as integers within specified ranges
  month_input = check_input.get_int_range('Enter month:', 1,12)
  day_input = check_input.get_int_range('Enter day:', 1,31)
  year_input = check_input.get_int_range('Enter year:', 2000,3000)

  # Format the date as 'MM/DD/YYYY' with leading zeros as needed
  if month_input < 10 and day_input < 10:
    return '0' + str(month_input) + '/' + '0'+str(day_input) + '/' + str(year_input)
  if month_input < 10:
    return '0' + str(month_input) + '/' + str(day_input) + '/' + str(year_input)
  elif day_input < 10:
    return str(month_input) + '/' + '0'+str(day_input) + '/' + str(year_input)
  else:
    return str(month_input) + '/' + str(day_input) + '/' + str(year_input)

# Function to get a time from the user
def get_time():
  print('Enter time:')
  hour = str(check_input.get_int_range('Enter hour: ', 0, 23))
  minute = str(check_input.get_int_range('Enter minute: ', 0, 59))

  # Format the time as 'HH:MM' with leading zeros as needed
  if int(hour) < 10:
    hour = '0' + hour
  if int(minute) < 10:
    minute = '0' + minute
  return (f'{hour}:{minute}')

def main():
  tasklist = ts.Tasklist()

  
  
  while True:
    # Display the tasklist statistics
    print('-Tasklist-')
    print(f"Tasks to complete: {len(tasklist)}")
    user_choice = main_menu()

    # Use a match statement to perform actions based on the user's choice
    match user_choice:
    # Display the current task (assumes there's at least one task)
      case 1:
        print(tasklist[0])

      # Display all tasks in the tasklist
      case 2:
        for tsk in tasklist:
          print(tsk)
          print()
      # Mark the current task as complete
      case 3:
        tasklist.mark_complete()
      # Get date, time, and description for a new task and add it to the tasklist
      case 4:
        date = get_date()
        print()
        time = get_time()
        desc = input('Enter task description: ')
        tasklist.add_task(desc, date, time)
      # Get date from user and use that to search through tasks for same dates
      case 5:
        date = get_date()
        print()
        for tsk in tasklist:
          if date == tsk.task_date:
            print(tsk)
        print()
        
      case 6:
        tasklist.save_file()
        break

main()