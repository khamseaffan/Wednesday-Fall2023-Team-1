from spotipy.oauth2 import SpotifyOAuth
import os
from dotenv import load_dotenv

# Load variables from .env
load_dotenv()

CLIENT_ID = os.getenv("SPOTIPY_CLIENT_ID")
CLIENT_SECRET = os.getenv("SPOTIPY_CLIENT_SECRET")

# REDIRECT_URI = 'http://vcheck-env-1014.eba-megnbk6g.us-west-2.elasticbeanstalk.com/login/callback' #Release URI
# REDIRECT_URI = "http://127.0.0.1:8000/login/callback"
REDIRECT_URI = "http://vbcheck-env.eba-psppdhep.us-west-2.elasticbeanstalk.com/login/callback"  # Development testing URI

SCOPE = "user-top-read user-read-recently-played user-read-private"
sp_oauth = SpotifyOAuth(
    CLIENT_ID, CLIENT_SECRET, REDIRECT_URI, scope=SCOPE, show_dialog=True
)


def get_spotify_token(request):
    token_info = request.session.get("token_info", None)
    if token_info and sp_oauth.is_token_expired(token_info):
        refresh_user_token = token_info.get("refresh_token")
        if refresh_user_token:
            new_token = sp_oauth.refresh_access_token(refresh_user_token)
            request.session["token_info"] = new_token
            return new_token
        else:
            # Error getting refresh token
            return None
    elif token_info:
        # Token still valid, return old token
        return token_info
    else:
        # Error getting saved token
        return None
