from stackprint import Stack

def Mremove_all(self, item):
    if self.isEmpty():
            print("Queue is empty! None was returned")
            return None
    else:
      val = self.items[self.front]
      self.items[self.front] = None
      if self.front != self.rear:
        if self.front == item:
          self.front = self.size - 1
        else:   
          return val

def main():
    n = 39
    s = Stack()
    s.push(1)
    s.push(4)
    s.push(5)
    a = 7
    b = 2
    print(Mremove_all(s, 4))

def Mre(a, b):
  if(a == 0 or b == 0):
    print(a - b)
    print("Banana")
  else:
    print("apple")
    return(Mre(a-1, b-1))

Mre(7, 2)