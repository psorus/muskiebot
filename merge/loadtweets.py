import json
import os


def curlit(task,cou=5,uid=44196397):
    with open("job_"+str(task),"r") as f:
        job=f.read()
    os.system(job.strip().replace("###cou###",str(cou)).replace("###uid###",str(uid))+" -o output.txt")

def load():
    with open("output.txt","r") as f:
        q=f.read()
    return json.loads(q)

def gettweets(q):
    ret={}
    for key,val in q["globalObjects"]["tweets"].items():
        tex=val["full_text"]
        dat=val["created_at"]
        ret[dat]=tex
    return ret

def update_media(cou=5,uid=44196397):
    curlit("media",cou=cou,uid=uid)
    return gettweets(load())
def update_profile(cou=5,uid=44196397):
    curlit("profile",cou=cou,uid=uid)
    return gettweets(load())
def update(cou=5,uid=44196397):
    return {**update_media(cou,uid),**update_profile(cou,uid)}


#print(update())

#print(update(cou=1,uid="2899773086"))


