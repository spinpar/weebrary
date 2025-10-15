import requests
from django.shortcuts import render
from DATABASE.models import Anime

def homepage(request):
    error = None
    if request.method == "POST":
        try:
            url = "https://kitsu.io/api/edge/anime?filter[text]=death"
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()

            for item in data.get("data", []):
                attributes = item.get("attributes", {})
                mal_id = int(item.get("id", 0))
                if mal_id == 0:
                    continue

                title = attributes.get("canonicalTitle", "")
                synopsis = attributes.get("synopsis", "")
                rating_str = attributes.get("averageRating", None)
                rating = float(rating_str) if rating_str else None

                Anime.objects.update_or_create(
                    mal_id=mal_id,
                    defaults={
                        "title": title,
                        "synopsis": synopsis,
                        "rating": rating
                    }
                )

        except requests.exceptions.RequestException as e:
            error = f"API error: {e}"
        except Exception as e:
            error = f"Save error: {e}"

    saved_anime = Anime.objects.all()
    return render(request, "home.html", {"data": saved_anime, "error": error})
