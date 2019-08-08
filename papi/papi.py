from webob import Request, Response

from .lib.error_handler import debug_exception_handler, default_exception_handler
from .lib.exceptions import PapiRouteException
from .lib.route import Route


class Papi:
    def __init__(self, debug=False):
        self._routes = {}
        self._debug = debug
        self._exception_handler = default_exception_handler

    @property
    def debug(self):
        return self._debug

    def add_exception_handler(self, handler):
        self._exception_handler = handler

    def _handle_exception(self, request, response, exception):
        if self._debug is False:
            self._exception_handler(request, response, exception)
        else:
            debug_exception_handler(request, response, exception)

    def add_route(self, path, handler):
        if path in self._routes:
            raise PapiRouteException("Route already exists.")
        self._routes[path] = Route(path=path, handler=handler)

    def route(self, path):
        def wrapper(handler):
            self._routes[path] = Route(path=path, handler=handler)
            return handler

        return wrapper

    def _find_route(self, path):
        for pattern, route in self._routes.items():
            matched, kwargs = route.match(request_path=path)
            if matched is True:
                return route, kwargs

        return None, {}

    def get_response(self, request):
        response = Response()
        response.content_type = "application/json"

        route, kwargs = self._find_route(path=request.path)

        try:
            if not route:
                raise PapiRouteException("Route not found.")
            route.handle_request(request, response, **kwargs)
        except Exception as e:
            self._handle_exception(request, response, e)

        return response

    def __call__(self, environ, start_response):
        request = Request(environ)
        response = self.get_response(request)

        return response(environ, start_response)
