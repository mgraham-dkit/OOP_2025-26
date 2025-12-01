from services import Service


def get_active_services(service_dict):
    live_services = []
    for service in service_dict.values():
        if service.get_status():
            live_services.append(service)

    return live_services

def create_service(service_dict: dict[int, Service]) -> Service:
    print("Enter the following service information:")

    # Get service id (make sure it is not already in use)
    valid_id = False
    while not valid_id:
        new_service_id = int(input("Service id: "))
        if service_dict.get(new_service_id) is not None:
            print("Service id in use. Please try again.")
        else:
            valid_id = True

    # Get name of new service
    new_service_name = input("Name of service: ")
    # Get port for new service
    new_port = int(input("Port to run on: "))
    # Inform user about what options they have for restart mode

    # Get restart mode setting (make sure it is valid by using the Service class method to validate it)
    valid_mode = False
    while not valid_mode:
        print("Restart mode - options include: \"always\", \"never\" or \"unless-stopped\"")
        new_restart_mode = input("Restart mode for service: ")
        if not Service.validate_mode(new_restart_mode):
            print("Please enter a valid restart mode option")
        else:
            valid_mode = True

    # Create service using entered components
    new_service = Service(new_service_id, new_service_name, new_port, new_restart_mode)
    # Return new service for use in main program
    return new_service


def display_menu():
    print("Please select one of the following options:")
    print("0) Exit")
    print("1) Display service details")
    print("2) Display all active services")
    print("3) Add a service")
    print("4) Start a service")


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
            case "3":
                added_service = create_service(services)
                # Add service to dictionary
                services[added_service.service_id] = added_service
            case "4":
                # Ask the user for the service to be started
                service_id = int(input("Enter service id:\n"))
                # Find it in the dictionary
                required_service = services.get(service_id)
                # If there was one with the supplied id
                if required_service is not None:
                    # Start it
                    required_service.launch()
                    print(f"Service {required_service.service_id} started")
                else:
                    # Otherwise inform the user there was no service under that id
                    print("No service matching supplied id")
            case _:
                print("Please choose one a valid option.")


    print("Program terminating...")