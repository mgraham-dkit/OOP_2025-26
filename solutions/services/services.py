from __future__ import annotations
from _datetime import datetime

class Service:
    _RESTART_OPTIONS = ["never", "always", "unless-stopped"]

    def __init__(self, service_id: int, name: str, port: int, restart_mode: str = "never"):
        self.service_id = service_id
        self.name = name

        # Port number validation
        if port < 0 or port > 65535:
            print(f"Illegal port value. {port} is not within range of legal ports. Defaulting to 13000")
            port = 13000


        self._port = port

        # Validate restart mode
        if not Service.validate_mode(restart_mode):
            print(f"Illegal restart mode. {restart_mode} was not found in list of valid mode options. Defaulting to \"never\"")
            restart_mode = "never"
        self._restart_mode = restart_mode

        self._is_active = False
        self._last_startup = None


    def launch(self) -> None:
        """Starts the service.

        This method sets the _is_active status to True and resets _last_startup to now.

        """
        self._is_active = True
        self._last_startup = datetime.now()


    def stop(self) -> str:
        if not self._is_active:
            return "Service is not active."

        self._is_active = False

        if self._restart_mode == "always":
            self.launch()
            return "Service restart mode = \"always\". Service reactived."

        return "Service deactivated"

    def move(self, new_port: int) -> bool:
        if new_port < 0 or new_port > 65535:
            return False

        self._port = new_port
        return True

    def get_port(self) -> int:
        return self._port

    def get_mode(self) -> str:
        return self._restart_mode

    def get_status(self) -> bool:
        return self._is_active

    def get_startup_time(self) -> datetime:
        return self._last_startup

    def __str__(self) -> str:
        if self._is_active:
            active_msg = "ACTIVE"
        else:
            active_msg = "DEACTIVATED"
        return f"Service {self.service_id}: {self.name} is running on {self._port}. Status: {active_msg}"

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}[service_id={self.service_id}, name={self.name}, _port={self._port}, _restart_mode={self._restart_mode}, _is_active={self._is_active},_last_startup={self._last_startup}]"

    def __eq__(self, other: Service) -> bool:
        if not isinstance(other, Service):
            return False

        return self.service_id == other.service_id

    def __ne__(self, other: Service) -> bool:
        if not isinstance(other, Service):
            return True

        return self.service_id != other.service_id
        # Alternative:
    #   return not self == other

    @staticmethod
    def validate_mode(restart_mode: str) -> bool:
        if restart_mode.lower() in Service._RESTART_OPTIONS:
            return True

        return False