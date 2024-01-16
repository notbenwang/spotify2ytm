# spotify2ytm - Python Application to convert Spotify Playlists to Youtube Music Playlists

## Motivation
As an avid Youtube Music user (don't roast me), I wanted an easy, or rather a more convenient way to transfer a Spotify playlist into a Youtube Music playlist. 
While there exists programs that are capable of this, I wanted to see if I could program an application as an exercise to allow me to a) work with the Spotify and Youtube API's, and b) gain a familiarity with using API's in conjunction with Python.   


## References and Caution
While the Spotify API was used for this project, there is technically no official "Youtube Music" API, and with the regular Youtube API being severely limited in terms of the amount of possible searches that can be conducted in any given time frame,
I did end up using this unofficial Youtube API which you can find here: https://ytmusicapi.readthedocs.io/en/stable/

Because this isn't the official Youtube Music API and not supported/endorsed by Google, I can't for certain say that there is strong security in this program, which is why I would be hesitant to recommend using this specific program or application in conjunction
with your Youtube account. With that being said, I have not suffered any issues regarding this, but there is still a reason for concern, so use at your own risk.

## How to Use
You'll first need to get an oauth.json file for your Youtube account into the directory (specifically the Youtube TV one, https://developers.google.com/youtube/v3/guides/auth/devices). Originally, I was planning on making a web application to avoid this, but after considering the security risks for the unofficial Youtube API used, thought that it would be better to just
have it as a Python application that only the most lazy would use (me). If you need help getting the oauth.json file, here's a tutorial: https://developers.google.com/identity/protocols/oauth2 

When you have the oauth set up, there should be a download button where you can download the oauth.json file.

You will also need a Spotify API client and secret key. You can find a tutorial on how to set that up here: https://www.youtube.com/watch?v=WAmEZBEeNmg&ab_channel=AkamaiDeveloper 

For myself, I put the keys in a .env file, but you can also just hard code it into the spotify_playlist.py file as well.

Then, download the necessary dependencies (YTMusic, python-dotenv, etc.)

Then, in the ytmusic.py file, simply put the url for the spotify playlist in the variable 'url', and then the program will run and eventually print out a link to the Youtube Music playlist.

## Future

In the future, I would like to expand on this project to see if I could develop the program in reverse (convert YoutubeMusic playlist to Spotify Playlist), and use some web framework to make it easier for users to use the application without doing all the complicated setup. 
I would also like to develop this application in the contexts of an actual Youtube Music API, rather than an unofficial one which might have security liabilities. 


