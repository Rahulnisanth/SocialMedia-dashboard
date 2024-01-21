import instaloader

username = 'teamvoltanalysis'
password = "TeamVoltAnalysis@user"
# userS = '_.nxvin._08'
# userS = 'mattimadhan'
userS = 'madhus1862'


l = instaloader.Instaloader()

l.login(username, password)

def printer(iterable):
    print("Next", iterable)
    try:
        for i in iterable:
            print("i", i)
    except Exception as e:
        print(e)

# print("l", l)
# posts = instaloader.Profile.from_username(l.context, userS).get_igtv_posts()
# printer(posts)
# posts = instaloader.Profile.from_username(l.context, userS).get_followed_hashtags()
# printer(posts)
posts = instaloader.Profile.from_username(l.context, userS).get_followees()
printer(posts)
posts = instaloader.Profile.from_username(l.context, userS).get_posts()
printer(posts)
posts = instaloader.Profile.from_username(l.context, userS).mediacount
printer(posts)
posts = instaloader.Profile.from_username(l.context, userS).get_followers()
printer(posts)
posts = instaloader.Profile.from_username(l.context, userS).get_tagged_posts()
printer(posts)
posts = instaloader.Profile.from_username(l.context, userS).has_highlight_reels
printer(posts)
