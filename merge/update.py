

class updatable(object):

    def __init__(s,upd,sen,senfirst=False):
        s.las=upd()
        if senfirst:sen(s.las)
        s.upd=upd
        s.sen=sen

    def run(s):
        ac=s.upd()
        if ac!=s.las:
            s.las=ac
            s.sen(ac)


class updatable_dic(updatable):

    def __init__(s,upd,sen):
        s.upd=upd
        s.sen=sen
        s.usedt=[]
    def run(s):
        ac=s.upd()
        for key,val in ac.items():
            if not key in s.usedt:
                s.usedt.append(key)
                s.sen({key:val})


if __name__=="__main__":
    upds=[1,1,1,2,2,1,2]
    def upd():
        for zw in upds:yield zw

    x=updatable(upd().__next__,print)
    for zw in upds[1:]:x.run()

