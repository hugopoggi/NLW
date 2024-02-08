from src.views.http_types.http_reponse import HttpResponse
from .error_types.http_unprocessable_entity import HtttpUnprocessableEntityError

def handle_errors(error: Exception) ->HttpResponse:
    if isinstance (error, HtttpUnprocessableEntityError):
        return HttpResponse(
            status_code=error.status_code,
            body={
                "errors": [{
                    "tittle": error.name,
                    "detail": error.message
                }]
            }
        )
    
    return HttpResponse(
        status_code=500,
        body={
            "erros": [{
                "title":"Server Error",
                "detail": str(error)
            }]
        }
    )
