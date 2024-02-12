import task

class Tasklist:

  '''
  Attributes:
    tasklist - A list of Task objects
  '''

  def __init__(self):
    tasks = open('tasklist.txt','r')
    self._tasklist = []

    # Loop through each row in the file
    for row in tasks:
      # Split the row into details (description, date, time) using a comma as the separator
      details = row.strip().split(',')
      # Create a new Task object with the details and append it to the tasklist
      self._tasklist.append(task.Task(details[0], details[1], details[2]))

    self._tasklist.sort()
    tasks.close()

  def add_task(self, desc, date, time):
    # Create a new Task object with the provided description, date, and time
    self._tasklist.append(task.Task(desc, date, time))
    self._tasklist.sort()

  def mark_complete(self):
    del self._tasklist[0]

  def save_file(self):
    tasks = open('tasklist.txt', 'w')
    for row in self._tasklist:
      tasks.write(row.__repr__())
    tasks.close()

  def __getitem__(self, index):
    return self._tasklist[index]

  def __len__(self):
    return len(self._tasklist)

  def get_current_task(self):
    return self._tasklist[0]

  def __iter__(self):
    self._n = 0
    return self

  def __next__(self):
    self._n += 1
    if self._n >= len(self._tasklist):
      raise StopIteration
    else:
      return self._tasklist[self._n]
