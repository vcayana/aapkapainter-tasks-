dev is_anagram(S1,S2):
    if sorted(S1.lower())==sorted(S2.lower()):
        print("Yes")
    else:
        print("No")
is_anagram("Mary","Army")
