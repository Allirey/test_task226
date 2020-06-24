import datetime as dt
from django.views.generic import View
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import File
from .forms import FileForm


class UploadView(View):
    def get(self, request):
        file_form = FileForm()
        return render(request, 'files/index.html', {'form': file_form})

    def post(self, request):
        form = FileForm(request.POST, request.FILES)

        if form.is_valid():
            form_file = form.cleaned_data['file']
            expire = form.cleaned_data['expire']

            if form_file.size < 2**20 * 20:
                file = File(file=form_file, expires=timezone.now() + dt.timedelta(seconds=float(expire)))
                file.save()

                response = {'id': file.id, 'url': file.file.url, 'error': 0}
            else:
                response = {'error': 1, 'msg': 'max size to upload: 20 Mb!'}
        else:
            response = {'error': 1, 'msg': 'form data not valid!'}

        return JsonResponse(response)


def detail(request, file_id):
    file = get_object_or_404(File, id=file_id)

    return render(request, 'files/detail.html', {'file': file})
