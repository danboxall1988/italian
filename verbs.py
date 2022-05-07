import random
import sys

multi_verbs = {"fare" : ["do", "make"],
               "prendere" : ["get", "take"],
               "sentire" : ["hear", "feel"],
               "tenere" : ["hold", "keep"],
               "piacere" : ["like", "enjoy"]
               }

verbs_dict = {
              "andare" : "go",
              "venire" : "come",
              "parlare" : "speak",
              "pensare" : "think",
              "portare" : "wear",
              "arrivare" : "arrive",
              "mettere" : "put",
              "volere" : "want",
              "potere" : "can",
              "avere" : "have",
              "credere" : "believe",
              "capire" : "understand",
              "rimanere" : "remain",
              "lasciare" : "leave"}

verbs_dict2 = {
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
               "guardare" : "watch",
               "morire" : "die",
               "finire" : "finish"}

class VerbGame:
    def __init__(self):
        self.list1 = list(verbs_dict.keys())
        self.list2 = list(verbs_dict2.keys())
        self.multi_list = list(multi_verbs.keys())
        self.total_hint_count = 0
        self.current_verb_hint_count = 0
        self.guess = None
        self.hint = None
        self.current_verb = None
        self.answer = None

    def show_hint(self):
        self.current_verb_hint_count += 1
        if self.current_verb_hint_count == 1:
            self.hint[0] = self.answer[0]
        elif self.current_verb_hint_count == len(self.answer):
            self.guess = self.answer
        else:
            index = random.randint(1, len(self.answer) - 1)
            while self.hint[index] != '-':
                index = random.randint(1, len(self.answer) - 1)
            self.hint[index] = self.answer[index]
        print(''.join(self.hint))

    def play_verb(self):
        index = random.randint(0, len(self.list1) - 1)
        self.current_verb = self.list1[index]
        self.current_verb_hint_count = 0
        guessed_correct = False
        self.answer = verbs_dict[self.current_verb]
        self.hint = ['-'] * len(self.answer)
        while not guessed_correct:
            print()
            print(self.current_verb)
            print()
            self.guess = input()
            if self.guess == '#':
                self.show_hint()
            elif self.guess ==  'q':
                sys.exit()
            elif self.guess == self.answer:
                print("\nCORRECT!\n")
            elif self.guess != self.answer:
                print("\nINCORRECT!\n")
                self.show_hint()
        return index

    def play1(self):
        while len(self.list1) > 0:
            index = self.play_verb()
            self.list1.pop(index)


if __name__ == "__main__":
    vg = VerbGame() 
    vg.play1()

