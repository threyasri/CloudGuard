class ApplicationState:
    """Manage the current application health state."""

    def __init__(self):
        self._failed = False

    @property
    def is_failed(self):
        return self._failed

    def simulate_failure(self):
        self._failed = True

    def recover(self):
        self._failed = False


application_state = ApplicationState()
