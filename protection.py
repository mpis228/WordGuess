from AddPlay import AnswerErrorInStart


class Check:

    def __init__(self, yes, no):
        self.yes = yes
        self.no = no

    def chek(self, answer_user):
        if answer_user in self.yes:
            return True
        elif answer_user in self.no:
            return False
        else:
            raise AnswerErrorInStart()

    def cheking_play(self, answer_user):
        if len(answer_user) == self.yes:
            return True
        elif len(answer_user) == self.no:
            return True
        else:
            return False
