class CloudBalancerConfigReader:
    def __init__(self, file_name):
        self.input_txt = open(file_name, 'r')
        self.ttask = 0
        self.umax = 0
        self.tasks = []
        self.cost = 0
        self.global_low_limit = 1
        self.global_high_limit = 10
    
    def problem_mounter(self):
        line_counter = 0
        for line in self.input_txt:
            line_counter += 1
            value = line.split("\n")
            line_value = int(value[0])
            if line_counter == 1:
                self.set_ttask(line_value)
            elif line_counter == 2:
                self.set_umax(line_value)
            else :
                self.tasks.append(line_value)

    def set_ttask(self, task_ticks):
        if self.global_low_limit <= task_ticks <= self.global_high_limit:
            self.ttask = task_ticks
        else:
            return 0

    def set_umax(self, max_users):
        if self.global_low_limit <= max_users <= self.global_high_limit:
            self.umax = max_users
        else:
            raise ValueError()

    def get_ttask(self):
        return self.ttask

    def get_umax(self):
        return self.umax

    def get_tasks(self):
        return self.tasks
