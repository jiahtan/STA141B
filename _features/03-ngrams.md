---
id: ngams
name: N-Gram and Density Measures
heading: N-Gram and Density Measures
subheading:  Analysis
image: 
---

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
