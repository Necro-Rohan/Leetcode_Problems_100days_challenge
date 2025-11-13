import heapq
class TaskManager:

    def __init__(self, tasks: List[List[int]]):
        self.taskMemo = {}
        self.priQue = []
        heapq.heapify(self.priQue)
        for userId, taskId, priority in tasks:
            heapq.heappush(self.priQue, [-priority, -taskId, userId])
            self.taskMemo[taskId] = (userId, priority)

    def add(self, userId: int, taskId: int, priority: int) -> None:
        self.taskMemo[taskId] = (userId, priority)
        heapq.heappush(self.priQue, [-priority, -taskId, userId])

    def edit(self, taskId: int, newPriority: int) -> None:
        oldUserId = self.taskMemo[taskId][0]
        self.taskMemo[taskId] = (oldUserId, newPriority)
        heapq.heappush(self.priQue, [-newPriority, -taskId, oldUserId])

    def rmv(self, taskId: int) -> None:
        self.taskMemo.pop(taskId)

    def execTop(self) -> int:
        highestPriTaskUserId = -1
        while self.priQue:
            priority, taskId, userId = heapq.heappop(self.priQue)
            if -taskId in self.taskMemo and self.taskMemo[-taskId] == (userId, -priority):
                highestPriTaskUserId = userId
                del self.taskMemo[-taskId]
                break
        return highestPriTaskUserId


# Your TaskManager object will be instantiated and called as such:
# obj = TaskManager(tasks)
# obj.add(userId,taskId,priority)
# obj.edit(taskId,newPriority)
# obj.rmv(taskId)
# param_4 = obj.execTop()