from mitmproxy import http

def response(flow: http.HTTPFlow) -> None:
    flow.response.content = flow.response.content.decode().replace("Login real website", "Login fake").encode()