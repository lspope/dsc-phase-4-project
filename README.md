
# NLP for Classifying Consumer Tweets

## Phase 4 Project
### Flatiron Online Data Science Bootcamp

Prepared and presented by: [Leah Pope](https://www.linkedin.com/in/leahspope/) (full time Data Science student)

Presentation: [here](./extras/PhaseFourProject_LeahPope.pdf)

Presentation Video: [Coming Soon!](addlink)

Blog: [On Medium](https://leahspope7.medium.com/comparing-vader-and-text-blob-to-human-sentiment-77068cf73982)

![tweeting](images/joshua-hoehne-Lh_sFxD8AkI-unsplash.jpg)


# Introduction

The goal of this project is to build a Natural Language Processing model to analyze sentiment about Apple and Google products. I'll classify a Tweet as negative, positive or neutral based on its content.


The Stakeholders for my project are marketing professionals in either company who are interested in learning consumer sentiment. It appears that these tweets were gathered during a session of the South by Southwest film, culture, music, and technology conference. This consumer sentiment would be of interest to the conference marketing professionals and vendor organizers.


# Data Description
The dataset for the project comes from [CrowdFlower](https://data.world/crowdflower) via [data.world](https://data.world/crowdflower/brands-and-product-emotions). Human raters rated the sentiment in over 9,000 Tweets as positive, negative, or neither.

# EDA Questions Explored
### Question 1: What is the general breakdown for these Tweets?
### Question 2: Are the two brands represented equally in the labeled data?
### Question 3: What insights can the data provide for specific brands?
#### [Notebook](./notebooks/eda.ipynb)


# Corpus EDA Questions Explored
### Question 1: What are the most common words in Postitive/Negative/Neutral Tweets?
### Question 2: Is there a difference in character count between Postitive/Negative/Neutral Tweets?
#### [Notebook](./notebooks/eda_corpus.ipynb)

# Modeling
### Creating binary and multiclass classifiers for Tweets on Apple and Google products.
#### [Notebook for Binary Classifiers](./notebooks/modeling.ipynb)
#### [Notebook for Multiclass Classifers](./notebooks/modeling2.ipynb)


# Next Steps/Future Work
Futher analysis into the following areas could yield additional insights.

* Check if punctuation count could be a good feature for Tweet classification.
* Use [spacy](https://spacy.io/) to replace [NLTK](https://www.nltk.org/)
* Try using SMOTE to address class imbalance and see if it results in similar increases in overfitting as RandomOverSampling
* Hyper-parameter tuning for the Random Forest classifiers.
* Better understanding of using [LIME](https://github.com/marcotcr/lime) to explain model behaviour.
* Try Transfer Learning using the [GloVE](https://nlp.stanford.edu/projects/glove/) pre-trained [word embeddings for Twitter](https://github.com/stanfordnlp/GloVe)
* Get more Tweets for the corpus!
    * Research for pre-labled Tweets
    * Perform Sentiment Analysis using [VADER](https://github.com/cjhutto/vaderSentiment) tool and compare VADER result to the human-annotated Tweets in this corpus. If VADER sentiment is similar enough to human labled sentiment, I could get more Google/Apple product Tweets and label them using VADER to create a larger corpus. :)

# For More Information
* Review the non-technical presentation [here](./extras/PhaseFourProject_LeahPope.pdf)
* View the non-technical presentation video [Coming Soon](link)
* Read my blog post [Coming Soon](https://lspope.github.io/)
* Contact the author [Leah Pope](https://www.linkedin.com/in/leahspope/)


# Repository Structure
```
--notebooks
----data_cleaning.ipynb
----eda.ipynb
----eda_corpus.ipynb
----modeling.ipynb  (binary classifiers are here)
----modeling2.ipynb (multiclasss classifiers are here)
--data
----cleaned_tweets_all.csv
----cleaned_tweets_positive.csv
----cleaned_tweets_negative.csv
----cleaned_tweets_neutral.csv
----crowdflower-brands-and-product-emotions/ (dir for data downloaded from challenge website)
--extras (dir for Project Presentation and other project supporting files)
--images (dir for images)
```
