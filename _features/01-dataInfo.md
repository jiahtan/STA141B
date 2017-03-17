---
id: data
name: Our Data
heading: Our 
subheading: Data
image: 
---

To perform our analysis, we first scraped the list of 100 songs from [Billboard](http://www.billboard.com/articles/list/2155531/the-hot-100-all-time-top-songs) for the song name, year, and artist. 

Then we turn to [songlyrics](http://www.songlyrics.com/) to retrieve the lyrics for each song. Out of the 100 songs, we were unable to retrieve lyrics for 4 songs due to collaboration between the artists, the song title not matching, or the title from Billboard was a combination of two songs. For these special cases, we scrape individual sites. 

Besides getting just the lyrics, we also used [Spotify's API](https://developer.spotify.com/web-api/get-audio-features/) to extract audio features of the songs. For a detail description of the features, clicked the spotify link above. 