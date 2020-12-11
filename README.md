
# NLP for Classifying Consumer Tweets

## Phase 4 Project
### Flatiron Online Data Science Bootcamp

Prepared and presented by: [Leah Pope](https://www.linkedin.com/in/leahspope/) (full time Data Science student)

Presentation: [here](./extras/PhaseFourProject_LeahPope.pdf)

Presentation Video: [here](addlink)

Blog:[here](https://lspope.github.io/)

![tweeting](images/joshua-hoehne-Lh_sFxD8AkI-unsplash.jpg)


# Introduction

The goal of this project is to build a Natural Language Processing model to analyze sentiment about Apple and Google products.  I'll classify a Tweet as negative, positive or neutral based on its content.


The Stakeholders for my project are marketing professionals in either company who are interested in learning consumer sentiment. It appears that these tweets were gathered during a session of the South by Southwest film, culture, music, and technology conference. This consumer sentiment would be of interest to the conference marketing professionals and vendor organizers.


# Data Description
The dataset for the project comes from CrowdFlower via [data.world](https://data.world/crowdflower/brands-and-product-emotions). Human raters rated the sentiment in over 9,000 Tweets as positive, negative, or neither.
* judge_1377884607_tweet_product_company.csv

# EDA Questions Explored
### Question 1: What is the general breakdown for these Tweets?
#### [Notebook](./notebooks/eda.ipynb)

### Question 2: Are the two companies represented equally in the labeled data?
#### [Notebook](./notebooks/eda.ipynb)

### Question 3: What insights can the data provide for specific brands?
#### [Notebook](./notebooks/eda.ipynb)


# Corpus EDA Questions Explored
### Question 1: What the most common words in Postitive/Negative/Neutral Tweets?
#### [Notebook](./notebooks/eda_corpus.ipynb)

### Question 2: Is there a difference in character count between Postitive/Negative/Neutral Tweets?
#### [Notebook](./notebooks/eda_corpus.ipynb)


# Modeling
### Creating binary and multiclass classifiers for Tweets on Apple and Google products.
#### [Notebook for Binary Classifiers](./notebooks/modeling.ipynb)
#### [Notebook for Multiclass Classifers](./notebooks/modeling1.ipynb)



# Next Steps/Future Work

Futher analysis into the following areas could yield additional insights.

* Check if punctuation count could be a good feature for Tweet classification.
* Try (SMOTE)[https://imbalanced-learn.readthedocs.io/en/stable/generated/imblearn.over_sampling.SMOTE.html#r001eabbe5dd7-1] to address [class imblance](https://machinelearningmastery.com/smote-oversampling-for-imbalanced-classification/) and see if it results in similar increases in overfitting as RandomOverSampling.
* Hyper-parameter tuning on the binary and multiclass classifier models using GridSearchCV.
* Better understanding of using (LIME)[https://github.com/marcotcr/lime] to explain model behaviour.
* Try Transfer Learning using the (GloVE)[https://nlp.stanford.edu/projects/glove/] pre-trained word embeddings for Twitter) [https://github.com/stanfordnlp/GloVe]
* Get more Tweets for the corpus!


# For More Information
* Review the non-technical presentation [here](./extras/PhaseFourProject_LeahPope.pdf)
* View the non-technical presentation video [here](link)
* Read my blog post [here](https://lspope.github.io/)
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
