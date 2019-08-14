from locust import HttpLocust, TaskSet, task
import numpy as np


class MyTaskSet(TaskSet):
    @task
    def predict(self):
        payload = {'X': np.random.randn(2, 13).tolist()}
        self.client.post('/predict', json=payload)


class MyLocust(HttpLocust):
    task_set = MyTaskSet
    min_wait = 50
    max_wait = 200
