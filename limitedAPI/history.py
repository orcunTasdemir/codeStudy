from dataclasses import dataclass

@dataclass
class Record:
  timestamp: int
  count: int
  
class History():
    def __init__(self):
        self.state = dict()
        
    def getOperationsCount(self, consumer:str, after:int, length:int):
        
        records = filter(
            lambda x: x.timestamp >= after and x.timestamp <= after+length,
            self.state.get(consumer, []) 
        )
        return sum([record.count for record in records])
    
    def addOperations(self, count:int, consumer:str, timestamp:int):
        prev = self.state.get(consumer, [])
        self.state[consumer] = prev + [Record(timestamp, count)] 
        