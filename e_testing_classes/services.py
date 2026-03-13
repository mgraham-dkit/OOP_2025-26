from __future__ import annotations
from _datetime import datetime
from types import NotImplementedType
import logging

logger = logging.getLogger(__name__)


class Service:
    _RESTART_OPTIONS = ["never", "always", "unless-stopped"]

    def __init__(self, service_id: int, name: str, port: int, restart_mode: str = "never"):
        self.service_id = service_id
        self.name = name

        # Port number validation
        if not Service.validate_port(port):
            raise ValueError(f"Invalid port. Port (specified as {port}) must be within range 0-65535")

        self._port = port

        # Validate restart mode
        if not Service.validate_mode(restart_mode):
            logger.warning(f"Illegal restart mode. {restart_mode} was not found in list of valid mode options. Defaulting to \"never\"")
            restart_mode = "never"

        self._restart_mode = restart_mode

        self._is_active = False
        self._last_startup = None

    @staticmethod
    def validate_port(port: int) -> bool:
        if port is None or not isinstance(port, int):
            logger.warning("Attempt to validate None/non-numeric as a port")
            raise ValueError("Port must be a specified integer value")

        if port < 0 or port > 65535:
            return False

        return True

    def launch(self) -> None:
        """Starts the service.

        This method sets the _is_active status to True and resets _last_startup to now.

        """
        self._is_active = True
        self._last_startup = datetime.now()


    def stop(self) -> str:
        if not self._is_active:
            logger.warning(f"Attempt to stop a non-active service ({self.service_id}:{self.name} on {self._port})")
            return "Service is not active."

        self._is_active = False
        logger.info(f"{self.service_id}:{self.name} was stopped.")

        if self._restart_mode == "always":
            logger.info(f"{self.service_id}:{self.name} auto-restarted on {self._port})")
            self.launch()
            return "Service restart mode = \"always\". Service reactivated."

        return "Service deactivated"

    def move(self, new_port: int) -> bool:
        """Changes the port associated with this Service if it's within the valid range of ports (0-65535).

        Args:
            new_port (int): The port to move this Service to (must be >= 0 and <= 65535)

        Returns:
            True if the port could be moved, False otherwise
        """
        if not Service.validate_port(new_port):
            logger.warning(f"Attempt to move {self.service_id}:{self.name} to invalid port")
            return False

        self._port = new_port
        logger.info(f"{self.service_id}:{self.name} now assigned to port {self._port}")
        return True

    def get_port(self) -> int:
        return self._port

    def get_mode(self) -> str:
        return self._restart_mode

    def get_status(self) -> bool:
        return self._is_active

    def get_startup_time(self) -> datetime | None:
        return self._last_startup

    def __str__(self) -> str:
        if self._is_active:
            active_msg = "ACTIVE"
        else:
            active_msg = "DEACTIVATED"
        return f"Service {self.service_id}: {self.name} is running on {self._port}. Status: {active_msg}"

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}[service_id={self.service_id}, name={self.name}, _port={self._port}, _restart_mode={self._restart_mode}, _is_active={self._is_active},_last_startup={self._last_startup}]"

    def __eq__(self, other: object) -> bool | NotImplementedType:
        """ Compares two Service objects (this Service and a supplied parameter)

        Compares the service_id in both objects
        Args:
            other (object): The other Service object to check against

        Returns:
             NotImplemented if other is not a Service;
             True if other's service_id equals this service_id; False if the service_ids differ.
        """
        if not isinstance(other, Service):
            return NotImplemented

        return self.service_id == other.service_id

    def __ne__(self, other: Service) -> bool | NotImplementedType:
        if not isinstance(other, Service):
            return NotImplemented

        return not self == other

    def __hash__(self):
        return hash(self.service_id)

    def __format__(self, format_spec: str) -> str:
        match format_spec.lower():
            case "short":
                return f"Service {self.service_id} : {self.name} on {self._port}"
            case "full":
                return f"Service {self.service_id} : {self.name} on {self._port}\n Mode: {self._restart_mode} - Status: {self._is_active}"
            case _:
                print("Invalid option selected")
                return repr(self)

    @staticmethod
    def validate_mode(restart_mode: str) -> bool:
        if restart_mode.lower() in Service._RESTART_OPTIONS:
            return True

        return False


class DatabaseService(Service):
    def __init__(self, service_id: int, name: str, port: int, database_type:str, username:str, password:str, restart_mode: str = "never"):
        # Set up super class component
        super().__init__(service_id, name, port, restart_mode)

        # Store database service-specific information
        self.database_type = database_type
        self.username = username
        self._password = password

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}[service_id={self.service_id}, name={self.name}, _port={self._port}, _restart_mode={self._restart_mode}, _is_active={self._is_active},_last_startup={self._last_startup}, database_type={self.database_type}, username={self.username}, _password=********]"
