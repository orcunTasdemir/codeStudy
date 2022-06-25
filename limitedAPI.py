from typing import List
class Solution:  
    def __init__(self) -> None:
        self.server = dict()
        self.users = dict()
        self.parseAPIEventsFile('apiEvents.txt')
        self.time_window = self.server['time_window']
        self.limit = self.server['limit']
        self.events = self.server['events']
          
    def rate_limit(self, event: List ) -> int:
        if event[2] not in self.users.keys():
            self.users[event[2]] = dict()
            self.users[event[2]]['limit'] = self.limit
            self.users[event[2]]['windowStart'] = event[0]
        
        if(event[0] - self.users[event[2]]['windowStart'] > self.time_window):
            self.users[event[2]]['limit']  = self.limit
        if event[1] < self.users[event[2]]['limit'] :
            self.users[event[2]]['limit']  -= event[1]
            # set next window
            self.users[event[2]]['windowStart'] = event[0]
            return event[1]
        alll = self.users[event[2]]['limit'] 
        self.users[event[2]]['limit']  = 0
        # set next window
        self.users[event[2]]['windowStart'] = event[0]
        return alll
    
    def runServer(self):
        results = []
        for event in self.events:
            r = self.rate_limit(event)
            results.append(r)
        return results

    def parseAPIEventsFile(self, text_file) -> None:
        with open(text_file, "r") as api_txt:
            lines = api_txt.readlines()
            self.server['time_window'] = float(lines[0])
            self.server['limit'] = int(lines[1])
            self.server['num_of_events'] = int(lines[2]) 
            self.server['events'] = [list(int(x) if x.isdigit() else x for x in lines[line_num].strip(
                '\n').split(' '))  for line_num in range(3, self.server['num_of_events'] + 3)]

# user_input = input("Give the API events input: ");

s = Solution()
print(s.runServer())