class Task:
  '''
  Attributes:
    1. description – string description of the task.
    2. date – due date of the task. A string in the format: MM/DD/YYYY 
    3. time – time the task is due. A string in the format: HH:MM
  '''

  def __init__(self, desc, date, time):
    self._description = desc
    self._date = date
    self._time = time

  @property
  def task_date(self):
    return self._date
  
  def __str__(self):
    '''returns a string used to display the task’s information to the user.'''
    return str(self._description) + '\n' + '- Due: ' + str(self._date) + " at " + str(self._time)

  def __repr__(self):
    '''returns a string used to write the task to the file.'''
    return str(self._description) + ',' + str(self._date) + "," + str(self._time) + '\n'

  def __lt__ (self, other):
    datetimenum = int(self._date[6:] + self._date[0:2] + self._date[3:5] + self._time[:2] + self._time[3:])
    otherdatetimenum = int(other._date[6:] + other._date[0:2] + other._date[3:5] + other._time[:2] + other._time[3:])
    if datetimenum == otherdatetimenum:
      return self._description < other._description
    else:
      return datetimenum < otherdatetimenum

    '''returns true if the self task is less than the other task.'''

