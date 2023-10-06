
# MULTIPLE HERITAGE

"""
Beginning: 4 levels of heritage

"""


class Worker:

    def work(self):
        print("working")


class FrontEnd(Worker):

    def work(self):
        print("FrontEnd")


class BackEnd(Worker):

    def work(self):
        print("BackEnd")


class FullStack(FrontEnd, BackEnd):

    pass


ana = FullStack()
ana.work()

# With conflict, Python uses MRO algorithm
# that chose the first class function, like in
# the previous code
