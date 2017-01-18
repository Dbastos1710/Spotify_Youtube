# Spotify_Youtube

With Python 3.x, make a GET request using Spotify's API and recieve the top "n" albums from a certain country from the current date. Then, with the albums name, the script will write a query search in Youtube and select the first video result (from each album), opening it in a new tab.

Pre-requisites:
 - An OAuth token (generated by Spotify) is needed in order to grant access to Spotify's API.
 - To gererate an OAuth token, one must have a Spotify account.
 - The following python libraries will be used: requests, webbrowser, json, urllib.request, urllib.parse and re.
 
Here, https://developer.spotify.com/web-api/console/get-new-releases/, click on "GET OAUTH TOKEN", then, the login screen will 
and appear after filling the necessary account information, the token will be avaliable.
