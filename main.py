from majibu import majibu

def fikiria_jinsi_ya_jibu(swali):
    swali = swali.lower()
    jibu = majibu.get(swali, "repeat again.")
    return random.choice(jibu)

while True:
    swali_lake = input("You: ")

    jibu = fikiria_jinsi_ya_jibu(swali_lake)
    print("bot: ", jibu)
