from channels import route

from apps.app.consumers import connect_videos_streaming, receive_videos_streaming, disconnect_videos_streaming

channel_routing = [
    route("websocket.connect", connect_videos_streaming, path=r'^/ws/videos/'),
    route("websocket.receive", receive_videos_streaming, path=r'^/ws/videos/'),
    route("websocket.disconnect", disconnect_videos_streaming, path=r'^/ws/videos/'),
]
