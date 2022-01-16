from django.shortcuts import render, redirect
from store.models.help import Help
from django.views import View


class HelpView(View):
    def get(self, request):
        return render(request, 'help.html')

    def post(self, request):
        postData = request.POST
        name = postData.get('Name')
        email = postData.get('Email')
        message = postData.get('Message')

        help = Help(name=name,
                    email=email,
                    message=message)

        help.save()
        return redirect('homepage')