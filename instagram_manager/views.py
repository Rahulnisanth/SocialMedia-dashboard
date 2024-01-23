from django.http import JsonResponse, HttpResponse
from django.shortcuts import redirect, render
from .serializers import FetchInstagramUserData, FetchTopFollowers
from .forms import InstagramForm
from .models import Instagram, Account, Post, TopFollowers
from apps.authentication.models import Profile


def create_instagram_user_access(request, pk=None):
    link_form = InstagramForm()

    if request.method == "POST":
        link_form = InstagramForm(request.POST)

        if link_form.is_valid():
            temp = link_form.save(commit=False)
            temp.main_user = request.user.profile

            data = FetchInstagramUserData(temp, temp)
            print("Data after: " ,data)
            if data == {"status": "BadCredentialsException"}:
                return render(
                    request,
                    "home/dashboard-instagram.html",
                    {
                        "has_instagram": False,
                        'page': 'link-instagram',
                        "form": link_form,
                        'msg':"Invalid Credentials"
                    },
                )
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
        user_top_follower = TopFollowers.objects.get(user_id=user_instagram)
        user_top_followers = user_top_follower.top_followers
        print("top_followers", user_top_followers)
        try:
            user_instagram_post = list(Post.objects.filter(user_id=user_instagram))
            print("post"    , user_instagram_post)
        except Exception as e:
            if e == "Post matching query does not exist.":
                user_instagram_post = "No posts yet"

        print(
            "Inside create_instagram_user_access",
            user_instagram,
            user_instagram_account,
            user_instagram_post,
            user_top_followers,
        )

        if user_top_followers != '':
            return render(
                request,
                "home/dashboard-instagram.html",
                {
                    "has_instagram": True,
                    "instagram":user_instagram,
                    "account": user_instagram_account,
                    "posts": user_instagram_post,
                    "top_followers": eval(user_top_followers),
                },
            )
        return render(
                request,
                "home/dashboard-instagram.html",
                {
                    "has_instagram": True,
                    "instagram":user_instagram,
                    "account": user_instagram_account,
                    "posts": user_instagram_post,
                },
            )

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
