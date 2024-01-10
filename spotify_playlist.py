from dotenv import load_dotenv
import os
import base64
from requests import post, get
import json

load_dotenv()
client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET")
youtube_client_id = os.getenv("YOUTUBE_CLIENT_ID")
youtube_client_secret = os.getenv("YOUTUBE_CLIENT_SECRET")

def get_token():
    auth_string = client_id + ":" + client_secret
    auth_bytes = auth_string.encode("utf-8")
    auth_base64 = str(base64.b64encode(auth_bytes), "utf-8")

    url = "https://accounts.spotify.com/api/token"
    header = {
        "Authorization" : "Basic "+auth_base64,
        "Content-Type" : "application/x-www-form-urlencoded",
    }
    data = {"grant_type":"client_credentials"}
    result = post(url, headers=header, data=data)
    json_result = json.loads(result.content)
    token = json_result["access_token"]
    
    return token

def get_auth_header(token):
    return {"Authorization":"Bearer "+token}

def search_for_artist(token, artist_name):
    url = "https://api.spotify.com/v1/search"
    header = get_auth_header(token)
    # artist name is text value searching for
    # &type = field filters
    # &limit = 1 -> limit to the most popular
    query = f"?q={artist_name}&type=artist&limit=1"
    query_url = url + query
    result = get(query_url, headers=header)
    json_result = json.loads(result.content)["artists"]["items"]
    if len(json_result) == 0:
        print("No artist with this name exists...")
        return None
    return json_result[0]

def get_playlist_id_from_url(url):
    # Format:  url = https://open.spotify.com/playlist/{playlist_id}?si={random_stuff}
    # Example input = https://open.spotify.com/playlist/3PSSgpQV1kFBpEcqneLNL7?si=d6b4d0d6527c4c77
    # should return 3PSSgpQV1kFBpEcqneLNL7
    i = len(url)
    url = url.replace('https://open.spotify.com/playlist/', '')
    if len(url) >= i:
        print("Not a valid link, try again.")
        return None
    i = 0
    id = ""
    while url[i] != "?":
        id += url[i]
        i += 1
    return id

def get_playlist(token, playlist_id, offset=0, limit=100):
    url = f"https://api.spotify.com/v1/playlists/{playlist_id}/tracks?offset={offset}&limit={limit}"
    
    header = get_auth_header(token)
    result = get(url, headers=header)
    json_result = json.loads(result.content)
    return json_result

def get_playlist_ids(json_result):
    playlist_ids = []
    for item in json_result["items"]:
        playlist_ids.append(item["track"]["id"])
    return playlist_ids

def get_playlist_info(token, playlist_id):
    url = f"https://api.spotify.com/v1/playlists/{playlist_id}"
    header = get_auth_header(token)
    result = get(url, headers=header)
    json_result = json.loads(result.content)
    name = json_result["name"]
    description = json_result["description"]
    return name, description

def get_track(token, track_id):
    url = f"https://api.spotify.com/v1/tracks/{track_id}"
    header = get_auth_header(token)
    result = get(url, headers=header)
    json_result = json.loads(result.content)
    return json_result

def get_title_and_artist(track_json):
    artist = track_json["artists"][0]["name"]
    title = track_json["name"]
    return(title + ", " + artist)

def get_playlist_titles_from_playlist(url):
    print("Getting Spotify Data...")
    token = get_token()
    id = get_playlist_id_from_url(url)
    
    limit = 100
    offset = 0
    playlist_ids = []
    while (True):
        json_result = get_playlist(token, id, offset)
        playlist_ids += get_playlist_ids((json_result))
        offset += limit
        next = json_result["next"]
        if next is None:
            # print("SHOULD BREAK HERE")
            break
    # print(1)
    titles = []
    name, description = get_playlist_info(token, id)
    # print(1)
    for track_id in playlist_ids:
        track_data = get_track(token, track_id)
        titles.append(get_title_and_artist(track_data))
    # print(titles)
    return name, description, titles

def main():
    url1 = "https://open.spotify.com/playlist/3asKMEfHgxXDxVipXXAy7l?si=hNWK6boVT_yS4MapfZ39mA"
    url2 = "https://open.spotify.com/playlist/3PSSgpQV1kFBpEcqneLNL7?si=d6b4d0d6527c4c77"
    url3 = "https://open.spotify.com/playlist/4HqoCeOrNitfF9huMxxUdE?si=85a48efec8184271&nd=1&dlsi=32a47e51e5fb42a7"
    url4 = "https://open.spotify.com/playlist/4zDqZnHb8SXuQp434KAY82?si=cbe96f3da7c34fe5"
    url5 = "https://open.spotify.com/playlist/4zDqZnHb8SXuQp434KAY82?si=910030c0adce47de"
    url6 = "https://open.spotify.com/playlist/3asKMEfHgxXDxVipXXAy7l?si=hNWK6boVT_yS4MapfZ39mA"
    _,_,parameters = get_playlist_titles_from_playlist(url6)
    i = 1
    for p in parameters:
        print(str(i),".) ",p)
        i+=1
 
if __name__ == "__main__":
    main()
