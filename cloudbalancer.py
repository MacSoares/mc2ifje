class CloudBalancer:
    def __init__(self, file_name):
        self.input_txt = open(file_name, 'r')
        self.ttask = 0
        self.umax = 0
        self.tasks = []
        self.cost = 0
    
    def problem_mounter(self):
        line_counter = 0
        for line in self.input_txt:
            line_counter += 1
            if line_counter == 1:
                self.ttask = line
            elif line_counter == 2:
                self.umax = line
            else :
                value = line.split("\n")
                self.tasks.append(value[0])

    def get_ttask(self):
        return self.ttask

    def get_umax(self):
        return self.umax

    def get_tasks(self):
        return self.tasks
    
if __name__ == "__main__":
    balancer = CloudBalancer("input.txt")
    
    balancer.problem_mounter()

    print("Ttask :")
    print(balancer.get_ttask())
    print("Umax :")
    print(balancer.get_umax())
    print("Tasks :")
    print(balancer.get_tasks())


