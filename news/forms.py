from django import forms
from news.models.news_model import News
from news.models.user_model import Users
from news.models.category_model import Categories


class CreateCategoryForm(forms.Form):
    name = forms.CharField(
        label="Nome",
        max_length=200,
        required=True,
    )


class CreateNewsModelForm(forms.ModelForm):
    class Meta:
        model = News
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Uma label como o valor Título;
        # Um input do tipo text com o nome title;
        self.fields["title"].label = "Título"

        # Uma label como o valor Conteúdo;
        # Um textarea com o nome content;
        self.fields["content"].label = "Conteúdo"

        # Uma label como o valor Autoria;
        # Múltiplos option sendo seus valores os nomes das pessoas usuárias cadastradas no banco;  # noqa: E501
        self.fields["author"].label = "Autoria"
        self.fields["author"].widget = forms.Select(
            choices=[(user.id, user.name) for user in Users.objects.filter()]
        )

        # Uma label como o valor Criado em;
        # Um input do tipo date com o nome created_at;
        self.fields["created_at"].label = "Criado em"
        self.fields["created_at"].widget = forms.DateInput(
            attrs={"type": "date"}
        )

        # Uma label como o valor URL da Imagem;
        # Um input do tipo file com o nome image;
        self.fields["image"].label = "URL da Imagem"
        # self.fields["image"].upload_to = "img/"

        # Múltiplas label sendo seus valores os nomes das categorias cadastradas no banco;  # noqa: E501
        # Múltiplos input do tipo checkbox com o nome categories, cada input ligado a uma label de categoria;  # noqa: E501
        self.fields["categories"] = forms.ModelMultipleChoiceField(
            queryset=Categories.objects.all(),
            widget=forms.CheckboxSelectMultiple(),
        )


print("olá mundo")