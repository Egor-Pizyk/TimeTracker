import datetime
import json

from tabulate import tabulate

from classes.time import TimeComponent


class TrackerComponent(TimeComponent):
    def __init__(self):
        super().__init__()
        self.pause_count = 0
        self._is_countdown_start = False
        self._is_countdown_pause = False

    def commit_work_result(self):
        self.set_work_time(self._start, self._end)
        print("-" * 25)
        print(f'You work - {self.get_work_time()}\n')

        if not self._is_countdown_start and not self._is_countdown_pause:
            with open('history.json', 'r+') as file:
                file_data = json.load(file)
                file_data['data'].append({
                    "date": str(datetime.datetime.now().strftime('%d.%m.%y')),
                    "pauses": self.pause_count,
                    "time": str(self._time)
                })
                file.seek(0)
                json.dump(file_data, file, indent=4)

    def start_work(self):
        self.start_time_countdown()
        self._is_countdown_start = True

        if self.pause_count == 0:
            print(f'You start work at - {self._start.strftime("%H:%M:%S")}\n')
        else:
            print(f'You make {self.pause_count} pause')
            print(f'You continue work at - {self._start.strftime("%H:%M:%S")}\n')

    def stop_work(self):
        if self._end is None:
            self.end_time_countdown()

        self._time = None
        self._is_countdown_start = False

        if self._is_countdown_pause is not None:
            self._is_countdown_pause = None

        self.commit_work_result()

        self._start = None
        self._end = None

    def pause_work(self):
        self._is_countdown_start = False
        self._is_countdown_pause = True
        self.pause_count += 1

        self.end_time_countdown()
        self.commit_work_result()

        self._end = None

    def continue_work(self):
        self.start_time_countdown()
        self._is_countdown_start = True
        self._is_countdown_pause = False

    def get_history(self):
        data_list = []
        pause_list = []
        time_list = []

        with open('history.json', 'r') as json_file:
            data = json.load(json_file)

            for item in data['data']:
                data_list.append(item['date'])
                pause_list.append(item['pauses'])
                time_list.append(item['time'])

            print(f'{tabulate(list(zip(data_list, pause_list, time_list)), ["Data", "Pauses", "Time"])}\n')
