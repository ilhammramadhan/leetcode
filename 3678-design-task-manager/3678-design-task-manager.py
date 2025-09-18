class TaskManager:
    """
    Manages tasks using a max-heap for efficient execution of the top-priority task
    and a hash map for quick lookups to handle edits and removals.
    """

    def __init__(self, tasks: List[List[int]]):
        """
        Initializes the TaskManager with a list of tasks.
        
        Args:
            tasks: A list of [userId, taskId, priority] triples.
        """
        # A dictionary to store the current priority of each taskId. 
        # This helps in quickly checking if a task is valid and getting its current priority.
        self.task_map = {}
        
        # A min-heap to simulate a max-heap.
        # Elements are tuples of (-priority, -taskId, userId).
        # We negate the values to make heapq's min-heap act like a max-heap,
        # where the highest priority and taskId are at the top.
        self.max_heap = []

        for userId, taskId, priority in tasks:
            self.task_map[taskId] = (userId, priority)
            heapq.heappush(self.max_heap, (-priority, -taskId, userId))

    def add(self, userId: int, taskId: int, priority: int) -> None:
        """
        Adds a new task to the system.
        
        Args:
            userId: The ID of the user.
            taskId: The ID of the task.
            priority: The priority of the task.
        """
        self.task_map[taskId] = (userId, priority)
        heapq.heappush(self.max_heap, (-priority, -taskId, userId))

    def edit(self, taskId: int, newPriority: int) -> None:
        """
        Updates the priority of an existing task.
        
        Args:
            taskId: The ID of the task to edit.
            newPriority: The new priority for the task.
        """
        userId, _ = self.task_map[taskId]
        # Update the priority in the hash map.
        self.task_map[taskId] = (userId, newPriority)
        # Add a new entry to the heap. The old entry will be handled lazily.
        heapq.heappush(self.max_heap, (-newPriority, -taskId, userId))

    def rmv(self, taskId: int) -> None:
        """
        Removes a task from the system.
        
        Args:
            taskId: The ID of the task to remove.
        """
        # Simply remove the task from the hash map.
        # The corresponding entry in the heap will be ignored later.
        if taskId in self.task_map:
            del self.task_map[taskId]

    def execTop(self) -> int:
        """
        Executes the task with the highest priority.
        
        Returns:
            The userId of the executed task, or -1 if no tasks are available.
        """
        # Keep popping from the heap until a valid task is found.
        while self.max_heap:
            neg_priority, neg_taskId, userId = heapq.heappop(self.max_heap)
            current_priority = -neg_priority
            current_taskId = -neg_taskId
            
            # Check if the task is still valid and has the correct priority.
            if current_taskId in self.task_map:
                stored_userId, stored_priority = self.task_map[current_taskId]
                
                # Check for validity: the popped priority must match the stored priority.
                # This check handles the "stale" entries from the edit operation.
                if current_priority == stored_priority:
                    # Found the top-priority task.
                    del self.task_map[current_taskId]
                    return stored_userId

        # If the heap becomes empty, no valid tasks are left.
        return -1