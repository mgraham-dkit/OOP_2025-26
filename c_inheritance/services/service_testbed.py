from services import Service
from services import DatabaseService
import random as rand

service1 = Service(1, "webserver", 13560, "always")
service2 = Service(2, "cache", 38560, "never")
db_service = DatabaseService(10, "mysql_service", 3306, "mysql", "root", "", "unless-stopped")

service_list = [service1, service2, db_service]
rand.shuffle(service_list)

for service in service_list:
    print(repr(service))


for service in service_list:
    print(hash(service))