import os
import os
import requests
from dotenv import load_dotenv
import base64
from ya_disk.models import Ya_links


load_dotenv()


API_URL = os.getenv("API_URL")
PUBLIC_KEY = os.getenv("PUBLIC_KEY")
TOKEN = os.getenv("TOKEN")


def convert_to_base64(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        image_data = response.content
        base64_data = base64.b64encode(image_data)
        return base64_data.decode('utf-8')
    except requests.exceptions.RequestException as e:
        print(f"Error fetching image: {e}")
        return None


def fetch_data_and_update_db():
    api_url = API_URL
    public_key = PUBLIC_KEY
    token = TOKEN
    limit = 10000

    try:
        params = {
            'public_key': public_key,
            'path': "/Рендеры",
            'limit': limit,
            'fields': "_embedded.items.name,_embedded.items.file,_embedded.items.preview,_embedded.items.public_url"
        }

        response = requests.get(api_url, params=params, headers={'Authorization': f'OAuth {token}'})
        response.raise_for_status()
        data = response.json()

        if data:
            existing_links = Ya_links.objects.all()
            name_to_link = {link.name: link for link in existing_links}

            links_to_create = []
            links_to_update = []

            for item in data["_embedded"]["items"]:
                if item["name"] in name_to_link:
                    ya_link = name_to_link[item["name"]]

                    preview_url = item["preview"]
                    preview_base64 = convert_to_base64(preview_url)
                    ya_link.preview = preview_base64
                    ya_link.public_url = item["public_url"]
                    ya_link.file = item["file"]
                    links_to_update.append(ya_link)
                else:
                    preview_url=item["preview"]
                    preview_base64 = convert_to_base64(preview_url)
                    ya_link = Ya_links(
                        preview=preview_base64,
                        public_url=item["public_url"],
                        name=item["name"],
                        file=item["file"]
                    )
                    links_to_create.append(ya_link)

            Ya_links.objects.bulk_update(links_to_update, ["preview", "public_url", "file"])
            Ya_links.objects.bulk_create(links_to_create)

            return True
        else:
            print("No data fetched.")
            return False

    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return False