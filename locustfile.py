from locust import HttpUser, task, between

class MyUser(HttpUser):
    wait_time = between(5, 15)

    @task
    def my_task(self):
        self.client.get("/path/to/your/endpoint")