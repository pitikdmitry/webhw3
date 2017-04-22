import random, string
from models import Question, Profile, Tag, Answer
from django.contrib.auth.models import User

class FillDB(object):
    def get_random_name(self):
        pre_name_array = ['Super', 'Mega', 'Ultra', 'King', 'Best', 'Hero', 'Don', 'Lovely', 'Norm', 'Dc', 'Doctor',
                          'Kitty']
        name_array = ['John', 'Dre', 'Sasha', 'Arthur', 'Rick', 'Carl', 'Maggy', 'Homer', 'Glen', 'Niggan']
        return random.choice(pre_name_array) + random.choice(name_array)

    def get_random_tag(self):
        tags = ['javascrypt', 'java', 'c#', 'php', 'android', 'jquery', 'python', 'html', 'c++', 'ios', 'css', 'mysql',
                'sql',
                'asp.net', 'objective-c', 'ruby-on-rails', '.net', 'c', 'iphone', 'angularjs', 'arrays', 'sql-server',
                'json', 'ruby', 'r', 'ajax', 'regex', 'xml', 'node.js', 'asp.net-mvc', 'linux', 'django', 'wpf',
                'swift', 'database', 'xcode', 'android-studio']
        return random.choice(tags)

    def create_user(self):
        name = self.get_random_name()
        user = User.objects.create_user(name, name + '@mail.ru', 'qwerty123')
        user.save()
        return user

    def create_profile(self):
        user = self.create_user()
        nickname = user.username
        profile = Profile.objects.create(user=user, nickname=nickname)
        profile.save()

    def ask_with_answers(self):
        self.ask()
        self.answer_on_question(Question.objects.last().id)

    def ask(self):
        user = None
        while user == None:
            user = Profile.objects.get(pk=random.randint(1, Profile.objects.count()))

        title = ['How to boil']
        text = ['Kettle']

        tags = []
        for i in range(random.randint(1, 5)):
            tag_name = self.get_random_tag()
            tags.append(tag_name)

        q = Question.objects.create(user=user, title=''.join(title), text=''.join(text), rating=random.randint(0, 10))
        q.save()

    def answer_on_question(self, q_id):
        for i in range(random.randint(1, 5)):
            user = None
            while user == None:
                user = Profile.objects.get(pk=random.randint(1, Profile.objects.count()))

            question = Question.objects.get(pk=q_id)
            text = []

            for i in range(random.randint(100, 500)):
                random_letter = random.choice(string.ascii_letters + string.digits)
                if i % 80 == 0: text.append('\n')
                text.append(random_letter)

            a = Answer.objects.create(user=user, question=question, text=''.join(text), rating=random.randint(0, 10))
            a.save()

    def create_func(self):
        self.create_user()
        self.create_profile()
        self.ask_with_answers()