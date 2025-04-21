from django import forms
from .models import ContactMessage, SupportMessage, Comment

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Adınız'}),
            'email': forms.EmailInput(attrs={'placeholder': 'E-posta adresiniz'}),
            'message': forms.Textarea(attrs={'placeholder': 'Mesajınız', 'rows': 5}),
        }
        error_messages = {
            'name': {'required': 'Lütfen adınızı girin.'},
            'email': {'required': 'Lütfen e-posta adresinizi girin.', 'invalid': 'Geçerli bir e-posta adresi girin.'},
            'message': {'required': 'Lütfen mesajınızı girin.'},
        }

class SupportMessageForm(forms.ModelForm):
    REASON_CHOICES = [
        ('technical', 'Teknik Sorun'),
        ('feedback', 'Geri Bildirim'),
        ('other', 'Diğer'),
    ]
    reason = forms.ChoiceField(choices=REASON_CHOICES, label='Sebep')

    class Meta:
        model = SupportMessage
        fields = ['name', 'phone', 'email', 'reason', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Adınız'}),
            'phone': forms.TextInput(attrs={'placeholder': 'Telefon numaranız'}),
            'email': forms.EmailInput(attrs={'placeholder': 'E-posta adresiniz'}),
            'reason': forms.Select(attrs={'class': 'form-select'}),
            'message': forms.Textarea(attrs={'placeholder': 'Mesajınız', 'rows': 5}),
        }
        error_messages = {
            'name': {'required': 'Lütfen adınızı girin.'},
            'phone': {'required': 'Lütfen telefon numaranızı girin.'},
            'email': {'required': 'Lütfen e-posta adresinizi girin.', 'invalid': 'Geçerli bir e-posta adresi girin.'},
            'reason': {'required': 'Lütfen bir sebep seçin.'},
            'message': {'required': 'Lütfen mesajınızı girin.'},
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['author', 'content']
        widgets = {
            'author': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Adınız'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Yorumunuz', 'rows': 4}),
        }