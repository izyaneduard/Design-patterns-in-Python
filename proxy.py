# Simple demonstration of the Proxy pattern.
class Implementation:
  def f(self):
    print("Implementation.f()")
  def g(self):
    print("Implementation.g()")
  def h(self):
    print("Implementation.h()")

class Proxy:
  def __init__(self):
    self.__implementation = Implementation()
  def __getattr__(self, name):
    return getattr(self.__implementation, name)

if __name__ == '__main__':
  p = Proxy()
  p.f(); p.g(); p.h();
