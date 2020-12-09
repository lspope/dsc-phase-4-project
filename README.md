
# NLP for Classifying Consumer Tweets

## Phase 4 Project
### Flatiron Online Data Science Bootcamp

Prepared and presented by: [Leah Pope](https://www.linkedin.com/in/leahspope/) (full time Data Science student)

Presentation: [here](./extras/PhaseFourProject_LeahPope.pdf)

Presentation Video: [here](addlink)

Blog:[here](https://lspope.github.io/)

![tweeting](images/joshua-hoehne-Lh_sFxD8AkI-unsplash.jpg)


# Introduction

The goal of this project is to build a Natural Language Processing model to analyze sentiment about Apple and Google products.  I'll be classifying a Tweet as negative or positive based on its content (a binary classification problem).


The Stakeholders for my project are ?


# Data Description
The dataset for the project comes from CrowdFlower via [data.world](https://data.world/crowdflower/brands-and-product-emotions). Human raters rated the sentiment in over 9,000 Tweets as positive, negative, or neither.
* judge_1377884607_tweet_product_company.csv

# EDA Questions Explored
### Question 1: What is the general breakdown for these Tweets?
#### [Notebook](./notebooks/eda.ipynb)

### Question 2: Are the two companies represented equally in the labeled data?
#### [Notebook](./notebooks/eda.ipynb)

### Question 3: What insights can the data provide for specific products?
#### [Notebook](./notebooks/eda.ipynb)


# Modeling
### Creating a binary classifier for positive/negative consumer Tweets on Apple and Google products.
#### [Notebook](./notebooks/classifer_modeling.ipynb)



# Next Steps/Future Work

Futher analysis into the following areas could yield additional insights.

* __idea 1__  Multiclass classifier with negative/positive/neutral sentiment classes.

* __idea 2__ ?


# For More Information
* Review the non-technical presentation [here](./extras/PhaseFourProject_LeahPope.pd)
* View the non-technical presentation video [here](link)
* Read my blog post [here](https://lspope.github.io/)
* Contact the author [Leah Pope](https://www.linkedin.com/in/leahspope/)


# Repository Structure
```
--notebooks
----data_cleaning.ipynb
----eda.ipynb
----modeling.ipynb
--data
----cleaned_tweets_all.csv
----cleaned_tweets_positive.csv
----cleaned_tweets_negative.csv
----cleaned_tweets_neutral.csv
----original (dir for raw data downloaded from challenge website)
--extras (dir for Project Presentation and other supporting files)
```
