from services import Service
from services import DatabaseService
import random as rand

service1 = Service(1, "webserver", 13560, "always")
service2 = Service(2, "tomcat", 8080, "unless-stopped")
db_service = DatabaseService(10, "mysql_service", 3306, "mysql", "root", "", "unless-stopped")
service3 = Service(3, "cache", 38560, "never")

service_list = [service1, service2, db_service, service3]
rand.shuffle(service_list)

for service in service_list:
    print(repr(service))

for service in service_list:
    print(service)

# Attempt to move service2 to an invalid port
service2.move(100000)

# Attempt to start service3 (a service that is not currently active)
service3.stop()