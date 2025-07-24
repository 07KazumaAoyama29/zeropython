favorite_language = {"haruto": "C#", "kazuma": "Python"}
vote_people = ["hiroto", "haruto", "kanato"]
for name in vote_people:
    if name in favorite_language.keys():
        print(f"{name}、投票ありがとう")
    else:
        print(f"{name}、投票してください")