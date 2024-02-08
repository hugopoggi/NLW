from src.views.http_types.http_reponse import HttpResponse

def handle_errors(error: Exception) ->HttpResponse:
    return HttpResponse(
        status_code=500,
        body={
            "erros": [{
                "title":"Server Error",
                "detail": str(error)
            }]
        }
    )
