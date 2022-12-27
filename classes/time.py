import datetime


class TimeComponent:
    def __init__(self):
        self._start = None
        self._end = None
        self._time = None

    def start_time_countdown(self):
        self._start = datetime.datetime.now()

    def get_start(self):
        return self._start

    def end_time_countdown(self):
        self._end = datetime.datetime.now()

    def get_end(self):
        return self._end

    def get_work_time(self):
        return self._time

    def set_work_time(self, start_countdown, end_countdown):
        if self._time is None:
            self._time = end_countdown - start_countdown
        else:
            self._time += end_countdown - start_countdown

