Original Research 



# Analyzing Factors Affecting Overall Customer Satisfaction Using Hotel Ratings and Reviews With BERTopic and Three-Factor Theory 

SAGE Open July-September 2025: 1–17 � The Author(s) 2025 DOI: 10.1177/21582440251335169 journals.sagepub.com/home/sgo 

## Jun Li<sup>1</sup> , Byunghyun Lee<sup>1</sup> , and Jaekyeong Kim<sup>2,3</sup> 

### Abstract 

This research was conducted to aid hotels in identifying and enhancing the hotel selection attributes that customers deem important for maintaining revenue and competitive advantage. Departing from conventional survey methods, we utilized BERTopic on the extensive review data from TripAdvisor to extract crucial hotel selection attributes. Through RIPA and PRCA analyses across various hotel star ratings, we sought insights into customer perceptions. The findings unveiled eight hotel selection attributes deemed significant by customers, revealing no differences in implicitly derived importance, satisfaction performance and overall customer satisfaction for staff, trip type, and resort fees across hotel star ratings. However, variations were evident in other hotel selection attributes. Thus, in contrast to prior studies, this research employed big data techniques like BERTopic for topic extraction and utilized PRCA additionally to compensate for the limitations of RIPA, identifying differences among attributes included in the same quadrant. 

### Keywords 

BERTopic, three-factor theory, revised importance-performance analysis, penalty-reward contrast analysis, hotel selection attributes, overall customer satisfaction 

## Introduction 

Advancements in information and communication technologies such as the Internet of Things (IoT), artificial intelligence (AI), and mobile technologies have led to a significant surge in users engaging with online services. This trend has also extended to the hospitality and tourism industries, where various online services are offered (Aldebert et al., 2011; Law et al., 2020; Navı´o-Marco et al., 2018; Yang et al., 2021). Consequently, many customers now use hotel e-commerce platforms to make reservations and pay for their preferred accommodation. One prominent hotel e-commerce platform is TripAdvisor, the world’s largest travel platform, which caters to an average of 490 million users monthly (TripAdvisor, 2019). On these hotel e-commerce platforms, not only do users provide satisfaction ratings for their hotel experiences but they also have the capability to craft detailed reviews of their stays. According to Ady and Quadri-Felitti (2015), as many as 95% of customers make decisions about booking hotels based on customers 

ratings and reviews. Furthermore, it has been demonstrated that the more positive the evaluations of a hotel are, the higher its revenue tends to be in a proportional manner (Anderson & Lawrence, 2014; Gao et al., 2020). Accordingly, to enhance revenue and secure a competitive edge, hotels should identify and improve the attributes that customers consider important through ratings and reviews (Kim & Park, 2017). Therefore, many previous studies have predominantly utilized traditional IPA (Importance-Performance Analysis) techniques to analyze hotel selection attributes that customers consider 

1Department of Big Data Analytics, Graduate School, Kyung Hee University, Seoul, Republic of Korea 

2School of Management, Kyung Hee University, Seoul, Republic of Korea 

3Department of Big Data Analytics, Kyung Hee University, Seoul, Republic of Korea 

#### Corresponding Author: 

Jaekyeong Kim, School of Management, Kyung Hee University, 26 Kyungheedae-ro, Dongdaemun-gu, Seoul 02453, Republic of Korea. Email: jaek@khu.ac.kr 

Creative Commons CC BY: This article is distributed under the terms of the Creative Commons Attribution 4.0 License (https://creativecommons.org/licenses/by/4.0/) which permits any use, reproduction and distribution of the work without further permission provided the original work is attributed as specified on the SAGE and Open Access pages (https://us.sagepub.com/en-us/nam/open-access-at-sage). 

2 

SAGE Open 

important, and their corresponding satisfaction levels (Cvelbar & Dwyer, 2013; Wilkins, 2010). However, traditional IPA has limitations such as multicollinearity issues and the tendency for most hotel selection attribute factors to be skewed toward the first and third quadrants (W. Deng, 2007). To address these limitations, researchers are increasingly utilizing the Revised ImportancePerformance Analysis (RIPA) technique to analyze the relative importance of and satisfaction with hotel selection attributes (S. Huang, 2010; S. Huang et al., 2015; Liu, 2010). Most studies employing the RIPA technique have used data collected through surveys. However, previous studies based on survey data collection have limitations in that they can only gather information on artificially defined hotel selection attributes, and it can be challenging to collect large amounts of data. Therefore, in this study, to address these limitations, we collect a vast amount of hotel star ratings and review data from TripAdvisor. These reviews intricately encompass details of customers’’ travel experiences and preferences (Ding et al., 2020). Utilizing the BERTopic, a sophisticated topic modeling technique, we apply it to the gathered review data to extract the hotel selection attributes deemed significant by the customers. These extracted attributes are then analyzed using the RIPA method, similar to prior research (Bi et al., 2019; Joung & Kim, 2021). 

However, there exists a limitation in the RIPA results where it becomes challenging to discern differences among attributes within the same quadrant. Even if attributes are within the same quadrant, their impact on overall satisfaction can vary significantly (G. C. Ku & Shang, 2020). Recent studies in the hotel and tourism domain have indicated the presence of asymmetric relationships between service attributes and overall satisfaction (Davras & Caber, 2019; C. Zhang et al., 2021; W. T. Zhang et al., 2022). To solve these problems, PRCA (Penalty-Reward Contrast Analysis) is used to be a key analytical technique in these studies (C. Zhang et al., 2021; W. T. Zhang et al., 2022). Therefore, following the RIPA analysis, this study aims to employ the PRCA method to understand how attributes within each quadrant are influenced by specific factors. 

According to previous studies, major differences have been noted in the hotel selection attributes considered significant by customers and overall satisfaction based on hotel star ratings (Soifer et al., 2021). Hotel star ratings serve as the most indicative measure of a hotel’s quality and service scope, shaping customer expectations and biases (Rhee & Yang, 2015). Moreover, varying criteria such as price, provided services, and facilities are associated with different hotel star ratings. Therefore, hotel star ratings can be considered as benchmarks for customers to evaluate service quality (W. J. Huang et al., 

2018). Martin-Fuentes (2016) conducted an analysis of overall customer satisfaction based on hotel star ratings by collecting data from over 14,000 hotels in more than 100 cities worldwide from TripAdvisor and Booking. The results indicated a positive correlation between higher hotel star ratings and overall customer satisfaction. Similarly, Mohsin et al. (2019) performed a survey and IPA (Interpretative Phenomenological Analysis) targeting customers of 3, 4, and 5-star hotels in Lisbon, Portugal, analyzing satisfaction regarding hotel selection attributes. Their analysis revealed differences in the importance of hotel selection attributes and satisfaction levels based on hotel star ratings. Therefore, in this study, we aim to classify and compare hotels in New York, USA, based on the rating criteria provided by TripAdvisor. To achieve this, we collect rating and review data from customers who have visited New York hotels on TripAdvisor. Subsequently, we apply BERTopic to the collected review data to extract the hotel selection attributes valued by customers. We plan to utilize RIPA to understand the relative importance and satisfaction of these selection attributes based on hotel star ratings. Finally, by conducting PRCA, we categorize hotel selection attributes into the three-factor theory: Excitement Factor, Performance Factor, and Basic Factor, providing insights accordingly. 

In this study, we apply BERTopic to a vast amount of reviews to extract the selection attributes that customers deem important, categorized by hotel star ratings. This approach, based on a substantial volume of data, offers a more extensive analysis of customer selection attributes compared to traditional survey-based research. Consequently, the survey questionnaire developed on this basis can potentially yield more objective survey data than previous methods. 

Therefore, this study expands the research on service quality by applying RIPA and additionally utilizes PRCA to understand the impact of hotel selection attributes on overall customer satisfaction. Through this approach, we anticipate providing more specific insights compared to studies that solely rely on RIPA to analyze customer satisfaction regarding hotel selection attributes. Furthermore, based on the results of this study, hotels can enhance their service quality and contribute to overall hotel marketing and management strategies. 

## Related Work 

## BERTopic 

Topic modeling entails the identification of latent themes embedded within collections of words or documents and grouping akin subjects (Blei, 2012). Latent Dirichlet Allocation (LDA) is one of prominent techniques in this domain (Jelodar et al., 2019). However, basic principle 

3 

Li et al. 

of LDA is deriving topics based on word frequency, which leads to the limitation of not considering the context’s sequence and meaning. Recently, a context-aware topic modeling technique called BERTopic has emerged. Unlike traditional topic modeling methods, BERTopic considers the contextual information of words, making it distinct in its approach (Grootendorst, 2022). Therefore, BERTopic is reported to exhibit superior performance compared to conventional prominent topic modeling techniques, as it is built upon a BERT model trained with consideration of contextual word information (Egger & Yu, 2022; Grootendorst, 2022; Meaney et al., 2022). 

The BERTopic algorithm involves a four-step process to derive topics: document embedding extraction, embedding dimension reduction, embedding clustering, and generating topic representations using class-based TF-IDF. First, BERTopic utilizes a pretrained language model, BERT, to perform embedding. Second, Uniform Manifold Approximation and Projection (UMAP) are employed to reduce the dimensions of the embeddings. Third, the Hierarchical Density-Based Spatial Clustering of Applications with Noise (HDBSCAN) generates clusters of semantically similar documents. Finally, the classbased term frequency-inverse document frequency (cTF-IDF) was used to extract keywords representing the topics. However, in this study, K-means clustering was used instead of HDBSCAN. This is because prior research has shown that using K-means clustering instead of HDBSCAN in short sentences, such as reviews, can yield more accurate results (de Groot et al., 2022). Therefore, to extract the topics of hotel selection attributes that are significant to customers who visited hotels from the collected reviews, this study utilizes BERTopic. 

## RIPA 

Traditional Importance-Performance Analysis (IPA) was initially proposed by Martilla and James (1977) as an analytical method to assess the importance of and satisfaction with products and services. However, traditional IPA has limitations such as multicollinearity issues and the skewing of attributes related to products and services toward the first and third quadrants (W. J. Deng et al., 2008; Kano, 1984; Matzler et al., 2004). To address these limitations, W. Deng (2007) introduced the RIPA method. RIPA initially computes overall satisfaction and attribute-specific satisfaction for each product and service. Then, a partial correlation analysis was conducted between attribute-specific satisfaction after undergoing a natural logarithm transformation and overall satisfaction. The resulting partial correlation coefficients were used as the relative importance values. Through this approach, the limitations of traditional IPA, where 



Figure 1. RIPA (W. Deng, 2007). 

attributes tend to be skewed toward the first and third quadrants, can be minimized. 

RIPA consists of four quadrants, as illustrated in Figure 1. The X-axis represents satisfaction performance with products and services, whereas the Y-axis represents implicitly derived importance. The four quadrants were formed based on the average values of the X-axis (Satisfaction Performance) Y-axis (Implicitly derived Importance). Among the four quadrants, the first represents the ‘‘Keep up the good work’’ quadrant. Attributes with both high importance and satisfaction are located in this quadrant. Service providers must maintain the attributes in this quadrant to enhance customer satisfaction continuously. The second quadrant, ‘‘Concentrate here’’ quadrant represents a quadrant where attributes have high importance but low satisfaction. In this quadrant, the attributes require focused improvements by company managers to enhance customer satisfaction. The third quadrant represents the ‘‘Low priority’’ quadrant. This quadrant is characterized by attributes that have both low importance and low satisfaction. For the attributes within this quadrant, it is more effective to allocate more resources to improve the attributes located in the first or second quadrant rather than giving them higher priority. Lastly, the fourth quadrant represents the ‘‘Possible overkill’’ quadrant. This quadrant is characterized by attributes with low importance and high satisfaction. This signifies that excessive resources and effort are being devoted to these attributes. 

In the field of the hotel industry, studies analyzing customer satisfaction using the RIPA method proposed by W. Deng (2007) have been actively conducted (Caber et al., 2012; S. Huang, 2010; G. C. M. Ku & Mak, 2017). However, these previous studies mainly collected data through survey methods, which limited information collection to factors subjectively predefined by researchers 

4 

SAGE Open 



satisfaction when fulfilled, but dissatisfaction arises when they are not fulfilled. Therefore, in this study, we employed the PRCA technique to determine the category of each hotel selection attribute in terms of the threefactor theory. Subsequently, we intend to incorporate these findings into the interpretation of RIPA results, ultimately providing significant insights and recommendations. 

## Methodology 

Figure 2. Three-factor theory (Kano, 1984). 

and posed challenges in acquiring large-scale data. Therefore, to address these limitations, we utilized data collected from TripAdvisor, including a vast number of reviews and ratings, using web-crawling techniques. Furthermore, we applied BERTopic to the collected reviews to extract hotel selection attributes. Subsequently, we intend to perform RIPA using the derived hotel-selection attributes. 

## PRCA 

The PRCA is an applied method based on Kano (1984) study aimed at identifying attributes that can enhance customer satisfaction. This technique is used to analyze the asymmetric impact of product and service attributes (Brandt, 1987). PRCA involves two main steps in determining how each attribute affects overall satisfaction. First, the performance of each attribute for products and services was divided into two groups: High Performance and Low Performance. Dummy variables were generated based on this division. In the second step, the two sets of dummy variables were treated as independent variables and the overall satisfaction rating was set as the dependent variable. Multiple regression analysis was conducted to determine how these variables collectively influenced the overall satisfaction rating. Subsequently, using the obtained regression coefficients of the two sets of dummy variables, the method determines the categorization of each attribute into one of the three factors within the context of the three-factor theory (Fuller€ & Matzler, 2008). 

As depicted in Figure 2, the Three-Factor Theory is classified into three factors: Excitement, Performance, and Basic factors (Matzler & Sauerwein, 2002). Excitement factors lead to satisfaction when fulfilled; however, their absence does not necessarily result in dissatisfaction. Performance factors lead to satisfaction when fulfilled and dissatisfaction when not fulfilled. Finally, the basic factors do not necessarily lead to 

In this study, we aimed to address the limitations of traditional survey methods, which often incur significant time and cost, by collecting rating and review data from customers’ own experiences on TripAdvisor. Consequently, the collected data were analyzed based on hotel star ratings to identify the hotel selection attributes that customers consider important and to explore the differences among them. To achieve this, our study follows a five-step procedure outlined in (Figure 3). In the first stage, data collection involved gathering information about hotels located in New York, along with reviews and ratings provided by hotel guests from the hotel e-commerce platform, TripAdvisor. In the second stage, prior to BERTopic analysis, sentences were segmented and preprocessed. This study utilized NPMI (Normalized Pointwise Mutual Information) values to estimate the number of topics and to extract topics and keywords. In the third stage, Sentiment Analysis is conducted using the Valence Aware Dictionary for Sentiment Reasoning (VADER) sentiment lexicon (Hutto & Gilbert, 2014). In the fourth stage of RIPA, satisfaction was based on the average sentiment scores of sentences within each topic. Furthermore, the previously segmented sentences are restored to their original reviews. In the restored reviews, the sentiment scores for each topic are subjected to a natural logarithm. Subsequently, a partial correlation analysis was conducted between the transformed sentiment scores and overall satisfaction ratings. The resulting partial correlation coefficients were used as indicators of importance. Finally, in the fifth stage, the PRCA analysis was performed. This stage classifies hotel selection attributes into excitement, performance, and basic factors based on the sentiment scores for each topic during the RIPA analysis stage. 

## Data Collection 

As depicted in Figure 4, comprehensive information on hotels provided by TripAdvisor was gathered during the data collection phase. Specifically, the data collection phase involved gathering information from TripAdvisor regarding hotels located in New York, USA. The reason 

Li et al. 

5 



Figure 3. Research framework. 



<!-- Start of picture text -->
Overall Customer Satisfaction<br>Hotel Name<br>Hotel Class<br>Hotel Review<br><!-- End of picture text -->

Figure 4. Data collection examples. 

for choosing New York City in this study is that it has the highest number of hotels and reviews on TripAdvisor (Xiang et al., 2018). Additionally, New York City attracts customers with diverse purposes such as business, leisure, and family travel (Xiang et al., 2018). Therefore, we collected information on reviews written by customers who visited hotels in New York, including the overall satisfaction ratings on a 5-point scale, the dates of the reviews and ratings, hotel names, and hotel star ratings. Hotels with fewer than 200 collected reviews were excluded from the analysis. This exclusion was done to prevent potential biases in the results, as hotels with fewer than 200 reviews might lead to skewed outcomes (Arenas-Ma´ rquez et al., 2021). 

more than one sentence associated with distinct attributes (Albayrak et al., 2021; Shang et al., 2022). The reviews were segmented into sentences using the Spacy package within Python. Following this, preprocessing steps such as conversion to lowercase, tokenization, removal of special characters, and elimination of stopwords are carried out. Subsequently, the number of topics was estimated. In this study, the topic count was estimated using the NPMI value (Bouma, 2009). NPMI serves as a metric to gauge the semantic coherence of topics. Higher values indicate stronger semantic consistency. After determining the number of topics, BERTopic was executed to derive topics and keywords. Subsequently, suitable names were assigned to each topic, based on the extracted topics and keywords. 

## BERTopic 

Prior to conducting the BERTopic analysis, the collected reviews were divided into individual sentences, as shown in Figure 5. This is because a single review comprises 

## Sentiment Analysis 

In this study, the VADER sentiment lexicon was employed to assign sentiment scores to the reviews for 

6 

SAGE Open 



Figure 5. Spacy sentence segmentation and BERTopic analysis process. 





Figure 6. Converting to a 5-point scale after sentiment analysis. 

Table 1. Convert Composite Score to 5-Point Scale (Albayrak et al., 2021). 

|21|20.9|20.8|20.7|20.6|20.5|20.4<br>|20.3|20.2|20.1|0|0.1|0.2|0.3<br>0.4|0.5|0.6<br>0.7<br>0.8<br>0.9<br>1|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|Awful|(1)||||Bad (|2)||||Neutral (3)|Good|(4)|||Perfect (5)|
|<br>‘‘\2|<br> 0.55’’||||<br>‘‘ø2|<br> 0.55 and|\0’’|||<br>‘‘= 0’’|<br>‘‘.0|<br>and|<0.55’’||<br>‘‘.0.55’’|



each topic. Sentiment scores were derived within the range of 21 to + 1 (Hutto & Gilbert, 2014). A sentiment score close to 21 indicates a negative sentiment, while a score near + 1 indicates a positive sentiment for the respective sentence. 

In line with TripAdvisor’s provision of a 5-point Likert scale for customers to evaluate their overall satisfaction with hotels, this study referred to Albayrak et al. (2021) and Shang et al. (2022). Using VADER, the derived sentiment scores were transformed into a 5-point Likert scale, as shown in Table 1. Specifically, sentiment scores below 20.55 were converted to 1 point, and scores greater than or equal to 20.55 but less than 0 were transformed to 2 points. For sentiment, scores of 0, 3 were assigned; scores greater than 0 and less than or equal to 0.55 correspond to 4 points; and scores above 0.55 are mapped to 5 points. Figure 6 serves as an example, illustrating the sentiment scores derived from the sentiment analysis of four sentences within Review 1, transformed into a 5-point Likert scale. 

## RIPA 

In the RIPA phase, sentiment scores on a 5-point Likert scale for each topic were arithmetically averaged to produce an index used as the Satisfaction Performance value in the RIPA method. An example of this is shown in Figure 7. Initially, as shown in Step 1 of Figure 7, Review 1 consists of four sentences. Sentence 1 has a sentiment score of 5 for Topic 2, sentence 2 has a sentiment score of 3 for Topic 1, sentence 3 has a sentiment score of 3 for Topic 2, and finally, sentence 4 has a sentiment score of 2 for Topic N. Thus, both sentences 1 and 3 share a common sentiment score for Topic 2. In such cases, following the approach of Shang et al. (2022), the sentiment scores were arithmetically averaged and restored to their original form. Consequently, the final sentiment score for Topic 2 became 4. Therefore, in Step 2, the sentences that were previously divided were reconstructed to their original form within the review, followed by computing the arithmetic mean for each topic to derive the Satisfaction Performance. 

Li et al. 

7 



Figure 7. Satisfaction performance derivation process. 

In Step 3 of Figure 8, the sentiment scores for each topic in every review were natural logarithmic transformations, and a partial correlation analysis was conducted between the overall satisfaction score of the review and the sentiment scores. 

Finally, in Step 4 of Figure 9, the partial correlation coefficients obtained from the analysis are utilized as Implicitly Derived Importance values within the context of the RIPA, enabling a comparative analysis of the implicitly derived importance and satisfaction performance of the selected attributes across different hotel star ratings. 

## PRCA 

In the PRCA step, we first created two dichotomized High Performance and Low Performance dummy variables for each hotel-selection attribute. We then analyzed how the High Performance and Low Performance dummy variables for each hotel selection attribute affect overall satisfaction using a multiple regression analysis. 

topic from the sentiment analysis step (Albayrak & Caber, 2013). If the sentiment score is 4 or 5, High Performance is labeled as 1 and Low Performance is labeled as 0. Conversely, if the emotional score was 1 or 2, we marked High Performance as 0 and Low Performance as 1. For a sentiment score of 3, enter 0 for High Performance and 0 for Low Performance. 

### Step 2: Regression analysis 

In step 2, we set the dummy variables of high and low performance for each topic as independent variables and the rating, which refers to overall hotel guest satisfaction, as the dependent variable. We then classified each hotel selection attribute into factors of the three-factor theory using the nonstandardized coefficients of high and low performance calculated by performing multiple regression analysis for each hotel star rating. 

### Step 3: Classifying the attributes 

### Step 1: Variate the dummy 

In Step 1, we created dummy variables for High Performance and Low Performance using the sentiment scores of the reviews for each hotel-selection attribute 

Finally, the unstandardized coefficients of High Performance and Low Performance for each hotel selection attribute, calculated from the multiple regression analysis for each hotel star rating were used to classify each hotel selection attribute into excitement, 

8 

SAGE Open 



Figure 8. Implicitly derived importance derivation process. 





Figure 9. RIPA matrix example. 

performance, and basic factors. For this purpose, this study classifies hotel selection attributes as excitement factors if the value of the unstandardized coefficient of High Performance divided by the value of the unstandardized coefficient of Low Performance is greater than 1.1, basic factors if it is less than 0.9, and performance factors if it is greater than 0.9 and less than 1.1, according to the criteria proposed by Fuller and Matzler (2008).€ 

in New York, USA, from January to December 2019. The basic statistics for this study are presented in Table 2. Ultimately, 26,879 reviews and ratings for 161 3-star hotels, were further divided into 197,978 sentences. For the 4-star hotels, there were 43,885 reviews and ratings for 159 hotels. The reviews were divided into a total of 318,977 sentences. Finally, 77,690 reviews and ratings for the 5-star hotels, spread across 39 hotels were obtained. These reviews were divided into 571,087 sentences. 

## Experimental Results 

## Data Basic Statistics 

Customer reviews and ratings were collected from the TripAdvisor platform for 3, 4, and 5-star hotels located 

## Topic Identification 

Before conducting the BERTopic analysis, the number of topics was determined using the NPMI values, as 

9 

Li et al. 

Table 2. Data-Driven Statistics. 

|Category|3-Star hotel|4-Star hotel|5-Star hotel|Total|
|---|---|---|---|---|
|Hotel|161|159|39|359|
|Sentence|197,978|318,977|54,132|571,087|
|Review|26,879|43,885|6,926|77,690|





Figure 10. NPMI result. 

illustrated in Figure 10. Figure 10 shows the NPMI values for each topic. It is evident that the NPMI value is highest when the number of topics is set to 8. This indicates that when the number of topics was set to 8, the keywords of the topics exhibited a high level of semantic consistency. Therefore, in this study, the number of topics was set to 8. 

The study derived 8 topics using BERTopic, along with their corresponding 10 keywords, as presented in Table 3. Moreover, each topic was named by considering the keywords within the topic as well as relevant keywords from previous research (Ban et al., 2019; 

Buschken€ & Allenby, 2016; Srivastava & Kumar, 2021; Xu & Li, 2016; J. Zhang & Piramuthu, 2018). Topic 1 is composed of keywords such as ‘‘room,’’ ‘‘clean,’’ and ‘‘bed,’’ indicating a topic related to the quality of the room. Topic 2 is composed of keywords such as ‘‘breakfast,’’ ‘‘bar,’’ ‘‘restaurant,’’ and ‘‘coffee,’’ indicating a topic related to F&B (food and beverage) services. In Topic 3, keywords like ‘‘bathroom,’’ ‘‘shower,’’ and ‘‘towel’’ appear, signifying attributes related to the quality and condition of the bathroom. The main keywords in Topic 4 are ‘‘staff,’’ ‘‘helpful,’’ and ‘‘service,’’ focusing on the behavior and attitude of the staff members. Topic 5 is a trip type and consists of keywords such as travel, family, and business. The types of customers who visit the hotel are divided into family, couple, and business, which means customized services are provided according to these types of visits. Topic 6 revolves around location attributes with keywords like ‘‘park,’’ ‘‘square,’’ and ‘‘center.’’ In Topic 7, keywords like ‘‘desk,’’ ‘‘reception,’’ and ‘‘bag’’ appear, highlighting the services offered at the front desk. Lastly, Topic 8 pertains to resort fees, with keywords like ‘‘fee,’’ ‘‘charge,’’ ‘‘wifi,’’ and ‘‘tax,’’ indicating charges that are separate from the base room rate. These could include amenity fees, resort fees, or hidden hotel booking fees that guests might have to pay in addition to the room rate. Table 3 lists the keywords related to each topic as a result of the BERTopic analysis. 

## RIPA and PRCA Result 

The RIPA analysis results for hotel star ratings of 3, 4, and 5-star categories are presented in Figures 11 to 13, respectively. In the RIPA Matrix, the X-axis corresponds to Satisfaction Performance, whereas the Y-axis represents Implicitly Derived Importance. The average satisfaction for 3-star hotels was 3.733, with an average importance of 0.176. For 4-star hotels, the average 

Table 3. BERTopic Result. 

|Topic1<br>Room|Topic2<br>F&B|Topic3<br>Bathroom|Topic4<br>Staff|Topic5<br>Trip type|Topic6<br>Location|Topic7<br>Front desk|Topic8<br>Resort fee|
|---|---|---|---|---|---|---|---|
|Room|Breakfast|Bathroom|Staff|Trip|Park|Desk|Fee|
|Clean<br>Bed<br>Elevator|Bar<br>Restaurant<br>Coffee|Shower<br>Noise<br>Sleep|Helpful<br>Friendly<br>Service|Visit<br>Location<br>Family|Square<br>Subway<br>Walk|Luggage<br>Reception<br>Bag|Charge<br>Wifi<br>Check|
|Comfortable|Food|Towel|Customer|Birthday|Central|Guest|Reservation|
|Small|Drink|Window|Thank|Weekend|Station|Greet|Card|
|View|Wine|Light|Professional|Travel|Close|Doorman|Credit|
|Recommend|Lounge|Quiet|Accommodate|City|Distance|Smile|Resort|
|Floor|Eat|Air|Care|Business|Broadway|Check|Tax|
|Price|Rooftop|Toilet|Help|Place|Location|Staff|Pay|



10 

SAGE Open 



Figure 11. 3-Star hotel RIPA result. 



Figure 12. 4-Star hotel RIPA result. 



For 3-star hotels, the RIPA analysis results indicate that attributes such as room, staff, front desk, and F&B contained the ‘‘Keep up the good work’’ quadrant, while resort fees and bathroom attributes are contained in the ‘‘Low Priority’’ quadrant. Meanwhile, location and trip type are positioned in the ‘‘Possible Overkill’’ quadrant. 

Upon examining the RIPA analysis results for 4-star hotels, it is observed that attributes like room, staff, and front desk are contained in the ‘‘Keep up the good work’’ quadrant. The bathroom attribute is contained in the ‘‘Concentrate Here’’ quadrant, and the resort fees attribute falls within the ‘‘Low Priority’’ quadrant. Additionally, attributes related to location, trip type, and F&B are in the ‘‘Possible Overkill’’ quadrant. 

Moving to the analysis of 5-star hotels, the results reveal that attributes like staff, room, and F&B are encompassed by the ‘‘Keep up the good work’’ quadrant. Attributes of the bathroom and resort fees are contained in the ‘‘Low Priority’’ quadrant, while attributes related to trip type, front desk, and location fall within the ‘‘Possible Overkill’’ quadrant. 

The PRCA results for 3-star hotels are presented in Table 4. The PRCA analysis results for 3-star hotels indicate that attributes such as room, F&B, staff, trip type, and front desk are classified as excitement factors, whereas only the bathroom attribute is a performance factor. Furthermore, the location and resort fee attributes were categorized as basic factors. 

The PRCA results for 4-star hotels are listed in Table 5. In the case of 4-star hotels, the PRCA analysis results demonstrate that attributes such as room, F&B, staff, trip type, and front desk are classified as excitement factors, whereas bathroom, location, and resort fee attributes are classified as basic factors. 

The PRCA outcomes for 5-star hotels are presented in Table 6. The PRCA analysis results for 5-star hotels reveal that F&B, staff, trip type, location, and front desk attributes are identified as excitement factors. The bathroom attribute was classified as a performance factor, and attributes related to room and resort fees were categorized as basic factors. 

Finally, summarizing the RIPA and PRCA analysis results for 3-star, 4-star, and 5-star hotel categories in this study yields Table 7. 

## Discussion 

Figure 13. 5-Star hotel RIPA result. 

satisfaction was 3.777, accompanied by an average importance of 0.209. Finally, for 5-star hotels, the average satisfaction was 3.847, with an average importance of 0.168. 

In this study, we extracted the factors that hotel visitors consider important using BERTopic and analyzed the attributes and satisfaction that customers consider important for 3, 4, and 5-star hotels through RIPA and PRCA. Firstly, the hotel selection attribute regarding the room is contained in the ‘‘Keep up the good work’’ 

Li et al. 

11 

Table 4. 3-Star Hotel PRCA Result. 

||Dummy variable regressi|on coefficients****|||
|---|---|---|---|---|
|Hotel selection attributes|High performance|Low performance|IR|Categorization|
|Room|0.421***|20.246***|1.711|Excitement factor|
|F&B|0.376***|20.11***|3.418|Excitement factor|
|Bathroom|0.745***|0.796***|0.936|Performance factor|
|Staff|0.444**|20.044***|10.091|Excitement factor|
|Trip type|0.319|0.01***|31.9|Excitement factor|
|Location|0.074***|20.427***|0.173|Basic factor|
|Front desk|0.657***|0.487***|1.349|Excitement factor|
|Resort fee|0.359***|0.796***|0.451|Basic factor|



Note. IR = high performance/|low performance|. ***p\.001, **p\.01; R<sup>2</sup> : .358; F: 937.28; ****Unstandardized Beta Coefficient. Dependent Variable: Overall customer satisfaction. 

Table 5. 4-Star Hotel PRCA Result. 

||Dummy variable regressi|on coefficients****|||
|---|---|---|---|---|
|Hotel selection attributes|High performance|Low performance|IR|Categorization|
|Room|0.381***|20.17***|2.241|Excitement factor|
|F&B|0.385***|20.037***|10.405|Excitement factor|
|Bathroom|0.728***|0.905***|0.804|Basic factor|
|Staff|0.345***|20.145***|2.379|Excitement factor|
|Trip type|0.286*|20.028***|10.214|Excitement factor|
|Location|0.115***|20.3***|0.383|Basic factor|
|Front desk|0.758***|0.555***|1.366|Excitement factor|
|Resort fee|0.451***|0.977***|0.462|Basic factor|



Note. IR = high performance/|low performance|. ***p\.001, *p\.05; R<sup>2</sup> : .347; F: 1456.979;<sup>****</sup> Unstandardized Beta Coefficient. Dependent Variable: Overall customer satisfaction. 

Table 6. 5-Star Hotel PRCA Result. 

||Dummy variable regressi|on coefficients****|||
|---|---|---|---|---|
|Hotel selection attributes|High performance|Low performance|IR|Categorization|
|Room|0.142***|20.343***|0.414|Basic factor|
|F&B|0.361***|0.129***|2.798|Excitement factor|
|Bathroom|0.677***|0.708***|0.956|Performance factor|
|Staff|0.233***|20.124***|1.879|Excitement factor|
|Trip type|0.162***|20.14***|1.157|Excitement factor|
|Location|0.88*|20.227***|3.877|Excitement factor|
|Front desk|0.696***|0.614***|1.134|Excitement factor|
|Resort fee|0.395**|0.913***|0.433|Basic factor|



Note. IR = high performance/|low performance|. ***p\.001, **p\.01, *p\.05; R<sup>2</sup> : .294; F: 180.092; ****Unstandardized Beta Coefficient. Dependent Variable; Overall customer satisfaction. 

quadrant for all 3, 4, and 5-star hotels. This is consistent with the findings of the previous study conducted by Mohsin et al. (2019), which supports this result. Thus, it can be inferred that room is a significant factor considered by all customers visiting 3, 4, and 5-star hotels and that it is a selection attribute that currently satisfies their 

level of satisfaction. Therefore, this study suggests that hotels maintain their current approach to providing room services. According to the PRCA results, 3 and 4- star hotels were classified as excitement factors, while 5- star hotels were classified as basic factors. This suggests that customers of 3 and 4-star hotels primarily visit the 

12 

SAGE Open 

Table 7. 3, 4, 5-Star Hotel RIPA and PRCA Result. 

|Hotel selection|3-Star hotel||4-Star hotel||5-Star hotel||
|---|---|---|---|---|---|---|
|attributes|RIPA|PRCA|RIPA|PRCA|RIPA|PRCA|
|Room<br>F&B<br>Bathroom|Keep up the good work<br>Keep up the good work<br>Low priority|Excitement<br>Excitement<br>Performance|Keep up the good work<br>Possible overkill<br>Concentrate here|Excitement<br>Excitement<br>Basic|Keep up the good work<br>Keep up the good work<br>Low Priority|Basic<br>Excitement<br>Performance|
|Staff|Keep up the good work|Excitement|Keep up the good work|Excitement|Keep up the good work|Excitement|
|Trip type|Possible overkill|Excitement|Possible overkill|Excitement|Possible overkill|Excitement|
|Location|Possible overkill|Basic|Possible overkill|Basic|Possible overkill|Excitement|
|Front desk|Keep up the good work|Excitement|Keep up the good work|Excitement|Possible overkill|Excitement|
|Resort fee|Low priority|Basic|Low priority|Basic|Low priority|Basic|



area primarily for tourism purposes; therefore, they may not spend a significant amount of time in their rooms (Xue & Zhang, 2020). On the other hand, customers of 5- star hotels tend to enjoy leisure and vacations by utilizing the facilities and services within the hotel premises (Gupta & Dixit, 2022). In essence, it can be inferred that because customers of 3-star and 4-star hotels spend more time within the hotel premises if their satisfaction with the room is not met, dissatisfaction is likely to arise. Therefore, it is recommended that 3-star and 4-star hotels focus on the continuous improvement of services provided within the rooms, such as cleanliness, ambiance, and room service. On the other hand, for 5-star hotels, maintaining this approach is advisable. 

Secondly, the aspect of F&B as a hotel selection attribute is placed in the ‘‘Keep up the good work’’ quadrant for both 3-star and 5-star hotels. This indicates that both the importance and satisfaction levels of the customers were high in this regard. On the other hand, for 4-star hotels, the F&B aspect falls within the ‘‘Possible Overkill’’ quadrant, suggesting that while customers perceive lower importance, their satisfaction levels remain high. Satisfaction with F&B services leads to a sense of contentment when met; however, dissatisfaction arises when expectations are not fulfilled. Therefore, both 3- star and 5-star hotels must maintain their current service quality for F&B. On the other hand, 4-star hotels can suffice with their basic F&B offerings, as customers still experience satisfaction. Furthermore, it is evident that F&B acts as an excitement factor for hotels for all 3-star ratings: 3-star, 4-star, and 5-star. Thus, it is anticipated that by maintaining the existing quality of F&B services while offering a more diverse range of services and personalized experiences, customer satisfaction and the intention to revisit can be enhanced. 

Thirdly, the hotel selection attribute related to bathrooms was found to be located in the ‘‘Low Priority’’ quadrant for both 3-star and 5-star hotels, identified as a Performance factor. In other words, this attribute has relatively lower importance and satisfaction than other 

hotel selection attributes. Therefore, even though this attribute is not perceived as highly significant compared with other service qualities, improving service quality beyond its current state could lead to increased customer satisfaction. To address this, it is deemed necessary for 3-star and 5-star hotels to adequately consider bathroom quality attributes as a prospective long-term improvement initiative. On the other hand, 4-star hotels are situated in the ‘‘Concentrate Here’’ quadrant, indicating that there is an immediate need for improvement in this attribute. Furthermore, as indicated by the PRCA results, it was categorized as a basic factor. This signifies that if satisfaction with the bathroom is not met, overall dissatisfaction can arise. Upon reviewing the content of the reviews regarding this aspect, it is evident that comments revolve around factors such as a small bathroom size and instances of fixtures or floors showing signs of wear, which contribute to this perception. Therefore, it is imperative for 4-star hotels to prioritize attributes related to bathrooms over other hotel selection criteria. Regular facility inspections and maintenance measures should be undertaken to address any instances of damaged fixtures and facilities and ensure an improved guest experience. Furthermore, it’s worth noting that many customers prefer the provision of packaged bathroom amenities. Thus, hotels should consider investing in quality bathroom supplies and focus on maintaining high levels of bathroom cleanliness to enhance customer satisfaction (Jeong & Kubickova, 2021). 

Fourthly, the staff attribute was contained in the ‘‘Keep up the good work’’ quadrant, indicating its significance in all 3, 4, and 5-star hotels. Furthermore, according to the PRCA analysis results, it was categorized as an excitement factor. Therefore, when customers are satisfied with the hotel selection attribute, satisfaction is generated; however, if customers are not satisfied, it does not necessarily result in dissatisfaction. Accordingly, it is advisable for hotel management to maintain the current employee training approach while periodically assessing how staff service performance behaviors influence 

13 

Li et al. 

customers. For instance, hotels could consider implementing programs that allow customers to evaluate aspects of service such as staff professionalism and attitudes. Therefore, hotel management must enhance and refine the quality of staff services. 

Fifthly, the trip type for all 3, 4, and 5-star hotels falls within the ‘‘Possible Overkill’’ quadrant. Furthermore, based on the PRCA results, this attribute was classified as an excitement factor. Therefore, customers experience satisfaction when this hotel selection attribute is fulfilled, but do not necessarily feel dissatisfaction when it is not met. Accordingly, service attributes related to trip type are not considered important by all customers and can be regarded as attributes for which the current satisfaction levels are already met. In light of this, it is deemed that the hotel should not invest further in enhancing services specifically tailored for business and leisure customers, as providing an excessive level of service might not be necessary. Therefore, it is recommended that hotels focus more on services such as room and staff attitude rather than investing extensively in services related to business and leisure. 

Sixthly, the location attribute is contained in the ‘‘Possible Overkill’’ quadrant for 3-star, 4-star, and 5-star hotels. Thus, it can be deduced that this attribute generally leads to customer satisfaction but is not considered highly important. Moreover, the PRCA results categorized 3 and 4-star hotels as basic factors, while 5-star hotels were classified as excitement factors. This implies that customers of 3 and 4-star hotels often visit for tourism purposes, favoring hotels with convenient public transportation accessibility. Therefore, dissatisfaction can arise among the customers of 3 and 4-star hotels if their expectations regarding location are not met. By contrast, customers of 5-star hotels tend to indulge in leisure and vacation activities while utilizing the facilities and services within the hotel (Alzoubi et al., 2021; Gupta & Dixit, 2022; Xue & Zhang, 2020). Therefore, it can be inferred that they do not prioritize the accessibility of the hotel’s location. It is crucial for hotel management to maintain the current operational approach rather than rapidly enhancing the accessibility of the hotel’s location. 

Seventhly, the front desk attribute has been categorized within the quadrant ‘‘Keep up the good work’’ quadrant for both 3 and 4-star hotels, corroborating the findings of prior research studies (Mohsin et al., 2019; Ying et al., 2018). Furthermore, the PRCA results consistently identified this as an excitement factor. Customers of 3 and 4-star hotels consider the front desk attribute to be significant and are currently experiencing a level of satisfaction fulfillment. Therefore, it is advisable for 3 and 4-star hotels to maintain the current quality of front desk services provided to customers while also considering long-term service expansion. For instance, by 

expanding the scope of front-desk services in areas not typically offered by 3 and 4-star hotels, such as 24-hr customer support, professional telephone assistance, and multilingual support, hotels can continuously enhance customer satisfaction while broadening their service offerings. On the other hand, it is observed that 5-star hotels are situated in the ‘‘Possible Overkill’’ quadrant, and PRCA results also indicate their classification as excitement factors. Therefore, although customers do not significantly prioritize this attribute, their satisfaction appears to be fulfilled. 5-star hotels, the highest tier of accommodation, are known to offer personalized services to their customers (Ao, 2017). Customers are indeed experiencing satisfaction because of the high-quality services provided. Therefore, it is recommended that 5-star hotels should maintain the current state of their front desk services. 

Eighthly, resort fees are contained in the ‘‘low-priority’’ quadrant for all 3, 4, and 5-star hotels. The PRCA results classified this as a basic factor. In essence, this attribute has lower significance and satisfaction than other service qualities, and achieving satisfaction with this aspect does not necessarily result in overall contentment. This pertains to services where customers are charged additional fees for amenities such as Wi-Fi usage, gym access, and similar conveniences during their hotel stay. Rather than investing in enhancing these services, hotels aim to prevent customer dissatisfaction by providing coupons or discount vouchers to ensure a seamless experience. 

## Conclusions 

To address the limitations of previous studies, this research collected an extensive amount of rating and review data. The study conducted a comparative analysis of the implicitly derived importance and satisfaction performance regarding selection attributes categorized by hotel star ratings. For this purpose, a vast amount of overall satisfaction ratings and reviews data was collected from TripAdvisor and utilized in the analysis. Specifically, BERTopic was applied to hotel reviews collected from TripAdvisor, resulting in the identification of 8 topics that customers consider crucial: Room, F&B, Bathroom, Staff, Trip type, Location, Front desk, and Resort fee. Moreover, previous studies utilizing RIPA did not address the differences among factors within the same quadrant, indicating a limitation. To overcome this limitation, our study conducted additional PRCA analysis. As analysis results indicated that there was no significant difference in customer importance and satisfaction regarding staff, trip type, and Resort fees among 3, 4, and 5-star rated hotels. However, differences were observed in the customer importance and satisfaction 

14 

SAGE Open 

levels for the remaining selection attributes among the different hotel star ratings. 

The theoretical implications of this study are as follows: Firstly, this study addressed the limitations of survey methods, which proved challenging, time-consuming, and costly when investigating hotel guests from various countries and diverse accommodations. In order to overcome these challenges, this research collected voluntarily provided data from hotel patrons. Consequently, this approach holds significant merit in exploring the subject matter. 

Secondly, this study conducted RIPA analysis by categorizing hotels based on their star ratings, thus examining the differences in customers’ perceptions of the implicitly derived importance and satisfaction performance related to hotel attributes. Specifically, the observation that only 4-star hotels have the Bathroom attribute falling under the ‘‘Concentrate Here’’ quadrant confirms distinctions in customers’ importance and satisfaction across various star ratings. Furthermore, a review analysis of the Bathroom attribute for 4-star hotels revealed a prevalent dissatisfaction with physical aspects such as bathroom size and equipment damage. Therefore, this underscores the need for detailed consideration of physical factors (size, amenities, facilities) pertaining to bathrooms, and this insight is expected to contribute to future studies on customer satisfaction with hotel attributes. 

Thirdly, in the previous RIPA studies, the limitations persisted in understanding the differences among factors falling within the same quadrant. Addressing this gap, the current study conducted additional PRCA to discern how each hotel attribute influences customers. In essence, PRCA was employed to unveil distinctions among attributes situated in the same quadrant according to the RIPA analysis results. Therefore, this research, attempting to overcome these limitations, stands as a pioneering effort, poised to contribute significantly to numerous subsequent studies in the future. 

The practical significance of this study is as follows. Firstly, in 3-star hotels, guests typically allocate their travel budget more toward tourism-related expenses such as sightseeing, transportation, and dining out, rather than on hotel accommodations (Qu et al., 2000; Xue & Zhang, 2020). Therefore, based on the findings of this study, the hotel selection attribute for front desk staff in 3-star hotels could focus on maintaining current service quality while integrating services that involve providing information about nearby tourist attractions and recommending preferred tourist destinations to guests. 

Secondly, for 4-star hotels, it has become evident that improvements in the bathroom facilities are urgently 

needed. Specifically, customers have expressed dissatisfaction with physical aspects such as the size of the bathroom, damaged fixtures, and the availability of amenities. Swift action is required to address these concerns. Therefore, it is imperative for 4-star hotels to regularly inspect and enhance bathroom facilities, ensuring prompt repairs and replacements to meet guest expectations. 

Thirdly, for 5-star hotels, which consistently offer exceptional services, the research findings affirm an overall higher level of customer satisfaction compared to other hotels. Therefore, it is imperative for these establishments to maintain the existing service quality in areas such as rooms, F&B, and staff. Furthermore, enhancing customer satisfaction specifically in the realm of bathroom facilities would significantly contribute to overall customer satisfaction. To achieve this, the incorporation of sophisticated bathroom designs and the provision of luxury-brand amenities should be considered. 

The limitations of this study and avenues for future research are as follows. Firstly, hotel star ratings, overall satisfaction ratings, and reviews were collected and analyzed. However, hotel e-commerce platforms offer diverse information, including customer profiles and the usefulness of reviews. Therefore, in future studies, collecting and analyzing such additional information could potentially yield more detailed and nuanced results than the present analysis. 

Secondly, this study did not consider the detailed demographic characteristics of hotel visitors, such as age and gender. According to previous research, the analysis of service satisfaction shows variations based on demographic characteristics (Sann et al., 2020). Moreover, as hotels attract customers from diverse cultural backgrounds, it will be necessary to analyze the cultural characteristics and demographic features of customers in the future. 

Thirdly, to mitigate the impact of COVID-19, this study collected and analyzed data from TripAdvisor from January to December 2019. Consequently, owing to the limitations of the collected data, there is a constraint in utilizing data from a more extended timeframe. In the future, collecting additional data and performing analyses categorized by different timeframes or distinguishing between pre-COVID and post-COVID periods could provide a more comprehensive understanding of customer perceptions and satisfaction regarding hotel selection attributes. This approach is expected to offer more detailed insights than that of the current study. 

### ORCID iDs 

Jun Li https://orcid.org/0009-0004-8938-9055 Byunghyun Lee https://orcid.org/0009-0009-5589-5415 

Li et al. 

15 

### Funding 

The author(s) declared no financial support for the research, authorship and/or publication of this article. 

### Declaration of Conflicting Interests 

The author(s) declared no potential conflicts of interest with respect to the research, authorship, and/or publication of this article. 

### Data Availability Statement 

Data sharing not applicable to this article as no datasets were generated or analyzed during the current study. 

### References 

- Ady, M., & Quadri-Felitti, D. (2015). Consumer research identifies how to present travel review content for more bookings. Hotels News Resource, 95. https://www.trustyou.com/ press/study-reveals-travelers-prefer-summarized-review-content-full-text-reviews 

- Albayrak, T., & Caber, M. (2013). The symmetric and asymmetric influences of destination attributes on overall visitor satisfaction. Current Issues in Tourism, 16(2), 149–166. https://doi.org/10.1080/13683500.2012.682978 

- Albayrak, T., Cengizci, A. D., Caber, M., & Nang Fong, L. H. (2021). Big data use in determining competitive position: The case of theme parks in Hong Kong. Journal of Destination Marketing & Management, 22, 100668. https://doi.org/ 10.1016/j.jdmm.2021.100668 

- Aldebert, B., Dang, R. J., & Longhi, C. (2011). Innovation in the tourism industry: The case of Tourism@. Tourism Management, 32(5), 1204–1213. https://doi.org/10.1016/j.tourman.2010.08.010 

- Alzoubi, H. M., Vij, M., Vij, A., & Hanaysha, J. R. (2021). What leads guests to satisfaction and loyalty in UAE fivestar hotels? AHP analysis to service quality dimensions. Enlightening Tourism. A Pathmaking Journal, 11(1), 102–135. https://doi.org/10.33776/et.v11i1.5056 

- Anderson, C. K., & Lawrence, B. (2014). The influence of online reputation and product heterogeneity on service firm financial performance. Service Science, 6(4), 217–228. https://doi.org/10.1287/serv.2014.0080 

- Ao, Y. (2017, June). Five-star hotel reception process optimization on the basis of differentiation [Conference session]. 2017 2nd International Conference on Education, Sports, Arts and Management Engineering (ICESAME 2017) (pp. 304–307). Atlantis Press. https://doi.org/10.2991/icesame-17.2017.68 

- Arenas-Ma´ rquez, F. J., Martinez-Torres, R., & Toral, S. (2021). Convolutional neural encoding of online reviews for the identification of travel group type topics on TripAdvisor. Information Processing & Management, 58(5), 102645. https://doi.org/10.1016/j.ipm.2021.102645 

- Ban, H. J., Choi, H., Choi, E. K., Lee, S., & Kim, H. S. (2019). Investigating key attributes in experience and satisfaction of hotel customer using online review data. Sustainability, 11(23), 6570. https://doi.org/10.3390/su11236570 

- Bi, J. W., Liu, Y., Fan, Z. P., & Zhang, J. (2019). Wisdom of crowds: Conducting importance-performance analysis (IPA) through online reviews. Tourism Management, 70, 460–478. https://doi.org/10.1016/j.tourman.2018.09.010 

- Blei, D. M. (2012). Probabilistic topic models. Communications of the ACM, 55(4), 77–84. https://doi.org/10.1145/2133806. 2133826 

- Bouma, G. (2009). Normalized (pointwise) mutual information in collocation extraction. Proceedings of GSCL, 30, 31–40. 

- Brandt, R. D. (1987). A procedure for identifying valueenhancing service components using customer satisfaction survey data. Add Value to Your Service, 6(1), 61–65. 

- Buschken,€ J., & Allenby, G. M. (2016). Sentence-based text analysis for customer reviews. Marketing Science, 35(6), 953–975. https://doi.org/10.1287/mksc.2016.0993 

- Caber, M., Albayrak, T., & Matzler, K. (2012). Classification of the destination attributes in the content of competitiveness (by revised importance-performance analysis). Journal of Vacation Marketing, 18(1), 43–56. https://doi.org/10. 1177/1356766711428802 

- Cvelbar, L. K., & Dwyer, L. (2013). An importance– performance analysis of sustainability factors for long-term strategy planning in Slovenian hotels. Journal of Sustainable Tourism, 21(3), 487–504. https://doi.org/10.1080/09669582. 2012.713965 

- Davras, O<sup>¨</sup> ., & Caber, M. (2019). Analysis of hotel services by their symmetric and asymmetric effects on overall customer satisfaction: A comparison of market segments. International Journal of Hospitality Management, 81, 83–93. https://doi. org/10.1016/j.ijhm.2019.03.003 

- de Groot, M., Aliannejadi, M., & Haas, M. R. (2022). Experiments on generalizability of BERTopic on multi-domain short text. arXiv preprint arXiv:2212.08459. https://doi.org/ 10.48550/arXiv.2212.08459 

- Deng, W. (2007). Using a revised importance–performance analysis approach: The case of Taiwanese hot springs tourism. Tourism Management, 28(5), 1274–1284. https://doi. org/10.1016/j.tourman.2006.07.010 

- Deng, W. J., Kuo, Y. F., & Chen, W. C. (2008). Revised importance–performance analysis: Three-factor theory and benchmarking. Service Industries Journal, 28(1), 37–51. https://doi.org/10.1080/02642060701725412 

- Ding, K., Choo, W. C., Ng, K. Y., & Ng, S. I. (2020). Employing structural topic modelling to explore perceived service quality attributes in Airbnb accommodation. International Journal of Hospitality Management, 91, 102676. https://doi. org/10.1016/j.ijhm.2020.102676 

- Egger, R., & Yu, J. (2022). A topic modeling comparison between LDA, NMF, Top2Vec, and BERTopic to demystify Twitter posts. Frontiers in Sociology, 7, 886498. https:// doi.org/10.3389/fsoc.2022.886498 

- Fuller,€ J., & Matzler, K. (2008). Customer delight and market segmentation: An application of the three-factor theory of customer satisfaction on life style groups. Tourism Management, 29(1), 116–126. https://doi.org/10.1016/j.tourman.2007.03.021 

- Gao, B., Ding, X., Chen, W., Jiang, X., & Wu, J. (2020). When online reviews meet ACSI: how ACSI moderates the effects of online reviews on hotel revenue. Journal of Travel & 

16 

SAGE Open 

Tourism Marketing, 37(3), 396–408. https://doi.org/10.1080/ 10548408.2020.1767261 

- Grootendorst, M. (2022). BERTopic: Neural topic modeling with a class-based TF-IDF procedure. arXiv preprint arXiv:2203.05794. https://doi.org/10.48550/arXiv.2203.05794 

- Gupta, V., & Dixit, S. K. (2022). Influence of branded luxury guestroom amenities on guests’ hotel buying decisions: A case of five-star hotels in Delhi. In A. S. Kotur & S. K. Dixit (Eds.), The Emerald handbook of luxury management for hospitality and tourism (pp. 305–319). Emerald Publishing Limited. 

- Huang, S. (2010). A revised importance–performance analysis of tour guide performance in China. Tourism Analysis, 15(2), 227–241. https://doi.org/10.3727/108354210X1272486 3327803 

- Huang, S., Weiler, B., & Assaker, G. (2015). Effects of interpretive guiding outcomes on tourist satisfaction and behavioral intention. Journal of Travel Research, 54(3), 344–358. https://doi.org/10.1177/0047287513517426 

- Huang, W. J., Chen, C. C., & Lai, Y. M. (2018). Five-star quality at three-star prices? Opaque booking and hotel service expectations. Journal of Hospitality Marketing & Management, 27(7), 833–854. https://doi.org/10.1080/19368623. 2018.1448315 

- Hutto, C., & Gilbert, E. (2014). Vader: A parsimonious rulebased model for sentiment analysis of social media text. Proceedings of the International AAAI Conference on Web and Social Media, 8(1), 216–225. https://doi.org/10.1609/icwsm. v8i1.14550 

- Jelodar, H., Wang, Y., Yuan, C., Feng, X., Jiang, X., Li, Y., & Zhao, L. (2019). Latent Dirichlet allocation (LDA) and topic modeling: Models, applications, a survey. Multimedia Tools and Applications, 78, 15169–15211. https://doi.org/10. 1007/s11042-018-6894-4 

- Jeong, M., & Kubickova, M. (2021). Do the brand and packaging matter? The case of hotel bathroom amenities. Journal of Hospitality and Tourism Insights, 4(5), 565–581. https:// doi.org/10.1108/JHTI-03-2020-0030 

- Joung, J., & Kim, H. M. (2021). Approach for importance– performance analysis of product attributes from online reviews. Journal of Mechanical Design, 143(8), 081705. https://doi.org/10.1115/1.4049865 

- Kano, N. (1984). Attractive quality and must-be quality. Journal of the Japanese society for quality control, 31(4), 147–156. 

- Kim, W. G., & Park, S. A. (2017). Social media review rating versus traditional customer satisfaction: Which one has more incremental predictive power in explaining hotel performance? International Journal of Contemporary Hospitality Management, 29(2), 784–802. https://doi.org/10.1108/ IJCHM-11-2015-0627 

- Ku, G. C., & Shang, I. W. (2020). Using the integrated kano– RIPA model to explore teaching quality of physical education programs in Taiwan. International Journal of Environmental Research and Public Health, 17(11), 3954. https://doi. org/10.3390/ijerph17113954 

- Ku, G. C. M., & Mak, A. H. N. (2017). Exploring the discrepancies in perceived destination images from residents’ and tourists’ perspectives: A revised importance–performance analysis approach. Asia Pacific Journal of Tourism Research, 

22(11), 1124–1138. https://doi.org/10.1080/10941665.2017. 1374294 

- Law, R., Leung, D., & Chan, I. C. C. (2020). Progression and development of information and communication technology research in hospitality and tourism: A state-of-the-art review. International Journal of Contemporary Hospitality Management, 32(2), 511–534. https://doi.org/10.1108/ IJCHM-07-2018-0586 

- Liu, Y. D. (2010). A revised importance–performance analysis for assessing image: The case of cultural tourism in Britain. Tourism Analysis, 15(6), 673–687. https://doi.org/10.3727/ 108354210X12904412049893 

- Martilla, J. A., & James, J. C. (1977). Importance-performance analysis. Journal of Marketing, 41(1), 77–79. https://doi.org/ 10.1177/002224297704100112 

- Martin-Fuentes, E. (2016). Are guests of the same opinion as the hotel star-rate classification system? Journal of Hospitality and Tourism Management, 29, 126–134. https://doi.org/ 10.1016/j.jhtm.2016.06.006 

- Matzler, K., Bailom, F., Hinterhuber, H. H., Renzl, B., & Pichler, J. (2004). The asymmetric relationship between attribute-level performance and overall customer satisfaction: A reconsideration of the importance–performance analysis. Industrial Marketing Management, 33(4), 271–277. https://doi.org/10.1016/S0019-8501(03)00055-5 

- Matzler, K., & Sauerwein, E. (2002). The factor structure of customer satisfaction: An empirical test of the importance grid and the penalty-reward-contrast analysis. International Journal of Service Industry Management, 13(4), 314–332. https://doi.org/10.1108/09564230210445078 

- Meaney, C., Escobar, M., Stukel, T. A., Austin, P. C., & Jaakkimainen, L. (2022). Comparison of methods for estimating temporal topic models from primary care clinical text data: Retrospective closed cohort study. JMIR Medical Informatics, 10(12), e40102. https://doi.org/10.2196/40102 

- Mohsin, A., Rodrigues, H., & Brochado, A. (2019). Shine bright like a star: Hotel performance and guests’ expectations based on star ratings. International Journal of Hospitality Management, 83, 103–114. https://doi.org/10.1016/j. ijhm.2019.04.012 

- Navı´o-Marco, J., Ruiz-Go´ mez, L. M., & Sevilla-Sevilla, C. (2018). Progress in information technology and tourism management: 30 years on and 20 years after the internetRevisiting Buhalis & Law’s landmark study about eTourism. Tourism Management, 69, 460–470. https://doi.org/10. 1016/j.tourman.2018.06.002 

- Qu, H., Ryan, B., & Chu, R. (2000). The importance of hotel attributes in contributing to travelers’ satisfaction in the Hong Kong hotel industry. Journal of Quality Assurance in Hospitality & Tourism, 1(3), 65–83. https://doi.org/10.1300/ J162v01n03_04 

- Rhee, H. T., & Yang, S. B. (2015). Does hotel attribute importance differ by hotel? Focusing on hotel star-classifications and customers’ overall ratings. Computers in Human Behavior, 50, 576–587. https://doi.org/10.1016/j.chb.2015.02.069 

- Sann, R., Lai, P. C., & Liaw, S. Y. (2020). Online complaining behavior: Does cultural background and hotel class matter? Journal of Hospitality and Tourism Management, 43, 80–90. https://doi.org/10.1016/j.jhtm.2020.02.004 

Li et al. 

17 

- Shang, Z., Luo, J. M., & Kong, A. (2022). Topic modelling for S ki resorts: An analysis of experience attributes and seasonality. Sustainability, 14(6), 3533. https://doi.org/10.3390/ su14063533 

- Soifer, I., Choi, E. K., & Lee, E. (2021). Do hotel attributes and amenities affect online user ratings differently across hotel star ratings? Journal of Quality Assurance in Hospitality & Tourism, 22(5), 539–560. https://doi.org/10.1080/1528008X. 2020.1814935 

- Srivastava, A., & Kumar, V. (2021). Hotel attributes and overall customer satisfaction: What did COVID-19 change? Tourism Management Perspectives, 40, 100867. https://doi. org/10.1016/j.tmp.2021.100867 

- TripAdvisor. (2019, May 25). TripAdvisor, Inc. Earnings press release available on company’s investor relations site. http:// ir.tripadvisor.com/news-releases/news-release-details/tripadvisor-inc-earnings-press-release-available-companys-28 

- Wilkins, H. (2010). Using importance-performance analysis to appreciate satisfaction in hotels. Journal of Hospitality Marketing & Management, 19(8), 866–888. https://doi.org/10. 1080/19368623.2010.514554 

- Xiang, Z., Du, Q., Ma, Y., & Fan, W. (2018). Assessing reliability of social media data: Lessons from mining TripAdvisor hotel reviews. Information Technology & Tourism, 18, 43–59. https://doi.org/10.1007/s40558-017-0098-z 

- Xue, L., & Zhang, Y. (2020). The effect of distance on tourist behavior: A study based on social media data. Annals of 

   - Tourism Research, 82, 102916. https://doi.org/10.1016/j. annals.2020.102916 

- Xu, X., & Li, Y. (2016). The antecedents of customer satisfaction and dissatisfaction toward various types of hotels: A text mining approach. International Journal of Hospitality Management, 55, 57–69. https://doi.org/10.1016/j.ijhm.2016.03.003 

- Yang, H., Song, H., Cheung, C., & Guan, J. (2021). How to enhance hotel guests’ acceptance and experience of smart hotel technology: An examination of visiting intentions. International Journal of Hospitality Management, 97, 103000. https://doi.org/10.1016/j.ijhm.2021.103000 

- Ying, T., Wen, J., & Wang, L. (2018). Language facilitation for outbound Chinese tourists: Importance–performance and gap analyses of New Zealand hotels. Journal of Travel & Tourism Marketing, 35(9), 1222–1233. https://doi.org/10. 1080/10548408.2018.1487902 

- Zhang, C., Xu, Z., Gou, X., & Chen, S. (2021). An online reviews-driven method for the prioritization of improvements in hotel services. Tourism Management, 87, 104382. https://doi.org/10.1016/j.tourman.2021.104382 

- Zhang, J., & Piramuthu, S. (2018). Product recommendation with latent review topics. Information Systems Frontiers, 20, 617–625. https://doi.org/10.1007/s10796-016-9697-z 

- Zhang, W. T., Choi, I. Y., Hyun, Y. J., & Kim, J. K. (2022). Hotel service analysis by penalty-reward contrast technique for online review data. Sustainability, 14(12), 7340. https:// doi.org/10.3390/su14127340 

