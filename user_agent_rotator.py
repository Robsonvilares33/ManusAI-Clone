from fake_useragent import UserAgent

def get_random_user_agent():
    ua = UserAgent()
    return ua.random

if __name__ == "__main__":
    print(get_random_user_agent())


