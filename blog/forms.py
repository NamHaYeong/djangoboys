from django import forms
from .models import Post


# 폼은 일반폼(Form)과 모델폼(Model Form) 두 종류가 있다.\
# Form (일반 폼) : 화면에 나타날 입력 필드를 직접 필드 정의, 위젯 설정이 필요
# Model Form (모델 폼) : 모델과 필드를 지정하면 모델폼이 자동으로 폼 필드를 생성
# PostForm : 만들 폼의 이름(Post라는 Model과 연결되는 폼이다.)
# forms.ModelForm 은 장고에게 이 폼이 ModelForm이라는 것을 알려주는 역할

# PostForm : 만들 폼의 이름(Post Model)과 연결되는 폼이다.
# forms.ModelForm은 ModelForm이라는 것을 알려주는 구문
class PostForm(forms.ModelForm):
    # 이 폼을 만들기 위해서 어떤 모델이 쓰여야 하는지 장고에 알려주는 구문
    class Meta:  # postform과 관련된 정보 설정
        model = Post  # post 모델과 연결된다
        fields = ('title', 'text',)  # 이 폼에 나타낼 필드를 지정
