from django.http import JsonResponse, HttpResponse
from django.shortcuts import redirect, render
from .serializers import FetchInstagramUserData


def create_instagram_user_access(request, pk):
    if request.method == "POST":
        user_data = request.POST.get("user_data", None)

        if user_data is not None:
            serializer = FetchInstagramUserData(data={"user_data": user_data})

            return JsonResponse(
                {"success": True, "message": "User data saved successfully"}
            )

        else:
            return JsonResponse(
                {"success": False, "message": "User data not provided"}, status=400
            )

    else:
        return JsonResponse(
            {"success": False, "message": "Unsupported method"}, status=405
        )

def fetch_data_from_account():
    pass
