import json

def RequestMiddleware (get_response):
  def middleware (request):
    try: 
      if request.body:
        body = request.body
        request._body = json.loads(body)
    except:
      request._body = request.body

    return get_response(request)
  
  return middleware