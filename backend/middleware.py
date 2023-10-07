import json

def RequestMiddleware (get_response):
  def middleware (request):
    if request.body:
      request._body = json.loads(request.body)

    return get_response(request)
  
  return middleware