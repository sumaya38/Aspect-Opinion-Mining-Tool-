from django.shortcuts import render
from django.core.files.storage import FileSystemStorage

def home(request):
        return render(request, 'home.html')


def upload(request):
    if request.method == 'POST' and request.FILES['myfile'] and request.FILES['myfile1']:
        myfile = request.FILES['myfile']
        myfile1 = request.FILES['myfile1']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        filename1 = fs.save(myfile1.name, myfile1)
        uploaded_file_url1 = fs.url(filename)
        uploaded_file_url2 = fs.url(filename1)
        request.session['data_file'] = uploaded_file_url1
        request.session['feature_file'] = uploaded_file_url2
        file_content = request.FILES['myfile1'].read()
        if request.session.get('data_file'):
            from sentiment.code.aspect_based_senti_analysis_method import analyzer

            result = analyzer(request.session['data_file'], request.session['feature_file'])
        return render(request, 'home.html', {
            'uploaded_file_url1': uploaded_file_url1,
            'uploaded_file_url2': uploaded_file_url2,
            'file_content': file_content,
            'result': result
        })