from balancer_config import CloudBalancerConfigReader

class CloudBalancerController:

    def __init__(self, file_name):
        self.cost = 0
        self.ticks = 0
        self.tick_count = 1
        self.users = []
        self.user_on_server = { "servers_online":0 , "users_count":0}
        self.config = CloudBalancerConfigReader(file_name)
        self.output = open("output.txt", "w")
        self.output.close()

    def get_ticks_number(self):
        total_tasks = self.config.get_tasks()
        self.ticks = len(total_tasks)
        return self.ticks

    def manage_users_and_server_pill(self,user,add=False,delete=False):

        if add:
            for add in range(user):
                self.users.append(1)
        if delete:
            if len(self.users) != 0:
                self.users.pop()
            else:
                return False
        total_users = len(self.users)
        self.user_on_server["users_count"] = total_users

        if (total_users % self.config.umax) != 0:
            self.user_on_server["servers_online"] = int(total_users / self.config.umax)+1
        else:
            self.user_on_server["servers_online"] = int(total_users / self.config.umax)

        return True
    
    def add_user(self, quantity):
        add = True
        delete = False
        managed = True
        for user in range(quantity):
            managed = self.manage_users_and_server_pill(1,add, delete)
        return managed

    def pop_user(self):
        managed = self.manage_users_and_server_pill(None,False,True)
        return managed
    
    def manage_file(self):
        self.output = open("output.txt", "a")
        servers_range = range(self.user_on_server["servers_online"])
        servers_online = self.user_on_server["servers_online"]
        users_on_time = self.user_on_server["users_count"]
        users_not_managed = len(self.users)
        for servers in servers_range:

            if users_not_managed > 1:
                self.output.write("%s," %(self.config.umax))
                users_not_managed -= self.config.umax
            elif users_not_managed <= 1:
                self.output.write("%s," %(users_not_managed))
            
            if users_on_time == 0:
                self.output.write("0")
            
        self.output.write("\n")

    def generate_output(self):
        self.config.problem_mounter()
        iterable = 0
        ttask = self.config.ttask
        managed = True
        while self.tick_count != 0:
            if iterable < len(self.config.tasks):
                managed = self.add_user(self.config.tasks[iterable])
            
            if self.tick_count % ttask == 0:
                managed = self.pop_user()

            if managed:
                self.tick_count +=1
            else:
                self.tick_count = 0
            
            self.manage_file()
            self.output.close()
            iterable +=1  
            

if __name__ == "__main__":
    balancer = CloudBalancerController("input.txt")
    balancer.generate_output()