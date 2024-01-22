import instaloader

# username = "ranjan_.ray._"
# password = "@Fuckyou01"
# username = "kindly__fellow_rs"
# password = "ranjith179"

username = "colonel_o2"
password = "colonel_41"

# userS = '_.nxvin._08'
userS = "colonel_o2"


l = instaloader.Instaloader()

l.login(username, password)


def printer(iterable):
    print("Next", iterable)
    try:
        for i in iterable:
            print("i", i)
    except Exception as e:
        print(e)

# try:
#     l.login(username, password)
# except instaloader.exceptions.TwoFactorAuthRequiredException as e:
#     print(e)
#     # Prompt user for the verification code
#     verification_code = input("Enter the two-factor authentication code: ")
#     try:
#         l.two_factor_login(verification_code)
#     except Exception as e:
#         print(f"Error during 2FA login: {e}")
#     posts = list(instaloader.Profile.from_username(l.context, userS).get_posts())[0].url
#     print("Post-Url", posts)
# except Exception as e:
#     print(e)

# Get the post shortcode from the post URL
# post_shortcode = instaloader.Instaloader.parse_shortcode_from_url(post_url)

# Get the post
# post = instaloader.Post.from_shortcode(l.context, post_shortcode)

# Fetch likes for the post
# likes = post.get_likes()

# Print the usernames of users who liked the post
# for like in likes:
#     print(like.username)

# print("l", l)
# posts = instaloader.Profile.from_username(l.context, userS).get_igtv_posts()
# printer(posts)
# posts = instaloader.Profile.from_username(l.context, userS).get_followed_hashtags()
# printer(posts)
# posts = instaloader.Profile.from_username(l.context, userS).get_followees()
# printer(posts)

# posts = instaloader.Profile.from_username(l.context, userS).mediacount
# printer(posts)
# posts = instaloader.Profile.from_username(l.context, userS).get_followers()
# printer(posts)
# posts = instaloader.Profile.from_username(l.context, userS).get_tagged_posts()
# printer(posts)
# posts = instaloader.Profile.from_username(l.context, userS).has_highlight_reels
# printer(posts)

posts = list(instaloader.Profile.from_username(l.context, userS).get_posts())
print("Post-Url", posts)

