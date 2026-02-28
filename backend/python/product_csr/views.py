import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from product_csr.services.product_service import ProductService

service = ProductService()

@csrf_exempt
def products(request):

    if request.method == "GET":
        return JsonResponse(
            {"products": service.get_all_products()},
            safe=False
        )

    if request.method == "POST":
        try:
            data = json.loads(request.body)
            product = service.create_product(data)
            return JsonResponse(product, status=201)
        except ValueError as e:
            return JsonResponse({"error": str(e)}, status=400)

    return JsonResponse({"error": "Method not allowed"}, status=405)