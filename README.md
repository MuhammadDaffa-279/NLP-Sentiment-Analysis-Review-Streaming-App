# NLP Deep Learning Project
## NLP-Sentiment-Analysis-Review-Streaming-App

---

## Project Information
***Background:***   
Music streaming application is becoming more a competitive market lately. Therefore, application developer require to address their services based on what the customer want and become a customer centric. This project will address the sentiment analysis on the review made by customer's of Spotify app and create a model that can accurately predict the sentiment review with at least 85% accuracy.

***Objective:***
1. Identify Good and Bad review from the Spotify Customer
2. Explore what content is related to the good review and bad review
3. Perform improvement strategy based on sentiment analysis


---

## Deployment

***Deployment URL***:  
https://huggingface.co/spaces/Muhammad-Daffa/Sentiment-Review-Prediction

---

## Dataset

The dataset is obtained from kaggle website. Each record in the file represents review from the customer with its rating label. The rating label indicates whether the customer tends to have a positive or negative sentiments.


https://www.kaggle.com/datasets/mfaaris/spotify-app-reviews-2022/data


---

## Project Output / Conclusion

The metric that will be focused for evaluating model is **Accuracy**. We want the model to **identify** correctly the type of sentiment of the review made by the customer.
Understanding the data is very important for our app improvement, where we are able to find out which are the good and bad topic about our application

Base and Improved Model Accuracy:

| Parameter     | Base Model | Improved Model|
| ----------- | ----------- |----------- |
| Train-set   | 0.51 | 0.9     |
| Test-set  | 0.51 | 0.88    |


***Business Recommendation:***  
As the model is a good-fit and well predicting the sentiment from review. The business recommendation are in the following:
- Focus more on Bad Sentiment/Topic and address the issues. Some of the Bad Review includes words "bug", "annoying", "issue", "fix", etc. This indicates several problem in application need to be addressed.

