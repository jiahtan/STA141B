---
id: Analysis Part I
name: Analysis Part I
heading: Analysis Part I 
subheading: Top 100 of All Time
image: 
---

### __Distribution of the Songs Across Time__

<iframe src="./assets/plots/songByYear.html" width="650" height="450" style="border:none;"  align="middle"></iframe>

 To see if there was a “golden period” of music, where lots of songs got released that eventually ended up on this top 100 list, we examned how many songs end up in the top 100 list for each year. We can see many songs landing between the 70s and early 80s, follow by a period of inacitivty and a slight resurgeance prior to the 20s. Entering into the 20s is another period of low and spikes again around 2010. 

### __Repeated Artists__

<img src="./assets/images/artistRepeat.jpg">

Getting a frequency count on the number of artists that appear on the list more than once, we got 13 artists total. (We double count artists that share collaborations)

### __A Scoring System Approach__

<img src="./assets/images/rankingNfrequency.jpg" style="width:600px;height:400px;">

As a different approach to answering ‘when were the good songs released’, we generated a scoring system. To contrast between the barplot of song by year and the score plot, we can see that the 80’s period has been diminished some bit, and appears to be tied with 2011, which is interesting, since 2011 has 4 hit songs, and 1980-1983 had around 5-6 hits each. (Note: higher index -> better performance on top 100 chart).

<img src="./assets/images/2011Songs.JPG">

### __Spotify Audio Features__

<iframe src="./assets/plots/AudioFeaturePlot.html" width="1000" height="500" style="border:none;"  align="middle"></iframe>

Some interesting patterns that we noted in the audio features is that for valence and energy, there is a dip between the 1985 and 1990. This may indicate a period of sadder songs hitting the charts. 

### __N-Gram__

Ngrams are contiguous sequences of n items. For  our analysis we are looking at the bigrams and trigrams within the lyrics of the top 100 songs to see what are the most common 2-word and 3-word phrases. Since a single song may contain a lot of repetition of certain phrases, we only looked into bigrams and trigrams that appeared in more than one song.

<img src="./assets/images/try_by_song.jpg" style="width:600px;height:400px;">
<img src="./assets/images/bi_by_song.jpg" style="width:600px;height:400px;">

In general, we found that most of the bigrams were not meaningful, so we will focus more on the trigrams. The trigram that appeared in the most songs was  “I love you”, which was found in 14 of the 100 songs.

<img src="./assets/images/tri_by_freq.jpg" style="width:600px;height:400px;">
<img src="./assets/images/bi_by_freq.jpg" style="width:600px;height:400px;">

The most common trigram within the corpus of the 100 songs’ lyrics was “na na na”  and some other nonsensical  sequences.

### __Lexical Density__
Lexical Density = number of lexical words (or content words) divided by the total number of words. 

<img src="./assets/images/lexical_boxplot.png" style="width:600px;height:400px;">

### __Sentiment Analysis__

Sentiment Analysis was conducted using the Python package [TextBlob](https://textblob.readthedocs.io/en/dev/) via the [Pattern Analyzer](http://www.clips.ua.ac.be/pattern). The package returns a polarity and subjectivity measure.

- Polarity: positive or negative connotation, value between [-1,1]

<iframe src="./assets/plots/polarity.html" width="650" height="450" style="border:none" align="middle"></iframe>

From the plot of polarity against time, we can see that a majority of the songs are positive. However, there may be inaccuracy in the classification, because as we can see the most negative song is 'Call Me Maybe' by Carly Rae Jepsen, which we know for sure is not a negative song. However, since the lyrics repeats 'so bad' and 'crazy' many times, it has a negative score. 

- Subjectivity: subjective or objective, value between [0,1]

<iframe src="./assets/plots/subjectivity.html" width="650" height="450" style="border:none" align="middle"></iframe>

From the plot of subjectivity against time, we see that all of the songs are moderately subjective, siginifying the meaning of the words depend on the person.

Due to some inaccuracy in the polarity measure, we decided to create a new sentiment score using the combination of audio valence and polarity. We compute this score by scaling polarity to be between 0 and 1, then add this value to valence and divide by 2 to keep everything within the [0,1] range. Thus, scores closer to 1 will still be interpreted as positive and closer to 0 interpreted as negative. 

$$sentiment = \frac{\frac{polarity + 1}{2} + valence}{2}$$

<iframe src="./assets/plots/sentimentAdjusted.html" width="650" height="450" style="border:none" align="middle"></iframe>

Examining the plot with the adjusted score, we see that 'Call Me Maybe' is now ranked higher in positivity than previously. The general shape for the scatter plot follows the one for valence.

### __Word Clouds By Year__

<div class="images">
    <div class="imgContainer">
        <img src="./assets/images/1950 to 1959.png" height="400" width="400"/>
    </div>
    <div class="imgContainer">
         <img src="./assets/images/1960 to 1969.png" height="400" width="400"/>
    </div>
    <div class="imgContainer">
        <img src="./assets/images/1970 to 1979.png" height="400" width="400"/>
    </div>
    <div class="imgContainer">
        <img src="./assets/images/1980 to 1989.png" height="400" width="400"/>
    </div>
    <div class="imgContainer">
         <img src="./assets/images/1990 to 1999.png" height="400" width="400"/>
    </div>
    <div class="imgContainer">
        <img src="./assets/images/2000 to 2009.png" height="400" width="400"/>
    </div>
     <div class="imgContainer">
        <img src="./assets/images/2010 to 2019.png" height="400" width="400"/>
    </div>
</div>