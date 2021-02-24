from loadtweets import update_media,update_profile
from update import updatable_dic as updatable
from tele import scream

print("hi")


from time import sleep

uid=2899773086
uid=44196397


def load_media():
    return update_media(uid=uid,cou=10)
def load_profile():
    return update_profile(uid=uid,cou=10)

def formal_scream(q):
    for key,val in q.items():
        scream(f'At {key} Mr Musk tweetet "{val}"')

u=[updatable(load_media,formal_scream),updatable(load_profile,formal_scream)]
#u=[updatable(load_profile,formal_scream)]#,updatable(load_profile,formal_scream)]

print("Starting main loop")
scream("REBOOTING")

while True:
    for uu in u:
        try:
            uu.run()
        except:
            print("failure in running an updatable")
    sleep(10)
        











