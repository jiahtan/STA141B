---
id: Analysis Part II
name: Analysis Part II
heading: Analysis Part II 
subheading: Top 100 Year-End (1965-2015)
image: 
---

### __Similarity Between Top 100 of All Time and Year-End Top 100__

Using a collection of top 100 songs of the year for years between 1965 - 2015, we decided to compare the similarity lyrics of every year and every decade within the collection to the top 100 of all time. Similarity was computed by transforming the text into Tf-idf vectors and then computing matrix similarity between the corpus and each year and decade.

<img src="./assets/images/deca_sim.jpg">


The lyrics of the yearly top songs in the 90’s were the most similar to the lyrics within the top 100 of all time. The 2000’s were the most divergent of the all time lyrics. 

<img src="./assets/images/year_sim.jpg">

The similarity over years appears to follow a very similar shape as score over years from one of our previous graphs. It seems that in general, it would be wise to stick to the same kinds of lyrics used in the top 100 of all time in order to be popular.

### __Profanity and 'Love' Over the Decades__

<img src="./assets/images/LoveProfanity.jpg">

With the larger dataset, we were curious about the number of times the word 'love' appeared and whether songs contain more profanity in recent times than the past. Looking at the line plot, we can see that love is apparent in music throughout the times, but seem to have dropped a bit in recent decades. For profanity though, we can see a surge starting in the 90s and continuing till today. Although not very apparent, but it seems that the slight drop in the term 'love' crossed with the rise in profanity. 

