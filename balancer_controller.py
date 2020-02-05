from balancer_config import CloudBalancerConfigReader

class CloudBalancerController:

    def __init__(self, file_name):
        self.cost = 0
        self.ticks = 0
        self.tick_count = 0
        self.users = []
        self.user_on_server = { "servers_online":0 , "users_count":0}
        self.config = CloudBalancerConfigReader(file_name)

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
                self.tick_count = 0
        
        total_users = len(self.users)
        self.user_on_server["users_count"] = total_users

        if (total_users % self.config.umax) != 0:
            self.user_on_server["servers_online"] = (total_users // self.config.umax)+1
        else:
            self.user_on_server["servers_online"] = (total_users % self.config.umax)

    
    def add_user(self, quantity):
        add = True
        delete = False
        for user in range(quantity):
            self.manage_users_and_server_pill(user,add, delete)

    def pop_user(self):
        self.manage_users_and_server_pill(None,False,True)

    def generate_output(self):
        self.config.problem_mounter()
        iterable = 0
        ttask = self.config.ttask
        while self.tick_count != 0:
            if iterable < len(self.config.tasks):
                self.add_user(self.config.tasks[iterable])
            if tick_count % ttask == 0:
                self.pop_user()
           
            tick_count +=1
            iterable +=1  

if __name__ == "__main__":
    balancer = CloudBalancerController("input.txt")
    balancer.generate_output()