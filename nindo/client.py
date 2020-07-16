import asyncio
import urllib.parse

from .http import HTTPClient
from .artist import Artist, RankedArtist
from .util import AsyncIterator

__all__ = (
    "NindoClient",
)


class NindoClient:
    def __init__(self, **kwargs):
        self.loop = kwargs.get("loop", asyncio.get_event_loop())
        self._http = HTTPClient(**kwargs)

    def search(self, term):
        async def _to_wrap():
            data = await self._http.request(f"/search/smart/{urllib.parse.quote(term)}")
            for artists in data:
                yield Artist(artists, http=self._http)

        return AsyncIterator(_to_wrap())

    def _ranked_artists(self, path):
        async def _to_wrap():
            data = await self._http.request(path)
            for artist in data:
                yield RankedArtist(artist, http=self._http)

        return AsyncIterator(_to_wrap())

    def youtube_top_views(self):
        return self._ranked_artists("/ranks/charts/youtube/rankViews/big")

    def youtube_top_likes(self):
        return self._ranked_artists("/ranks/charts/youtube/rankLikes/big")

    def youtube_top_followers(self):
        return self._ranked_artists("/ranks/charts/youtube/rankSubGain/big")

    def youtube_top(self):
        return self._ranked_artists("/ranks/charts/youtube/rank/big")

    def instagram_top_likes(self):
        return self._ranked_artists("/ranks/charts/instagram/rankLikes/big")

    def instagram_top_follower(self):
        return self._ranked_artists("/ranks/charts/instagram/rankSubGain/big")

    def instagram_top(self):
        return self._ranked_artists("/ranks/charts/instagram/rank/big")

    def tiktok_top_likes(self):
        return self._ranked_artists("/ranks/charts/tiktok/rankLikes/big")

    def tiktok_top_views(self):
        return self._ranked_artists("/ranks/charts/tiktok/rankViews/big")

    def tiktok_top_followers(self):
        return self._ranked_artists("/ranks/charts/tiktok/rankSubGain/big")

    def tiktok_top(self):
        return self._ranked_artists("/ranks/charts/tiktok/rank/big")

    def twitter_top_likes(self):
        return self._ranked_artists("/ranks/charts/twitter/rankLikes/big")

    def twitter_top_retweets(self):
        return self._ranked_artists("/ranks/charts/twitter/rankRetweets/big")

    def twitter_top_followers(self):
        return self._ranked_artists("/ranks/charts/twitter/rankSubGain/big")

    def twitter_top(self):
        return self._ranked_artists("/ranks/charts/twitter/rank/big")

    def twitch_top_viewer(self):
        return self._ranked_artists("/ranks/charts/twitch/rankViewer/big")

    def twitch_top_peak_viewer(self):
        return self._ranked_artists("/ranks/charts/twitch/rankPeakViewer/big")

    def twitch_top_followers(self):
        return self._ranked_artists("/ranks/charts/twitch/rankSubGain/big")

    def twitch_top(self):
        return self._ranked_artists("/ranks/charts/twitch/rank/big")