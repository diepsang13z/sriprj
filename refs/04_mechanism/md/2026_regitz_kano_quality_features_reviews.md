Information Technology & Tourism (2026) 28:20 https://doi.org/10.1007/s40558-025-00354-y 

**<mark>ORIGINAL RESEARCH</mark>** 



# **Online customer feedback for identifying KANO product quality features: a fine-grained topic detection and sentiment analysis approach** 

**Dominic Regitz**<sup>**1**</sup> **· Wolfram Höpken**<sup>**1**</sup> **· Matthias Fuchs**<sup>**2,3**</sup> 

Received: 3 February 2025 / Revised: 28 November 2025 / Accepted: 2 December 2025 / Published online: 26 February 2026 © The Author(s) 2025 

### **Abstract** 

Analyzing customer feedback, accessible on the Internet via social media platforms and tourism-related travel websites, empowers tourism service providers to pinpoint areas of success and concern. A notable approach to identifying factors determining customer satisfaction is the Kano method, which is nowadays typically applied to big data contexts to detect quality features through the analysis of online customer feedback. The present study introduces a novel fine-grained approach for classifying quality factors based on topic areas identified through unsupervised learning techniques. Specifically, a keyword clustering-based topic detection and lexiconbased sentiment analysis is followed by a regression analysis, to identify factors influencing customer satisfaction, which is finally validated using ANOVA. Technically, the proposed approach aims to discern the positive and negative impacts that various topic areas, identified through unsupervised learning in online feedback data, may have on overall customer satisfaction. Findings show that automatically identified topic areas within customer feedback can be meaningfully categorized as Must-Be, One-Dimensional or Attractive Qualities. More specifically, while most identified topic areas exhibit One-Dimensional Quality characteristics, influencing overall customer satisfaction positively when fulfilled and negatively when not, nuanced variations emerge across different attributes. Furthermore, the regression models revealed significant influences between attribute performance and overall customer satisfaction, underscoring the statistical reliability of the models applied. To summarize, our study contributes to theory by providing a refined method for detecting Kano factors on a more fine-grained level and by identifying statistically significant and practically reliable Kano factors that asymmetrically influence overall customer satisfaction. 

**Keywords** Online customer feedback · Kano model · Fine-grained topic detection · Sentiment analysis · Linear regression 

Extended author information available on the last page of the article 

```
1 3
```

**<mark>20</mark>** <mark>Page 2 of 31</mark> 

D. Regitz et al. 

## **1 Introduction** 

The proliferation of customer feedback on online platforms has become a valuable source for businesses, particularly within the hospitality industry. As such, the Internet has fundamentally changed the way tourism-related information is created, shared, and consumed. Experiences with products and services are now widely accessible through social media on tourism dedicated platforms, such as TripAdvisor (Xiang & Gretzel 2010; Gretzel & Sigala 2017). Most importantly, online customer feedback is perceived as more credible among customers due to its comparative lack of commercial self-interests when contrasted with sources like travel agencies and advertisements. Consequently, online customer feedback has been increasingly considered by all types of travelers in the planning phase of upcoming trips and vacation stays (Marine-Roig 2022). 

However, online customer feedback is of immense value not only for the end users, but also for the providers of tourism services. As online customer feedback truly reflects the opinions and experiences of previous customers, problem areas can be discovered and addressed, to make tourism planning activities and strategies more customer-centered and more effective (Mehraliyev et al. 2022). This is further corroborated by the fact that the total number of reviews on TripAdvisor, one of the most popular travel feedback platforms, has increased more than fivefold between 2014 and 2022. As of now, TripAdvisor hosts over one billion customer reviews within the tourism sector alone (PRNewswire 2022). The fact that TripAdvisor was the second most visited travel and tourism-related website as of June 2024 further illustrates tourists’ interest in posting and reading travel-related online feedback (Semrush 2024). Based on this background, tourism scientists have emphasized the significance of online customer feedback for tourism service providers. Customer feedback in particular facilitates the identification of those product features that have a strong influence on overall customer satisfaction. Therefore, in this study, online customer feedback is used to analyze and identify product features based on Kano’s three-factor model of customer satisfaction (Kano 1984). 

The Kano model, developed by Noriaki Kano already in the early 1980s, provides a framework for understanding how different product or service quality features affect overall customer satisfaction. This analytical framework helps businesses prioritize improvements and innovations based on what will most effectively enhance customer satisfaction (Kano 1984). In this context, the Kano model assists companies in identifying and prioritizing customer needs related to products and services. The identification of such quality features, however, traditionally relied on data obtained from manual or semi-automated customer surveys (Kano 1984; Sauerwein et al. 1996; Fuchs and Weiermair 2003). While this traditional survey approach provides valuable insights, it has several well-documented limitations, including response biases and the substantial time and effort required to collect and analyze survey-based data (Mikulić and Prebežac 2016; Slevitch 2024). To overcome these challenges, a key focus of recent research has been to leverage online customer feedback for the identification of such Kano-based quality features (Zhou et al. 2023; Lee et al. 2021; Chen et al. 2019; Zhang et al. 2021; Binder et al. 2023). Building on this body of research, the study at hand adopts advanced natural language processing (NLP) techniques to 

```
1 3
```

Online customer feedback for identifying KANO product quality… 

<mark>Page 3 of 31</mark> **<mark>20</mark>** 

analyze online customer feedback collected from TripAdvisor. These methods allow for the semi-automatic extraction and categorization of customer feedback, providing a more detailed and accurate near real-time picture of the drivers behind overall customer satisfaction. More precisely, NLP enables the identification of the most relevant topics within reviews (topic detection), as well as the assessment of the emotional tone associated with the identified topics (sentiment analysis). Paired with a subsequent regression analysis, these methods provide comprehensive insights into what customers value most and how strongly different quality features affect overall customer satisfaction. 

Our study builds on previous tourism research suggesting that the Kano methodology is particularly suitable to advance the understanding of customer satisfaction in tourism and hospitality, both conceptually and theoretically. The objective of this study is to enhance the traditional Kano model analysis by incorporating NLP, i.e., topic detection and sentiment analysis techniques. By leveraging the vast amounts of customer feedback available online, we aim to develop an approach to automatically identify and categorize the key quality attributes most strongly influencing overall customer satisfaction in the hospitality domain. 

In contrast to previous studies that likewise applied machine learning-based methods for detecting topics within a Kano analytical framework, our study introduces an advanced topic-clustering approach in order to identify more fine-grained themes from customer online feedback. This approach, for the first time, enables the estimation of the influence of more nuanced topics on overall tourist satisfaction. The concrete research question reads as follows: 

RQ: Can more fine-grained topic detection and sentiment analysis techniques be applied to validly and reliably identify the relevant Kano-based quality attributes that affect overall customer satisfaction in the hospitality domain? 

As previous works, the study at hand uses online customer feedback data from one of the major online feedback platforms in tourism, namely TripAdvisor, to validate the proposed methodology (Schmunk et al. 2014; Kim et al. 2016; Tontini et al. 2017; Höpken et al. 2017; Bi et al. 2020; Lee et al. 2021; Njeri et al. 2022). Specifically, online reviews are collected systematically from TripAdvisor for the Lake Constance region. The border region surrounding Lake of Constance is particularly suitable as a study area, as it attracts not only international visitors from around the world but also domestic visitors from the three neighboring countries Germany, Switzerland, and Austria. 

The paper is structured as follows: First, we provide an overview of approaches to analyzing customer satisfaction using the Kano model, followed by a brief review of online customer feedback analyses employing text mining methods, as well as studies on customer satisfaction modeling based on online customer feedback. The methods section describes the data collection and machine learning (ML) techniques, as well as the categorization and the validation processes employed in the study at hand. Finally, we present and discuss our findings, concluding with insights into major limitations and suggestions for future research. 

```
1 3
```

**<mark>20</mark>** <mark>Page 4 of 31</mark> 

D. Regitz et al. 

## **2 Related work** 

### **2.1 Analyzing customer satisfaction and the KANO model** 

Analyzing customer satisfaction has been one of the most important research topics across different disciplines and application domains for many years. A fundamental assumption in this context is that customer satisfaction can be conceptualized as the difference between expectations on the one hand and perceived quality on the other, first introduced by Oliver (1980) through the Disconfirmation of Expectations theory. Based on this approach, Zeithaml et al. (1988) developed the SERVQUAL model, which aims at measuring the difference between expectations and perceptions in five distinct dimensions, namely reliability, responsiveness, tangibles, assurance, and empathy. The SERVQUAL model has also been applied to the tourism domain (e.g. Bhattacharya et al. 2023), albeit to a rather limited extent. 

In contrast, the Kano model, a conceptual framework developed in the 1980’s to better comprehend the formation of customer satisfaction, categorizes quality attributes into three key groups: (1) Must-Be Quality, (2) One-Dimensional Quality and (3) Attractive Quality. While Must-Be Quality features represent fundamental elements whose absence (i.e., low delivered quality) leads to dissatisfaction, Attractive Quality attributes encompass features that pleasantly surprise customers but are not considered essential (Kano 1984). The key groups within the Kano model are principally different from the five SERVQUAL dimensions, as they do not distinguish certain aspects of the service quality itself, but instead represent service elements that exhibit a different marginal influence on overall customer satisfaction. This distinction constitutes the main motivation of using the Kano model in the present study. 

In the context of tourism, the Kano model has gained widespread applicability as it offers a structured approach for identifying and prioritizing such quality attributes that significantly influence overall customer satisfaction (Kuo et al. 2016; Fuchs and Weiermair 2003; Jannach et al. 2014; Slevitch 2024). Typically, customer satisfaction studies depict the association between attribute performance and overall satisfaction as linear or symmetric. Nevertheless, theoretical arguments as well as empirical evidence suggest that this relationship can exhibit asymmetry or non-linearity (Fuchs and Weiermair 2004; Bi et al. 2020). Ever since Kano’s initial work in 1984, researchers have increasingly focused on examining such asymmetric or non-linear relationships between attribute performance and customer satisfaction (Tontini et al. 2017; Xu 2020; Mikulić et al. 2016; Zavira et al. 2023). 

Sauerwein et al. (1996), for example, propose a methodology based on Kano’s framework that allows the identification of the influence that different components of products and services have on overall customer satisfaction. After the identification of such product requirements, a questionnaire was constructed, and the collected data were analyzed with regressive methods. This allowed for the categorization of the product requirements into Must-Be, One-Dimensional or Attractive Quality. Likewise, Kuo et al. (2016) surveyed hotel guests in Taiwan to rate 27 hotel service quality attributes in terms of their importance and satisfaction. These quality attributes were rated and classified into five categories using Kano’s model of customer satisfaction by developing a Kano-specific questionnaire. Furthermore, customer ratings 

```
1 3
```

Online customer feedback for identifying KANO product quality… 

<mark>Page 5 of 31</mark> **<mark>20</mark>** 

were subjected to the quality function deployment (QFD) planning process, translating those customer needs into technical requirements. Zavira et al. (2023) identified restaurant consumers’ needs through the Kano model based on data collected through questionnaires. They found out that attributes, such as fast service, unique offers and affordable prices, contributed to a relatively larger extent to customer satisfaction if positively perceived by tourists, but, interestingly enough, do not lead to any decrease in customer satisfaction if negatively perceived. Yilmaz et al. (2022) conducted an analysis of the impact of the COVID pandemic on the accommodation industry. In total, 22 new consumer needs and 11 previously obscure customer needs were identified, showing that new consumer preferences formed through the pandemic were effectively addressed. Most recently, Yang et al. (2025) analyzed the failure attributes related to hotel robots, classifying them using the Kano model, demonstrating that the Kano model can also be applied to specific IT-services, identifying both functionalities and failures driving customer dis-/satisfaction. Lin et al. (2024) applied text mining techniques and the Kano modelling framework to the specific domain of coastal and marine tourism. Clustering was used to group eighty key terms into three dimensions of servicescape and consecutively into 18 more granular elements. Subsequently, the Kano model was used to categorize these elements into the four quality factors attractive, one-dimensional, must-be, and indifferent. The study proved the potential of the Kano model to provide a nuanced understanding of factors influencing overall customer satisfaction in the area of coastal and marine tourism. Since its introduction by Kano in 1984, different methods for categorizing such quality attributes have emerged. Mikulic et al. (2011) and Slevitch (2024) conducted a critical examination of empirical techniques routinely employed to categorize corresponding quality factors and deemed approaches, such as the Importance Performance Grid, as unsuitable. Originally and still today, corresponding Kano analyses are carried out on the basis of data obtained from surveys (Sauerwein et al. 1996; Kuo et al. 2016; Zavira et al. 2023; Yilmaz et al. 2022). The collection of such primary data, however, is highly time-consuming and costly. As the Internet provides vast amounts of online customer feedback (Fuchs et al. 2017), an increasing number of approaches have recently been developed that carry out corresponding analyses aimed at identifying Kano classifications based on online customer feedback (Zhou et al. 2023; Lee et al. 2021; Zhang et al. 2021). Major methods presented in the literature are critically discussed in the following sections. 

### **2.2 Text-mining based analysis of online customer feedback** 

In today’s research landscape, studying online customer feedback using text mining methods has become a widespread and firmly established practice, with applications spanning a wide range of fields. In their literature review, Rouhani and Mozaffari (2022) identified the main research topics, research trends, and comparisons of research topics in the field of sentiment analysis through social media, themselves employing Latent Dirichlet Allocation (LDA), a probabilistic topic modeling approach. Their LDA-based study demonstrated that machine learning methods are the most important topics and, thus, methods used for executing sentiment analysis on social media. 

```
1 3
```

**<mark>20</mark>** <mark>Page 6 of 31</mark> 

D. Regitz et al. 

Especially within the context of tourism, leveraging online customer feedback analysis has become increasingly important, as it provides authentic insights into experiences shared by individuals, contributing to a comprehensive understanding of tourism offers (such as hotels) and customer needs (Gretzel & Sigala 2017). To achieve this goal, commonplace methodologies, such as Topic Detection or Sentiment Analysis, are routinely employed, enabling a more nuanced understanding of online customer feedback (Schmunk et al. 2014; Garcia et al. 2021; Nguyen et al. 2021; Höpken et al. 2024). Notably, these methods are often used in conjunction thereby offering a thorough understanding of both the thematic content and the emotional tone present in such customer feedback (Ali et al. 2022; Zhou et al. 2023; Zhang et al. 2021; Al-Smadi et al. 2019). 

For instance, Ahani et al. (2021) assessed the satisfaction of medical travelers by analyzing online review, utilizing LDA to identify key topic areas within medical tourism reviews. Similarly, Mishra et al. (2021) collected tourism-related data from Twitter, emphasizing the sub-domains reflecting hospitality and healthcare experience. After conducting a sentiment analysis based on the Valence Aware Dictionary for Sentiment Reasoning (VADER), topic modelling was employed to reveal hidden themes related to tourism healthcare and hospitality by using LDA. Schmunk et al. (2014) employed Support Vector Machines (SVM), the Naive Bayes algorithm, various lexica-based methods and k-Nearest Neighbor (k-NN) to detect most relevant topics in online reviews obtained from TripAdvisor, with the most favorable outcomes achieved through SVM and lexica-based approaches. Ali et al. (2022) developed a method that combines topic detection and sentiment analysis to extract insights about the city of Marrakech. This method involves the extraction of online customer feedback, the identification of latent topics using LDA and the application of sentiment analyses for each identified topic area. Likewise, Garcia et al. (2021) analyzed tweets related to the overall topic of COVID-19, using topic detection and sentiment analysis in conjunction. The authors found out that most posts related to the pandemic had a negative sentiment. Pang et al. (2002) observed that in sentiment analyses for online reviews, Naïve Bayes Classification produced the least favorable results, while SVM exhibited the superior performance throughout their study. More recently, Tran et al. (2023) proposed an Interpretable Random Forest approach for opinion mining on hotel reviews. Through this, the task of sentiment polarity detection is performed. Finally, Abdelgwad et al. (2022) conducted an aspect-based sentiment analysis on hotel reviews using the Bidirectional Encoder Representations from Transformers (BERT) model. Experimental results have shown that this model outperformed State-of-the-Art approaches and is especially robust to overfitting. 

### **2.3 Customer satisfaction modeling and online customer feedback analysis** 

The surge in online review data has led to a proliferation of studies analyzing customer satisfaction based on online customer feedback, pursuing three primary objectives (Zhou et al. 2023): (1) the identification of key attributes influencing customer satisfaction through methods such as sentiment analysis or topic detection; (2) investigating the correlation between product or service attributes and overall customer satisfaction, and (3); developing customer satisfaction models based on online cus- 

```
1 3
```

Online customer feedback for identifying KANO product quality… 

<mark>Page 7 of 31</mark> **<mark>20</mark>** 

tomer feedback. The studies discussed below, which build on attribute (i.e., topic) modelling and sentiment analysis, examine how the performance of different tourism service attributes affects overall customer satisfaction (Zhou et al. 2023). 

Chatterjee et al. (2023) argue that SERVQUAL, for example, has in the past typically been used on the base of survey data. The authors bridge this gap by using the SERVQUAL dimensions to analyze UGC with text mining approaches. Tontini et al. (2017) analyzed the semantic aspects of complaints and compliments in online reviews provided by hotel guests in TripAdvisor and concluded that there is indeed a non-linear impact of comments on customer satisfaction. Likewise, Xu (2020) employed a method based on text mining and text regression to analyze online reviews. He found out that asymmetric effects exist between the topical focus of online reviews and the determinants of overall customer satisfaction. Tan et al. (2022) conducted a conjoint analysis on attributes affecting customers’ preference for hotel accommodations. They concluded that price was the most preferred attribute by the customers, followed by the inclusivity of breakfast and accessibility to nearby landmarks. Yousaf et al. (2023) explored the impact of COVID-19 through the analysis of online reviews. Interestingly, the pandemic was found to have a steady positive effect on the occurrence of hygiene-related (i.e. must- be quality) topics within the positive aspects of online reviews. 

Athanasopoulou et al. (2023) analyzed online hotel reviews to determine whether different hotel service attributes show asymmetric effects on overall customer satisfaction. For this purpose, positive and negative comments on hotels are analyzed using the three-factor theory and the Penalty Reward Contrast Analysis (PRCA). Based on their findings, location and personnel qualities were identified as the most important (non-linear) influence factors on customer satisfaction. Kim et al. (2016) analyzed online hotel reviews gained from TripAdvisor to identify and compare factors known as ‘satisfiers’ (i.e. attractive quality factors) and ‘dissatisfiers’ (i.e., must be quality factors). A total of 919 reviews were analyzed, collected from full-service and limited-service hotels. Results showed that satisfiers and dissatisfiers in full-service hotels were distinct, with the exception of the service-related factors staff and service. 

Likewise, Bi et al. (2020) explored the asymmetric effects of attribute performance on customer satisfaction. To this extent, again the PRCA and Asymmetric Impact-Performance Analysis (AIPA) were applied to analyze customer feedback gained from TripAdvisor. Such topic areas have then been categorized as either Must-Be, OneDimensional or Attractive Quality attributes following the Kano model framework. Notably, the results have shown that the asymmetric effects of attribute performance and customer satisfaction vary across different market segments (such as different types of hotels). Zhou et al. (2023) analyzed online customer feedback in tourism services guided by the Kano model. First, LDA was used to extract the key dimensions from online reviews. Subsequently, the tourists’ emotional attitudes towards each service dimension were identified. Through a back-propagation Artificial Neural Network, the relationship between tourists’ sentiment orientation towards different quality dimensions and their overall satisfaction was detected. Finally, based on an extended Kano model, a multi-dimensional attribute classification was performed. 

```
1 3
```

**<mark>20</mark>** <mark>Page 8 of 31</mark> 

D. Regitz et al. 

Similarly, Lee et al. (2021) proposed an extended method for conducting a text mining-based mapping for KANO quality factors. For this aim, a total of 3,791 online hotel reviews has been collected from TripAdvisor. The review data were then analyzed using LDA to identify corresponding topic areas. To this extent, the reviews have been split into two groups into which (1) the emotion analysis is positive, and star points are 4 or 5 and (2) the emotion analysis is negative, and star points are 1 or 2. Quality factors based on the Kano model have been finally derived from the positive and negative sentiment extracted. Likewise, Chen et al. (2019) presented a Kanobased framework to extract, quantify and classify different product features based on online customer reviews. First, a sentiment analysis was performed to mine customer opinions on a set of product features extracted from online customer feedback. Second, these product features were classified into four Kano categories (Must-Be, One-Dimensional, Attractive and Indifferent) based on the aggregation of individual customer opinions. In this step, the correlation between feature sentiment scores and product ratings was measured. Lastly, anomaly detection and novelty detection were applied to flag unusual and emergent customer opinions. 

Wu et al. (2022) presented an approach that allows for the construction of Kano questionnaires based on online comment mining. First, comments were extracted from the Internet, and then visualized in terms of their feature word co-occurrence to identify main user concerns. Based on this, a Kano questionnaire was built to conduct a survey, determining the types of requirements corresponding to those features as well as their degree of importance. Most recently, Binder et al. (2023) proposed a method for automatically classifying Kano model factors in app reviews. In this approach, corresponding reviews were manually annotated as either Must-Be, OneDimensional, Attractive or Indifferent quality and used to train and test several classifiers. Njeri et al. (2022) examined wildlife tourism experiences in Kenya guided by the Kano model to assess overall tourist satisfaction. Tourist reviews were collected from TripAdvisor and then analyzed with Microsoft Azure Generator to compute and assign sentiment scores. The reviews were grouped as positive, neutral, or negative and then further categorized as either Must-Be, One-Dimensional, Attractive, Indifferent or Reverse quality. Similarly, Al Rabaiei et al. (2021) developed a method to integrate the Kano model with data mining approaches to select relevant attributes that drive customer satisfaction, aiming to address the problem of selecting features that may be irrelevant to customer satisfaction. The experiments indicate that XGBoost regression and Decision Tree regression produced the best results for this particular problem. 

Zhang et al. (2021) proposed an approach based on online customer feedback to determine the prioritization of hotel service resource allocation from both subjective and objective aspects. To achieve this, LDA was used to extract service attributes from customer feedback. Sentiment tendencies and intensities of those corresponding service attributes were identified using a Recursive Neural Tensor Network (RNTN). An improved version of the PRCA was then applied to analyze the relationship between attribute performance and customer satisfaction. The topic areas were subsequently categorized as basic, low-performance, performance, high-performance, or excitement features, respectively. Lastly, Zhao et al. (2024) developed an extension of the Kano model, the Strength–Frequency Kano model, considering the interaction 

```
1 3
```

Online customer feedback for identifying KANO product quality… 

<mark>Page 9 of 31</mark> **<mark>20</mark>** 

between strength and frequency to classify the requirements expressed by travelers. By applying sentiment and statistical analysis, the study identified 13 traveler requirements in 13,217 online reviews and classified them into one-dimensional, must-be, attractive, and indifferent requirements. Using an optimization model to determine classification thresholds, the study enables at maximizing traveler satisfaction at minimal costs and, consequently, prioritize service improvements. 

While the aforementioned studies also endeavor to ascertain relevant quality factors using the Kano model through the analysis of online customer feedback (Chen et al. 2019; Zhang et al. 2021; Lee et al. 2021; Binder et al. 2023; Zhou et al. 2023; Zhao et al. 2024), they suffer from several limitations. Topic and sentiment analysis often occur at the level of entire customer review rather than at the more detailed sentence or statement level. Additionally, topics are often predefined, limiting the depth of analysis. Collectively, these studies overlook the opportunity to analyze customer feedback at the most granular level and to aggregate results precisely enough to identify statistically significant and practically reliable Kano factors. By addressing these research gaps, our approach seeks to answer the following research question: Can more fine-grained topic detection and sentiment analysis techniques be applied to validly and reliably identify the relevant Kano attributes that affect overall customer satisfaction in the hospitality domain? 

To address this research question, the present paper introduces a novel more finegrained approach for classifying quality factors based on topic areas identified through unsupervised learning techniques. To achieve this goal, each review is segmented into its constituent sentences, which, therefore, are subsequently subjected to a sentence-level topic detection and sentiment analysis (Höpken et al. 2024). Following the identification of a specific topic area and the corresponding sentiment expressed by the customer in each sentence, this information is aggregated at the review level. Through this step, the quantities of positive and negative expressions related to each topic area for each review are determined and statistically regressed on overall customer satisfaction. This novel approach facilitates a more nuanced understanding of the positive and negative impact of the fulfillment or non-fulfillment of each topic area on overall customer satisfaction. Based on these empirical results, the respective topic areas are subsequently classified as either (1) Must-Be, (2) One-Dimensional or (3) Attractive Quality features, following the Kano model of customer satisfaction (Kano 1984). Finally, the findings undergo a validation procedure using ANOVA, which allows us to determine whether the fulfillment or non-fulfillment of the respective factors is indeed reflected in the extracted customer feedback. 

Although our proposed methodology aligns with Zhou et al.’s (2023) approach, which also involves dividing reviews into sentences and subjecting them to topic detection and sentiment analysis, there are notable differences. Unlike their method of aggregating sentences related to the same topic, our approach adopts a more finegrained perspective by identifying the exact number of positive and negative entries for each topic area at the review level, thereby more precisely representing the relative strength of the expressed feedback. This enables a more accurate depiction of the magnitude and polarity of the online feedback identified, enhancing the granularity of insights into the asymmetric process of overall customer satisfaction formation. 

```
1 3
```

**<mark>20</mark>** <mark>Page 10 of 31</mark> 

D. Regitz et al. 

Furthermore, our approach employs a regression analysis instead of an artificial neural network, enabling the _explicit_ identification of the positive and negative influence that each occurrence of a topic area has on overall customer satisfaction in case of fulfillment or non-fulfillment. This process provides clearly interpretable results that highlight the impact of each topic area, thus making the findings more actionable for practitioners (Höpken & Fuchs 2022). A final ANOVA further validates whether the insights gained are indeed representative. As such, the proposed validation technique ensures the reliability and robustness of the methodology, enabling researchers and practitioners to derive actionable insights with greater confidence. 

Other studies in this domain have conducted similar analyses based on PRCA (Bi et al. 2020; Zhang et al. 2021) or by regressing the feature sentiment score with the overall product or review rating (Chen et al. 2019), which distinguishes our approach from previous work. Overall, our proposed method enhances the robustness and applicability of the Kano model in the context of online customer feedback. By providing a more detailed and statistically validated analysis, practitioners can derive actionable insights with greater confidence, ultimately leading to improved customer satisfaction strategies. Lastly, by utilizing unsupervised learning techniques for topic detection, our approach minimizes human bias and ensures consistent results across different datasets. This objective and automated method is crucial for generating reliable insights that can be confidently applied in hospitality management practice. 

Table 1 provides an overview of the existing literature, including data sources, approaches, key findings, and the corresponding limitations and research gaps relevant to the present study. 

To summarize, previous research has intensively applied machine learning-based methods to implement a Kano analytical framework in the hospitality context. However, in doing so, only relatively broad categories of Kano-based quality attributes have been empirically identified. More nuanced topical themes driving customer satisfaction have not yet been identified in course of the Kano framework. This highly relevant specific research gap is addressed in our proposed method, which applies an unsupervised machine learning approach to identify fine-grained topics as valid nuanced influences on overall customer satisfaction. Through this approach, the present study contributes to the existing body of knowledge by (1) providing a refined method for analyzing Kano factors at a more fine-grained level and (2) identifying statistically significant and practically reliable factors influencing overall customer satisfaction. 

## **3 Methodology** 

Figure 1 provides an overview of the proposed method and illustrates the sequence of steps performed, which are discussed in more detail next. After extracting customer reviews from TripAdvisor, each review is split into individual sentences and further pre-processed through tokenization and stemming. Subsequently, each sentence is subjected to topic detection and sentiment analysis and subsequently traced back to its original review. Through this process, the number of positive and negative entries for each review is identified and used as input for a linear regression. Based 

```
1 3
```

Online customer feedback for identifying KANO product quality… 

<mark>Page 11 of 31</mark> **<mark>20</mark>** 

**Table 1** Literature overview 

|Author|Year|Data Source /<br>Method|Key Findings|Limitations / Gaps|
|---|---|---|---|---|
|Sauer-<br>wein et<br>al.|1996|Kano survey, re-<br>gression analysis|Product requirements classified into<br>must-be, one-dimensional, attractive|Survey-based|
|Kuo et<br>al.|2016|Kano survey, QFD|27 hotel service attributes classified;<br>technical requirements derived|Survey-based; limited<br>attributes|
|Yilmaz<br>et al.|2022|Kano survey|Changed customer needs due to<br>COVID-19|Survey-based; adapted<br>to emerging customer<br>preferences|
|Zavira<br>et al.|2023|Kano survey|Attributes positively affecting restau-<br>rant consumer satisfaction identified<br>i|Survey-based; low<br>flexibility|
|Lin et<br>al.|2025|Kano survey, senti-<br>ment analysis, Kano<br>classification|Three service dimensions identified<br>and classified into Kano categories|Survey-based; applied<br>to coastal/marine<br>tourism|
|Yang et<br>al.|2025|Kano survey, Kano<br>classification|Robot failure attributes classified<br>into Kano categories|Survey-based; applied<br>to robot failures|
|Bhat-<br>tacharya<br>et al.|2023|AHP-SERVQUAL<br>survey|Inconsistencies in gaps in tourism<br>services identified|Survey-based;<br>SERVQUAL dimen-<br>sions orthogonal to<br>Kano dimensions|
|Chat-<br>terjee et<br>al.|2023|Online reviews,<br>sentiment analysis,<br>SERVQUAL<br>classification|Comparative importance of<br>SERVQUAL dimensions uncovered|SERVQUAL dimen-<br>sions orthogonal to<br>Kano dimensions|
|Chen et<br>al.|2019|Online reviews,<br>sentiment analysis,<br>Kano classification|Features classified into must-be, one-<br>dimensional, attractive, indifferent|Aggregated at feature-<br>level; no review-level<br>analysis|
|Lee et<br>al.|2021|Online reviews,<br>LDA, sentiment<br>analysis|Kano factors derived from positive/<br>negative reviews<br>i|Grouping into<br>two groups; lower<br>granularity|
|Zhang<br>et al.|2021|Online reviews,<br>LDA, RNTN,<br>PRCA|Attributes classified into basic, low<br>performance, performance, high<br>performance, excitement<br>i|PRCA uses aggregated<br>scores; no detailed<br>sentence-level analysis|
|Wu et<br>al.|2022|Kano survey, online<br>comments,|Feature co-occurrence identified|Combination of survey-<br>based and online<br>comments|
|Binder<br>et al.|2023|App reviews, Kano<br>classification|Automatic Kano classification<br>validated|Manual annotation;<br>limited to app domain|
|Zhou et<br>al.|2023|i<br>Online reviews,<br>LDA, ANN, senti-<br>ment analysis|Multi-dimensional Kano approach;<br>key attributes identified|Less fine-grained; no<br>review-level regression;<br>ANN less interpretable|
|Zhao et<br>al.|2024|Online reviews,<br>sentiment analysis,<br>statistical analysis|13 travelers’ requirements classified<br>into four strength/frequency-based<br>categories|Specific Kano model<br>extension|



on the resulting regression models, the topic areas are categorized as Must-Be, OneDimensional or Attractive Quality features according to Kano’s model of customer satisfaction. Finally, these findings are subjected to an ANOVA to test whether they are indeed reflected in the customer feedback extracted from TripAdvisor. 

```
1 3
```

**<mark>20</mark>** <mark>Page 12 of 31</mark> 

D. Regitz et al. 



**Fig. 1** Overview 

### **3.1 Data collection and preparation** 

As discussed, the study at hand is based on online customer feedback data obtained from TripAdvisor, specifically focusing on English reviews related to the Lake of Constance region in southern Germany. Using a web crawler, reviews from the years 2018 to 2023 were extracted, totaling 1,392 entries. The dataset includes six attributes, providing information about the reviewed hotel, the review title, the review text, the review date, and the users’ overall rating on a scale from 1 to 5. As highlighted, each online review was segmented into individual sentences, enabling a more fine-grained approach for both the conduction of topic detection and sentiment analysis at the sentence level. Further data preparation steps involved standard text-mining tasks, such as tokenization, stemming, removal of stop-words and TF-IDF-based word-vector creation (Liu 2011). After these pre-processing steps had been completed, empty entries were removed from the data set, affecting a total of 154 sentences. In total, the 1,392 reviews were transformed into 9,757 sentences for further analysis. Approximately 25% of these sentences were manually labeled according to their sentiment, allowing for the assessment of accuracy in the subsequent sentiment analysis. 

### **3.2 Topic detection and sentiment analysis** 

After preparing the review data, each sentence was subjected to both topic detection and sentiment analysis. These steps involve the automated identification and classification of topics mentioned in user reviews and the users’ sentiment toward these topics. For the task of topic detection, keyword clustering was performed using the k-means clustering algorithm. Keyword clustering identifies groups of sentences containing the same keywords (i.e. words with high TF-IDF-values), thereby constituting latent topics. Before conducting the cluster analysis, sentiment-related words (i.e., adjectives such as _good_ or _bad_ ) were filtered out to improve the quality of the 

```
1 3
```

Online customer feedback for identifying KANO product quality… 

<mark>Page 13 of 31</mark> **<mark>20</mark>** 

resulting clusters, as such adjectives typically do not represent meaningful keywords. Entries that were empty after tokenization and stemming were removed from the data set. Furthermore, clustering was conducted on several subsets (33% and 66%) of the data set to validate the robustness and consistency of the resulting clusters. Finally, two cluster models have been created, each encompassing a different number of clusters (k = 5 and k = 10), allowing for the identification of more fine-grained topic areas. K-means clustering was chosen as the algorithm for topic detection because previous research has demonstrated its effectiveness for this task, particularly due to its good interpretability based on clearly identified keywords (Wartena et al. 2008; Menner et al. 2016; Fuchs and Höpken 2022). Compared to more recent and semantically powerful transformer-based approaches, such as BERT or RoBERTa, TF-IDF-based keyword clustering can still achieve competitive results on certain datasets, especially smaller ones, as in our study (Subakti et a. 2022). 

As second main step, each entry was subjected to sentiment analysis to determine users’ sentiment toward the topic areas identified through the cluster-based topic detection. Sentiment analysis was performed using a lexicon-based approach with the wordlists by Hu and Liu (Hu and Liu 2004), which encompass approximately 7,000 opinion words in total. Based on these lists, each sentence was categorized as ‘positive’, ‘negative’ or ‘neutral’ after examining whether it contained more positive or negative words or no sentiment-related word at all. Despite its simplicity, previous research has demonstrated the effectiveness of lexicon-based approaches, supporting their application to sentiment analysis tasks (Feldman 2013; Schmunk et al. 2014; Aung et al. 2017; Mehraliyev et al. 2022; Chen et al. 2022). 

### **3.3 Regression analysis** 

Having classified each entry of the dataset according to its topic and sentiment, the objective of the subsequent regression analysis was to quantify the impact of positive and negative feedback associated with specific topic areas on overall customer satisfaction, as measured by the five-point satisfaction rating from TripAdvisor. In contrast to the preceding tasks of topic detection and sentiment analysis, this analysis was conducted at the review level. Therefore, each sentence was linked back to its original review, allowing for the identification of how many positive and negative sentences related to each topic area were contained within each review (Fig. 2). This information was then used to be regressed on the overall customer satisfaction specified by the user for each review as a five-point rating. For this transformation process, neutral sentences were removed, as they do not convey sentiment and, therefore, cannot provide meaningful insights into customer satisfaction. Consequently, as a matter of feature selection, it was appropriate to exclude neutral sentences from the regression analysis. 

### **3.4 Categorization and validation** 

Based on the positive and negative influences each topic area exerts on overall customer satisfaction, the final methodological goal was to categorize these topic areas as either Must-Be, One-Dimensional or Attractive Quality factors. This categoriza- 

```
1 3
```

**<mark>20</mark>** <mark>Page 14 of 31</mark> 

D. Regitz et al. 



**Fig. 2** Dataset transformation as input to regression analysis 

tion process closely aligns with Brandt’s (1987) approach, in which Penalty, Reward, and Hybrid factors were identified based on the positive and negative effects particular topic areas exhibit. More precisely, if a topic area exerts a negative influence on overall customer satisfaction in the case of non-fulfillment but lacks a positive impact in the case of fulfillment, it is categorized as Must-be Quality. Similarly, if a topic area has a positive regressive impact in the case of fulfillment but no negative impact in the case of non-fulfillment, it is categorized as Attractive Quality. Finally, if a topic area exerts both positive and negative influences on overall customer satisfaction, it is categorized as One-Dimensional Quality. 

During the linear regression analysis, all regression coefficients were tested for statistical significance, and only factors showing a significant influence on overall customer satisfaction ( _p_ < 0.05) were considered. Nevertheless, a second level of validation was performed based on an ANOVA. More specifically, the aim was to examine whether the non-fulfillment of a Must be feature or the fulfillment of an Attractive quality feature is indeed reflected in the corresponding hotel reviews. Thus, the underlying testing assumptions are that the non-fulfillment of a Must be feature has a significant negative impact on overall satisfaction, whereas the fulfillment of Attractive quality features has a significant positive impact. 

## **4 Findings** 

### **4.1 Topic detection** 

For the task of topic detection, a keyword clustering approach was applied, identifying cluster models with five and ten clusters (i.e., topics). These resulting models are presented in Fig. 3. In the first cluster model (k = 5), the following topic areas were identified: _Room_ , _Food_ , _Location_ , _Stay_ , and _Staff_ . These topic clusters were also identified in the k = 10 model, in addition to more fine-grained topic areas, such as _Connectivity_ , _Breakfast_ or _Service_ . The average within-centroid distance for the k = 5 model was 0.944, with values ranging between 0.898 and 0.982. The more fine-grained model achieved slightly better results, with an average within-centroid 

```
1 3
```

Online customer feedback for identifying KANO product quality… 

<mark>Page 15 of 31</mark> **<mark>20</mark>** 



**Fig. 3** Cluster models for k = 5 (upper part) and k = 10 (lower part) 

```
1 3
```

**<mark>20</mark>** <mark>Page 16 of 31</mark> 

D. Regitz et al. 

distance of 0.940, ranging from 0.830 to 0.911. These results demonstrate a good coherence of both cluster models. To verify the robustness of these cluster models, clustering was also conducted on subsets of the dataset comprising 33% and 66% of the total entries. The resulting clusters were consistent with those shown in Fig. 3, differing only slightly in the most frequent words within each cluster. 

In the following section, the most frequent words within each cluster are presented to illustrate potential overlaps and to evaluate the distinctiveness of the clusters, complementing the model descriptions above. The heatmap in Fig. 4 summarizes the TFIDF values for the three most important words in each cluster. In the k = 5 model, the highest-weighted terms reveal clear semantic boundaries: _room_ , _bed_ , and _bathroom_ dominate Cluster 0 ( _Room_ ); _breakfast_ , _service(e)_ , and _food_ characterize Cluster 1 ( _Food_ ); _hotel_ , _locat(ion)_ , and _park_ define Cluster 2 ( _Location_ ); _stai(y)_ , _night_ , and _would_ are central to Cluster 3 ( _Stay_ ); and _staff_ , _recept(ion)_ , and _check(-in)_ clearly mark Cluster 4 ( _Staff_ ). 

Across topic clusters, only a few words show notable overlap. For instance, the word _hotel_ appears in several clusters but with a distinctly higher TF-IDF weight in Cluster 2, emphasizing its relevance to location-related content. Given that the dataset consists of hotel reviews, minor overlaps of this kind are to be expected. Similarly, _breakfast_ and _service(e)_ appear marginally in other clusters but remain dominant in Cluster 1, indicating that these terms are almost exclusively discussed within the context of _food_ and _service_ experiences. Overall, the TF-IDF distribu- 



**Fig. 4** k = 5 Clustering TF-IDF weights 

```
1 3
```

Online customer feedback for identifying KANO product quality… 

<mark>Page 17 of 31</mark> **<mark>20</mark>** 

tions demonstrate a high degree of topical separation, suggesting that the clustering approach effectively isolates coherent topic areas within the review data. Building on these findings, Fig. 5 presents the corresponding heatmap for the k = 10 model, which provides a more fine-grained representation of the data and allows for a 



**Fig. 5** k = 10 Clustering TF-IDF weights 

```
1 3
```

**<mark>20</mark>** <mark>Page 18 of 31</mark> 

D. Regitz et al. 

closer examination of subtopics within the previously identified thematic areas. The TF-IDF weights again reveal clear topic boundaries with minimal overlap between clusters. Words like _breakfast_ , _buffet_ , and _choic(e)_ are dominant within the _Breakfast_ cluster, while _service(e)_ , _highli(ghts)_ , and _staff_ form the center of the _Service_ cluster. Similarly, _room_ , _bed_ , and _bathroom_ remain highly distinctive for accommodationrelated content. 

Although a few general terms such as _hotel_ , _breakfast_ or _stay_ appear across multiple clusters, their relative TF-IDF weights emphasize their contextual relevance. For example, _hotel_ is most strongly associated with the _Location_ and _Stay_ clusters. Notably, Cluster 9 ( _Staff_ ) also contains a considerable number of terms related to _breakfast_ , while Cluster 5 ( _Service_ ) includes similar vocabulary, indicating minor thematic overlap between these two areas. 

### **4.2 Sentiment analysis** 

Following the topic detection, a sentiment analysis was conducted using a lexicon-based approach. To validate the lexicon-based sentiment analysis, 25% of the sentences (i.e., 2,478) were manually annotated according to their sentiment. The analysis achieved an overall accuracy of 77.28%, with the positive class reaching the highest class-precision, while the neutral class showed the lowest detection performance. When the lexicon-based sentiment analysis was applied to the full dataset, a total of 5,923 entries were classified as positive, 2,482 as neutral and 1,352 as negative. Such a class distribution is not unusual, as most online reviews on platforms, such as TripAdvisor, tend to be positive in nature. For instance, in 2020 alone, 82% of all reviews on TripAdvisor were rated with either four or five stars (TripAdvisor 2021), which aligns with the relatively low number of negative entries identified in this study. 

### **4.3 Regression models and categorization** 

In the following subsection, the findings from the regression models based on both cluster models are presented. These models describe the positive and negative impact of each corresponding topic area on overall customer satisfaction. Figure 6 presents the results for the k = 5 cluster model (i.e., the less fine-grained model), illustrating the positive and negative effects associated with each topic cluster. 

Overall, the model achieved a satisfactory coefficient of determination (R²) of 0.386 (expressed as the squared correlation between the actual and predicted dependent variable) and an adjusted R² of 0.382. Notably, only the cluster 0 ( _Room_ ) exhibited a purely negative influence on overall customer satisfaction, meaning it is classified as a Must-Be Quality factor. In contrast, the remaining clusters display both a positive impact on customer satisfaction in the case of fulfillment and a negative impact in the case of non-fulfillment, meaning they are classified as One-Dimensional Quality factors. Interestingly, a cluster with a purely positive impact on customer satisfaction could not be identified. This may be attributed to the cluster model not being finegrained enough, with the corresponding topic areas lacking the granularity needed to represent such potential Attractive Quality features that exhibit a purely positive 

```
1 3
```

Online customer feedback for identifying KANO product quality… 

<mark>Page 19 of 31</mark> **<mark>20</mark>** 



**Fig. 6** Linear regression model k = 5 clustering 

impact on overall customer satisfaction. To explore this aspect in greater detail, the multiple regression model has next been executed for the more fine-grained cluster model consisting of 10 clusters (Fig. 7). 

Similar to the cluster model discussed above, most clusters exhibit either a purely negative influence on customer satisfaction or a mix of positive and negative effects. Likewise, the more complex model based on ten clusters achieved an R² (i.e., squared correlation) of 0.334 and an adjusted R² of 0.324. Within this model, however, one distinctive cluster (Cluster 2, _Connectivity_ ) stands out with a solely positive impact on overall customer satisfaction. This cluster is primarily composed of topic words such as _location_ , _walk_ and _station_ , suggesting clear thematic discussions about the hotel’s connectivity to public transportation and noteworthy points of interest (POIs) easily accessible. Since this cluster exhibits a positive impact on customer satisfaction in case of fulfillment, but no negative impact in case of non-fulfillment, it is 

```
1 3
```

**<mark>20</mark>** <mark>Page 20 of 31</mark> 

D. Regitz et al. 



**Fig. 7** Linear regression model k = 10 clustering 

classified as Attractive Quality. Interestingly, the topic area _Room_ once again exhibits a purely negative impact on overall customer satisfaction. Service-related clusters, such as cluster 5 and cluster 9 exhibit a strong negative impact on overall customer satisfaction in the case of non-fulfillment, further emphasizing the essential need 

```
1 3
```

Online customer feedback for identifying KANO product quality… 

<mark>Page 21 of 31</mark> **<mark>20</mark>** 

for hotels to provide helpful and friendly staff to achieve high levels of customer satisfaction. 

### **4.4 Validation of results** 

Based on the presented regression models, most identified topic areas can be classified as Must-Be or One-Dimensional Quality features. When applying a more finegrained topic detection approach, however, one topic area was identified that can be categorized as Attractive Quality. The goal of the final validation step was to determine whether such Must-Be or Attractive Quality features are indeed represented or reflected in the corresponding online reviews. More specifically, an ANOVA was conducted on the Topics Cluster 0 ( _Room_ , Must-Be quality) of the k = 5 model and Cluster 2 ( _Connectivity_ , Attractive Quality) of the k = 10 model. The ANOVA results for the Must-Be Quality feature _Room_ (Cluster 0) are summarized in Fig. 8. 

More technically, the validation involved dividing the reviews into two groups: one group containing all entries with at least one negative remark toward the topic area Cluster 0 ( _Room_ ), and the other group containing all entries with no negative remarks. ANOVA revealed a significant difference in overall customer satisfaction between both groups, indicating that non-fulfillment of the identified Must-Be Quality factor indeed negatively impacts customer satisfaction. This finding is further supported by the distribution of review ratings between the two groups. Entries 



**Fig. 8** ANOVA must-be quality factor cluster 0 ( _Room_ ) 

```
1 3
```

**<mark>20</mark>** <mark>Page 22 of 31</mark> 

D. Regitz et al. 



**Fig. 9** ANOVA attractive quality factor cluster 2 ( _Connectivity_ ) 

containing at least one negative remark toward the Must-Be quality factor show approximately 50% of reviews rated between one and three, whereas the comparison group comprises only around 15% of reviews within this rating range. These results underscore that non-fulfillment of the Must-Be Quality factor has a strong negative effect on overall customer satisfaction and, thus, reconfirm that these topic areas have reliably been classified as Must-Be Quality factor. Following the same principle, an ANOVA was conducted for the Attractive Quality Factor Cluster 2 ( _Connectivity_ ). The results of this analysis are presented in Fig. 9. 

Once again, the results indicate that the fulfillment of the Attractive Quality factor is indeed reflected in the corresponding online reviews. Entries containing at least one positive remark toward the Attractive Quality Factor are rarely found among negative reviews, with almost all of these reviews being rated with four or five stars. The comparative group, however, comprising reviews without any positive remarks towards the Attractive Quality factor, shows a significantly higher proportion of negative or neutral reviews, with user ratings ranging only from one to three stars. 

### **4.5 Discussion** 

The findings of this study provide valuable insights into the relationship between hospitality service quality factors and overall customer satisfaction, as conceptualized by the Kano model. 

```
1 3
```

Online customer feedback for identifying KANO product quality… 

<mark>Page 23 of 31</mark> **<mark>20</mark>** 

### **4.5.1 Kano quality factors based on fine-grained topic areas** 

The approach of clustering online reviews at the sentence level enabled the effective identification of coherent and fine-grained topic areas, including broader topics such as _Room_ , _Food_ or _Location_ , as well as more nuanced topics such as _Connectivity_ (a sub-category of _Location_ ) and _Breakfast_ (a sub-category of _Food_ ). The regression analysis based on these topic areas and their corresponding sentiments provide significant findings on their impact on overall customer satisfaction. Notably, most topic areas exhibit One-Dimensional Quality characteristics, influencing overall customer satisfaction positively when fulfilled and negatively when not. The statistical significance of the regression results, with p-values predominately being below 0.001, underscores the robustness and reliability of these findings. 

When examining the specific influence of different topics on overall customer satisfaction, substantial variations can be observed. The topic clusters _Staff_ and _Service_ show the strongest influence, indicating that these aspects constitute central determinants behind a satisfactory hotel stay. In contrast, the topics _Room_ , _Stay_ and _Check-In_ display a consistently negative influence on overall customer satisfaction, classifying them as Must-Be Quality factors. These aspects are rarely mentioned positively but tend to elicit negative impressions when expectations are not met. A comparatively high level of customer expectation regarding these dimensions may further contribute to this effect pattern. 

Conversely, the topic _Connectivity_ shows only a positive influence on overall customer satisfaction and can, therefore, be classified as a pure Attractive Quality factor. This may be partly explained by its comparatively lower overall influence on customer satisfaction; expectations concerning a hotel’s connectivity are generally modest, and fulfillment of such aspects is appreciated rather than assumed. Conceptually, the results suggest that _Attractive Quality_ features are discernible only at a more fine-grained level of clustering. Such attributes do not tend to correspond to broad topic areas like _Location_ , _Food_ , or _Service_ as wholes, but rather to specific subcategories within these dimensions. Consequently, identifying Attractive Quality factors necessitates a more fine-grained topic clustering approach capable of capturing more nuanced topic areas, such as Connectivity within the broader category of _Location_ . This finding constitutes an important insight into the conceptual understanding and empirical identification of Kano quality features in online feedback data through unsupervised machine learning methods. 

Finally, the ANOVA results further validated the regression-based findings. Mustbe Quality features, such as room quality, were found to significantly reduce customer satisfaction when not fulfilled, as evidenced by the notable contrasts in ratings between reviews with and without negative remarks regarding these factors. A similar pattern was observed for the identified Attractive Quality factor _Connectivity_ , with reviews containing positive remarks toward this topic area predominantly associated with higher overall satisfaction rating. 

```
1 3
```

**<mark>20</mark>** <mark>Page 24 of 31</mark> 

D. Regitz et al. 

### **4.5.2 Theoretical contribution** 

As highlighted in this paper, previous studies applying machine learning approaches within a Kano analytical framework have typically identified only relatively broad quality categories (Chen et al. 2019; Lee et al. 2021; Zhang et al. 2021). As an important theoretical contribution to the research field of Kano-based customer satisfaction modeling using online customer feedback (Chen et al. 2019; Zhang et al. 2021; Lee et al. 2021; Binder et al. 2023; Zhou et al. 2023; Zhao et al. 2024), this study presented an unsupervised machine learning technique capable of identifying more fine-grained topics and corresponding nuanced Kano quality features for the hospitality domain. In technical terms, online customer feedback is grouped into fine-grained topics at the sentence or statement level, and the corresponding sentiment is aggregated back to the review level and related to overall customer satisfaction through a linear regression. All regression coefficients pointed into the expected direction, and 15 out of 20 were statistically significant, thereby underpinning the effectiveness and validity of the presented approach. An additional ANOVA-based validation confirmed that Must-Be or Attractive Quality features are indeed reflected in the corresponding online reviews, providing additional empirical support for the robustness of the proposed methodology. 

On a conceptual level, this study provides new insights into the influence of different topics, i.e., service elements, on customer satisfaction and their classification into the various quality categories of the Kano model. The categorization of topics covered all three Kano categories, demonstrating the applicability of the Kano framework for analyzing user generated content in the form of online customer feedback. Notably, Attractive Quality features could only be identified at the fine-grained topic level, demonstrating that the proposed approach to fine-grained topic detection is essential to unlock the full analytical potential of the Kano modelling approach – constituting a contribution to the research field of customer satisfaction analysis based on the Kano model (Bi et al. 2020; Zavira et al. 2023; Zhou et al. 2023; Slevitch et al. 2024). 

### **4.5.3 Practical implications** 

The implications of these findings are invaluable for practitioners and businesses in the hospitality industry, offering actionable insights and contributing to a broader understanding of customer satisfaction dynamics based on online customer feedback. Analyzing customer feedback at the level of fine-grained topics or features fosters a more nuanced understanding of how attribute performance affects overall customer satisfaction. This, in turn, enables businesses to effectively prioritize areas for improvement and develop targeted strategies to enhance customer satisfaction and ultimately customer loyalty. Such improvements allowing a more precise resource allocation support both the optimization of the tourism offer and its online marketing. Compared to traditional feedback analysis based on customer survey data, the analysis of online feedback offers several advantages. First, customer feedback in the form of user-generated content (UGC) represents the most authentic source of customer opinions. This aspect is particularly relevant for the human-centered experience context of the hospitality sector. Second, the general effort to gather online feedback, 

```
1 3
```

Online customer feedback for identifying KANO product quality… 

<mark>Page 25 of 31</mark> **<mark>20</mark>** 

especially in large quantities, is comparably low. Thus, the relevance of the findings should contribute to a more regular use of online data for quality monitoring in the hospitality sectors. Finally, online customer feedback allows for timely and continuous analysis, facilitating the early identification of trends and short-term changes in customer perceptions over time, thus, strengthening the hotel businesses’ potential to innovative. 

Regarding the specific results of this study, the features _Staff_ and _Service_ exert the strongest impact on customer satisfaction and should therefore be given the highest managerial priority. The targeted differentiation of topics or features according to the Kano categories enables a more precise and focused assessment of the factors influencing customer satisfaction. The model identified _Room_ , _Stay_ , and _Check-In_ as _Must-be_ factors. Unlike _One-Dimensional_ factors, which influence satisfaction in both directions, _Must-Be_ factors should meet expectations but need not necessarily exceed them, as exceeding expectations in these areas does not further increase satisfaction. _Attractive_ factors, on the other hand, have a lower overall priority compared to _Must-Be_ and _One-Dimensional_ factors. However, they possess the strong potential to evoke positive emotions and differentiate a property positively from its competitors. In this study, _Connectivity_ emerged as an _Attractive_ factor, suggesting that accommodation providers may explore ways to improve the perceived connectedness of their properties. However, the cost–benefit ratio of such improvements should be critically evaluated, particularly since this factor has a relatively low overall impact on customer satisfaction. 

When considering the practical implementation of the proposed approach, it should be noted that the extraction of UGC, particularly through web-scraping techniques, may raise ethical and data-protection concerns. Although users have made their feedback publicly available, the large-scale and automated extraction and analysis of UGC can give rise to privacy issues that need to be carefully addressed when applying such methods in practice. 

## **5 Conclusions** 

This study explored the intricate non-linear relationship between attribute performance and overall customer satisfaction by employing a methodology encompassing topic detection, sentiment analysis, regression analysis and validation through ANOVA. More concretely, the paper presented a novel, fine-grained approach for classifying quality factors based on topic areas identified through unsupervised machine learning techniques. Identifying specific topic areas and the corresponding sentiment on the statement or sentence level facilitates a more nuanced understanding of the positive and negative effects of fulfillment or non-fulfillment of each topic area on overall customer satisfaction. A subsequent regression analysis provided clearly interpretable results that highlight the impact of each topic area, thereby making the findings more actionable for practitioners (Höpken & Fuchs 2022). A final Analysis of Variance (ANOVA) further validated the proposed approach and enabled a positive answer to the research question: Can more fine-grained topic detection and 

```
1 3
```

**<mark>20</mark>** <mark>Page 26 of 31</mark> 

D. Regitz et al. 

sentiment analysis techniques be applied to validly and reliably identify the relevant Kano attributes that affect overall customer satisfaction in the hospitality domain? 

The findings indicate that while most identified topic areas exhibit One-Dimensional Quality characteristics, positively influencing customer satisfaction when fulfilled and negatively when not, subtle variations across attributes can still be observed. The regression models revealed significant relationships between attribute performance and overall customer satisfaction, underscoring the statistical reliability of the models applied. Moreover, the final validation procedure, particularly the ANOVA, further reinforced the credibility of these findings. For instance, Must-Be quality factors such as room quality were found to exert a significant negative effect on customer satisfaction when not fulfilled, whereas the identified Attractive Quality factor Connectivity demonstrated a positive impact when fulfilled. These results emphasize the asymmetric nature of customer satisfaction formation and the importance of specific attributes in shaping the customers’ overall evaluation. Accordingly, this study contributes to theory and method development as well as to the building of knowledge for tourism businesses by (1) providing a refined method for analyzing Kano factors on a more fine-grained level and (2) identifying statistically significant and practically reliable Kano factors that asymmetrically influence customer satisfaction. 

The insights discussed above carry important implications for businesses operations in the hospitality industry. By gaining a deeper understanding of how attribute performance affects overall customer satisfaction, hospitality providers can more effectively prioritize areas for improvement, thereby enhancing their competitiveness and reputation within the marketplace. In conclusion, our research contributes to a broader understanding of customer satisfaction dynamics reflected in online customer feedback, offering actionable insights for businesses seeking to optimize their offerings and elevate the customer experience. The employed methodology, combining advanced topic detection, sentiment analysis, and rigorous validation, underscores the robustness and practical significance of the findings achieved. 

## **6 Limitations and future research** 

Despite the significant findings presented, this study is subject to several limitations. One limitation concerns the sample size and geographical scope of the analysis. The study focused solely on English-language reviews extracted from TripAdvisor concerning the Lake of Constance region in southern Germany. Since most online reviews for this region are predominately written in German and the COVID-19 pandemic caused a sharp decline in review activity during 2020 and 2021, only 1,392 entries could be extracted for the five lake cities of Konstanz, Lindau, Bregenz, Friedrichshafen, and St. Gallen. Expanding the geographical scope to include reviews from other regions and diverse types of tourist destinations could enhance the generalizability of the findings and provide deeper insights into regional variations of the drivers of customer satisfaction. 

Furthermore, because only English reviews were considered, the exclusion of non-English reviews may have omitted relevant feedback from non-English speaking 

```
1 3
```

Online customer feedback for identifying KANO product quality… 

<mark>Page 27 of 31</mark> **<mark>20</mark>** 

tourists, thereby limiting the practical insights derived. Future research could address this limitation by incorporating multi-lingual reviews, offering a more comprehensive and culturally inclusive understanding of customer satisfaction across different visitor segments. 

Another limitation inherent in the analysis of user-generated content (UGC) is the potential for selection bias. The Lake Constance region may be particularly affected by such bias, as the typical tourist in this area tends to be older and less digitally active, resulting in a smaller proportion of tourists using social media compared to visitors in more urban destinations. Consequently, extending the study to other destinations, particularly urban ones, would be both reasonable and valuable to assess the robustness and transferability of the findings. 

The lexicon-based sentiment analysis achieved an overall accuracy of 77.28%. While this represents a satisfactory result, a margin of error remains, especially within the neutral class, which may influence the interpretation of sentiment polarity for a subset of review sentences. Future studies could therefore employ more advanced sentiment analysis methods suitable for multi-lingual contexts, such as transformerbased models (e.g., BERT or GPT), which better capture the linguistic context and, thus, detect more subtle sentiment expressions, thereby improving both accuracy and analytical depth. 

Finally, future research could also benefit from integrating data from multiple social media and online review platforms. Such multi-modal data analytics approach would provide a more holistic and nuanced perspective on the relationship between online feedback and overall customer satisfaction. Addressing these areas systematically would further enhance the robustness, applicability, and explanatory power of data-driven analyses of online customer feedback in the tourism domain. 

**Author contributions** All authors conceptualized the research design and methodology. D.R. executed all analysis and prepared all figures. All authors wrote and reviewed the manuscript. 

**Funding** Open Access funding enabled and organized by Projekt DEAL. 

**Data availability** Data is available at  h t t p s : / / g i t h u b . c o m / d o m e r e g / R e s e a r c h _ D a t a _ K a n o. 

### **Declarations** 

**Competing interests** The authors declare no competing interests. 

**Open Access** This article is licensed under a Creative Commons Attribution 4.0 International License, which permits use, sharing, adaptation, distribution and reproduction in any medium or format, as long as you give appropriate credit to the original author(s) and the source, provide a link to the Creative Commons licence, and indicate if changes were made. The images or other third party material in this article are included in the article’s Creative Commons licence, unless indicated otherwise in a credit line to the material. If material is not included in the article’s Creative Commons licence and your intended use is not permitted by statutory regulation or exceeds the permitted use, you will need to obtain permission directly from the copyright holder. To view a copy of this licence, visit  h t t p : / / c r e a t i v e c o m m o n s . o r g / l i c e n s e s / b y / 4 . 0 / . 

```
1 3
```

**<mark>20</mark>** <mark>Page 28 of 31</mark> 

D. Regitz et al. 

## **References** 

- Abdelgwad MM, Soliman THA, Taloba AI (2022) Arabic aspect sentiment Polarity classification using BERT. J Big Data 9(1):115. https://doi.org/10.1186/s40537-022-00656-6 

- Ahani A, Nilashi M, Zogaan WA, Samad S, Aljehane NO, Alhargan A, Sanzogni L (2021) Evaluating medical travelers’ satisfaction through online review analysis. J Hospitality Tourism Manage 48:519–537. https://doi.org/10.1016/j.jhtm.2021.08.005 

- Ali T, Omar B, Soulaimane K (2022) Analyzing tourism reviews using an LDA topic-based sentiment analysis approach. MethodsX 9(101894). https://doi.org/10.1016/j.mex.2022.101894 

- Al Rabaiei K, Alnajjar F, Ahmad A (2021) Kano model integration with data mining to predict customer satisfaction. Big Data Cogn Comput 5(4):66. https://doi.org/10.3390/bdcc5040066 

- Al-Smadi M, Al-Ayyoub M, Jararweh Y, Qawasmeh O (2019) Enhancing aspect-based sentiment analysis of Arabic hotels’ reviews using morphological, syntactic and semantic features. Inf Process Manag 56(2):308–319. https://doi.org/10.1016/j.ipm.2018.01.006 

- Athanasopoulou P, Giovanis N, Ioakimidis A M (2023) How are guests satisfied? Exploring the asymmetric effects of hotel service attributes on customer satisfaction by analyzing online reviews. Tourism: Int Interdisciplinary J 71(1):8–28. https://doi.org/10.37741/t.71.1.1 

- Aung KZ, Myo NN (2017) Sentiment analysis of students’ comment using lexicon based approach. In 2017 IEEE/ACIS 16th international conference on computer and information science (ICIS), IEEE, pp 149–154. https://doi.org/10.1109/ICIS.2017.7959985 

- Bhattacharya P, Mukhopadhyay A, Saha J, Samanta B, Mondal M, Bhattacharya S, Suman P (2023) Perception-satisfaction based quality assessment of tourism and hospitality services in the Himalayan region: an application of AHP-SERVQUAL approach on Sandakphu Trail, West Bengal, India. Int J Geoheritage Parks 11(2):259–275. https://doi.org/10.1016/j.ijgeop.2023.04.001 

- Bi JW, Liu Y, Fan ZP, Zhang J (2020) Exploring asymmetric effects of attribute performance on customer satisfaction in the hotel industry. Tour Manag 77(104006).  h t t p s : / / d o i . o r g / 1 0 . 1 0 1 6 / j . t o u r m a n . 2 0 1 9 . 1 0 4 0 0 6 

- Binder M, Vogt A, Bajraktari A, Vogelsang A (2023) Automatically classifying Kano model factors in app reviews. In International Working Conference on Requirements Engineering: Foundation for Software Quality, Cham: Springer Nature Switzerland, pp 245–261.  h t t p s : / / d o i . o r g / 1 0 . 6 0 8 4 / m 9 . fi  g s h a r e . 2 1 6 1 8 8 5 8 

- Brandt RD (1987) A procedure for identifying value-enhancing service components using customer satisfaction survey data. Add Value your Service 6(1):61–65 https://doi.org/10.1108/eb024732. 

- Chatterjee S, Ghatak A, Nikte R, Gupta S, Kumar A (2023) Measuring SERVQUAL dimensions and their importance for customer-satisfaction using online reviews: a text mining approach. J Enterp Inform Manage 36(1):22–44. https://doi.org/10.1108/JEIM-06-2021-0252 

- Chen D, Zhang D, Liu A (2019) Intelligent Kano classification of product features based on customer reviews. CIRP Ann 68(1):149–152. https://doi.org/10.1016/j.cirp.2019.04.046 

- Chen J, Becken S, Stanic B (2022) Lexicon-based Chinese Language sentiment analysis method. Comput 

   - Sci Inform Syst 16(2):639–655. https://doi.org/10.2298/CSIS181015013C 

- Feldman R (2013) Techniques and applications for sentiment analysis. Commun ACM 56(4):82–89. https://doi.org/10.1145/2436256.243627 

- Fuchs M, Höpken W (2022) Clustering: Hierarchical, k-means, density-based spatial clustering of applications with noise (DBSCAN). In: Egger R (ed) Applied data science in tourism: interdisciplinary approaches, methodologies, & applications. Springer Nature, pp 129–149 

- Fuchs M, Höpken W, Lexhagen M (2017) Business intelligence for destinations: creating knowledge from 

- social media. In Advances in social media for travel, tourism and hospitality, Routledge, pp 290–310 

- Fuchs M, Weiermair K (2003) New perspectives of satisfaction research in tourism destinations. Tourism Rev 58(3):6–14. https://doi.org/10.1016/j.cirp.2019.04.046 

- Fuchs M, Weiermair K (2004) Destination benchmarking: an indicator-system’s potential for exploring guest satisfaction. J Travel Res 42(3):212–225. https://doi.org/10.1177/0047287503258 

- Garcia K, Berton L (2021) Topic detection and sentiment analysis in Twitter content related to COVID-19 

   - from Brazil and the USA. Appl Soft Comput 101(107057).  h t t p s : / / d o i . o r g / 1 0 . 1 0 1 6 / j . a s o c . 2 0 2 0 . 1 0 7 0 5 7 

Gretzel U, Signala M (2017) Advances in social media for travel, tourism and hospitality. Routledge 

```
1 3
```

Online customer feedback for identifying KANO product quality… 

<mark>Page 29 of 31</mark> **<mark>20</mark>** 

- Höpken W, Fuchs M (2022) Artificial neural networks. In: Buhalis D (ed) Encyclopedia of tourism management and marketing. Edward Elgar Publishing, Cheltenham, pp 187–189.  h t t p s : / / d o i . o r g / 1 0 . 4 3 3 7 / 9 7 8 1 8 0 0 3 7 7 4 8 6 . a r t i fi  c i a l . n e u r a l . n e t w o r k s 

- Höpken W, Fuchs M, Lexhagen M (2024) Analyzing tourism online reviews: an extended approach to hierarchical topic detection using keyword clustering. Tourism: Int Interdisciplinary J 72(1):7–19. https://doi.org/10.37741/t.72.1.1 

- Höpken W, Fuchs M, Menner T, Lexhagen M (2017) Sensing the online social sphere using a sentiment analytical approach. Analytics in smart tourism design: concepts and methods. 129–146.  h t t p s : / / d o i . o r g / 1 0 . 1 0 0 7 / 9 7 8 - 3 - 3 1 9 - 4 4 2 6 3 - 1 _ 8 

- Hu M, Liu B (2004) Mining and summarizing customer reviews. In Proceedings of the tenth ACM SIGKDD international conference on Knowledge discovery and data mining, pp 168–177.  h t t p s : / / d o i . o r g / 1 0 . 1 1 4 5 / 1 0 1 4 0 5 2 . 1 0 1 4 0 7 3 

- Jannach D, Zanker M, Fuchs M (2014) Leveraging multi-criteria customer feedback for satisfaction analysis and improved recommendations. Inform Technol Tourism 14:119–149.  h t t p s : / / d o i . o r g / 1 0 . 1 0 0 7 / s 4 0 5 5 8 - 0 1 4 - 0 0 1 0 - z 

- Kano N, Seraku N, Takahashi F, Tsuji S (1984) Attractive quality and must-be quality 

- Kim B, Kim S, Heo CY (2016) Analysis of satisfiers and dissatisfiers in online hotel reviews on social media. Int J Contemp Hospitality Manage 28(9):1915–1936. https://doi.org/10.1108/IJCHM-04-2015-0177 

- Kuo CM, Chen HT, Boger E (2016) Implementing City hotel service quality enhancements: integration of Kano and QFD analytical models. J Hospitality Mark Manage 25(6):748–770.  h t t p s : / / d o i . o r g / 1 0 . 1 0 8 0 / 1 9 3 6 8 6 2 3 . 2 0 1 6 . 1 0 9 6 2 2 5 

- Lee H, Cha MS, Kim T (2021) Text mining-based mapping for Kano quality factor. ICIC Express Lett Part B Applications: Int J Res Surv 12(2):185–191. https://doi.org/10.24507/icicelb.12.02.185 

- Lin Z, Zhang S, Yhang WJ (2024) Exploring servicescape in coastal and marine tourism: insights from text mining and application of Kano model. Asia Pac J Tourism Res 30(2):176–193.  h t t p s : / / d o i . o r g / 1 0 . 1 0 8 0 / 1 0 9 4 1 6 6 5 . 2 0 2 4 . 2 4 2 6 1 7 5 

- Liu B (2011) Web data mining: exploring hyperlinks, contents, and usage data (Vol. 1). Berlin: springer. https://doi.org/10.1007/978-3-642-19460-3 

- Marine-Roig E (2022) Content analysis of online travel reviews. Handbook of e-Tourism. Springer International Publishing, Cham, pp 557–582. https://doi.org/10.1007/978-3-030-48652-5_31 

- Mehraliyev F, Chan ICC, Kirilenko AP (2022) Sentiment analysis in hospitality and tourism: a thematic and methodological review. Int J Contemp Hospitality Manage 34(1):46–77.  h t t p s : / / d o i . o r g / 1 0 . 1 1 0 8 / I J C H M - 0 2 - 2 0 2 1 - 0 1 3 2 

- Menner T, Höpken W, Fuchs M, Lexhagen M (2016) Topic detection: identifying relevant topics in tourism reviews. In Information and Communication Technologies in Tourism 2016: Proceedings of the International Conference in Bilbao, Spain, February 2–5, 2016, Springer International Publishing, pp 411–423. https://doi.org/10.1007/978-3-319-28231-2_30 

- Mikulić J, Prebežac D (2011) A critical review of techniques for classifying quality attributes in the Kano model. Managing Service Quality: Int J 21(1):46–66. https://doi.org/10.1108/09604521111100243 

- Mikulić J, Prebežac D (2016) The Kano model in tourism research: a critical note. Annals Tourism Res 61:25–27. https://doi.org/10.1016/j.annals.2016.07.014 

- Mishra RK, Urolagin S, Jothi JAA, Neogi AS, Nawaz N (2021) Deep learning-based sentiment analysis and topic modeling on tourism during Covid-19 pandemic. Front Comput Sci 3(775368).  h t t p s : / / d o i . o r g / 1 0 . 3 3 8 9 / f c o m p . 2 0 2 1 . 7 7 5 3 6 8 

- Nguyen VH, Ho T (2021) Analyzing customer experience in hotel services using topic modeling. J Inform Process Syst 17(3):586–598. https://doi.org/10.3745/JIPS.04.0217 

- Njeri Kaberere I, Kc B, Hoogendoorn G (2022) Wildlife tourism experiences at the Maasai Mara, kenya: using Kano model to assess tourists’ satisfaction. Tourism: Int Interdisciplinary J 70(4):740–746. https://doi.org/10.37741/t.70.4.14 

- PRNewswire (2022) Travelers push Tripadvisor past 1 billion reviews & opinions! PRNewswire.  h t t p s : / / w w w . p r n e w s w i r e . c o m / n e w s - r e l e a s e s / t r a v e l e r s - p u s h - t r i p a d v i s o r - p a s t - 1 - b i l l i o n - r e v i e w s - - o p i n i o n s - 3 0 1 4 7 2 3 2 9 . h t m l 

- Rouhani S, Mozaffari F (2022) Sentiment analysis researches story narrated by topic modeling approach. Social Sci Humanit Open 6(1). https://doi.org/10.1016/j.ssaho.2022.100309 

- Sauerwein E, Bailom F, Matzler K, Hinterhuber HH (1996) The Kano model: how to delight your customers. Int Working Seminar Prod Econ 1(4):313–327.  h t t p s : / / w w w . r e s e a r c h g a t e . n e t / p u b l i c a t i o n / 2 4 0 4 6 2 1 9 1 _ T h e _ K a n o _ M o d e l _ H o w _ t o _ D e l i g h t _ Y o u r _ C u s t o m e r s 

```
1 3
```

<mark>Page 30 of 31</mark> 

D. Regitz et al. 

**<mark>20</mark>** 

- Schmunk S, Höpken W, Fuchs M, Lexhagen M (2014) Sentiment analysis: Extracting decision-relevant knowledge from UGC. In Information and Communication Technologies in Tourism 2014: Proceedings of the International Conference in Dublin, Ireland, January 21–24, 2014, Springer International Publishing, pp 253–265. https://doi.org/10.1007/978-3-319-03973-2_19 

- Semrush (2024) Top websites in worldwide - Travel & tourism industry. Semrush.  h t t p s : / / w w w . s e m r u s h . c o m / t r e n d i n g - w e b s i t e s / g l o b a l / t r a v e l - a n d - t o u r i s m 

- Slevitch L (2024) Kano model categorization methods: typology and systematic critical overview for hospitality and tourism academics and practitioners. J Hospitality Tourism Res 10963480241230957. https://doi.org/10.1177/10963480241230957 

- Subakti A, Murfi H, Hariadi N (2022) The performance of BERT as data representation of text clustering. J Big Data 9(15). https://doi.org/10.1186/s40537-022-00564-9 

- Tan ANL, Prasetyo YT, Persada SF, Nadlifatin R (2022) Conjoint analysis on the attributes affecting the customers’ preference of hotel accommodation. In Proceedings of the 8th International Conference on Industrial and Business Engineering, pp 413–418. https://doi.org/10.1145/3568834.3568900 

- Tontini G, dos Santos Bento G, Milbratz TC, Volles BK, Ferrari D (2017) The critical incident technique (CIT) and Penalty-Reward contrast analysis (PRCA) applied to online reviews on tripadvisor: evaluation of satisfaction of hotel customers. Int J Hospitality Manage 66(1):106–116.  h t t p s : / / d o i . o r g / 1 0 . 1 0 1 6 / j . i j h m . 2 0 1 7 . 0 7 . 0 1 1 

- Tran PQ, Le HTM, Huynh HX (2023) Opinion mining with interpretable random forests. In Proceedings of the 2023 8th International Conference on Intelligent Information Technology, pp 27–32.  h t t p s : / / d o i . o r g / 1 0 . 1 1 4 5 / 3 5 9 1 5 6 9 . 3 5 9 1 5 9 5 

- Tripadvisor (2021) The power of reviews. Tripadvisor.  h t t p s : / / w w w . t r i p a d v i s o r . c o m / p o w e r o f r e v i e w s . p d f 

- Wartena C, Brussee R (2008) Topic detection by clustering keywords. In 2008 19th international workshop on database and expert systems applications, IEEE, pp 54–58.  h t t p s : / / d o i . o r g / 1 0 . 1 1 0 9 / D E X A . 2 0 0 8 . 1 2 0 

- Wu S, Guo Y (2022) Research on user requirement analysis based on online comment mining and kano model. In International Conference on Human-Computer Interaction, Cham: Springer International Publishing, pp 343–350. https://doi.org/10.1007/978-3-031-06394-7_44 

- Xiang Z, Gretzel U (2010) Role of social media in online travel information search. Tour Manag 31(2):179–188.  h t t p s : / / d o i . o r g / 1 0 . 1 0 1 6 / j . t o u r m a n . 2 0 0 9 . 0 2 . 0 1 6 

- Xu X (2020) Examining an asymmetric effect between online customer reviews emphasis and overall satisfaction determinants. J Bus Res 106:196–210.  h t t p s : / / d o i . o r g / 1 0 . 1 0 1 6 / j . j b u s r e s . 2 0 1 8 . 0 7 . 0 2 2 

- Yang H, Xu H, Qu Y (2025) Managing service failures of hotel robots by combining the Kano model with the service blueprint. Curr Issues Tourism 1–14.  h t t p s : / / d o i . o r g / 1 0 . 1 0 8 0 / 1 3 6 8 3 5 0 0 . 2 0 2 5 . 2 5 5 0 6 4 5 

- Yılmaz Kaya B (2022) Contemplation and analysis of pandemic impacts on accommodation industry and a system reformulation proposal with Kano model: Turkey case. Curr Issues Tourism 25(8):1226– 1241.  h t t p s : / / d o i . o r g / 1 0 . 1 0 8 0 / 1 3 6 8 3 5 0 0 . 2 0 2 1 . 2 0 0 7 8 6 0 

- Yousaf S, Kim JM (2023) Did COVID-19 change preferences for hygiene-related service attributes as satisfiers and dissatisfiers? An analysis of textual content of online hotel reviews. J Hospitality Tourism Manage 56:264–271. https://doi.org/10.1016/j.jhtm.2023.07.001 

- Zavira CM, Ismoyowati D, Yuliando H (2023) Korean restaurants’ consumer needs based on marketing mix through the Kano model. AGRARIS: J Agribusiness Rural Dev Res 9(1):129–149.  h t t p s : / / d o i . o r g / 1 0 . 1 8 1 9 6 / a g r a r i s . v 9 i 1 . 1 8 4 

- Zhang C, Xu Z, Gou X, Chen S (2021) An online reviews-driven method for the prioritization of improvements in hotel services. Tour Manag 87(104382).  h t t p s : / / d o i . o r g / 1 0 . 1 0 1 6 / j . t o u r m a n . 2 0 2 1 . 1 0 4 3 8 2 

- Zhao M, Liu M, Xu C, Zhang C (2024) Classifying travellers’ requirements from online reviews: an improved Kano model. Int J Contemp Hosp M 36(1):91–112. https://doi.org/10.1108/IJCHM-06-2022-0726 

- Zhou K, Yao Z (2023) Analysis of customer satisfaction in tourism services based on the Kano model. Systems 11(7):345. https://doi.org/10.3390/systems11070345 

**Publisher’s note** Springer Nature remains neutral with regard to jurisdictional claims in published maps and institutional affiliations. 

```
1 3
```

Online customer feedback for identifying KANO product quality… 

<mark>Page 31 of 31</mark> **<mark>20</mark>** 

## **Authors and Affiliations** 

### **Dominic Regitz**<sup>**1**</sup> **· Wolfram Höpken**<sup>**1**</sup> **· Matthias Fuchs**<sup>**2,3**</sup> 

- Wolfram Höpken wolfram.hoepken@rwu.de 

Dominic Regitz 

dominic.regitz@rwu.de 

Matthias Fuchs 

matthias.fuchs@unibz.it 

- 1 University of Applied Sciences Ravensburg-Weingarten, Weingarten, Germany 

- 2 Competence Centre for Sustainable Tourism, Bruneck-Brunico, Italy 

- 3 Free University of Bozen-Bolzano, Bolzano, Italy 

```
1 3
```

