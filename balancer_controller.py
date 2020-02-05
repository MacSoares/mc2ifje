from balancer_config import CloudBalancerConfigReader

class CloudBalancerController:

    def __init__(self):
        self.servers = []
        self.cost = 0
        self.ticks = 0
        self.users = []
        self.user_on_server = { "servers_online":0 , "users_count":0}
        self.config = CloudBalancerConfigReader("input.txt")

    def get_ticks_number(self):
        total_tasks = self.config.get_tasks
        self.ticks = len(total_tasks)
        return self.ticks

    def manage_users_and_server_pill(self,user,add=False,delete=False):

        if add:
            for add in range(user):
                self.users.append(user)
        if delete:
            self.users.pop()
        
        total_users = len(self.users)
        self.user_on_server["users_count"] = total_users

        if (total_users % self.config.umax) != 0:
            self.user_on_server["servers_online"] = (total_users // self.config.umax)+1
        else:
            self.user_on_server["servers_online"] = (total_users % self.config.umax)

    
    def add_user(self, quantity):
        add = True
        delete = False
        for user in range(quantity)
            self.manage_users_pill(user,add, delete)

    def get_ticks_for_task(self):

    def alocate_user_to_server(self):

    def manage_users_on_servers(self):

    def update_cost(self):

    
    def generate_uptput(self):
        tick_count = 1
        iterable = 0
        ttask = self.config.ttask
        while tick_count != 0:
            self.add_user(self.config.tasks[iterable])
            if tick_count % ttask == 0:
                self.pop_user()
                


    def write_output_file(self):

    