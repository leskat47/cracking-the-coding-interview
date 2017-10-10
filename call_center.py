class Queue(object):

    def __init__(self):
        self.queue = []

    def enqueue(self, emp):
        self.queue.append(emp)
        print emp, " has been added"

    def dequeue(self):
        if self.queue:
            return self.queue.pop(0)
        else:
            return None


class Employee(object):

    def __init__(self, name):
        self.name = name
        self.respondent_queue.enqueue(self)

    def receive_call(self, call):
        self.call = call

    def complete_call(self):
        self.call = None
        self.respondent_queue.enqueue(self)

    def escalate(self):
        self.call.rank += 1
        dispatch_call(self.call, self.call.rank)

    @classmethod
    def find_respondent(cls):
        return cls.respondent_queue.dequeue()


class Respondent(Employee):

    respondent_queue = Queue()


class Manager(Employee):

    respondent_queue = Queue()


class Director(Employee):

    respondent_queue = Queue()


class Call(object):

    call_queue = Queue()

    def __init__(self, caller, rank=1):
        self.rank = rank
        self.caller = caller
        dispatch_call(self, rank)

    def set_handler(self, handler):
        self.handler = handler

    def add_to_queue(self):
        self.call_queue.enqueue(self)


def dispatch_call(call, rank=1):

    if rank == 1:
        next_staff = Respondent.find_respondent()

    if rank == 2 or not next_staff:
        next_staff = Manager.find_respondent()

    if rank == 3 or not next_staff:
        next_staff = Director.find_respondent()

    if not next_staff:
        print "Please wait"
        call.add_to_queue()
        return

    next_staff.receive_call(call)
    call.set_handler(next_staff)

a = Respondent("abigail")
b = Manager("betty")
c = Director("carlie")
Call("joe")
