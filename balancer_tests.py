from balancer_config import CloudBalancerConfigReader
import pytest

class TestBalancerConfig:
        
    def test_set_wright_ttask(self):
        balancer_conf = CloudBalancerConfigReader("test.txt")
        tasks = 5
        balancer_conf.set_ttask(tasks)
        assert balancer_conf.ttask == tasks
    
    def test_set_wrong_from_up_ttask(self):
        balancer_conf = CloudBalancerConfigReader("test.txt")
        tasks = 15
        balancer_conf.set_ttask(tasks)
        assert balancer_conf.ttask == 0

    def test_set_wrong_from_down_ttask(self):
        balancer_conf = CloudBalancerConfigReader("test.txt")
        tasks = -1
        balancer_conf.set_ttask(tasks)
        assert balancer_conf.ttask == 0

    def test_set_wright_umax(self):
        balancer_conf = CloudBalancerConfigReader("test.txt")
        users = 8
        balancer_conf.set_umax(users)
        assert balancer_conf.umax == users
    
    def test_set_wrong_from_up_umax(self):
        balancer_conf = CloudBalancerConfigReader("test.txt")
        users = 11
        balancer_conf.set_umax(users)
        assert balancer_conf.umax == 0

    def test_set_wrong_from_down_umax(self):
        balancer_conf = CloudBalancerConfigReader("test.txt")
        users = 0
        balancer_conf.set_umax(users)
        assert balancer_conf.umax == 0

    def test_problem_mounter_ok(self):
        balancer_conf = CloudBalancerConfigReader("test.txt")
        balancer_conf.problem_mounter()
        assert balancer_conf.ttask == 4
        assert balancer_conf.umax == 2
        assert balancer_conf.tasks is not None
