import requests
from django.shortcuts import render
from django.http import HttpResponse

FASTAPI_URL = "http://127.0.0.1:8001/predict"

def home(request):
    if request.method == "POST" and request.FILES.get("image"):
        image = request.FILES["image"]

        try:
            response = requests.post(
                FASTAPI_URL,
                files={"file": (image.name, image.read(), image.content_type)},
                timeout=30
            )

            if response.status_code != 200:
                return HttpResponse("Prediction service error")

            data = response.json()

            return render(request, "detector/result.html", {
                "predicted_class": data["class"],
                "confidence": round(data["confidence"], 2),
                "class_description": get_class_description(data["class"])
            })

        except Exception as e:
            return HttpResponse(str(e))

    return render(request, "detector/home.html")


def get_class_description(class_name):
    descriptions = {
        'L': 'Left Bundle Branch Block',
        'N': 'Normal',
        'P': 'Paced',
        'R': 'Right Bundle Branch Block',
        'V': 'Ventricular Premature Beat'
    }
    return descriptions.get(class_name, 'Unknown')
