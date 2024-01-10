from ytmusicapi import YTMusic
import spotify_playlist

def get_top_result(ytmusic, title):
    try:
        result = ytmusic.search(filter=title)[0]
        return result["videoId"]
    except Exception as e:
        try:
            result = ytmusic.search(filter="songs",query=title)[0]
            return result["videoId"]
        except Exception as e:
            print(title)

def get_video_ids(ytmusic, playlist_titles):
    ids = []
    for title in playlist_titles:
        ids.append(get_top_result(ytmusic, title))
    return ids

def create_playlist(ytmusic, title, description, video_ids):
    return ytmusic.create_playlist(title, description, "UNLISTED", video_ids)

def create_ytmusic_playlist_given_names(ytmusic, titles, name, description):
    video_ids = get_video_ids(ytmusic, titles)
    playlist_id = create_playlist(ytmusic, name, description, video_ids)
    return "https://music.youtube.com/playlist?list="+playlist_id

def get_playlist_id_from_url(url):
    # Format:  url = https://open.spotify.com/playlist/{playlist_id}
    # Example input = https://open.spotify.com/playlist/3PSSgpQV1kFBpEcqneLNL7?si=d6b4d0d6527c4c77
    # should return 3PSSgpQV1kFBpEcqneLNL7
    i = len(url)
    url = url.replace("https://music.youtube.com/playlist?list=", '')
    if len(url) >= i:
        print("Not a valid link, try again.")
        return None
    return url

def main():
    ytmusic = YTMusic("oauth.json")

    url = "https://open.spotify.com/playlist/1iPLDmDwRJXUU3JMZ3OLBS?si=6eb55ba1a29f4dbb"

    name, description, titles = spotify_playlist.get_playlist_titles_from_playlist(url)
    if not description:
        description = "This is some description because the original did not have a description." 

    link = create_ytmusic_playlist_given_names(ytmusic, titles, name, description)
    print(link)

    # url = "https://music.youtube.com/playlist?list=PLohRskd8z8rcDzumtCYkQRUrP9jdCuyjQ"
    # print(get_playlist_id_from_url(url))

if __name__ == "__main__":
    main()
