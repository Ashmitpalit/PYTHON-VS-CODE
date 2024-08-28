import random

name=["Ashmit","Aritra","Rajdip","Piyush","Gargi","Kanjari"]
action=["dances","walks","cries","laughs","plays","sings"]
words= ["willingly and ", "lonely and", "rudely and", "gently and", "seemingly and","mightfully and"]
action2= ["angrily", "peacefully", "slowly", "quickly", "unconsciously"]

def poemGeneration():
    lines = []
    for i in range(4):
        n = random.choice(name)
        a = random.choice(action)
        w = random.choice(words)
        a2 = random.choice(action2)
        line = f"{n} {a} {w} {a2}."
        lines.append(line)
        
    poem = "\n".join(lines)
    return poem

poem = poemGeneration()
print(poem)


