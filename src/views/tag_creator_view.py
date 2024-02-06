from src.views.http_types.http_request import HttpRequest
from src.views.http_types.http_reponse import HttpResponse

class TagCreatorView:
    '''
        reponsability for interecting with HTTP
    '''

    def validate_and_create(self, http_request: HttpRequest) -> HttpResponse:
        #body = http_request.body
        #product_code = body ["product_code"]


        print('Estou na minha view')
        print(http_request)

        return HttpResponse(status_code=200, body={"hello": "World"})
    