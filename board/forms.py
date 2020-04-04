from django.forms import ModelForm

from board.models import *

class TagForm(ModelForm):
    class Meta:
        model = Tag
        fields = ('title', )

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ('title', 'advert')

class AdvertForm(ModelForm):
    class Meta:
        model = Advert
        fields = ('title', 'body', 'tags')

# class KindOfAnimalForm(ModelForm):
#     class Meta:
#         model = KindOfAnimal
#         fields = (
#             'title',
#         )

# class SignupForm(UserCreationForm):
#     email = models.EmailField(max_length=254, help_text='Это поле обязательно')

#     class Meta:
#         model = User
#         fields = ('username', 'email', 'password1', 'password2')