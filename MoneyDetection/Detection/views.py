from django.shortcuts import render
from Detection.predict import Predict
# Create your views here.


p = Predict()
def detect(request):
    if(request.method == 'POST'):
        img = request.FILES.get('img')
        result = p.predictHTMLDirect(img)        
        return render(request, 'detection/home.html',{"var":"The given note was of " + str(result)+" rupees"})
    else:
        return render(request,'detection/home.html',{"var":"Select Image"})