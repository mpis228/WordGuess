from AddPlay import CharError, AnswerError


class TargetWord:

    def __init__(self, word: str):
        self.health = ['❤ ' for _ in range(len(word) + 1)]
        self.word = [char for char in word]
        self.word_completion = [i for i in '_' * len(self.word)]
        self.chares = set(self.word)

    def damage(self,):
        self.health.pop()
        if len(self.health) == 0:
            return None

    def full_word(self, word):
        word = [char for char in word]
        if word == self.word:
            print(self.word)
            self.word_completion = self.word
        else:
            print('Не правильно!')
            self.damage()

    def __count_index(self, word, char):
        total = []
        for i in range(len(word)):
            if word[i] == char:
                total.append(i)
        return total

    def puzzled(self, char: str):
        for i in self.__count_index(self.word, char):
            self.word_completion[i] = char
        print(*self.word_completion)
        """return self.word_completion"""

    def one_char(self, char: str):
        if char not in self.word_completion:
            if char in self.word:
                self.puzzled(char)
                print('угадали!')

            else:
                self.damage()
                print('не угадали')
        else:
            CharError()

    def define_answer(self, answer):
        if len(answer) == len(self.word):
            return self.full_word(answer)
        elif len(answer) == 1:
            if self.one_char(answer):
                print('ДА вы угадали букву ')
        else:
            AnswerError()

    def win_or_over(self):
        if len(self.health) == 0:
            print(
                'Вы проиграли!',
                'хотите попробовать еще раз?',
                sep='\n'
            )
            return True
        elif self.word_completion.count('_') == 0:

            print(
                'Вы выграли!'
                'хотите попробовать еще раз?',
                sep='\n'
            )
            return True
        else:
            return False
