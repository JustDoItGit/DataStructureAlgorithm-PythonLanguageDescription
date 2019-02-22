from random import randint
from stack_prio_que import PrioQueue
from sQueue import SQueue


class Simulation:
    def __init__(self, duration):
        self._eventq = PrioQueue()
        self._time = 0
        self._duration = duration

    def run(self):
        while not self._eventq.is_empty():  # 模拟到事件队列空
            event = self._eventq.dequeue()
            self._time = event.time()  # 事件的时间就是当前时间
            if self._time > self._duration:  # 时间用完就结束
                break
            event.run()  # 模拟这个事件，其运行可能生成新事件

    def add_event(self, event):
        self._eventq.enqueue(event)

    def cur_time(self):
        return self._time


class Event:
    def __init__(self, event_time, host):
        self._ctime = event_time
        self._host = host

    def __lt__(self, other_event):
        return self._ctime < other_event._ctime

    def __le__(self, other_event):
        return self._ctime > other_event._ctime

    def host(self):
        return self._host

    def time(self):
        return self._ctime

    def run(self):  # 具体事件类必须定义这个方法
        pass
