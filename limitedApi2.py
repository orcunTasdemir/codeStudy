from yaml import parse
from collections import defaultdict
import json
from typing import List


def parseAPIEventsFile(text_file) -> None:
    data = defaultdict()
    with open(text_file, "r") as api_txt:
        lines = api_txt.readlines()
        data['time_window'] = float(lines[0])
        data['limit'] = int(lines[1])
        data['num_of_events'] = int(lines[2])
        data['events'] = [list(int(x) if x.isdigit() else x for x in lines[line_num].strip(
            '\n').split(' ')) for line_num in range(3, data['num_of_events'] + 3)]
        users = list(set([event[2] for event in data['events']]))
        data['users'] = dict()
        for user in users:
            data['users'][user] = {'name': user,
                                   'events': [],  # [event[0:2] for event in data['events'] if event[2] == user],
                                   'limitUsed': 0}
        # with open('data.json', 'w+') as f:
        #     f.write(json.dumps(data))
    return data


data = parseAPIEventsFile('apiEvents.txt')


class Solution:

    def __init__(self, time_window: float, limit: int) -> None:

        self.time_window = data['time_window']
        self.limit = data['limit']

    def calculateLimitUsed(self, event: List, actualUsed) -> None:
        user_name = event[2]
        # append it to the events list
        data['users'][user_name]['events'].append(
            event[0:2] + [actualUsed])

        data['users'][user_name]['limitUsed'] = 0
        if data['users'][user_name]['events']:
            rev_list = list(reversed(data['users'][user_name]['events']))
            # print('rev_list: ', rev_list)
            windowStart = rev_list[0][0] - self.time_window
            # print('window starts at: ', windowStart)
            for event in rev_list:
                if(event[0] > windowStart):
                    data['users'][user_name]['limitUsed'] += event[2]

    def calculateLimitUsed2(self, event: List):
        user = event[2]
        data['users'][user]['limitUsed'] = 0
        if data['users'][user]['events']:
            rev_list = list(reversed(data['users'][user]['events']))
            # print('rev_list: ', rev_list)
            windowStart = event[0] - self.time_window
            # print('window starts at: ', windowStart)
            for event in rev_list:
                if(event[0] > windowStart):
                    data['users'][user]['limitUsed'] += event[2]

    def rate_limit(self, event: List) -> int:
        self.calculateLimitUsed2(event)

        print(data['users'])
        # print(data['users'][event[2]]['limitUsed'])
        limitWanted = event[1]
        limitUsed = data['users'][event[2]]['limitUsed']
        # if the limit used is greater than the limit return 0
        if limitUsed >= self.limit:
            return 0
        # if there is limit left, use the limit
        else:
            limitLeft = (self.limit - data['users'][event[2]]['limitUsed'])
            if limitWanted > limitLeft:
                # data['users'][event[2]]['limitUsed'] = self.limit
                self.calculateLimitUsed(event, limitLeft)
                return limitLeft
            else:
                # data['users'][event[2]]['limitUsed'] += limitWanted
                self.calculateLimitUsed(event, limitWanted)
                return limitWanted

    def runServer(self):
        results = []
        for event in data['events']:
            r = self.rate_limit(event)
            results.append(r)
        # print(data)
        return results


s = Solution(data['time_window'], data['limit'])
print(s.runServer())
