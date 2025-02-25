class ErrorAplicacion(Exception):
    def __init__(self,campo):
        super().__init__(campo)