from __future__ import annotations

# from dataclasses import dataclass
from datetime import date
from typing import Dict
from urllib.parse import quote

from django.db import models


class Song(models.Model):
    melon_uid = models.CharField(max_length=20, unique=True)
    rank = models.PositiveSmallIntegerField()
    album_name = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    artist_name = models.CharField(max_length=100)
    cover_url = models.URLField()
    lyrics = models.TextField()
    genre = models.CharField(max_length=100)
    release_date = models.DateField()
    like_count = models.PositiveIntegerField()

    @property
    def melon_detail_url(self) -> str:
        song_id = quote(self.melon_uid)
        return f"https://www.melon.com/song/detail.htm?songId={song_id}"

    @property
    def youtube_search_url(self) -> str:
        search_query = quote(f"{self.name}, {self.artist_name}")
        return f"https://www.youtube.com/results?search_query={search_query}"

    @classmethod
    def from_dict(cls, data: Dict) -> Song:
        return cls(
            melon_uid=data.get("곡일련번호"),
            rank=int(data.get("순위")),
            album_name=data.get("앨범"),
            name=data.get("곡명"),
            artist_name=data.get("가수"),
            cover_url=data.get("커버이미지_주소"),
            lyrics=data.get("가사"),
            genre=data.get("장르"),
            release_date=date.fromisoformat(data.get("발매일")),
            like_count=int(data.get("좋아요")),
        )
