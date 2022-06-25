

from yaml import parse


def parseAPIEventsFile(text_file) -> None:
    data = []
    with open(text_file, "r") as api_txt:
        lines = api_txt.readlines()
        data['time_window'] = float(lines[0])
        data['limit'] = int(lines[1])
        data['num_of_events'] = int(lines[2]) 
        data['events'] = [list(int(x) if x.isdigit() else x for x in lines[line_num].strip(
            '\n').split(' '))  for line_num in range(3, data['num_of_events'] + 3)]
        
    for event in data['events']:
        data[event[2]] = {'limitLeft': self.limit}
    return data


print(parseAPIEventsFile('apiEvents.txt'))


# class Solution:
    
#     def __init__(self) -> None:
#         self.server = dict()
#         self.parseAPIEventsFile('apiEvents.txt')
#         self.time_window = self.server['time_window']
#         self.limit = self.server['limit']
#         self.events = self.server['events']
#         self.users = set([[x[2], self.limit] for x in self.server['events']])
        
#     def rate_limit(self, event: List ) -> int:
#         # if the event list is only 3 units long I want to add the first timestamp to it
#         # to keep track of the window and also start the credit they have
#         if len(event) == 3:
#             event.append(event[0])
#             event.append(self.limit)
#         # if it is already 4 item check if the timewindow is passed, if  so,  add same credit back again
        
#         if(event[0] - event[3] > self.time_window):
#             event[4] = self.limit
#         # after these allocations of credit we can check operations 
#         # if the operations are less than the credit
#         if event[1] < event[4]:
#             event[4] -= event[1]
#             return event[1]
        
#         alll = event[4]
#         event[4] = 0
#         return alll
    
#     def runServer(self):
#         results = []
#         for event in self.events:
#             r = self.rate_limit(event)
#             results.append(r)
#         return results


# # user_input = input("Give the API events input: ");

# s = Solution()
# print(s.runServer())