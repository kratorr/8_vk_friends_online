import vk
import getpass


APP_ID = "6392625"


def get_user_login():
    login = input("Enter you login: ")
    return login


def get_user_password():
    password = getpass.getpass("Enter password: ")
    return password


def get_online_friends(APP_ID, user_login, user_password, api_version):
    session = vk.AuthSession(
         app_id=APP_ID,
         user_login=user_login,
         user_password=user_password,
         scope="friends"
    )
    api = vk.API(session)
    friends_online_ids = api.friends.getOnline(v=api_version)
    friends_online_names = api.users.get(user_ids=friends_online_ids, v=api_version)
    return friends_online_names


def output_friends_to_console(friends_online):
    if friends_online:
        print("Online friends: ", len(friends_online))
        for friend in friends_online:
            print(friend["first_name"], friend["last_name"])
    else:
        print("No friends online")


if __name__ == "__main__":
    api_version = 5.52
    try:
        login = get_user_login()
        password = get_user_password()
        friends_online = get_online_friends(APP_ID, login, password, api_version)
        output_friends_to_console(friends_online)
    except vk.exceptions.VkAPIError:
        print("Empty login")
    except vk.exceptions.VkAuthError:
        print("Invalid login or password")