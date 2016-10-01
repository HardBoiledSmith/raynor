from channels import route
from dashboard.consumers import connect_log_stream, disconnect_log_stream


channel_routing = [
    route("websocket.connect", connect_log_stream, path=r'^/dashboard/stream/$'),
    route("websocket.disconnect", disconnect_log_stream, path=r'^/dashboard/stream/$'),
]