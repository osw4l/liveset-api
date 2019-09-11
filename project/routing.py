from channels import route

channel_routing = [
	#route("websocket.connect", consumers.connect_model, path=r'^/ws/feed/model/'),
    #route("websocket.disconnect", consumers.disconnect_model, path=r'^/ws/feed/model/'),
]
