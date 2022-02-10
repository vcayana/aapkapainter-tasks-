def find_score(scores):
    score=[0,0]
    striker=0
    non_striker=1
    for run in scores:
        score[striker]=score[striker]+run
        if run%2!=2:
            striker,non_striker=non_striker,striker
    return "p1:",score[0],"P2:",score[1]
print(find_score([1,2,3,2,1]))
