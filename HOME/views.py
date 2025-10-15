import requests
from django.shortcuts import render

def homepage(request):
    data = None
    if request.method == "POST":
        try:
            response = requests.get("https://kitsu.io/api/edge/anime?filter[text]=death")
            if response.status_code == 200:
                data = response.json()
            else:
                data = {"error": f"API returned {response.status_code}"}
        except requests.exceptions.RequestException as e:
            print("The API failed:", e)
            data = {"error": str(e)}
    return render(request, "home.html", {"data": data})