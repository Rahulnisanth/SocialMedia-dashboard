import instaloader, random
from .models import Account, Post, Instagram, TopFollowers


def printer(iterable):
    print("Next", iterable)
    try:
        for i in iterable:
            print("i", i)
    except Exception as e:
        print(e)


def FetchInstagramUserData(formData, temp):
    data = {}

    userS = formData.user_id
    l = instaloader.Instaloader()
    try:
        l.login(formData.user_id, formData.password)
        temp.save()
    except instaloader.exceptions.BadCredentialsException as e:
        return {'status' : "BadCredentialsException"}
    instagram_instance = Instagram.objects.get(user_id=formData.user_id)
    
    print("Account", l.anonymous_copy())
    _posts = instaloader.Profile.from_username(l.context, userS).get_posts()
    for i in _posts:
        new_post = Post.objects.create(user_id=instagram_instance)
        new_post.post_name = i
        new_post.post_caption = i.caption
        new_post.likes = random.randint(10, 10000)
        new_post.comments = random.randint(10, 10000)
        new_post.save()
    
    new_account = Account.objects.create(user_id=instagram_instance)
    _followers = list(instaloader.Profile.from_username(l.context, userS).get_followers())
    
    new_account.biography = instaloader.Profile.from_username(
        l.context, userS
    ).biography
    new_account.followers = len(_followers)
    
    
    new_account.followings = len(
        list(instaloader.Profile.from_username(l.context, userS).get_followees())
    )
    new_account.media_count = instaloader.Profile.from_username(
        l.context, userS
    ).mediacount
    new_account.profile_url = instaloader.Profile.from_username(
        l.context, userS
    ).profile_pic_url
    new_account.save()

    print(_followers[:5])
    if len(_followers) < 5:
        _followers = _followers
    else:
        _followers = _followers[:5]
    
    data1 = []
    new_top_followers = TopFollowers.objects.create(user_id=instagram_instance)
    for i in _followers:
        temp = {}
        temp["name"] = i.full_name
        temp["profile"] = i.get_profile_pic_url()
        temp["following"] = len(list(i.get_followees()))
        print(temp)
        data1 += [temp]

    new_top_followers.top_followers = data1
    # posts = instaloader.Profile.from_username(l.context, userS).get_tagged_posts()
    # posts = instaloader.Profile.from_username(l.context, userS).has_highlight_reels
    new_top_followers.save()
    return data


def FetchTopFollowers(user):
    data = []

    instagram_instance = Instagram.objects.get(user_id=user.user_id)
    userS = user.user_id
    # userS = "_.nxvin._08"
    l = instaloader.Instaloader()
    l.login(user.user_id, user.password)

    top_followers = instaloader.Profile.from_username(l.context, userS).get_followers()
    
    return data
