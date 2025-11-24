from services import Service


def get_active_services(service_dict):
    live_services = []
    for service in service_dict.values():
        if service.get_status():
            live_services.append(service)

    return live_services


def display_menu():
    print("Please select one of the following options:")
    print("0) Exit")
    print("1) Display service details")
    print("2) Display all active services")
    print("3) Add a service")


if __name__ == "__main__":
    service1 = Service(1, "cache", 26138, "never")
    service2 = Service(2, "mysql", 3306, "unless-stopped")
    service3 = Service(3, "apache", 8080, "always")
    services = {
        service1.service_id : service1,
        service2.service_id : service2,
        service3.service_id : service3
    }

    keep_running = True

    while keep_running:
        display_menu()
        choice = input()

        match(choice):
            case "0":
                keep_running = False
            case "1":
                service_id = int(input("Enter service id:\n"))
                required_service = services.get(service_id)
                if required_service is not None:
                    print(required_service)
                else:
                    print("No service matching supplied id")
            case "2":
                active_services = get_active_services(services)
                if active_services:
                    for service in active_services:
                        print(f"{service.service_id}: {service.name}")
                else:
                    print("No services are currently active.")
            case _:
                print("Please choose one a valid option.")


    print("Program terminating...")