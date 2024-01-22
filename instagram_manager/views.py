from django.http import JsonResponse, HttpResponse
from django.shortcuts import redirect, render
from .serializers import FetchInstagramUserData, FetchTopFollowers
from .forms import InstagramForm
from .models import Instagram, Account, Post
from apps.authentication.models import Profile


def create_instagram_user_access(request, pk=None):
    if request.method == "POST":
        link_form = InstagramForm(request.POST)

        if link_form.is_valid():
            temp = link_form.save(commit=False)
            temp.main_user = request.user.profile
            temp.save()

            data = FetchInstagramUserData(temp)
            print(data)

            return redirect(
                "home/dashboard-instagram.html",
                {"has_instagram": True},
            )

        else:
            return JsonResponse(
                {"success": False, "message": "User data not provided"}, status=400
            )

    user_profile = Profile.objects.get(user=request.user)
    user_instagram = Instagram.objects.filter(main_user=user_profile)
    user_instagram_post = "No posts yet"
    user_instagram_account = ""
    if list(user_instagram) != []:
        user_instagram = Instagram.objects.get(main_user=user_profile)
        user_instagram_account = Account.objects.get(user_id=user_instagram)
        try:
            user_instagram_post = Post.objects.get(user_id=user_instagram)
        except Exception as e:
            if e == "Post matching query does not exist.":
                user_instagram_post = "No posts yet"

        # top_followers = FetchTopFollowers(user_instagram)
        top_followers = None
        print(
            "Inside create_instagram_user_access",
            user_instagram,
            user_instagram_account,
            user_instagram_post,
            top_followers,
        )

        return render(
            request,
            "home/dashboard-instagram.html",
            {
                "has_instagram": True,
                "account": user_instagram_account,
                "posts": user_instagram_post,
                "top_followers": top_followers,
            },
        )

    link_form = InstagramForm()
    return render(
        request,
        "home/dashboard-instagram.html",
        {
            "page": "link-instagram",
            "form": link_form,
        },
    )


def fetch_data_from_account():
    pass
