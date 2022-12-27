import time
found = ""
def add(x, y):
  return x + y
def subtract(x, y):
  return x - y
def multiply(x, y):
  return x * y
def divide(x, y):
  return x / y
def getStringEquation(x, oper, y):
  return str(x) + {add : " + ", subtract : " - ", multiply : " * ", divide : " / "}[oper] + str(y) + " = " + str(oper(x, y))

branches = []
answerBranches = []
goal = 0
end = 0
operations = [add, subtract, multiply, divide]
tries = 0
limit = 3
            
class Branch:
  def __init__(self, selection, equations = "", step = 1):
    self.branches = []
    self.selection = selection
    self.equations = equations
    self.step = step

  def generate(self):
    global answerBranches
    global goal
    global tries
    global found
    global end
    if goal in self.selection:
      end = time.time()
      answerBranches.append(self)
      found = self.equations
      return
    if self.step > limit:
      return
    for val1 in range(len(self.selection)):
      if type(self.selection[val1]) == float:
        continue
      for val2 in range(len(self.selection)):
        if found:
            return
        if val2 == val1:
          continue
        value1 = self.selection[val1]
        value2 = self.selection[val2]
        if type(value2) == float:
          continue
        for operation in operations:
          if operation(value1, value2) <= 0 or type(operation(value1, value2)) != int:
            continue
          try:
            copy = self.selection[:]
            del copy[val1]
            if val2 > val1:
                del copy[val2 - 1]
            else:
                del copy[val2]
            branch = Branch(copy+[operation(value1, value2)], equations = self.equations+"\n"+getStringEquation(value1, operation, value2), step = self.step + 1)
            tries+=1
            branch.generate()
          except Exception as e:
            print(str(e))

selection = input("Options, seperated by commas (e.g. 1,2,3): ")
selection = selection.split(",")
for s in range(len(selection)):
	selection[s] = int(selection[s])
	
goal = int(input("Goal: "))

start = time.time()
while not found:
  startBranch = Branch(selection)
  startBranch.generate()
  limit += 1

print(found)
print("That took", (end-start)*1000, "milliseconds.")
