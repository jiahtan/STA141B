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

Beside examining list of top 100 songs of all times, we also followed the course instructor's suggestions and looked at Billboard's year-end top 100 songs between the years 1965 and 2015 to see if there is any further insight. Due to time constraint, we did not webscraped the data for this part and instead used a [csv](https://github.com/walkerkq/musiclyrics) file someone else created with this information. 


<div class="images">
    <div class="imgContainer">
        <img src="https://upload.wikimedia.org/wikipedia/commons/2/2b/Billboard_Hot_100_logo.jpg" height="200" width="200"/>
    </div>
    <div class="imgContainer">
        <img src="http://vorm7.weebly.com/uploads/1/6/4/5/16458916/5896387_orig.png" height="250" width="250"/>
    </div>
    <div class="imgContainer">
        <img src="http://az616578.vo.msecnd.net/files/2016/06/14/636015184339992485-1040107779_spotify.jpg" height="200" width="200"/>
    </div>
</div>