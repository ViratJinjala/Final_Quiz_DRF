from django.http import JsonResponse
import json

class EmailDomainValidatorMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        self.trusted_domains = ["gmail.com", "microsoft.com", "outlook.com"]

    def __call__(self, request):
        print("hello from middleware")
        if request.path == "/users/register/" and request.method == "POST":
                if request.content_type == "application/json":
                    data = json.loads(request.body)
                    email = data.get("email", "")
                else:
                    email = request.POST.get("email", "")
                
                domain = email.split('@')[-1]

                if domain not in self.trusted_domains:
                    return JsonResponse({
                        "success": False,
                        "message": f"Email domain '{domain}' is not allowed."
                    }, status=403)
        return self.get_response(request)
