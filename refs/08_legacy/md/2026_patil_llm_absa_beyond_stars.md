Beyond the Star Rating: A Scalable Framework for Aspect-Based Sentiment Analysis Using LLMs and Text Classification 

Vishal Patil, Shree Vaishnavi Bacha, Revanth Yamani, Yidan Sun, Mayank Kejriwal 

University of Southern California, Marina del Rey, 90292, CA, USA. 

*Corresponding author(s). E-mail(s): kejriwal@isi.edu; Contributing authors: vspatil@usc.edu; sbacha@usc.edu; yamani@usc.edu; yidans@isi.edu; 

#### **Abstract** 

Customer-provided reviews have become an important source of information for business owners and other customers alike. However, effectively analyzing millions of unstructured reviews remains challenging. While large language models (LLMs) show promise for natural language understanding, their application to large-scale review analysis has been limited by computational costs and scalability concerns. This study proposes a hybrid approach that uses LLMs for aspect identification while employing classic machine-learning methods for sentiment classification at scale. Using ChatGPT to analyze sampled restaurant reviews, we identified key aspects of dining experiences and developed sentiment classifiers using human-labeled reviews, which we subsequently applied to 4.7 million reviews collected over 17 years from a major online platform. Regression analysis reveals that our machine-labeled aspects significantly explain variance in overall restaurant ratings across different aspects of dining experiences, cuisines, and geographical regions. Our findings demonstrate that combining LLMs with traditional machine learning approaches can effectively automate aspect-based sentiment analysis of large-scale customer feedback, suggesting a practical framework for both researchers and practitioners in the hospitality industry and potentially, other service sectors. 

**Keywords:** Yelp, multi-factor, aspect-based analysis, sentiment analysis, regression models, text classification, large language model 

1 

# **1 Introduction** 

Online review platforms have become influential in informing consumer decisions and impacting business outcomes, especially in the hospitality industry [1–3]. On platforms like Google Reviews, Yelp, and TripAdvisor, customers can now easily share their experiences with a broader audience through electronic word-of-mouth. Such platforms offer a structured way of publishing and disseminating reviews on official businesses [4], in contrast with ‘organic’ reviewing prevalent on social media channels such as Instagram and TikTok. The reliance on reviews-specific platforms has grown even more since the COVID-19 pandemic, with surveys indicating that the proportion of consumers who ‘always’ or ‘regularly’ read online reviews significantly increased, rising from 60% in 2020 to 75% in 2024 [5]. This growing dependence on online reviews has made maintaining a positive reputation and responding to customer feedback essential for long-term business success. For instance, a study found that a one-star increase in Yelp rating leads to a 5–9% increase in revenue [6]. Unsurprisingly, restaurateurs and hospitality managers have now come to rely heavily on these platforms to gather feedback and engage with customers [7]. 

The high volume of data on such platforms also makes them amenable to automated analysis [8]. Researchers have extensively examined the relationship between domain-relevant attributes (e.g., service, food quality) and their association with customer satisfaction in the hospitality industry, initially using frequency-based methods [1, 9] and later, machine learning approaches [10]. Such domain-relevant attributes, called _aspects_ , may only be implicitly present in reviews. Also, customers may view some aspects neutrally, while having significantly negative (or positive) sentiments on others. Figure 1 illustrates two restaurant reviews, showing specific dining aspects with associated sentiments. Rather than conveying a single overall sentiment, reviews often reflect mixed sentiments across aspects (e.g., positive ambiance but negative food or service in the second review). 

Earlier studies often relied on predefined aspects based on qualitative methods (such as grounded theory and thematic analysis [11–13]) to explore associations between various qualitative factors and overall customer satisfaction. However, manually analyzing large sets of unstructured and continuously updating review data is intractable, which motivates the need for automated aspect-mining and for extracting per-review sentiments associated with each mined aspect. This problem is denoted as _Aspect-Based Sentiment Analysis (ABSA)_ . Prior work has explored using topic modeling techniques such as Latent Semantic Allocation (LSA) [14] to automatically discover the aspects evaluated in reviews and measure how sentiments toward different aspects are expressed [15, 16]. In recent years, deep learning methods, especially transformer-based models, have yielded significant progress on this problem of [17]. More complicated tasks, such as simultaneously identifying aspects, the opinions expressing the sentiment toward those aspects, and their associated sentiment polarity, have also been studied [18, 19]. 

Despite these advances, obtaining good performance across large, unstructured sets of reviews remains a challenge, particularly when models need to adapt across different domains and geographies. Therefore, one interesting question is whether large language models (LLMs) can supplement aspect discovery and sentiment analysis. 

2 



**Fig. 1** : Example of aspect-based sentiment analysis on two restaurant reviews. Identified aspects in the review text, such as **service** , **food** , and **ambiance** , are highlighted in bold. Positive sentiments are highlighted in green, and negative sentiments in red. 

LLMs have shown promise in automating such tasks owing to background knowledge acquired through their massive pre-training, with applications in fields like law and healthcare [20, 21]. However, given the large corpora of real reviews collected across many different U.S. states over a considerable length of time, there are open questions around using LLMs directly for ABSA at scale. One challenge with using commercial LLMs is cost: prompting ChatGPT on millions of reviews is expensive, but may not be functionally necessary if cheaper machine learning methods can achieve similar performance without incurring high cost. We begin our study by evaluating the capability of a commercial LLM like ChatGPT [22] to automate ABSA in large-scale restaurant review datasets. We explore the premise that ChatGPT may be more useful for augmenting or replacing thematic analysis (identification of specific aspects), while sentiments on identified aspects could be reasonably predicted using off-the-shelf, locally deployable text classification tools that don’t require LLMs to be prompted millions of times. 

Because it involves both LLMs and local methods, any such architecture for ABSA is complex, involving several options for models, parameters and other ‘design choices.’ Our first methodological contribution is to demonstrate and evaluate potential design choices for a scalable, high-quality and cost-effective ABSA architecture that could be used for systematically coding the corpus of reviews for aspects and sentiments. Once designed, we use the architecture to process millions of reviews. We then demonstrate the collective utility of extracted aspects and their predicted sentiments for explaining the variance of _overall_ restaurant ratings. As shown in Figure 1, these overall ratings (e.g., on a scale of 1-5) are provided directly by users. However, a systematic study 

3 

at scale has thus far been lacking on quantitatively determining whether (and which) specific aspects and corresponding sentiments can _explain_ the variance in these ratings. With the background above in place, we state the following two goals: 

1. **Aspect identification and sentiment labeling:** We sample, identify, and categorize the key aspects from user reviews alone, using an LLM like ChatGPT, that could be potentially associated with actual user experiences. We also propose and validate scalable off-the-shelf text classification models to automatically extract sentiment labels in each review for each identified aspect. The final result is an ABSA architecture that makes judicious use of LLMs and local machine learning methods, and that we apply on millions of reviews from the Yelp platform. 

2. **Impact analysis on restaurant ratings:** Using the predicted aspect-sentiments, we specify and fit a regression model to determine whether the predicted aspects and sentiments can explain the variance in overall restaurants’ ratings. In other words, we aim to measure whether, despite the noise in the reviews and the implicit content in their text (where aspects and sentiments are usually only latent, if at all), aspects provide explanatory power for predicting why some restaurants are rated highly compared to others. The analysis is completely quantitative, and backed by rigorous statistical testing. Through further analysis of coefficients, we also aim to quantify the relative importance of different aspects and to assess the role, if any, that the noise in the automatic sentiment labeling process may have played in the final quality of the regression. 

We investigate these objectives by collecting and analyzing 4.7 million reviews published over a 17-year period from the Yelp online platform in the U.S. and Canada. Experimentally, we find that sentiment predictions based on ChatGPT-identified key aspects from customer reviews, which were trained on human annotations, can reliably account for much of the variance in reviewers’ final aggregate ratings. Our approach offers a framework for analyzing large volumes of customer feedback in the hospitality industry, with potential applications in other service sectors. 

# **2 Materials and Methods** 

## **2.1 Data** 

This study uses the Yelp Open Dataset [23], a publicly available representative sample of business, user, and review data provided by Yelp, spanning various metropolitan areas primarily in the United States and Canada. The dataset is organized into several JavaScript Object Notation (JSON) files, each representing a different entity (businesses, reviews, and users), which can be joined through unique identifiers. 

For this analysis, we primarily utilized the ‘review’ and ‘business’ files. The review file contains individual reviews, including the review text, rating (on a scale of 1-5), and timestamp, with each review uniquely identified and linked to a specific business. The ‘business’ file contains business information such as location, business categories, and other metadata, with each business uniquely identified. Since this study focuses exclusively on restaurant businesses, we first merged the two files using the business 

4 

identifier as the common key, then filtered the merged dataset to include only those businesses where ‘restaurant’ was listed in their ‘categories’ field. 

The final dataset spans from 2005 to 2022 and consists of 4,724,684 restaurant reviews written by 1,446,031 unique users for 52,286 distinct restaurant businesses. The data covers 17 U.S. states and one Canadian province, with Pennsylvania having the highest number of reviews at 1,100,276, while Montana had the fewest, with only six reviews. Across all restaurants, the average overall business rating is 3.793, while the average individual review rating is 3.794. The variables used in this study are detailed in Table 1. 

||**Fields Used in the Study**|
|---|---|
|**Variable**|**Description**|
|`review_id`|Unique identifier for each review|
|`user_id`|Unique identifier for each user|
|`business_id`|Unique identifier for each business|
|`review_rating`|Star rating assigned by the user to the business (1-5 scale)|
|`text`|Full text of the review provided by the user|
|`date`|Date when the review was submitted|
|`name`|Name of the business|
|`address`|Full address of the business|
|`city`|City where the business is located|
|`state`|U.S. state or Canadian province where the business is located|
|`postal_code`|Postal code of the business location|
|`overall_rating`|Average overall rating of the business (1-5 scale)|
|`review_count`|Total number of reviews the business has received|
|`categories`|List of categories or tags associated with the business (e.g., restaurant<br>types, services offered)|



**Table 1** : Description of variables from the Yelp Open Dataset used for analysis. 

## **2.2 Aspect Discovery and Inter-Annotator Consistency** 

To identify recurring aspects of dining experiences in customer reviews, we randomly selected 30 restaurants in California and sampled 20 reviews from each. These 600 reviews were input into two models, ChatGPT-4o and ChatGPT-4o mini, with the prompt: 

_‘From the customer reviews above, identify key aspects of the dining experience for labeling purposes. For each identified aspect, assign a rating to each review on a 5-point scale.’_ 

Table 2 presents representative examples of the key aspects identified by both models across five sample businesses (with business IDs masked). We evaluated both occurrences (how often an aspect was identified by either model) and inter-model agreement (the percentage of businesses where both models identified the same aspect) for each aspect. The most frequent aspects were _service_ (100% occurrence, 100% agreement), _food quality_ (96.67% occurrence, 93.10% agreement), _price_ (93.33% occurrence, 100% agreement), _atmosphere/ambiance_ (86.67% occurrence, 86.67% agreement), 

5 

_menu variety_ (66.67% occurrence, 83.33% agreement), and _wait time_ (63.33% occurrence, 65% agreement). Note that some minor aspects were consolidated under broader categories. For example, _boba quality_ or _sushi quality_ were classified under _food quality_ . Less frequent or lower agreement aspects (<50% occurrence or <60% agreement) included _portion sizes_ , _vegan options_ , and several others. 

||**GPT-4o**|
|---|---|
|**Bussiness ID**|**Extracted Aspects**|
|`cOoTI*******VZzdw`|Service, Food Quality, Atmosphere/Ambiance, Value for Money, Speed of Ser-<br>vice, Accuracy of Order, Drink Quality, Friendliness of Staff, Consistency, Special<br>Dietary Offerings|
|`2N9WH*******-qN_A`|Food Quality, Service, Beverage Quality, Ambiance, Price/Value, Accuracy of<br>Order, Consistency, Dietary Options, Wait time|
|`6EizP*******ZMI9Lw`|Service, Food Quality, Ambiance, Presentation, Value for Money, Timeliness, Menu<br>Variety, Consistency, Portion Size, Drink Selection|
|`cpaML*******_GXow`|Service,<br>Boba<br>Quality,<br>Price,<br>Sushi<br>Quality,<br>Location<br>Convenience,<br>Atmo-<br>sphere/Ambiance, Portion Size, Authenticity, Customization Options|
|`RXA9e*******KHyIQ`|Food Quality, Service, Atmosphere/Ambiance, Cleanliness, Portion Size, Value for<br>Money, Speed/Timeliness, Authenticity, Consistency, Curb Appeal, Recommenda-<br>tions, Specialty Items|



||**GPT-4o-mini**|
|---|---|
|**Bussiness ID**|**Extracted Aspects**|
|`cOoTI*******VZzdw`|Food Quality, Service, Ambiance, Wait time, Value for Money, Menu Variety,<br>Cleanliness, Staff Friendliness, Portion Size, Recommendation Likelihood|
|`2N9WH*******-qN_A`|Cupcake Quality, Service, Food Quality (general), Atmosphere/Ambiance, Coffee<br>Quality, Value for Money, Selection Variety, Overall Satisfaction|
|`6EizP*******ZMI9Lw`|Atmosphere/Ambiance, Food Quality, Service, Value for Money, Reservation Expe-<br>rience, Specific Dishes, Overall Experience|
|`cpaML*******_GXow`|Boba Quality, Sushi Quality, Service, Value for Money, Convenience, Variety of<br>Menu Options, Customer Loyalty|
|`RXA9e*******KHyIQ`|Food Quality, Cleanliness, Service, Atmosphere, Value for Money, Menu Variety,<br>Takeout Experience, Outdoor Seating, Recommendation Likelihood|



**Table 2** : Key aspects extracted by GPT-4o and 4o-mini for five randomly selected businesses based on customer reviews. Business IDs are partially masked. 

To validate these LLM-derived aspects, we conducted a comparative analysis using Latent Dirichlet Allocation (LDA)-based topic modeling [14]. LDA is a widely used probabilistic model for topic extraction from a large corpus of unstructured text. It assumes that each document is a mixture of a pre-specified number of latent variables (‘topics’), where each topic is defined by a distribution of words. The model operates as a hierarchical graphical model, where for each document, a topic distribution is sampled from a Dirichlet prior, and then individual words are generated by first selecting a topic and then sampling a word from that topic’s word distribution. LDA has been found to be empirically useful in scenarios where the bag-of-words assumption holds, as it can uncover the underlying thematic structure without considering word order or context. 

6 

|**Topic 1**|**Positive Sentiment Group**<br>great, food, place, service, restaurant, good, time, chicken, santa, chase|
|---|---|
|**Topic 2**|best, clam, chowder, waiter, manhattan, italian, barbara, santa, favorite, great|
|**Topic 3**|delicious, food, perfect, place, kitchen, great, love, cherry, little, half|
|**Topic 4**|great, place, food, service, lunch, loved, drink, cheese, jonathan, good|
|**Topic 5**|calamari, happy, hour, appetizer, great, drink, chicken, bartender, day, good|



||**Negative Sentiment Group**|
|---|---|
|**Topic 1**|service, table, food, like, experience, place, completely, water, poached, came|
|**Topic 2**|overpriced, customer, service, view, star, mgmt, zero, place, building, need|
|**Topic 3**|dish, waiter, suggested, meat, salmon, bone, dry, fresh, specifically, fish|
|**Topic 4**|steak, sauce, meal, good, great, view, probably, beach, window, best|
|**Topic 5**|breakfast, drink, wait, free, hyatt, believe, restaurant, waited, pay, hotel|
||**Neutral Sentiment Group**|
|**Topic 1**|ordered, good, sauce, salad, dessert, restaurant, asked, veal, really, cannoli|
|**Topic 2**|fry, nice, price, plate, restaurant, way, lot, service, drop, soft|
|**Topic 3**|food, waitress, restaurant, party, look, place, great, overall, pretty, chicken|
|**Topic 4**|food, extra, sauce, charge, like, want, ask, minute, sat, place|
|**Topic 5**|food, restaurant, service, place, table, great, good, time, really, like|



**Table 3** : Examples of the most relevant words in topics generated by Latent Dirichlet Allocation (LDA) across the three sentiment groups (positive, negative, neutral) for restaurant reviews. Each group consists of five topics, with the ten most frequently associated words shown for each topic. 

In our analysis, we applied LDA to a subset of 211,747 reviews from Californiabased businesses, representing 4.48% of the overall dataset. Reviews were divided into three sentiment categories based on user ratings: positive (ratings above 3), negative (ratings below 3), and neutral (ratings equal to 3). Within each sentiment category, reviews were grouped by restaurant, and LDA was applied to extract five topics per restaurant. Each topic was defined by the ten most relevant words based on their contribution to the topic’s word distribution. 

The topics generated frequently included food-related words (e.g., ‘meat,’ ‘fish,’ ‘dry,’ and ‘fresh,’); albeit, these words were not tied to particular aspects of the dining experience. Besides, general sentiment words like ‘good,’ ‘great,’ and ‘like’ were common, although their specific context within the reviews was unclear. Words related to less frequently mentioned aspects, such as _ambiance_ or _menu variety_ , appeared less consistently across the topics. Given these limitations, we chose to focus on the six key aspects extracted by ChatGPT– _service_ , _food quality_ , _ambiance_ , _wait time_ , _price_ , and _menu variety_ . The LDA output, including the most relevant words for each sentiment group, is summarized in Table 3. 

To construct sentiment classification models for each identified aspect, we created a labeled dataset for training and evaluation. We started by randomly selecting 5,000 reviews from the full dataset of 4,724,684 reviews, including 1,899 5-star reviews (38.0%), 1,228 4-star reviews (24.6%), 657 3-star reviews (13.1%), 506 2-star reviews (10.1%), and 710 1-star reviews (14.2%). Five annotators independently scored the sentiment of 1,000 randomly assigned reviews for each aspect as positive (+1), neutral 

7 

|**Review**|**Service**|**Food**<br>**Quality**|**Ambiance**|**Wait**<br>**Time**|**Price**|**Menu**<br>**Variety**|
|---|---|---|---|---|---|---|
|The New Mexican style cuisine here is<br>damn good. I love the breakfast, espe-<br>cially with a bloody mary. Yum! The<br>green and red sauces are delicious but<br>SPICY so if you don’t like spice con-<br>sider the sour cream green chili sauce,<br>or half and half. The staff are pretty<br>great too.|1|1|NA|NA|NA|1|
|Great atmosphere, very cool looking on<br>the inside, makes you think you are in<br>a submarine or that’s how I see it. Food<br>was good and they have many beers<br>on tap. The only downside was slow<br>service, but maybe it was just a tough<br>night for the staff. Besides that, a great<br>place to come with friends or family.|-1|1|1|NA|0|1|
|Really good fries. . . about a dozen vari-<br>eties from Spanish, Irish, Mexican,<br>pizza & more. Wings (their specialty)<br>were great. Our waitress, Camilla, was<br>quick, attentive, friendly & helpful.<br>Plus she was as cute as a button. Bath-<br>rooms were clean. 50% off wings if you<br>check in on Yelp!! We shall return.|1|1|1|1|1|1|
|The one positive: the view. Service<br>was horrible, the drinks watered down<br>and the food was horrible. Order beer<br>by the bottle and don’t expect much<br>beyond a cool location.|-1|-1|1|NA|NA|NA|



**Table 4** : Example of sentiment labels for reviews assigned by one reviewer, with aspects rated by sentiment score: -1 (negative), 0 (neutral), 1 (positive), and ‘NA’ for ‘irrelevant’. 

(0), or negative (-1). When a review did not discuss a particular aspect, it was marked as ‘irrelevant’ (N/A), since not every review addressed all six aspects being evaluated. 

To assess the consistency of sentiment evaluations among annotators, we randomly selected 20 reviews from our 5,000-review dataset and had all annotators evaluate each aspect. Table 4 illustrates sentiment scores assigned by one annotator for four example reviews. We measured inter-annotator agreement using Fleiss’ Kappa with the `statsmodels` package in Python [24]. Fleiss’ Kappa [25] is a measure of inter-rater agreement for categorical items. It is calculated using the formula: 



Here, _Po_ represents the proportion of observed agreement among raters, and _Pe_ represents the proportion of agreement expected by chance. Fleiss’ Kappa values range from -1 to 1, where _κ_ = 1 represents perfect agreement, _κ_ = 0 indicates agreement no better than chance, and negative values suggest worse-than-chance agreement. Values between 0.61-0.80 are typically considered substantial agreement, while values above 

8 

0.80 indicate almost perfect agreement[26]. _Price_ shows nearly perfect agreement ( _κ_ = 0 _._ 943), followed by _menu variety_ ( _κ_ = 0 _._ 789), _food quality_ ( _κ_ = 0 _._ 774), _service_ ( _κ_ = 0 _._ 727), and _ambiance/atmosphere_ ( _κ_ = 0 _._ 675). _Wait time_ showed moderate agreement ( _κ_ = 0 _._ 460). 

As a complementary measure of inter-rater reliability, we also calculated Pearson’s correlation coefficient [27]. The correlation analysis showed high consistency across most aspects, with _price_ showing the highest correlation ( _µ_ = 0 _._ 918 _, p <_ 0 _._ 01) and _wait time_ showing the lowest but still significant correlation ( _µ_ = 0 _._ 745 _, p <_ 0 _._ 05). Hence, both methods consistently indicate strong inter-annotator agreement across most aspects. 

|**Ser**|**vice** (M|ean = 0.|855, p|< 0.05)||**Foo**|**d Quality** (Me|an = 0.8|83, p <|0.01)|
|---|---|---|---|---|---|---|---|---|---|---|
||A1|A2|A3|A4|A5||A1<br>A2|A3|A4|A5|
|A1|1|.83<sup>***</sup>|.95<sup>***</sup>|.88<sup>***</sup>|.78<sup>***</sup>|A1|1<br>.90<sup>***</sup>|.92<sup>***</sup>|.86<sup>***</sup>|.82<sup>***</sup>|
|A2||1|.91<sup>***</sup>|.84<sup>***</sup><br>|.83<sup>***</sup><br>|A2|1|.92<sup>***</sup>|.90<sup>***</sup><br>|.92<sup>***</sup><br>|
|A3|||1|.90<sup>***</sup>|.85<sup>***</sup>|A3||1|.81<sup>***</sup>|.90<sup>***</sup>|
|A4||||1|.85<sup>***</sup>|A4|||1|.88<sup>***</sup>|
|A5|||||1|A5||||1|
|**Am**|**biance**|(Mean =|0.864,|p < 0.05|)|**Wa**|**it Time** (Mean|= 0.745,|p < 0.|05)|
||A1|A2|A3|A4|A5||A1<br>A2|A3|A4|A5|
|A1|1|.90<sup>***</sup>|.98<sup>***</sup>|.79<sup>***</sup>|.98<sup>***</sup>|A1|1<br>.80<sup>***</sup>|.54<sup>*</sup>|.80<sup>***</sup>|.90<sup>***</sup>|
|A2||1|.91<sup>***</sup>|.72<sup>***</sup>|.96<sup>***</sup>|A2|1|.52<sup>*</sup>|.85<sup>***</sup>|.92<sup>***</sup>|
|A3|||1|.72<sup>***</sup>|.95<sup>***</sup>|A3||1|.55<sup>*</sup>|.61<sup>**</sup>|
|A4||||1|.75<sup>***</sup>|A4|||1|.88<sup>***</sup>|
|A5|||||1|A5||||1|
|**Pri**|**ce** (Me|an = 0.91|8, p <|0.01)||**Me**|**nu Variety** (Me|an = 0.8|72, p <|0.05)|
||A1|A2|A3|A4|A5||A1<br>A2|A3|A4|A5|
|A1|1|.94<sup>***</sup>|.91<sup>***</sup>|.99<sup>***</sup>|.98<sup>***</sup>|A1|1<br>.90<sup>***</sup>|.89<sup>***</sup>|.85<sup>***</sup>|.96<sup>***</sup>|
|A2||1|.85<sup>***</sup>|.91<sup>***</sup>|.92<sup>***</sup>|A2|1|.86<sup>***</sup>|.84<sup>***</sup>|.88<sup>***</sup>|
|A3|||1|.90<sup>***</sup>|.93<sup>***</sup>|A3||1|.82<sup>***</sup>|.88<sup>***</sup>|
|A4||||1|.96<sup>***</sup>|A4|||1|.90<sup>***</sup>|
|A5|||||1|A5||||1|
|||||*p < 0.0|5, **p <|0.01, **|*p < 0.001||||



**Table 5** : Inter-annotator agreement results measured by pairwise Pearson correlations across six dining aspects: _service_ , _food quality_ , _ambiance_ , _wait time_ , _price_ , and _menu variety_ . 

## **2.3 Text Vectorization** 

We partitioned our 5000-review labeled dataset into training (80%, 4,000 reviews) and validation (20%, 1,000 reviews) sets. Using the `nltk` library [28], we removed all punctuation and special characters, converted text to lowercase, eliminated common stopwords, and applied lemmatization to reduce words to their base forms. 

9 

We experimented with two text vectorization methods: TF-IDF (Term FrequencyInverse Document Frequency) and fastText. For TF-IDF, We used `Scikit-learn` ’s TF-IDF framework to transform the corpus into 400-dimensional feature vectors, while retaining default settings for other parameters. To address the inherent class imbalance in the dataset, we generated two sets of TF-IDF features: one preserving the original class distribution and another balanced using the Synthetic Minority Over-sampling Technique (SMOTE) [29]. SMOTE creates synthetic samples for minority classes by interpolating between existing instances, thus mitigating the impact of class imbalance on model performance. 

For the fastText approach, we trained a custom model on our corpus of 4.7 million reviews. We implemented the skip-gram algorithm with character n-grams ranging from sizes 3 to 6, generating 100-dimensional output vectors [30]. To assess the quality of the learned word representations, we conducted nearest-neighbor queries and analyzed the semantic similarity of neighboring words. For each review, we computed the L2-normalized element-wise mean of its constituent word vectors to obtain a fixed-size feature representation. FastText was implemented using Python’s `fastText` package. 

## **2.4 Classification Models and Architectures for Sentiment Labeling** 

We evaluated four established classification models using the aforementioned vectorization methods: _Multinomial Naive Bayes_ [31], _Logistic Regression_ [32], _Random Forest_ [33], and _Support Vector Machine (SVM)_ [34]. All models were implemented using the `Scikit-learn` library [35]. We evaluate the models using accuracy as an overall performance metric, and also calculate precision, recall, and F1-score to assess performance for each sentiment class (positive, neutral, negative). In classification tasks, accuracy is defined as the ratio of correctly predicted instances to the total number of instances (Accuracy = TrueTotalPositivesNumber+Trueof InstancesNegatives ). For each sentiment class, _precision_ measures how many of the predicted instances for that class were correct (Precision = <u>True Positives</u> True Positives + False Positives<sup>), while</sup><sup>_recall_measures how many of the actual instances</sup> of that class were correctly identified (Recall = True PositivesTrue <u>Positives+</u> False Negatives<sup>).TheF1-</sup> score combines these metrics using the harmonic mean (F1 = 2 _×_ PrecisionPrecision _<u>×</u>_ +RecallRecall<sup>).</sup> All metrics were computed using the `Scikit-learn` library [35]. 

Since not all reviews discussed the six aspects, a key design choice is whether and how to include reviews that do not mention the target aspects (marked as irrelevant) in the training process. Based on our selected vectorization and classification methods from the previous step, we consider two reasonable approaches: 

### **_One-Stage Classifier_** 

For each aspect, this model treats reviews not mentioning that aspect as neutral, using a three-point sentiment scale: -1 (negative), 0 (neutral/irrelevant), or 1 (positive). Using the labeled dataset of 5000 reviews, we trained fastText embeddings after preprocessing and split the data into 80% training and 20% validation sets. For each aspect ( _service_ , _food quality_ , _ambiance_ , _wait time_ , _price_ , and _menu variety_ ), a 

10 

multinomial logistic regression model predicts sentiment probabilities across the three classes. 

### **_Two-Stage Classifier_** 

This approach separates relevance and sentiment classification for each aspect: 

- **Stage 1 (Relevance):** Using the same dataset of 5000 reviews, we created binary labels (relevant/irrelevant) for each aspect based on whether reviews mentioned that aspect. After training fastText embeddings on the preprocessed data, we developed a binomial logistic regression model to classify aspect relevance using an 80-20 trainvalidation split. 

- **Stage 2 (Sentiment):** For each aspect, using only reviews that mentioned it, we trained another fastText embedding model and a multinomial logistic regression classifier to categorize aspect-specific sentiments as negative (-1), neutral (0), or positive (1). To address the class imbalance, random oversampling was applied to the minority class during training for each aspect. 

Both architectures predict the sentiment of each aspect independently and produce a 6-dimensional sentiment vector for each review, corresponding to the six aspects ( _service_ , _food quality_ , _ambiance_ , _wait time_ , _price_ , and _menu variety_ ). 

To generate predictions on the full Yelp restaurant dataset of 4.7 million reviews, we first processed all reviews through trained fastText embeddings. These embeddings were then input into two classifiers in parallel. The one-stage classifier directly predicts sentiment for each review. The two-stage classifier operates sequentially: in the first stage, it classifies each review as either relevant or irrelevant for each aspect. Only reviews marked as relevant proceed to the second stage, where their sentiment is determined; irrelevant reviews receive a neutral rating. 

Due to the different evaluation frameworks of the one-stage and two-stage classifiers, a direct comparison is non-trivial. To enable a fair comparison, we first filter the one-stage classifier’s predictions to include only those reviews relevant to each specific aspect. For example, for the _service_ aspect, we identified 664 reviews out of the 1000 validation-set reviews as relevant based on ground-truth labels and filtered the one-stage classifier’s predictions of these reviews. Similarly, the Stage 2 predictions of the two-stage classifier were generated using the same set of relevant reviews, which makes a direct comparison possible. 

To evaluate the performance differences between the two classifiers, we used the McNemar test [36]. This test is suited for cases where two models are applied to the same dataset, and the goal is to assess whether there is a statistically significant difference in their predictions. Let _n_ 01 represent the number of instances where the one-stage classifier made an incorrect prediction and the two-stage classifier made a correct prediction, and _n_ 10 represent the number of instances where the one-stage classifier made a correct prediction and the two-stage classifier made an incorrect prediction. The McNemar test evaluates whether the difference between these two counts is significant. The test statistic is computed as: 

11 

_χ_<sup>2</sup> =<sup><u>(</u></sup><sup>_n_01</sup><sup>_−n_10)2</sup> _n_ 01 + _n_ 10 

Under the null hypothesis that Stage 2 of the two-stage classifier performs no better than the one-stage classifier, this test statistic follows a chi-square distribution with one degree of freedom. We conducted a one-sided McNemar test using the `statsmodels` package [24] in Python to evaluate whether Stage 2 of the two-stage classifier significantly outperforms the one-stage classifier ( _α_ = 0 _._ 05). This is a critical design choice for determining the final architecture that we use for conducting ABSA over millions of reviews in the full corpus. 

## **2.5 Regression Models** 

To prepare for regression analysis, we aggregated the review-level predictions at the restaurant level across the full dataset of 52,286 restaurants. For each restaurant, we computed six aspect-specific averages ( _service_ , _food quality_ , _ambiance_ , _wait time_ , _price_ , and _menu variety_ ) independently using all available reviews, based on predictions from both the one-stage and two-stage classifiers, respectively. These aspect-wise average ratings are continuous variables ranging from -1 to +1. 

To account for geographic and cuisine-type variations in the regression models, we included the ‘state’ variable from the original dataset to control for geographic differences, and also created a standardized ‘cuisine’ variable. We first extracted cuisine-related terms from the multi-category ‘category’ field using regular expressions, initially using known cuisine types (e.g., ‘Italian,’ ‘Chinese,’ ‘Mexican,’). We then normalized variations in naming conventions (e.g., ‘Italian Restaurant’ and ‘Traditional Italian’ were standardized to ‘Italian’). For restaurants with more than one ambiguous cuisine type, we determined the primary cuisine based on the first listed category, or manually reviewed the ambiguous categories to assign the most representative label. After standardization, we retained the ten most frequent cuisines based on their occurrence: American (28.19%), Italian (14.81%), Mexican (8.18%), Chinese (5.66%), Japanese (2.94%), Thai (1.43%), Mediterranean (1.85%), Indian (1.83%), Cajun/Creole (1.76%), and Vietnamese (1.16%). All other cuisines, accounting for about 32.15% of the dataset, were categorized as ‘Other’. Table 6 provides examples from the final aggregated dataset. 

To quantify the relationship between predicted aspect ratings and overall business ratings while accounting for other factors, we applied linear regression analysis [27] using R. The general regression model is specified as follows: 

12 

|**Business ID**|**Serv-**<br>**ice**|**Qual-**<br>**ity**|**Ambi-**<br>**ance**|**Wait**<br>**Time**|**Price**|**Menu**|**Over-**<br>**all**|**State**|**Cuisine**|
|---|---|---|---|---|---|---|---|---|---|
|I8...WsWA|0.53|0.80|0.46|0.00|0.06|0.00|4.5|NV|American|
|UJ...RlA|0.27|0.77|0.07|-0.01|-0.01|0.03|4.5|LA|Indian|
|2L...dzw|-0.84|-0.30|0.00|-0.15|0.00|0.00|1.5|FL|Other|
|8T...FMg|0.25|0.50|0.06|-0.01|0.00|0.01|3.5|PA|Italian|
|BF...sQ|0.19|0.80|0.00|-0.01|0.01|0.03|4.0|FL|Mediter-<br>ranean|



**Table 6** : Example average predicted ratings for each restaurant across six aspects: _service_ , _food quality(quality)_ , _ambiance_ , _wait time_ , _price_ , and _menu variety (menu)_ The Overall column represents the restaurant’s overall rating. Business IDs are partially masked for anonymity, and the _State_ and _Cuisine_ columns indicate the location and main cuisine type offered, respectively. 

Overall rating = _β_ 0 



The term<sup>�</sup> _j_<sup>_γjXj_representsdifferentsetsofcontrolvariablesacrossfour</sup> regression model specifications: 

- Model 1 (Base): No controls ( _Xj_ = 0); 

- Model 2 (Cuisine-Controlled): Controls for cuisine types ( _Xj_ = _X_ cuisine); 

- Model 3 (State-Controlled): Controls for state ( _Xj_ = _X_ state); 

- Model 4 (Fully-Controlled): Controls for both cuisine and state ( _Xj_ = _X_ cuisine + _X_ state). 

Here, _β_ 0 is the intercept, _β_ 1 to _β_ 6 represent the expected changes in the overall rating for a one-unit increase in each corresponding aspect rating, holding other variables constant, and _ϵ_ denotes the error term. All four models were fitted using both the one-stage and two-stage classifier predictions separately. The complete workflow of our methodology, including data preparation, classification architectures, and regression analysis, is summarized in Figure 5 in the Appendices. 

13 

# **3 Results** 

## **3.1 Aspect Identification and Sentiment Labeling** 

Using the 5,000 labeled reviews, we evaluated four classification models across six attributes – _service_ , _food quality_ , _ambiance_ , _wait time_ , _price_ , and _menu variety_ – with two text vectorization methods. Figure 2 shows the average classification accuracy of each model across all six aspects, while Tables 10 and 11 in the Appendices detail the breakdown of each model’s performance, including precision, recall, F1-scores, and support for each sentiment category within each aspect. Among these models, SVM had the highest average accuracy (0.768) across all methods, followed by logistic regression (0.766) with fastText, random forest (0.758) with TF-IDF (class imbalance adjusted), and naive Bayes, which performed best with TF-IDF (0.730) but was incompatible with fastText. 



**Fig. 2** : Average classification accuracy of machine learning algorithms using different text vectorization methods (TF-IDF with and without class imbalance adjustment, and fastText) across all six aspects. 

Figure 3 shows the F1-scores of logistic regression and SVM with two vectorization methods. Despite its high accuracy, SVM showed significant limitations. With TFIDF (without class imbalance adjustment), SVM failed to predict any negative reviews for _ambiance_ and _menu variety_ and could not predict positive reviews for _wait time_ with the class imbalance adjusted. Using fastText, SVM also missed both positive and negative predictions for _price_ , positive predictions for _wait time_ , and negative predictions for _ambiance_ and _menu variety_ . Additionally, SVM was computationally slow on the full dataset (4.7 million reviews) and was even inefficient with the 5,000sample subset. Logistic regression, while 0.002 points lower in accuracy, only failed 

14 

to predict negative reviews for _menu variety_ . Considering accuracy, robustness, and computational efficiency, we selected logistic regression with fastText as our final model for both one-stage and two-stage classifiers. 



**Fig. 3** : Performance comparison of machine learning models across restaurant review aspects and sentiment classifications. This figure presents F1-scores and overall accuracy for Support Vector Machines (SVM), Logistic Regression (L.R.), and different vectorization approaches (TF-IDF with/without class imbalance handling, and FastText) across six restaurant aspects. For each aspect, F1-scores are shown for three sentiment categories (Negative, Neutral/Irrelevant, Positive). 

Tables 7 and 8 present the performance metrics for the one-stage and two-stage classifiers across six restaurant aspects. On accuracy, the one-stage classifier demonstrates consistent performance, with accuracy ranging from 0.73 for _service_ to 0.85 for _wait time_ . In the two-stage classifier, Stage 1 achieves strong performance with accuracies between 0.71 for _price_ and 0.91 for _food quality_ . However, Stage 2, despite being trained exclusively on relevant reviews, generally underperforms the one-stage classifier, with accuracies ranging from 0.61 for _wait time_ to 0.76 for _service_ and _food quality_ . Besides, Stage 2 of the two-stage classifier improves in detecting negative sentiments compared to one-stage classifier, with F1-scores increasing by an average of 0.31 (e.g., from 0.23 to 0.71 for _price_ and from 0 to 0.53 for _menu_ ), but shows significant reduction in F1-scores on neutral class detection, with an average decrease of 0.39 e.g., from 0.86 to 0.42 for _price_ , and 0.92 to 0.39 for _wait time_ . 

We also observed that the sentiment distribution in some categories is skewed. For instance, _food quality_ includes mostly positive reviews (621 positives vs. 160 negatives and 219 neutrals), while _wait time_ is predominantly neutral or irrelevant (838 neutrals 

15 

vs. 78 positives and 84 negatives). Precision and recall appear higher for categories with larger sample sizes in both classifiers—such as positive _food quality_ —compared to smaller classes, like negative _menu_ , which has only 26 samples. This sample size effect seems more noticeable in the one-stage classifier than in Stage 2 of the two-stage classifier. 

As stated earlier in Section 2, because the one-stage and two-stage classifiers are based on different premises, it is not straightforward to directly compare their performance. To ensure fair evaluation, we subset the one-stage predictions to include only relevant reviews and compared them with the Stage 2 predictions of the twostage classifier, which also focused exclusively on relevant reviews. One-sided McNemar tests revealed that the one-stage classifier significantly outperformed Stage 2 across all aspects, even within this controlled comparison. The strongest performance difference was observed for food quality ( _χ_<sup>2</sup> = 220 _._ 00, _p <_ 0 _._ 001), followed by ambiance/atmosphere ( _χ_<sup>2</sup> = 117 _._ 00, _p <_ 0 _._ 001), wait time ( _χ_<sup>2</sup> = 83 _._ 00, _p <_ 0 _._ 001), price ( _χ_<sup>2</sup> = 81 _._ 00, _p <_ 0 _._ 001), and menu variety ( _χ_<sup>2</sup> = 73 _._ 00, _p <_ 0 _._ 001). Even the smallest effect, observed for service ( _χ_<sup>2</sup> = 13 _._ 36, _p <_ 0 _._ 001), remained highly significant. 

|||**One-St**<br>|**age Classifi**<br>|**ier**<br>|||
|---|---|---|---|---|---|---|
|**Metric**|**Service**|**Ambiance**|**Quality**|**Menu**|**Wait Time**|**Price**|
|**Negative**|||||||
|Precision|0.81|0.62|0.68|0|0.64|0.79|
|Recall|0.75|0.11|0.58|0|0.46|0.13|
|F1-Score|0.78|0.19|0.63|0|0.54|0.23|
|Support|191|45|160|26|84|82|
|**Neutral/ I**<br>|**rrelevant**<br>||||||
|Precision|0.67|0.78|0.60|0.77|0.87|0.76|
|Recall|0.72|0.90|0.46|0.94|0.97|0.98|
|F1-Score|0.69|0.83|0.52|0.85|0.92|0.86|
|Support|398|692|219|737|838|734|
|**Positive**|||||||
|Precision|0.75|0.61|0.84|0.55|0.40|0.57|
|Recall|0.72|0.46|0.94|0.23|0.03|0.11|
|F1-Score|0.73|0.52|0.89|0.32|0.05|0.18|
|Support|411|263|621|237|78|184|
|**Accuracy**|0.73|0.74|0.78|0.75|0.85|0.75|



**Table 7** : Performance metrics, including accuracy, class-specific precision, recall, and F1-score, with support of the one-stage classifier across six aspects of restaurant reviews: _service, ambiance, food quality, menu, wait time,_ and _price_ . 

## **3.2 Impact of review aspects on overall restaurant ratings** 

To address our second research objective, we applied both the one-stage and two-stage classifiers to predict sentiment labels across all 4.7 million reviews. For each aspect, the one-stage classifier directly predicted sentiment as negative, neutral, or positive. The two-stage classifier first classified reviews as relevant or irrelevant, then predicted sentiment only for the relevant ones. Table 9 presents regression results based on the 

16 

|||**Two-St**|**age Classii**|**fier**|||
|---|---|---|---|---|---|---|
|**Metric**|**Service**|**Ambiance**|**Quality**|**Menu**|**Wait Time**|**Price**|
|||**Stage **|**1: Relevan**|**ce**|||
|**Relevant**|||||||
|Precision|0.76|0.75|0.91|0.69|0.73|0.82|
|Recall|0.94|0.47|1|0.12|0.17|0.06|
|F1-Score|0.84|0.58|0.95|0.21|0.27|0.11|
|Support|664|371|899|296|216|303|
|**Irrelevant**|||||||
|Precision|0.77|0.75|0.86|0.73|0.81|0.71|
|Recall|0.40|0.91|0.12|0.98|0.98|0.99|
|F1-Score|0.53|0.82|0.21|0.83|0.89|0.83|
|Support|336|629|101|704|784|697|
|**Accuracy**|0.76|0.75|0.91|0.72|0.81|0.71|
|||**Stage **|**2: Sentime**|**nt**|||
|**Negative**|||||||
|Precision|0.87|0.46|0.68|0.45|0.79|0.69|
|Recall|0.78|0.73|0.74|0.65|0.74|0.72|
|F1-Score|0.82|0.57|0.71|0.53|0.77|0.71|
|Support|191|45|160|26|84|82|
|**Neutral**|||||||
|Precision|0.25|0.33|0.35|0.3|0.37|0.33|
|Recall|0.61|0.49|0.6|0.55|0.41|0.59|
|F1-Score|0.35|0.4|0.44|0.38|0.39|0.42|
|Support|62|63|118|33|54|37|
|**Positive**|||||||
|Precision|0.94|0.92|0.94|0.95|0.62|0.93|
|Recall|0.78|0.72|0.79|0.79|0.62|0.77|
|F1-Score|0.85|0.81|0.86|0.87|0.62|0.84|
|Support|411|263|621|237|78|184|
|**Accuracy**|0.76|0.68|0.76|0.75|0.61|0.73|



**Table 8** : Performance metrics, including accuracy, class-specific precision, recall, F1-score, and support for stage one (relevance classification (relevant vs. irrelevant), as well as sentiment classification (negative, neutral, positive). The two-stage classifier operates across six aspects of restaurant reviews: _service, ambiance, food quality, menu, wait time,_ and _price_ . Note that Stage 2 was trained exclusively on relevant reviews. 

one-stage classifier predictions, with the two-stage classifier results shown in Table 12 in the Appendices. Predictions from both classifiers demonstrated strong model fit in the regression analysis, with R-squared values for the one-stage classifier ranging from 0.814 to 0.819. 

Across all four models, _food quality_ consistently emerges as the strongest predictor of overall ratings, with coefficients ranging from 1.58 to 1.59 (all p-values < 0.001). _Service_ follows as the second most important factor, with coefficients between 0.74 and 0.78 (all p-values < 0.05). _Menu variety_ also shows a significant positive relationship, with coefficients ranging from 0.66 to 0.70 (all p-values < 0.001). In contrast, _ambiance_ has a negative effect, with coefficients between -0.31 and -0.27 (all p-values < 0.001). _Wait time_ shows a smaller positive effect, with coefficients between 0.18 and 0.24 (all p-values < 0.001), while _price_ does not show statistical significance in any model. 

17 

|**Aspect**|**Model 1**|**Model 2**|**Model 3**|**Model 4**|
|---|---|---|---|---|
|Service|0.75 (0.73, 0.77)***|0.74 (0.72, 0.76)***|0.78 (0.76, 0.80)***|0.77 (0.76, 0.79)***|
|Food Quality|1.58 (1.56, 1.60)***|1.59 (1.57, 1.60)***|1.58 (1.56, 1.60)***|1.58 (1.57, 1.60)***|
|Ambiance|-0.31 (-0.33, -0.29)***|-0.31 (-0.33, -0.28)***|-0.27 (-0.30, -0.25)***|-0.27 (-0.29, -0.25)***|
|Wait Time|0.22 (0.15, 0.28)***|0.24 (0.17, 0.30)***|0.18 (0.12, 0.25)***|0.22 (0.15, 0.28)***|
|Price|0.06 (-0.05, 0.17)|0.05 (-0.06, 0.16)|0.08 (-0.03, 0.19)|0.07 (-0.04, 0.18)|
|Menu Variety|0.69 (0.64, 0.74)***|0.70 (0.64, 0.75)***|0.66 (0.61, 0.72)***|0.67 (0.61, 0.72)***|
|_R_<sup>2</sup>|0.814|0.815|0.818|0.819|



**Table 9** : Regression coefficients predicting overall restaurant ratings (one-stage classifier). This table presents the estimated coefficients, 95% confidence intervals, and significance levels for the six aspects across four regression models. These aspects represent the primary predictors, while control variables (cuisine and state) are analyzed separately in Figure 4. *** indicates significance level of _p <_ 0 _._ 001. 

Model 2 suggests that cuisine type is a strong predictor of ratings. As shown in Fig. 4 (a), using American cuisine as the reference, most cuisines show significant positive associations. Italian cuisine has the strongest positive effect ( _β_ = 0.152, p < 0.001), followed by Chinese ( _β_ = 0.115, p < 0.001) cuisine. Thai cuisine is the only type showing a slightly negative effect ( _β_ = -0.004), though this effect is not statistically significant. 

Model 3 reveals significant variation in ratings across different states, suggesting the influence of regional factors. Fig. 4(b) indicates that, compared to the reference state (Alberta), Montana shows the largest positive effect ( _β_ = 0.873, p < 0.05), followed by Hawaii ( _β_ = 0.571, p > 0.05) and North Carolina ( _β_ = 0.409, p > 0.05), though the latter two are not statistically significant. Following these, New Jersey ( _β_ = 0.154, p < 0.001) and Delaware ( _β_ = 0.129, p < 0.001) show substantial and significant positive effects. The effect sizes for the remaining states are relatively similar, ranging from Arizona ( _β_ = 0.095) to Florida ( _β_ = 0.127), all with p < 0.001. Model 4, which includes both cuisine and state controls, yields similar results to Models 2 and 3. Sensitivity analyses using the two-stage classifier confirm these findings. 

# **4 Discussion** 

This study addressed two key objectives: (1) using a combination of LLMs and traditional text classification for aspect identification and sentiment labeling at scale, and (2) analyzing the relationship between aspect-based sentiments and overall restaurant ratings. Earlier approaches to customer review analysis primarily relied on frequencybased methods to assess aspects of customer satisfaction [1, 9]. As the volume of online reviews grew, more scalable methods for analysis became necessary. Topic modeling techniques, such as Latent Dirichlet Allocation (LDA) and Latent Semantic Analysis (LSA), became popular tools for discovering latent themes in large datasets without predefined categories. For example, Calheiros et al. [37] applied sentiment classification and LDA to eco-hotel reviews, finding moderate positive sentiments for food and stronger positive feedback for hospitality aspects. Similarly, Akhtar et al. [38] used sentiment classification and LDA to support the development of a hotel recommender system. Titov and McDonald [39] introduced topic models for fine-grained analysis of 

18 



**Fig. 4** : Visualization of control variable effects from the main regression models. Panel (a) shows the effects of _cuisine_ from Model 2, and panel (b) shows the effects of _state_ from Model 3. Horizontal bars represent effect sizes, with 95% confidence intervals shown as error bars. Categories are ordered by effect magnitude, with numerical estimates displayed alongside each bar. Gray bars indicate non-significant effects ( _p >_ 0 _._ 05). Significance levels: *** _p <_ 0 _._ 001, ** _p <_ 0 _._ 01, * _p <_ 0 _._ 05. 

online reviews. Jo and Oh [15] developed the Aspect and Sentiment Unification Model (ASUM) that identifies aspect-sentiment pairs (‘senti-aspects’) in reviews, achieving sentiment classification comparable to supervised methods without needing labeled data. Xu et al. [16] used latent semantic analysis on hotel reviews to reveal distinct drivers of satisfaction and dissatisfaction across hotel types. 

Advances in machine learning have led researchers to integrate traditional textmining methods with complex models, including convolutional (CNN) and recurrent neural networks (RNN), for analyzing reviews in the hospitality and tourism sectors. For example, Ma et al. [40] used deep learning to assess the informational value of userprovided photos in hotel reviews, showing that combining photos with text improved predictions of review helpfulness compared to using either text or photos alone. Agarwal et al. [41] applied RNNs and CNNs to classify customer feedback by sentiment and intent, such as complaints or suggestions. Hossain et al. [42] used a combined CNN-LSTM model to analyze restaurant reviews, structuring customer feedback data to assess perceptions of restaurant quality, particularly for online delivery services. 

More recently, transformer-based models like BERT and GPT have significantly advanced performance on ABSA [43, 44]. These models excel at adapting to word context within sentences, showing improved effectiveness in both aspect identification and sentiment classification, as demonstrated by Xu et al. [45] and Sun et al. [46]. ABSA’s applications have also broadened to include fields like product reviews [47], healthcare feedback [48], and legal analysis [49]. Within hospitality specifically, ABSA 

19 

has identified key drivers of satisfaction, with food quality, service, and ambiance frequently emerging as top factors [50, 51]. Ryu and Han [52] emphasized ambiance’s role in loyalty, while Namkung and Jang [50] demonstrated food quality’s impact on return intentions. Despite these advances, applying ABSA to large, unstructured datasets remains challenging due to noisy and ambiguous data [53]. Hybrid models combining rule-based and deep learning approaches show promise in improving sentiment classification accuracy for complex reviews [54]. 

In continuing this line of study while addressing our first objective, we explored whether large language models (LLMs) like ChatGPT can complement ABSA by generating refined aspect labels and sentiment scores when labeled data is sparse or inconsistent. Using ChatGPT, we identified six primary aspects ( _service_ , _food quality_ , _ambiance_ , _wait time_ , _price_ , and _menu variety_ ) across 600 sampled reviews, which are consistent with factors commonly discussed in the literature [9, 55]. The strong agreement between the two ChatGPT models supports the validity of this approach. To address the scalability challenge outlined in our introduction, we created a humanlabeled dataset of 5,000 reviews, which was then used to train a classifier applied to 4.7 million reviews. The strong annotator agreement analyses suggest that the machine-extracted themes were well-defined and consistently identifiable by human annotators. 

Addressing our second objective regarding the impact on restaurant ratings, our regression models demonstrated strong goodness-of-fit, with _R_<sup>2</sup> values above 0.8 across all model specifications. This indicates that the machine-labeled aspects can explain a substantial portion of the variance in restaurant ratings and other included variables, though high _R_<sup>2</sup> values do not imply causation. Consistent with prior studies of a smaller-scale or more qualitative nature [50, 56], food quality and service were the strongest predictors of restaurant ratings. We also found a small positive relationship between wait time and ratings, suggesting that longer waits may signal high demand rather than dissatisfaction, potentially supporting the ‘social proof’ theory where customers associate crowded venues with higher quality [57]. Ambiance, unexpectedly, showed a negative association with ratings, contrasting with previous findings such as Ryu and Han [52]. We, however, also note moderate annotator agreement ( _κ_ = 0 _._ 675), indicating some variability in labeled perceptions of ambiance, which may have influenced the model’s predictions. Future investigation is also warranted. 

We also found stronger positive correlations between Italian and Chinese cuisines and higher ratings than American cuisine. Regional differences in ratings were observed, likely influenced by local preferences, economic conditions, and market competition. While research on regional variations in restaurant ratings is limited, broader studies suggest market conditions significantly influence customer preferences [58]. The high estimates observed in Montana may be attributed to the limited sample size (only six data points). 

This study has several limitations. First, we focused on only six LLM-identified aspects, which may overlook other dimensions of customer experience, especially since our initial analysis was based on just 600 reviews. Additionally, potential biases from manual labeling or the limited geographic coverage of the Yelp dataset across states 

20 

cannot be entirely ruled out despite the high R-squared values observed in our regression models. Finally, while the one-stage classifier was effective for neutral/irrelevant classes, it struggled with detecting negative sentiments. The two-stage classifier performed better with negative sentiments but had limitations in identifying neutral classes. Since the models predict sentiments for each aspect separately, a hybrid model could be considered, which applies the classifier that performs better for each sentiment class and aspect rather than using either the one-stage or two-stage classifier uniformly across all sentiment classes and aspects. 

# **5 Conclusion and Future Directions** 

This study demonstrates the effectiveness of combining large language models with traditional machine learning approaches for analyzing customer feedback at scale in the restaurant business. We find that ChatGPT can effectively identify key aspects from customer reviews, while trained classifiers can reliably scale sentiment analysis across millions of reviews. The strong correlation between predicted aspect sentiments and overall restaurant ratings validates this approach, suggesting that automated methods can extract meaningful patterns from large-scale text data that traditionally required intensive qualitative analysis. Through regression analysis, we quantified the relative importance of different aspects and also found patterns such as the positive correlation between wait times and ratings, and regional variations in customer preferences. 

Our results suggest several promising directions for future research. First, the proposed architecture could be extended to other review platforms like Google Reviews or TripAdvisor for cross-platform comparison of customer sentiments. Building on studies like Xiang et al. [59] and Phillips et al. [60], researchers could also use the system to develop industry-specific ontologies from large-scale unstructured data. Beyond hospitality, our framework could be adapted for industries such as retail and healthcare, where customer feedback is important in service improvement [61, 62]. Additionally, studying temporal trends in aspect sentiments could reveal shifts in customer preferences and expectations, such as those influenced by events like COVID-19. 

**Conflicts of interest:** The authors have no conflicts of interest to declare. **Acknowledgments:** None. 

**Funding:** This work received no specific funding. 

**Data availability statement:** The Yelp data used for this study are available at https://www.yelp.com/dataset 

# **References** 

- [1] Xie, K.L., Zhang, Z., Zhang, Z.: The business value of online consumer reviews and management response to hotel performance. International Journal of Hospitality Management **43** , 1–12 (2014) 

- [2] Alalwan, A.A., Rana, N.P., Dwivedi, Y.K., Algharabat, R.: Social media in marketing: A review and analysis of the existing literature. Telematics and informatics **34** (7), 1177–1190 (2017) 

21 

- [3] Chevalier, J.A., Mayzlin, D.: The effect of word of mouth on sales: Online book reviews. Journal of marketing research **43** (3), 345–354 (2006) 

- [4] Schuckert, M., Liu, X., Law, R.: Hospitality and tourism online reviews: Recent trends and future directions. Journal of Travel & Tourism Marketing **32** (5), 608– 621 (2015) 

- [5] BrightLocal: Local Consumer Review Survey. https://www.brightlocal.com/ research/local-consumer-review-survey/#methodology. Accessed: 2024-09-30 

- [6] Luca, M.: Reviews, reputation, and revenue: The case of yelp. com. Com (March 15, 2016). Harvard Business School NOM Unit Working Paper (12-016) (2016) 

- [7] Kwok, L., Xie, K.L., Richards, T.: Thematic framework of online review research: A systematic analysis of contemporary literature on seven major hospitality and tourism journals. International Journal of Contemporary Hospitality Management **29** (1), 307–354 (2017) 

- [8] Hu, M., Liu, B.: Mining and summarizing customer reviews. In: Proceedings of the Tenth ACM SIGKDD International Conference on Knowledge Discovery and Data Mining, pp. 168–177 (2004) 

- [9] Pantelidis, I.S.: Electronic meal experience: A content analysis of online restaurant comments. Cornell Hospitality Quarterly **51** (4), 483–491 (2010) 

- [10] Zhao, Y., Xu, X., Wang, M.: Predicting overall customer satisfaction: Big data evidence from hotel online textual reviews. International journal of hospitality management **76** , 111–121 (2019) 

- [11] Corbin, J.M., Strauss, A.: Grounded theory research: Procedures, canons, and evaluative criteria. Qualitative sociology **13** (1), 3–21 (1990) 

- [12] Braun, V., Clarke, V.: Using thematic analysis in psychology. Qualitative research in psychology **3** (2), 77–101 (2006) 

- [13] Guest, G., MacQueen, K.M., Namey, E.E.: Applied Thematic Analysis. sage publications, ??? (2011) 

- [14] Blei, D.M., Ng, A.Y., Jordan, M.I.: Latent dirichlet allocation. Journal of machine Learning research **3** (Jan), 993–1022 (2003) 

- [15] Jo, Y., Oh, A.H.: Aspect and sentiment unification model for online review analysis. In: Proceedings of the Fourth ACM International Conference on Web Search and Data Mining, pp. 815–824 (2011) 

- [16] Xu, X., Li, Y.: The antecedents of customer satisfaction and dissatisfaction toward various types of hotels: A text mining approach. International journal of hospitality management **55** , 57–69 (2016) 

22 

- [17] Schouten, K., Frasincar, F.: Survey on aspect-level sentiment analysis. IEEE transactions on knowledge and data engineering **28** (3), 813–830 (2015) 

- [18] Binder, M., Heinrich, B., Klier, M., Obermeier, A., Schiller, A.P.R.: Explaining the stars: Aspect-based sentiment analysis of online customer reviews (2019) 

- [19] Do, H.H., Prasad, P.W., Maag, A., Alsadoon, A.: Deep learning for aspect-based sentiment analysis: a comparative review. Expert systems with applications **118** , 272–299 (2019) 

- [20] Drápal, J., Westermann, H., Savelka, J., _et al._ : Using large language models to support thematic analysis in empirical legal studies. In: JURIX, pp. 197–206 (2023) 

- [21] Mathis, W.S., Zhao, S., Pratt, N., Weleff, J., De Paoli, S.: Inductive thematic analysis of healthcare qualitative interviews using open-source large language models: How does it compare to traditional methods? Computer Methods and Programs in Biomedicine **255** , 108356 (2024) 

- [22] OpenAI: ChatGPT. https://chat.openai.com/. Accessed: 2024-11-04 (2024) 

- [23] Inc., Y.: Yelp Open Dataset. https://www.yelp.com/dataset. Accessed: 2024-0930 (2023) 

- [24] Seabold, S., Perktold, J.: Statsmodels: Econometric and statistical modeling with python. In: 9th Python in Science Conference (2010) 

- [25] Fleiss, J.L.: Measuring nominal scale agreement among many raters. Psychological bulletin **76** (5), 378 (1971) 

- [26] Landis, J.R., Koch, G.G.: An application of hierarchical kappa-type statistics in the assessment of majority agreement among multiple observers. Biometrics, 363–374 (1977) 

- [27] Freedman, D.A.: Statistical Models: Theory and Practice. cambridge university press, ??? (2009) 

- [28] NLTK Project: Natural Language Toolkit (NLTK). Accessed: 2024-06-26 (2023). https://www.nltk.org/api/nltk.html 

- [29] Lemaître, G., Nogueira, F., Aridas, C.K.: Imbalanced-learn: A Python Toolbox to Tackle the Curse of Imbalanced Datasets in Machine Learning. Accessed: 2024-0626 (2023). https://imbalanced-learn.org/stable/references/generated/imblearn. over_sampling.SMOTE.html 

- [30] Bojanowski, P., Grave, E., Joulin, A., Mikolov, T.: Enriching Word Vectors with Subword Information. Accessed: 2024-06-26 (2017). https://fasttext.cc 

23 

- [31] Kibriya, A.M., Frank, E., Pfahringer, B., Holmes, G.: Multinomial naive bayes for text categorization revisited. In: AI 2004: Advances in Artificial Intelligence: 17th Australian Joint Conference on Artificial Intelligence, Cairns, Australia, December 4-6, 2004. Proceedings 17, pp. 488–499 (2005). Springer 

- [32] Hosmer Jr, D.W., Lemeshow, S., Sturdivant, R.X.: Applied Logistic Regression. John Wiley & Sons, ??? (2013) 

- [33] Breiman, L.: Random forests. Machine learning **45** , 5–32 (2001) 

- [34] Hearst, M.A., Dumais, S.T., Osuna, E., Platt, J., Scholkopf, B.: Support vector machines. IEEE Intelligent Systems and their applications **13** (4), 18–28 (1998) 

- [35] Pedregosa, F., Varoquaux, G., Gramfort, A., Michel, V., Thirion, B., Grisel, O., Blondel, M., Prettenhofer, P., Weiss, R., Dubourg, V., _et al._ : Scikit-learn: Machine learning in python. the Journal of machine Learning research **12** , 2825–2830 (2011) 

- [36] McNemar, Q.: Note on the sampling error of the difference between correlated proportions or percentages. Psychometrika **12** (2), 153–157 (1947) 

- [37] Calheiros, A.C., Moro, S., Rita, P.: Sentiment classification of consumer-generated online reviews using topic modeling. Journal of Hospitality Marketing & Management **26** (7), 675–693 (2017) 

- [38] Akhtar, N., Zubair, N., Kumar, A., Ahmad, T.: Aspect based sentiment oriented summarization of hotel reviews. Procedia computer science **115** , 563–571 (2017) 

- [39] Titov, I., McDonald, R.: Modeling online reviews with multi-grain topic models. In: Proceedings of the 17th International Conference on World Wide Web, pp. 111–120 (2008) 

- [40] Ma, Y., Xiang, Z., Du, Q., Fan, W.: Effects of user-provided photos on hotel review helpfulness: An analytical approach with deep leaning. International Journal of Hospitality Management **71** , 120–131 (2018) 

- [41] Agarwal, S.: Deep learning-based sentiment analysis: Establishing customer dimension as the lifeblood of business management. Global Business Review **23** (1), 119–136 (2022) 

- [42] Hossain, N., Bhuiyan, M.R., Tumpa, Z.N., Hossain, S.A.: Sentiment analysis of restaurant reviews using combined cnn-lstm. In: 2020 11th International Conference on Computing, Communication and Networking Technologies (ICCCNT), pp. 1–5 (2020). IEEE 

- [43] Devlin, J.: Bert: Pre-training of deep bidirectional transformers for language understanding. arXiv preprint arXiv:1810.04805 (2018) 

24 

- [44] Radford, A., Wu, J., Child, R., Luan, D., Amodei, D., Sutskever, I., _et al._ : Language models are unsupervised multitask learners. OpenAI blog **1** (8), 9 (2019) 

- [45] Xu, H., Liu, B., Shu, L., Yu, P.S.: Bert post-training for review reading comprehension and aspect-based sentiment analysis. arXiv preprint arXiv:1904.02232 (2019) 

- [46] Sun, C., Huang, L., Qiu, X.: Utilizing bert for aspect-based sentiment analysis via constructing auxiliary sentence. arXiv preprint arXiv:1903.09588 (2019) 

- [47] Pontiki, M., Galanis, D., Papageorgiou, H., Androutsopoulos, I., Manandhar, S., Al-Smadi, M., Al-Ayyoub, M., Zhao, Y., Qin, B., De Clercq, O., _et al._ : Semeval2016 task 5: Aspect based sentiment analysis. In: International Workshop on Semantic Evaluation, pp. 19–30 (2016) 

- [48] Bansal, A., Kumar, N.: Aspect-based sentiment analysis using attribute extraction of hospital reviews. New Generation Computing **40** (4), 941–960 (2022) 

- [49] Mudalige, C.R., Karunarathna, D., Rajapaksha, I., Silva, N., Ratnayaka, G., Perera, A.S., Pathirana, R.: Sigmalaw-absa: dataset for aspect-based sentiment analysis in legal opinion texts. In: 2020 IEEE 15th International Conference on Industrial and Information Systems (ICIIS), pp. 488–493 (2020). IEEE 

- [50] Namkung, Y., Jang, S.: Does food quality really matter in restaurants? its impact on customer satisfaction and behavioral intentions. Journal of Hospitality & Tourism Research **31** (3), 387–409 (2007) 

- [51] Lin, I.Y., Mattila, A.S.: Restaurant servicescape, service encounter, and perceived congruency on customers’ emotions and satisfaction. Journal of hospitality marketing & management **19** (8), 819–841 (2010) 

- [52] Ryu, K., Han, H.: Influence of the quality of food, service, and physical environment on customer satisfaction and behavioral intention in quick-casual restaurants: Moderating role of perceived price. Journal of Hospitality & Tourism Research **34** (3), 310–329 (2010) 

- [53] Liu, H., Chatterjee, I., Zhou, M., Lu, X.S., Abusorrah, A.: Aspect-based sentiment analysis: A survey of deep learning methods. IEEE Transactions on Computational Social Systems **7** (6), 1358–1375 (2020) 

- [54] Ray, P., Chakrabarti, A.: A mixed approach of deep learning method and rulebased method to improve aspect level sentiment analysis. Applied Computing and Informatics **18** (1/2), 163–178 (2022) 

- [55] Zhang, Y., Cole, S.T.: Dimensions of lodging guest satisfaction among guests with mobility challenges: A mixed-method analysis of web-based texts. Tourism 

25 

Management **53** , 13–27 (2016) 

- [56] Barber, N., Goodman, R.J., Goh, B.K.: Restaurant consumers repeat patronage: A service quality concern. International Journal of Hospitality Management **30** (2), 329–336 (2011) 

- [57] Cai, H., Chen, Y., Fang, H.: Observational learning: Evidence from a randomized natural field experiment. American Economic Review **99** (3), 864–882 (2009) 

- [58] Parsa, H., Self, J., Sydnor-Busso, S., Yoon, H.J.: Why restaurants fail? part iithe impact of affiliation, location, and size on restaurant failures: Results from a survival analysis. Journal of Foodservice Business Research **14** (4), 360–379 (2011) 

- [59] Xiang, Z., Du, Q., Ma, Y., Fan, W.: A comparative analysis of major online review platforms: Implications for social media analytics in hospitality and tourism. Tourism Management **58** , 51–65 (2017) 

- [60] Phillips, P., Barnes, S., Zigan, K., Schegg, R.: Understanding the impact of online reviews on hotel performance: an empirical analysis. Journal of travel research **56** (2), 235–249 (2017) 

- [61] Meesala, A., Paul, J.: Service quality, consumer satisfaction and loyalty in hospitals: Thinking for the future. Journal of Retailing and Consumer Services **40** , 261–269 (2018) 

- [62] Caemmerer, B., Wilson, A.: Customer feedback mechanisms and organisational learning in service operations. International Journal of Operations & Production Management **30** (3), 288–311 (2010) 

# **Appendices** 

CONTINUED ON NEXT PAGE 

26 

||||**S**|**ervi**|**ce**|||**Foo**|**d Qu**|**ality**|||**Atm**|**osp**|**here**||
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|Model|Class|Prec|Rec|F1|Acc|Supp|Prec|Rec|F1|Acc|Supp|Prec|Rec|F1|Acc|Supp|
|MNB+TFIDF(w)|Pos<br>Neu|.66<br>.60|.71<br>.66|.68<br>.63|.65|411<br>398|.69<br>.62|.98<br>.29|.81<br>.39|.69|621<br>219|.75<br>.72|.17<br>.98|.28<br>.83|.72|263<br>692|
||Neg|.81|.50|.62||191|.74|.12|.21||160|.00|.00|.00||45|
|LR+TFIDF(w)|Pos|.74|.73|.73|.71|411|.80|.92|.86|.73|621|.60|.43|.50|.74|263|
||Neu|.67|.73|.73||398|.56|.41|.47||219|.78|.90|.84||692|
||Neg|.76|.59|.66||191|.59|.46|.51||160|1.00|.11|.20||45|
|RF+TFIDF(w)|Pos|.72|.82|.77|.74|411|.73|.96|.83|.71|621|.61|.33|.43|.74|263|
||Neu|.75|.76|.75||398|.61|.34|.44||219|.76|.94|.84||692|
||Neg|.78|.54|.64||191|.62|.23|.34||160|.00|.00|.00||45|
|SVM+TFIDF(w)|Pos|.76|.73|.75|.73|411|.78|.95|.85|.74|621|.63|.34|.44|.74|263|
||Neu|.69|.79|.73||398|.63|.41|.49||219|.76|.94|.84||692|
||Neg|.79|.62|.69||191|.65|.40|.49||160|.00|.00|.00||45|
|MNB+TFIDF(wo)|Pos|.69|.68|.68|.67|411|.86|.77|.82|.68|621|.44|.65|.52|.52|263|
||Neu|.63|.61|.62||398|.42|.47|.45||219|.81|.46|.59||692|
||Neg|.68|.76|.72||191|.49|.61|.54||160|.14|.67|.23||45|
|LR+TFIDF(wo)|Pos|.76|.71|.73|.72|411|.87|.77|.82|.68|621|.47|.59|.52|.60|263|
||Neu|.70|.73|.71||398|.42|.48|.45||219|.83|.61|.70||692|
||Neg|.69|.73|.71||191|.47|.59|.52||160|.14|.51|.22||45|
|RF+TFIDF(wo)|Pos|.73|.78|.76|.74|411|.79|.85|.82|.70|621|.52|.42|.47|.70|263|
||Neu|.77|.74|.76||398|.50|.46|.48||219|.76|.85|.80||692|
||Neg|.66|.62|.64||191|.52|.42|.46||160|.19|.09|.12||45|
|SVM+TFIDF(wo)|Pos|.76|.73|.75|.73|411|.79|.93|.86|.73|621|.63|.41|.50|.75|263|
||Neu|.68|.78|.73||398|.57|.39|.46||219|.77|.92|.84||692|
||Neg|.78|.62|.69||191|.58|.44|.50||160|.00|.00|.00||45|
|LR+FT|Pos|.75|.72|.73|.73|411|.84|.94|.89|.78|621|.61|.46|.52|.74|263|
||Neu|.67|.72|.69||398|.60|.46|.52||219|.78|.90|.83||692|
||Neg|.81|.75|.78||191|.68|.58|.63||160|.62|.11|.19||45|
|RF+FT|Pos|.73|.70|.72|.70|411|.79|.95|.86|.75|621|.66|.39|.49|.75|263|
||Neu|.64|.72|.68||398|.61|.37|.46||219|.76|.93|.84||692|
||Neg|.79|.66|.72||191|.64|.51|.57||160|.50|.02|.04||45|
|SVM+FT|Pos|.77|.75|.76|.73|411|.83|.95|.89|.79|621|.64|.48|.55|.75|263|
||Neu|.69|.73|.71||398|.66|.46|.54||219|.78|.91|.84||692|
||Neg|.80|.74|.77||191|.74|.64|.69||160|.00|.00|.00||45|



**Table 10** : Complete model evaluation results for sentiment classification. Results include Positive (Pos), Neutral (Neu), and Negative (Neg) sentiment metrics (Precision, Recall, F1, and Accuracy) across all model combinations: TF-IDF (with and without class imbalance) and FastText vectorization, paired with Multinomial Naive Bayes (MNB), Logistic Regression (LR), Random Forest (RF), and Support Vector Machines (SVM). Metrics are presented for the aspects: _Service_ , _Food Quality_ , and _Atmosphere_ . Class distributions are provided in the Support (Supp) column. 

||||**Wa**|**it T**|**ime**||||**Price**|||||**Men**|**u**||
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|Model|Class|Prec|Rec|F1|Acc|Supp|Prec|Rec|F1|Acc|Supp|Prec|Rec|F1|Acc|Supp|
|MNB+TFIDF(w)|Pos<br>|.00|.00|.00|.85|78|.00<br>|.00|.00|.73|184<br>|.86<br>|.03|.05|.74|237<br>|
||Neu<br>|.85|1.00|.92||838|.73|1.00|.85||734|.74|1.00|.85||737|
||Neg|.81|.20|.32||84|.00|.00|.00||82|.00|.00|.00||26|
|LR+TFIDF(w)|Pos<br>|.73<br>|.10<br>|.18<br>|.86|78<br>|.58<br>|.16<br>|.25<br>|.75|184<br>|.55<br>|.30<br>|.39<br>|.75|237<br>|
||Neu|.87|.98|.93||838|.77|.98|.86||734|.79|.93|.85||737|
||Neg|.67|.37|.48||84|.64|.09|.15||82|.00|.00|.00||26|
|RF+TFIDF(w)|Pos|.00|.00|.00|.86|78|.67|.13|.22|.75|184|.64|.16|.25|.75|237|
||Neu|.86|1.00|.93||838|.75|.99|.86||734|.76|.97|.85||737|
||Neg|.85|.35|.49||84|.00|.00|.00||82|.00|.00|.00||26|
|SVM+TFIDF(w)|Pos|.00|.00|.00|.86|78|.67|.10|.17|.74|184|.61|.17|.26|.75|237|
||Neu|.86|.99|.92||838|.75|.99|.85||734|.76|.97|.85||737|
||Neg|.75|.32|.45||84|.67|.02|.05||82|.00|.00|.00||26|
|MNB+TFIDF(wo)|Pos|.18|.55|.28|.65|78|.28|.57|.37|.46|184|.39|.68|.49|.52|237|
||Neu|.93|.66|.77||838|.79|.41|.54||734|.83|.46|.60||737|
||Neg|.34|.71|.47||84|.22|.63|.32||82|.07|.46|.12||26|
|LR+TFIDF(wo)|Pos<br>|.22<br>|.50<br>|.30<br>|.73|78<br>|.35<br>|.47<br>|.40<br>|.58|184<br>|.41<br>|.55<br>|.47<br>|.61|237<br>|
||Neu<br>|.93<br>|.75|.83||838<br>|.80|.62|.70||734|.82|.64|.72||737|
||Neg|.41|.68|.51||84|.22|.50|.31||82|.08|.35|.13||26|
|RF+TFIDF(wo)|Pos|.22|.08|.11|.83|78|.48|.24|.32|.73|184|.48|.38|.42|.73|237|
||Neu|.88|.93|.91||838|.77|.91|.83||734|.79|.87|.83||737|
||Neg|.48|.50|.49||84|.35|.18|.24||82|.25|.04|.07||26|
|SVM+TFIDF(wo)|Pos|.57|.05|.09|.86|78|.67|.12|.20|.75|184|.57|.24|.34|.76|237|
||Neu|.87|.98|.92||838|.76|.98|.85||734|.78|.95|.85||737|
||Neg|.60|.38|.47||84|.62|.10|.17||82|.00|.00|.00||26|
|LR+FT|Pos|.40|.03|.05|.85|78|.57|.11|.18|.75|184|.55|.23|.32|.75|237|
||Neu|.87|.97|.92||838|.76|.98|.86||734|.77|.94|.85||737|
||Neg|.64|.46|.54||84|.79|.13|.23||82|.00|.00|.00||26|
|RF+FT|Pos|.00|.00|.00|.85|78|.40|.01|.02|.74|184|.57|.09|.15|.74|237|
||Neu|.86|.98|.92||838|.74|1.00|.85||734|.75|.98|.85||737|
||Neg|.62|.36|.45||84|1.00|.04|.07||82|.00|.00|.00||26|
|SVM+FT|Pos|.00|.00|.00|.86|78|.00|.00|.00|.73|184|.68|.06|.12|.74|237|
||Neu|.87|.98|.92||838|.73|1.00|.85||734|.75|.99|.85||737|
||Neg|.73|.42|.53||84|.00|.00|.00||82|.00|.00|.00||26|



**Table 11** : Complete model evaluation results for sentiment classification (continued). Performance metrics for _Wait Time, Price_ , and _Menu_ aspects across all model and vectorization combinations. 

|**Aspect/Variable**<br>|**Model 1**|**Model 2**|**Model 3**|**Model 4**|
|---|---|---|---|---|
|**Main Aspects**|||||
|Service<br>0.587|(0.011)***|0.464 (0.010)***|0.449 (0.011)***|0.450 (0.011)***|
|Food Quality<br>1.315 <br><br>|(0.009)***<br>|1.438 (0.009)***<br>|1.466 (0.009)***<br>|1.465 (0.009)***<br>|
|Ambiance<br>-0.379|(0.012)***|-0.374 (0.012)***|-0.341 (0.012)***|-0.336 (0.012)***|
|Wait Time<br>0.626 <br><br>|(0.027)***<br>|0.637 (0.026)***<br>|0.588 (0.026)***<br>|0.594 (0.026)***<br>|
|Price<br>0.142 <br>|(0.041)***<br>|0.106 (0.040)**<br>|0.075 (0.039).<br>|0.065 (0.039).<br>|
|Menu Variety<br>0.173 <br>|(0.027)***|0.079 (0.026)**|0.056 (0.026)*|0.059 (0.026)*|
|**State Effects**|||||
|Arizona|–|0.028 (0.009)**|–|0.050 (0.009)***|
|California|–|0.036 (0.012)**|–|0.057 (0.012)***|
|Colorado|–|-0.044 (0.329)<br>|–|-0.051 (0.325)<br>|
|Delaware|–|0.051 (0.013)***|–|0.065 (0.012)***|
|Florida|–|0.032 (0.008)***|–|0.050 (0.008)***|
|Hawaii|–|0.347 (0.329)|–|0.306 (0.325)|
|Idaho|–|0.047 (0.011)***|–|0.067 (0.011)***|
|Illinois|–|0.042 (0.013)***<br>|–|0.068 (0.012)***<br>|
|Indiana|–|0.058 (0.008)***|–|0.079 (0.008)***|
|Louisiana|–|0.023 (0.009)**|–|0.040 (0.009)***|
|Missouri|–|0.032 (0.008)***|–|0.051 (0.008)***|
|Montana|–|0.280 (0.329)<br>|–|0.336 (0.325)<br>|
|North Carolina|–|0.580 (0.329).|–|0.659 (0.325)*|
|New Jersey|–|0.086 (0.009)***<br>|–|0.090 (0.009)***<br>|
|Nevada|–|0.053 (0.011)***|–|0.072 (0.010)***|
|Pennsylvania|–|0.051 (0.007)***<br>|–|0.062 (0.007)***<br>|
|Tennessee|–|0.025 (0.008)**|–|0.052 (0.008)***|
|Other|–|-0.634 (0.329).|–|-0.629 (0.325).|
|**Cuisine Effects**<br>|||||
|Cajun/Creole|–|–|0.062 (0.011)***|0.067 (0.011)***|
|Chinese|–|–|0.203 (0.007)***|0.203 (0.007)***|
|Indian|–|–|0.047 (0.011)***|0.050 (0.011)***|
|Italian|–|–|0.120 (0.005)***|0.119 (0.005)***|
|Japanese|–|–|0.095 (0.009)***|0.098 (0.009)***|
|Mediterranean|–|–|0.008 (0.011)|0.011 (0.011)|
|Mexican|–|–|0.015 (0.006)**|0.014 (0.006)*|
|Other Cuisine|–|–|0.069 (0.004)***|0.070 (0.004)***|
|Thai|–|–|0.034 (0.012)**|0.036 (0.012)**|
|Vietnamese|–|–|0.129 (0.013)***|0.139 (0.014)***|
|Significance levels: *** p <|0.001, ** p <|0.01, * p < 0.05, .|p < 0.1||



**Table 12** : Regression results predicting overall restaurant ratings (two-stage classifier). Coefficients shown with standard errors in parentheses. Model 1: Global regression without controls; Model 2: Including _state_ fixed effects; Model 3: Including _cuisine_ fixed effects; Model 4: Including both _state_ and _cuisine_ fixed effects. 



**Fig. 5** : Workflow visualization for the classification and regression analysis of Yelp restaurant reviews, detailing the training of one-stage and two-stage classifiers, prediction processes based on review relevance and sentiment, and a final regression analysis to model overall business ratings from aggregated sentiment predictions. 

30 

