---
id: sentiment 
name: Sentiment Analysis
heading: Sentiment
subheading:  Analysis
image: 
---

Sentiment Analysis was conducted using the Python package [TextBlob](https://textblob.readthedocs.io/en/dev/) via the [Pattern Analyzer](http://www.clips.ua.ac.be/pattern). The package returns a polarity and subjectivity measure.

- Polarity: positive or negative connotation, value between [-1,1]

<iframe src="./assets/plots/polarity.html" width="650" height="450" style="border:none" align="middle"></iframe>

From the plot of polarity against time, we can see that a majority of the songs are positive. However, there may be inaccuracy in the classification, because as we can see the most negative song is 'Call Me Maybe' by Carly Rae Jepsen, which we know for sure is not a negative song. However, since the lyrics repeats 'so bad' and 'crazy' many times, it has a negative score. 

- Subjectivity: subjective or objective, value between [0,1]

<iframe src="./assets/plots/subjectivity.html" width="650" height="450" style="border:none" align="middle"></iframe>

From the plot of subjectivity against time, we see that all of the songs are moderately subjective, siginifying the meaning of the words depend on the person.