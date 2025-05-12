from django.http import JsonResponse
import json

class EmailDomainValidatorMiddleware:
    """
    Middleware to validate email domain during user registration.

    This middleware checks if the email address provided during a POST request to the `/register/`
    endpoint belongs to a trusted domain. If not, it blocks the request with a 403 response.

    Trusted domains include:
        - gmail.com
        - microsoft.com
        - outlook.com

    Methods:
        __init__(get_response): Initializes the middleware with the next layer in the stack.
        __call__(request): Intercepts the request and validates the email domain if applicable.
    """
    
    def __init__(self, get_response):
        """
        Initialize the middleware with the next callable in the chain and define trusted domains.
        """
        self.get_response = get_response
        self.trusted_domains = ["gmail.com", "microsoft.com", "outlook.com"]

    def __call__(self, request):
        """
        Process the incoming request.

        If the request is a POST to '/register/' and contains an email not in the list of trusted domains,
        it returns a 403 Forbidden response. Otherwise, it forwards the request to the next middleware/view.
        """
        if request.path == "/register/" and request.method == "POST":
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