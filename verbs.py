import random
verbs_dict = {"fare" : ["do", "make"],
              "andare" : "go",
              "venire" : "come",
              "parlare" : "speak",
              "pensare" : "think",
              "portare" : "wear",
              "arrivare" : "arrive",
              "mettere" : "put",
              "prendere" : ["get", "take"],
              "volere" : "want",
              "potere" : "can",
              "avere" : "have",
              "credere" : "believe",
              "capire" : "understand",
              "sentire" : ["hear", "feel"],
              "rimanere" : "remain",
              "lasciare" : "leave"}

verbs_dict2 = {"tenere" : ["hold", "keep"],
               "diventare" : "become",
               "lavorare" : "work",
               "usare" : "use",
               "entrare" : "enter",
               "chiamare" : "ring",
               "ricordare" : "remember",
               "vivere" : "live",
               "passare" : "pass",
               "decidere" : "decide",
               "appire" : "open",
               "seguire" : "follow",
               "aspettare" : "wait",
               "piacere" : ["like", "enjoy"],
               "guardare" : "watch",
               "morire" : "die",
               "finire" : "finish"}

hint_count = 0

def print_hint(answer):
    print(f"{answer[0]} ", end="")
    for i in range(len(answer) - 1):
        print("- ", end="")
    print("")

def show_hint(answer):
    hint_count += 1
    if type(answer) == list:
        print_hint(answer[0])
        print_hint(answer[1])
    else:
        print_hint(answer)

italian_verbs = list(verbs_dict.keys())

index = random.randint(0, len(italian_verbs) - 1)
verb = italian_verbs[index]
answer = verbs_dict[verb]
guessed_correct = False

while len(italian_verbs) > 0:
    if guessed_correct:
        index = random.randint(0, len(italian_verbs) - 1)
        verb = italian_verbs[index]
        answer = verbs_dict[verb]
    print(verb)
    guess = input()
    if guess == "#":
        show_hint(answer)
        guessed_correct = False
        continue
    else:
        if type(answer) == list:
            print("two meanings...")
            if guess in answer:
                print("CORRECT!!!")
                guessed_correct = True
            else:
                print("WRONG!!!")
                show_hint(answer)
                guessed_correct = False
                continue
        else:
            if guess == answer:
                print("CORRECT!!!")
                guessed_correct = True
            else:
                show_hint(answer)
                guessed_correct = False
                continue
    italian_verbs.pop(index)
print(f"you finished with {hint_count} hints")
