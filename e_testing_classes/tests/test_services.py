import pytest

from e_testing_classes.services import Service

# Create fixtures to generate different versions of Service object
@pytest.fixture
def service():
    return Service(1, "webserver", 13560, "never")

# Test move method of Service class
# Valid actions
def test_move(service):
    new_port = 17000
    move_status = service.move(new_port)

    assert move_status is True
    assert service.get_port() == new_port

def test_move_valid_lower_bound(service):
    new_port = 0
    move_status = service.move(new_port)

    assert move_status is True
    assert service.get_port() == new_port

def test_move_valid_upper_bound(service):
    new_port = 65535
    move_status = service.move(new_port)

    assert move_status is True
    assert service.get_port() == new_port

# The above two valid action tests could be replaced with a single parameterised test
@pytest.mark.parametrize("valid_port, expected", [
    (0, True),
    (18000, True),
    (65535, True)
])
def test_move_valid(service, valid_port, expected):
    move_status = service.move(valid_port)

    assert move_status is expected
    assert service.get_port() == valid_port

# Invalid actions
def test_move_port_too_high(service):
    new_port = 170000
    original_port = service.get_port()
    move_status = service.move(new_port)

    assert move_status is False
    assert service.get_port() == original_port

def test_move_port_too_low(service):
    new_port = -1
    original_port = service.get_port()
    move_status = service.move(new_port)

    assert move_status is False
    assert service.get_port() == original_port

# The above two invalid action tests could be replaced with a single parameterised test
@pytest.mark.parametrize("invalid_port, expected", [
    (170000, False),
    (-1, False)
])
def test_move_invalid(service, invalid_port, expected):
    original_port = service.get_port()
    move_status = service.move(invalid_port)

    assert move_status is expected
    assert service.get_port() == original_port

# Exception-based testing
# Test constructor creating Service object - only valid data supplied
def test_create_service():
    service_id = 1
    port = 17000
    name = "test service"
    restart_mode = "never"
    service = Service(service_id=service_id, port=port, name=name, restart_mode=restart_mode)

    # Confirm all values have been set correctly
    assert service.service_id == service_id
    assert service.get_port() == port
    assert service.name == name
    assert service.get_mode() == restart_mode
    assert service.get_startup_time() is None
    assert service.get_status() is False


# Test constructor creating Service object - invalid data supplied that will trigger an exception
def test_create_service_invalid_port():
    id = 1
    port = -1
    name = "test service"
    restart_mode = "never"

    with pytest.raises(ValueError, match="Invalid port"):
        service = Service(service_id=id, port=port, name=name, restart_mode=restart_mode)
