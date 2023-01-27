import requests
import json

# just replace the end of this url with the id of your emote set
url = "https://7tv.io/v3/emote-sets/611ea25d3990c04e921506f7"
headers = {
    'Content-Type': 'application/json',
}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    emote_set_data = response.json()
    emotes = emote_set_data["emotes"]
    emote_list = []
    # try to load the existing emotes.json file
    try:
        with open("emotes.json", "r") as infile:
            existing_emotes = json.load(infile)
            existing_names = [emote["name"].lower() for emote in existing_emotes]
    except:
        existing_emotes = []
        existing_names = []
    for emote in emotes:
        emote_name = emote["name"].lower()
        if emote_name not in existing_names:
            emote_image = "https://cdn.7tv.app/emote/"+emote["id"]+"/2x"
            emote_list.append({"name":emote["name"],"image":emote_image})
    existing_emotes += emote_list
    # write the new emotes to the file
    with open("emotes.json", "w") as outfile:
        json.dump(existing_emotes, outfile)
    print("Emotes exported to emotes.json")
else:
    print(f"Error: {response.status_code}")
