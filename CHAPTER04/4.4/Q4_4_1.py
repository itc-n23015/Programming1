vote_num = 0
def vote():
    print("投票します")
    global vote_num
    vote_num += 1

def reset_box():
    global vate_num
    print("票の数は {} です".format(vate_num))
