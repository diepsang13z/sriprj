

## ARTICLE 



> https://doi.org/10.1057/s41599-024-04226-4 **OPEN** 

# Unveiling the spatial and temporal variation of customer sentiment in hotel experiences: a case study of Beppu City, Japan 

Feiyu Hu 1, Jun Pan2✉ & Haijun Wang3 

This study examined the fluctuation of customer sentiment regarding hotel experiences in Beppu City, Japan, as reflected in TripAdvisor reviews. A total of 4004 reviews in English and Japanese, contributed by both international and domestic customers, were collected from 233 hotels in Beppu between April 1st, 2015, and March 31st, 2023, for sentiment analysis. The Google Cloud Natural Language Processing API was utilized for sentiment extraction. This study employed spatio-temporal analysis to investigate the variation of sentiment over time and across different areas, as well as to explore differences in sentiment between international and domestic customers. The research results underscore a notable regional disparity in hotel satisfaction, particularly in the Kitahama and Cyuou Area of Beppu, following the COVID-19 pandemic. 

> 1 College of Sustainability and Tourism, Ritsumeikan Asia Pacific University, Beppu, Japan. 2 Department of Big Data Science, School of Science, Zhejiang University of Science and Technology, Hangzhou, China.<sup>3</sup> School of Electronic and Information Engineering (School of Big Data Science), Taizhou University, Taizhou, China.<sup>✉</sup> email: panjun@zust.edu.cn 

1 

HUMANITIES AND SOCIAL SCIENCES COMMUNICATIONS | (2024) 11:1695 | https://doi.org/10.1057/s41599-024-04226-4 

<u>ARTICLE</u> 

HUMANITIES AND SOCIAL SCIENCES COMMUNICATIONS <u>|</u> https://doi.org/10.1057/s41599-024-04226-4 

### Introduction 

lobal tourism trends significantly impact local economies through various channels. One of the most immediate and Gnoticeable benefitsfitsts is the direct revenue generated from 

noticeable benefitsfitsts is the direct revenue generated from tourism activities (Calero & Turner, 2020; Li et al., 2018). Tourist expenditures on accommodation, dining, and transportation inject substantial financial resources into the local economic landscape, stimulating commercial activities and directly contributing to economic growth. This heightened demand benefits hotels, restaurants, and local attractions, thereby fostering economic vitality in tourist destinations. 

Concurrently, the tourism industry has undergone a significant digital transformation, ushering in an era of enhanced operational efficiency and expanded market reach (Alrawadieh et al., 2021; Cuomo et al., 2021; Pencarelli, 2020). The integration of digital technologies such as online booking platforms, mobile applications, and digital payment systems has streamlined processes and improved the overall customer experience. Tourists now enjoy real-time information and seamless booking experiences, potentially increasing tourist arrivals and spending. Additionally, the emergence of social media has significantly impacted customer decision-making in the digital world. In the tourism sector, in particular, online platforms such as TripAdvisor have become indispensable repositories of hotel-related information contributed by fellow travelers and customers. Customer reviews are a crucial and influential source of information for travelers, playing a significant role in their hotel selection process (Chang et al., 2023; Lo & Yao, 2019). 

Building on the importance of digital platforms, customer reviews have become essential to the hospitality and tourism industry due to their accessibility, rapid generation, simplicity of collection, and non-intrusiveness with human subjects (Lu & Stepchenkova, 2015). These reviews impact decision-making (Varkaris & Neuhofer, 2017), trust-building (Martínez-Navalón et al., 2021), quality improvement (Ananthakrishnan et al., 2023), and customer engagement (So et al., 2021). A comprehensive understanding of the importance of reviews and their impact can help companies and researchers utilize this valuable resource to improve customer experience and drive industry progress. 

Given the vast volume of review data, manually reading and analyzing each review is impractical and time-consuming. This challenge has led to the application of Natural Language Processing (NLP) for text mining due to its ability to extract meaningful information and provide valuable insights from a large volume of text data about products and services (Hirschberg & Manning, 2015). In the field of NLP, there are two primary areas of interest: sentiment analysis and emotion recognition (Nandwani & Verma, 2021). Although these terms are sometimes used interchangeably, they have distinct differences. Sentiment analysis focuses on evaluating whether data exhibits a positive, negative, or neutral sentiment. In contrast, emotion recognition aims to identify and categorize specific emotional states experienced by humans, such as anger, happiness, or sadness (Nandwani & Verma, 2021). 

In the context of hotel reviews, sentiment analysis proves to be a more appropriate approach for evaluating customer satisfaction compared to emotion analysis, which focuses on individual emotional states like happiness or anger. The primary objective of sentiment analysis is to determine whether the sentiment conveyed in the text is positive, negative, or neutral, which is of great importance when evaluating hotel reviews. Sentiment analysis provides a quick understanding of the customer’s overall opinion or attitude towards a particular hotel. Several studies have applied sentiment analysis to hotel reviews (García-Pablos et al., 2016; Luo et al., 2021; Ray et al., 2021). For example, in the analysis of hotel reviews on TripAdvisor, Kuhzady and Ghasemi discovered that 

travelers assessed hotels based on their opinions regarding factors such as location, room quality, staff, and restaurant. These factors were found to play a crucial role in determining overall satisfaction or dissatisfaction with the experience (Kuhzady & Ghasemi, 2019). Additionally, advancements in sentiment analysis encompass aspect-based sentiment analysis (ABSA), which concentrates on identifying sentiments linked to specific attributes of a product or service (Pontiki et al., 2016). This method is particularly relevant for hotel reviews, where customers commonly assess aspects like location, room quality, staff, and dining options, thus offering more nuanced insights into customer satisfaction. Moreno-Ortiz et al. further developed techniques for sentiment analysis within the tourism industry (Moreno-Ortiz et al., 2019). 

According to the findings from a comprehensive review of sentiment studies in the field of tourism, it was asserted that sentiment analysis has the potential to emerge as a pivotal method in tourism research (Alaei et al., 2019). Although the majority of sentiment analysis research in tourism has primarily centered around the domain of hotel accommodations (Ma et al., 2018; Schuckert et al., 2015b), only a limited number of studies have focused on analyzing hotel reviews in multiple languages. Most of these studies primarily concentrate on English as the predominant language in the travel domain (Gharzouli et al., 2022). 

While sentiment analysis and NLP approaches have significantly advanced our understanding of tourist behavior and satisfaction, recent global events have introduced new complexities to the tourism landscape. Most notably, the COVID-19 pandemic has profoundly altered the trajectory of global tourism, leading to a significant decline in tourist numbers and posing unprecedented challenges to tourist destinations worldwide (Butler, 2022; Lee & Chen, 2022; Palazzo et al., 2022; Vaishar & Šťastná, 2022). Studies have investigated the pandemic’s effects on customer satisfaction in various regions, including North America, Europe, and several Asian countries (Mehta et al., 2023; Nilashi et al., 2021; Song et al., 2022). These studies highlight the variations in customer satisfaction influenced by the pandemic, yet there is a notable gap in understanding these variations in the context of Japan, particularly in renowned resort cities like Beppu. The global nature of this crisis necessitates a comprehensive, region-specific analysis to better understand its impacts on tourism satisfaction. 

To illustrate these broader trends in a specific regional context, this study examines Beppu City, a distinctive case in Japan’s tourism landscape. Located in Oita Prefecture in the Kyushu Region, Beppu has emerged as a popular tourist destination due to its world’s second-largest geothermal spring water resources (Fujii et al., 2017) and traditional hot spring (also known as “onsen”) culture. The city has a long history of hot spring culture and has developed a unique reputation as a tourism destination (Tsukamoto, 2016). In the pre-COVID-19 period of 2019, Beppu received a total of 8,335,773 visitors, including 620,841 international tourists. However, the number of tourists experienced a significant decline in subsequent years, with 4,427,103 visitors (including 67,197 international tourists) in 2020 and 3,722,365 visitors (2131 international tourists) in 2021 (Beppu City, 2023). 

Moreover, the significance of hotel location in relation to hotel satisfaction has been highlighted in several studies (Alvarez Leon et al., 2021; Latinopoulos, 2020; Mellinas et al., 2019; Yang et al., 2018). However, most of these studies have analyzed hotel satisfaction and location under the assumption that the association between them remains constant over time, without considering the potential impact of temporal dynamics. In other words, the variation in satisfaction in the interaction between time and space has not been revealed. This presents an opportunity to explore how the relationship between hotel location and 

2 

HUMANITIES AND SOCIAL SCIENCES COMMUNICATIONS | (2024) 11:1695 | https://doi.org/10.1057/s41599-024-04226-4 

<u>ARTICLE</u> 

HUMANITIES AND SOCIAL SCIENCES COMMUNICATIONS <u>|</u> https://doi.org/10.1057/s41599-024-04226-4 

### Table 1 Summary of relevant literature. 

|Research variable/concept|Title of key relevant papers|Authors|Year|
|---|---|---|---|
|Global tourism trends &<br>impact on local economies|Regional economic development and tourism: A literature<br>review to highlight future directions for regional tourism<br>research|Calero C, Turner LW|2020|
||Tourism as an important impetus to promoting economic<br>growth: A critical review|Li KX, Jin M, Shi W|2018|
|Digital transformation|Digital transformation and revenue management: Evidence<br>from the hotel industry|Alrawadieh Z, Alrawadieh Z, Cetin G|2021|
||Digital transformation and tourist experience co-design:<br>Big social data for planning cultural tourism|Cuomo MT, Tortora D, Foroudi P, Giordano A,<br>Festa G, Metallo G|2021|
||The digital revolution in the travel and tourism industry|Pencarelli T|2020|
|Social media|An improved model for sentiment analysis on luxury hotel<br>review|Chang V, Liu L, Xu Q, Li T, Hsu C|2023|
||What makes hotel online reviews credible? An<br>investigation of the roles of reviewer expertise, review<br>|Lo AS, Yao SS|2019|
||rating consistency, and review valence|||
|Customer reviews|The influence of social media on the consumers’ hotel<br>decision journey|Varkaris E, Neuhofer B|2017|
||Evaluation of User Satisfaction and Trust of Review<br>Platforms: Analysis of the Impact of Privacy and E-WOM in<br>the Case of TripAdvisor|Martínez-Navalón J-G, Gelashvili V, Gómez-<br>Ortega A|2021|
||I Hear You: Does Quality Improve with Customer Voice?<br>Understanding customer engagement and social media<br>activities in tourism: A latent profile analysis and cross-<br>validation|Ananthakrishnan U, Proserpio D, Sharma S<br>So KKF, Wei W, Martin D|2023<br>2021|
|Sentiment analysis|A review on sentiment analysis and emotion detection<br>from text|Nandwani P, Verma R|2021|
||Understanding service attributes of robot hotels: A<br>sentiment analysis of customer online reviews|Luo JM, Vu HQ, Li G, Law R|2021|
||An ensemble-based hotel recommender system using<br>sentiment analysis and aspect categorization of hotel<br>reviews|Ray B, Garain A, Sarkar R|2021|
||Design and validation of annotation schemas for aspect-<br>based sentiment analysis in the tourism sector|Moreno-Ortiz A, Salles-Bernal S, Orrequia-Barea<br>A|2019|
||Sentiment Analysis in Tourism: Capitalizing on Big Data|Alaei AR, Becken S, Stantic B|2019|
|Impact of pandemics|COVID-19 and its potential impact on stages of tourist<br>Destination Development|Butler R|2022|
||The impact of COVID-19 on the travel and leisure industry<br>returns: Some international evidence|Lee C-C, Chen M-P|2022|
||Customer expectations in the hotel industry during the<br>COVID-19 pandemic: a global perspective using sentiment<br>analysis.|Mehta MP, Kumar G, Ramkumar M|2023|
||What is the impact of service quality on customers’<br>satisfaction during COVID-19 outbreak? Newfindings from<br>online reviews analysis|Nilashi M, Abumalloh RA, Alghamdi A, Minaei-<br>Bidgoli B, Alsulami AA, Thanoon M, Asadi S,<br>Samad S|2021|
||Does hotel customer satisfaction change during the|Song Y, Liu K, Guo L, Yang Z, Jin M|2022|
||COVID-19? A perspective from online reviews|||



customer satisfaction may evolve over time, particularly in the context of major disruptions like the COVID-19 pandemic. 

This study addresses existing research gaps by analyzing customer satisfaction with hotels through sentiment analysis of reviews written in English and Japanese. Specifically, it examines the spatiotemporal variation of customer satisfaction with city hotel experiences in Beppu City, focusing on changes over time and across different areas. The study pays particular attention to the impact of the COVID-19 pandemic on customer reviews and satisfaction. 

To summarize the key literature and highlight the relevant studies, we present Table 1 below: 

### Methods 

Data sources. TripAdvisor, the world’s largest travel guidance platform, hosts over 1 billion reviews and opinions covering nearly 8 million businesses (TripAdvisor.com, 2022). Widely 

trusted by travelers (Martínez-Navalón et al., 2021), TripAdvisor serves as a crucial resource for global tourists seeking recommendations for accommodations and activities based on the insights and experiences of previous visitors. Numerous studies have utilized TripAdvisor’s online reviews as rich data sources for tourism research (Alaei et al., 2019; Calero-Sanz et al., 2022; Garner & Kim, 2022; Gharzouli et al., 2022; Mellinas et al., 2019). 

Given the platform’s comprehensive coverage and reliability as a data source, this study employed a Python-based web crawler to collect online hotel reviews specific to Beppu City from TripAdvisor. In addition to review content, the study gathered supplementary information including hotel addresses, review titles, review dates (year-month), and overall ratings. TripAdvisor employs a 1–5 star rating scale, with additional dimensions that can be assessed separately without influencing the final score (Rita et al., 2022). The rating classification used to differentiate between positive, neutral, and negative reviews followed these 

3 

HUMANITIES AND SOCIAL SCIENCES COMMUNICATIONS | (2024) 11:1695 | https://doi.org/10.1057/s41599-024-04226-4 

<u>ARTICLE</u> 

HUMANITIES AND SOCIAL SCIENCES COMMUNICATIONS <u>|</u> https://doi.org/10.1057/s41599-024-04226-4 

criteria: 1–2 stars were categorized as negative, 3 stars as neutral, and 4–5 stars as positive. 

Segmentation of international and domestic tourists. To address potential cultural biases and enhance the accuracy of sentiment analysis, we segmented the reviews based on their language. Reviews written in English were primarily assumed to be from international tourists. This assumption is grounded in the widespread use of English as a global language and the likelihood that international travelers would use English when posting reviews on an international platform like TripAdvisor. Conversely, reviews written in Japanese were assumed to be from domestic tourists, reflecting the predominant use of Japanese by locals and the cultural context in which domestic travelers would likely write reviews in their native language. This segmentation enabled separate analysis of the two groups, allowing for the identification of sentiment and satisfaction differences between international and domestic customers. By examining these groups independently, we aimed to uncover significant variations in satisfaction levels and sentiment expression that could be attributed to cultural differences. For example, a previous study in Hong Kong found that non-English-speaking guests were more exacting about five-star hotels and service quality, while Englishspeaking guests preferred larger rooms in four-star hotels (Schuckert et al., 2015a). 

Sentiment analysis. Understanding the linguistic nuances is crucial for accurate sentiment analysis. English and Japanese are two distinct languages with notable differences. English uses a single alphabet for uniform spelling, while Japanese employs three writing systems: kanji, hiragana, and katakana. Translating reviews between these languages may result in the loss of significant details. To effectively preserve sentiments in reviews for both languages, it is advisable to analyze the reviews in their original language using the same methodology or software technology (Nakayama & Wan, 2019). 

The Google Cloud Natural Language (NL) API possesses this capability for sentiment analysis. It utilizes a cutting-edge model known as the Large Language Model (LLM), which is distinguished by its vast scale and training on extensive datasets (Hawker & Koukoumidis, 2023). Google Cloud NL API’s robust pre-trained models enable developers to easily incorporate natural language understanding into their applications. These models offer a variety of features, including sentiment analysis (Geewax, 2018; Google, 2023c), and can be applied to analyze content in multiple languages, such as English and Japanese (Geewax, 2018; Google, 2023b). Google Cloud NL API has been employed for sentiment analysis in numerous studies (Garvey & Maskal, 2020; Pham et al., 2020; Tamrakar et al., 2022; Venkit & Wilson, 2021). In a comparative evaluation of sentiment analysis and star ratings for consumer reviews, Google was found to be the most resilient tool, consistently outperforming star ratings and other sentiment analysis tools, with its performance remaining unaffected by contextual factors (Al-Natour & Turetken, 2020). Consequently, we adopted Google Cloud NL API for sentiment textual analyses of customer hotel reviews. 

According to Google’s NL API, sentiment evaluation involves two numerical parameters: “score” and “magnitude”, which are applied to both the entire text and individual sentences (Geewax, 2018; Google, 2023a). The “score”, ranging from −1 to 1, represents the text’s sentiment: scores between 0 and 1 indicate positive sentiment, while scores between −1 and 0 suggest negative sentiment. Scores close to zero signify a neutral sentiment. To measure the overall emotional intensity, Google’s NLP utilizes the “magnitude” parameter, which reflects the 

cumulative emotional expression within the text. Magnitude is an absolute value ranging from 0 to positive infinity and is typically proportional to the length of the text. It enables the differentiation between documents containing mixed (positive and negative) sentiments and those expressing genuinely neutral opinions. 

A preliminary sensitivity analysis was conducted to determine the optimal score thresholds for classifying reviews as positive, neutral, or negative. The results showed no significant difference across various threshold selections. Consequently, this study categorized reviews as follows: scores between 0.1 and 1 were considered positive, scores between −1 and −0.2 were deemed negative, and scores within the range of [−0.2, 0.1] were classified as neutral. It should be noted that neutral scores with higher magnitudes may indicate mixed sentiments with some emotional intensity while remaining predominantly neutral. 

Spatial distribution. According to the Tourism Statistics Annual Survey in Beppu (Beppu City, 2023), annual hotel occupancy statistics are calculated across four distinct areas: Kannawa and Myouban Area, Horita and Kankaiji Area, Kitahama and Cyuou Area, and Other Area. Beppu City is renowned for its hot spring resorts, locally referred to as “ryokan” or “onsen hotels”. These traditional hotels are strategically located near major attractions and hot spring areas, particularly in the Kannawa and Myouban Area, and Horita and Kankaiji Area. They offer guests a unique hot spring cultural experience, providing access to authentic Japanese hospitality and multi-course traditional meals. Alongside these traditional hot spring resorts, the Kitahama and Cyuou Area in downtown hosts modern and Western-style hotels that cater to customers seeking international standards of comfort or traveling for business. Given the distinctive geographical distribution of hotels in Beppu, this study divided the city into four areas for spatial analysis (Fig. 1). 

Temporal analysis. Interrupted Time Series (ITS) analysis is a valuable method for examining the long-term effects of an intervention by assessing changes before and after the intervention at a specific and well-defined time point (McDowall et al., 2019). It is widely utilized for investigating the impact of interventions and measuring their longitudinal effects (Hu et al., 2020; Leske et al., 2021; O’Donnell et al., 2019). 

ITS analysis can be effectively applied to gauge the temporal variations in customer reviews. This approach is especially pertinent in the context of the COVID-19 pandemic and the first nationwide state of emergency in Japan, which presents a readily observable event with a distinct time point on April 7th, 2020 (Prime Minister’s Office of Japan, 2023). The state of emergency led to a significant decrease in inbound tourism due to travel restrictions, quarantine measures, and general uncertainty. Moreover, domestic travel was also impacted, as people were less likely to travel within Japan, leading to cancellations of domestic trips, hotel bookings, and tourism-related activities. Popular tourist destinations experienced a substantial decrease in visitors, and the tourism sector faced significant bankruptcy and unemployment (Kyan & Takakura, 2022). We employed segmented regression analysis with an ITS design to assess the impact of the intervention (Japan’s first nationwide state of emergency) on hotel satisfaction in Beppu City. As historical customer reviews on TripAdvisor only provide year-month information, the specific review dates were unavailable. Consequently, for this study, all reviews generated in April 2020 and onwards were categorized as part of the postintervention period, while reviews submitted before April 2020 were considered part of the pre-intervention period. A preliminary analysis was conducted to determine the volume 

4 

HUMANITIES AND SOCIAL SCIENCES COMMUNICATIONS | (2024) 11:1695 | https://doi.org/10.1057/s41599-024-04226-4 

<u>ARTICLE</u> 

HUMANITIES AND SOCIAL SCIENCES COMMUNICATIONS <u>|</u> https://doi.org/10.1057/s41599-024-04226-4 

of customer reviews, and it was observed that some hotels had no reviews within 3 months after April 2020. Therefore, hotel satisfaction was assessed in 6-month intervals, computed as the percentage of positive reviews divided by the total number of reviews. Figure 2 depicts the time periods selected for the ITS 



Fig. 1 Hotel distribution in four areas in Beppu. This figure shows hotels’ locations in the four areas (Kitahama and Cyuou Area, Kannawa and Myouban Area, Horita and Kankaiji Area, and Other Area) of Beppu City. 

analysis, covering the timeframe from April 1st, 2015, to March 31st, 2023. 

The model is 



Here, Y t: customer satisfaction rate at time t, calculated by dividing the number of positive responses by the total number of responses; time: 6-month intervals at time t, ranging from 1 to 16; intervention: an indicator that takes the value 0 before the intervention and 1 after the intervention; time after intervention: 0 before the intervention and ranges from 1 to 6 after the intervention, representing different post-intervention time periods; e: error. 

In this model (1), β1 estimates the baseline trend of the outcome, while β2 and β3 estimate the level and trend changes attributable to the intervention. The term “level” refers to the impact of the intervention on hotel satisfaction, and “trend” indicates the subsequent rate of change in satisfaction resulting from the intervention. 

Figure 3 illustrates the key steps in the methodology, including data collection, review segmentation, sentiment analysis, spatial distribution, and temporal analysis. Each step is briefly explained, with relevant references provided to support the methodological choices. 

### Results 

During the study period from April 1st, 2015, to March 31st, 2023, a total of 4518 textual reviews of 233 hotels in Beppu were collected from TripAdvisor as of June 24th, 2023. Since the majority of these hotels received fewer than 10 reviews in either English or Japanese (156 hotels accounted for only 514 reviews or 11.4% of the total), the analysis focused on 77 hotels that had at least 10 reviews in either English or Japanese. This subset comprised a total of 4004 reviews (88.6% of the 4518 reviews), consisting of 759 reviews submitted in English and 3245 reviews written in Japanese. 

Sentiment analysis and hotel overall ratings. To assess the alignment between customer sentiments in reviews and their corresponding overall ratings, sentiment analysis was conducted. Table 2 presents the results of sentiment analysis for both English 



Fig. 2 Relevant time periods for ITS analysis. This figure clarifies the data range used in the analysis and illustrates the chosen timeframes for the ITS analysis, spanning from April 1, 2015, to March 31, 2023. The chosen timeframes allow for an ITS analysis of the impact of the intervention (implemented in April 2020) on reviews. 



Fig. 3 Step-by-step methodology for sentiment analysis. This figure offers a view of each step in the analysis, with each step accompanied by a brief explanation and relevant references. 

5 

HUMANITIES AND SOCIAL SCIENCES COMMUNICATIONS | (2024) 11:1695 | https://doi.org/10.1057/s41599-024-04226-4 

<u>ARTICLE</u> 

HUMANITIES AND SOCIAL SCIENCES COMMUNICATIONS <u>|</u> https://doi.org/10.1057/s41599-024-04226-4 

and Japanese reviews. Out of 759 reviews, 643 (84.7%) reflected positive experiences with the hotels, while 7.9% conveyed negative responses. Additionally, 11.3% of the reviews exhibited inconsistent sentiments when compared to the overall ratings. Nevertheless, the sentiment analysis results closely corresponded to the hotels’ overall ratings, with 81.9% of the sentiments being positive and 5.4% being negative. Reviews in Japanese indicated notably higher positive responses (87.1%) and slightly higher negative responses (8.8%) compared to the overall rating percentages of 75.9% and 8.3%, respectively. Moreover, among the 3,245 reviews in Japanese, 18.7% expressed sentiments that varied from their corresponding overall ratings. Overall, out of all 4,004 reviews analyzed, 3,310 reviews (82.7%) exhibited consistent sentiment responses with the final overall ratings. Notably, approximately half of the customers provided higher ratings than their expressed sentiments in the English reviews. Conversely, for reviews in Japanese, 62.7% of customers rated the hotels lower than the sentiments conveyed in their reviews. 

Hotel satisfaction changes over time and space. Out of the 4004 reviews examined, 694 reviews displayed inconsistent sentiment responses compared to their overall ratings. To ensure a reliable measure of hotel satisfaction, the remaining 3310 reviews, which aligned with their final overall ratings in terms of sentiment, were used to evaluate the hotel satisfaction experience. Details regarding the number of reviews and hotels are presented in 

Table 2 Results of sentiment analysis and hotel overall ratings. 

|||Hotel over|all rating|s||
|---|---|---|---|---|---|
|||Negative|Neutral|Positive|Total|
|Reviews in English||||||
|Sentiment analysis|Negative|40|20|0|60|
||Neutral|1|33|22|56|
||Positive|0|43|600|643|
||Total|41|96|622|759|
|Reviews in Japanes|e|||||
|Sentiment analysis|Negative|188|79|20|287|
||Neutral|67|135|128|330|
||Positive|13|301|2314|2628|
||Total|268|515|2462|3245|



Table 3. Among these 3310 reviews, 2945 were submitted before the intervention. In terms of review distribution, the Kitahama and Cyuou Area had the largest number of hotels (34) and received over half of all the reviews, while the Other Area had the fewest hotels (5) and accounted for only 317 of the total reviews. 

Table 4 presents the coefficient estimates from the linear segmented regression (Model 1) assessing the impacts of the nationwide state of emergency intervention on hotel satisfaction based on all 3310 reviews. The results indicate no significant differences after the intervention. 

To further investigate the influence of the intervention in different areas, four additional ITS analyses were conducted. The area-based ITS analyses (Table 5) revealed no significant impact after the intervention in the Horita and Kankaiji Area, as well as the Other Area. However, the Kitahama and Cyuou Area, and the Kannawa and Myouban Area exhibited notable changes in both level and trend. In the Kannawa and Myouban Area, hotel satisfaction declined following the intervention (Coefficient −0.1408, P-value 0.032) and showed a marginal increase thereafter (Coefficient 0.0288, P-value 0.063). Conversely, the Kitahama and Cyuou Area experienced a significantly higher satisfaction rate immediately after the intervention (Coefficient 0.1394, P-value 0.004), followed by a significant decrease (Coefficient −0.0406, P-value 0.001). 

Figure 4 illustrates the 6-month interval prevalence of hotel satisfaction in all areas of Beppu. Before the intervention, the prevalence remained stable at approximately 89%, subsequently declining gradually to 82% by time 16 (ending March 31st, 2023). 

Figure 5 displays the prevalence of hotel satisfaction in Beppu, categorized by area. In the Kitahama and Cyuou Area, the satisfaction rate was exceptionally high (100%) during the first half-year following the intervention. However, it decreased significantly over subsequent years, reaching 79% by the end of March 2023. In the other three areas, there was a decline in the satisfaction rates during the first half-year after the intervention, followed by an increasing trend in subsequent years. 

Out of the 3310 reviews analyzed, 2914 were positive (600 in English and 2314 in Japanese), and 228 were negative (40 in English and 188 in Japanese). Figure 6 depicts sentiment word clouds, showcasing words with higher frequencies within their respective sentiment categories derived from hotels in Beppu City. The top 3 words in both English and Japanese positive reviews are the same: “onsen” (温泉), “room” (部屋), and “hotel” (ホテル). Similarly, the prominent words from negative reviews 

### Table 3 The number of reviews and hotels. 

||Review number||Hotel number|
|---|---|---|---|
||Before the intervention|After the intervention||
|Kitahama and Cyuou Area|1479|190|34|
|Horita and Kankaiji Area|584|51|9|
|Kannawa and Myouban Area|593|96|29|
|Other Area|289|28|5|
|Total|2945|365|77|



Table 4 Interrupted time series for satisfaction analysis in Beppu (all areas). 

|All four areas|||||
|---|---|---|---|---|
|Variable|Coefficient|Standard error|t-value|P-value|
|Trend|−0.0003|0.0026|−0.107|0.917|
|Intervention|0.0066|0.0257|0.258|0.800|
|Trend change after invention|−0.0094|0.0061|−1.531|0.152|



6 

HUMANITIES AND SOCIAL SCIENCES COMMUNICATIONS | (2024) 11:1695 | https://doi.org/10.1057/s41599-024-04226-4 

<u>ARTICLE</u> 

HUMANITIES AND SOCIAL SCIENCES COMMUNICATIONS <u>|</u> https://doi.org/10.1057/s41599-024-04226-4 

Table 5 Interrupted time series for satisfaction analysis in four distinct areas. 

|Variable|Coefficient|Standard error|t-value|P-value|
|---|---|---|---|---|
|Kitahama and Cyuou Area|||||
|Trend|0.0002|0.0039|0.039|0.970|
|Intervention|0.1394|0.0388|3.590|0.004**|
|Trend change after invention|−0.0406|0.0093|−4.371|0.001***|
|Horita and Kankaiji Area|||||
|Trend|0.0021|0.0090|0.232|0.821|
|Intervention|−0.1408|0.0901|−1.562|0.144|
|Trend change after invention|0.0226|0.0216|1.049|0.315|
|Kannawa and Myouban Area|||||
|Trend|−0.0015|0.0059|−0.250|0.807|
|Intervention|−0.1426|0.0587|−2.429|0.032*|
|Trend change after invention|0.0288|0.0140|2.052|0.063|
|Other Area|||||
|Trend|−0.0136|0.0162|−0.836|0.420|
|Intervention|−0.0349|0.1622|−0.215|0.833|
|Trend change after invention|0.0278|0.0388|0.718|0.486|



*p < 0.05, **p < 0.01, ***p < 0.001. 



Fig. 4 Prevalence of satisfaction before and after the first nationwide state of emergency (All four areas). This figure presents the prevalence of hotel satisfaction across all areas of Beppu, as captured at 6-month intervals. 

are “hotel,” “room,” and “staff ” in English reviews, and “部屋” (“room”), “ホテル” (“hotel”), and “食事” (“meal”) in Japanese reviews. 

Based on the interrupted time series analysis results (Table 5), except for the Kitahama and Cyuou Area, the other three areas did not exhibit a significant decline in satisfaction rates after the intervention (the COVID-19 pandemic). In the Kitahama and Cyuou Area, all 26 negative reviews in English were submitted before the COVID-19 pandemic. Consequently, the word cloud in Japanese (Fig. 7) was generated solely from negative reviews to display significant words associated with unsatisfactory hotel experiences in the Kitahama and Cyuou Area, both before (58 reviews) and after (17 reviews) the intervention. The results indicate that the most common aspect of dissatisfaction mentioned in the reviews before the intervention was related to “部屋” (room). However, after the intervention, the significant words in negative reviews shifted to include “ホテル” (hotel), “フロント” (reception), “部屋” (room), and “対応” (response). 

### Discussion 

This study employed sentiment analysis on TripAdvisor reviews in both English and Japanese to investigate the spatio-temporal variations in customer satisfaction with hotel experiences in Beppu City. Customer online reviews have emerged as a significant factor 

in shaping travelers’ decisions, influencing their choice-making process, building trust, driving quality improvement, and fostering enhanced customer engagement (Abubakar & Ilkan, 2016; Levy et al., 2013; Mauri & Minazzi, 2013; Mellinas et al., 2015). Utilizing the Google Cloud Natural Language API for its resilience and performance in sentiment analysis, our study identified a substantial alignment between the sentiments expressed in reviews and overall ratings. This finding is consistent with previous studies investigating the relationship between online review sentiment and customer ratings (Bigne et al., 2023; Geetha et al., 2017; Martin-Fuentes et al., 2020). The consistency between sentiments and ratings demonstrates the effectiveness of TripAdvisor reviews in reflecting genuine customer experiences in both languages. 

Furthermore, segmenting the data analysis between international and domestic tourists revealed intriguing cultural differences. English reviews tended to provide higher ratings than the sentiment expressed in the text, while Japanese reviews often rated hotels lower than the conveyed sentiment. This finding aligns with cross-cultural communication research comparing Japanese and English book reviews, which shows that Japanese reviewers are more likely to hedge their praise and avoid overtly positive evaluations, whereas English reviewers are more explicit in their praise. This reflects the Japanese cultural emphasis on negative politeness and group harmony (Itakura, 2013). This discrepancy highlights the need to account for varying communication norms when interpreting customer feedback across cultures. Specifically, sentiment analysis enables a more nuanced understanding of true satisfaction levels by uncovering variances between textual content and quantitative ratings. 

Our examination of temporal variations in hotel satisfaction gained particular relevance within the context of the COVID-19 pandemic, a period marked by significant upheaval in global tourism due to travel restrictions and uncertainties that undeniably impacted the hospitality industry (Aigbedo, 2021; Sigala, 2020). While overall satisfaction remained relatively stable before and after the intervention, distinct changes occurred across different areas of Beppu City following the first nationwide state of emergency in Japan. By analyzing four distinct areas in Beppu City, we observed unique patterns across diverse regions. The concentration of downtown hotels, predominantly modern establishments, in the Kitahama and Cyuou Area, which accounted for the majority of reviews, contrasts with the prevalence of traditional hot spring resorts in the Kannawa and Myouban Area, as well as the Horita and Kankaiji Area. This study uncovered differences in satisfaction 

7 

HUMANITIES AND SOCIAL SCIENCES COMMUNICATIONS | (2024) 11:1695 | https://doi.org/10.1057/s41599-024-04226-4 

<u>ARTICLE</u> 

HUMANITIES AND SOCIAL SCIENCES COMMUNICATIONS <u>|</u> https://doi.org/10.1057/s41599-024-04226-4 



Fig. 5 Prevalence of satisfaction before and after the first nationwide state of emergency in four distinct areas. This figure illustrates the distribution of hotel satisfaction levels in Beppu, with distinct patterns emerging across different areas. 

trends when considering the distinct distribution of traditional hotels (ryokans) and modern hotels. 

The Horita and Kankaiji Area, and the Other Area did not show significant declines in satisfaction post-intervention. The Kannawa and Myouban Area experienced a decline in satisfaction, followed by a marginal recovery. This finding suggests that despite a decrease in the number of customers, the pandemic exerted only a marginal negative impact on the satisfaction of ryokans. In contrast, the Kitahama and Cyuou Area exhibited an immediate increase in satisfaction, followed by a significant decline. The area-level satisfaction variation may be partially explained by the differences between ryokans and modern hotels. Ryokans, typically offering dinner and breakfast comprised of Japanese food included in the charges, allow customers to have “heya-shoku” (dining in the guestroom), avoiding public restaurants during the pandemic. Additionally, while hotels are standardized, ryokans provide more personalized Japanese-style hospitality and attendants, aligning with the long-recognized importance of personalization in service quality (Morishita, 2021). Service quality, a key determinant of customer satisfaction (Alnawas & Hemsley-Brown, 2019; Ren et al., 2015), becomes particularly crucial during a pandemic. It has been observed that hotels can enhance their emotional appeal by delivering tailored services and considerate gestures, fostering a sense of comfort and security for guests throughout their stay (Ghorbani et al., 2023). Furthermore, the pandemic has heightened customer sensitivity to the cleanliness of accommodation. Morishita indicates that compared to ryokans, hotel service difficulties with room cleanliness and structure are significantly associated with dissatisfaction (Morishita, 2023). The complex reasons behind this geographical variation demand further investigation to effectively and fully understand and address spatial inequalities. 

The word cloud analysis revealed crucial insights into terms associated with both positive and negative reviews. Positive reviews prominently featured terms such as “onsen”, “room”, and “hotel,” highlighting the importance of a satisfying traditional hot springs experience, high-quality rooms, and overall hotel facilities in shaping customer satisfaction. Conversely, negative reviews consistently identified “hotel” and “room” as persistent sources of dissatisfaction. This finding aligns with the survey results on customer satisfaction in three ryokans and three hotels in Japan, which showed that customers were satisfied with the hot springs (onsen) in ryokans but dissatisfied with the rooms in hotels (Morishita, 2023). 

A detailed analysis of negative reviews in the Kitahama and Cyuou Area revealed a significant shift in customer concerns. Prior to the intervention, concerns predominantly centered on “room”. However, after the intervention, concerns expanded to include broader aspects such as “hotel”, “response”, and “reception”. This transition suggests potential changes in service quality and staff responsiveness specific to downtown hotels during and after the pandemic, superseding the previous emphasis on room cleanliness. An earlier study highlighted the importance of prompt crisis management in the hospitality industry for effective pandemic response and recovery (Garrido-Moreno et al., 2021). The observed inadequacies in response may be attributed to a reduced workforce in Japan’s accommodation sector, a consequence of the COVID-19 outbreak (Hoshi et al., 2021). 

This study has several limitations. A significant constraint is the absence of specific review dates, which limited the precision of the temporal analysis. The classification of reviews as either international or domestic-based solely on language (English or Japanese) may introduce bias, as international customers may express their opinions in Japanese, while domestic customers may use English. Additionally, the exclusive use of data from 

8 

HUMANITIES AND SOCIAL SCIENCES COMMUNICATIONS | (2024) 11:1695 | https://doi.org/10.1057/s41599-024-04226-4 

<u>ARTICLE</u> 

HUMANITIES AND SOCIAL SCIENCES COMMUNICATIONS <u>|</u> https://doi.org/10.1057/s41599-024-04226-4 



Fig. 6 Word cloud from reviews in Beppu. This figure employs word clouds to visualize the sentiment landscape of Beppu City hotel reviews. The clouds, grouped by language (English and Japanese), showcase the most frequent words within positive and negative feedback categories. 



Fig. 7 Word cloud in Japanese from negative reviews in Kitahama and Cyuou Area (left: before the intervention; right: after the intervention). Figure 7 focuses on the Kitahama and Cyuou Area, employing a word cloud constructed solely from negative reviews in Japanese to pinpoint significant words linked to disappointing hotel experiences before and after the intervention. 

TripAdvisor.com limits the study’s comprehensiveness; expanding the dataset to include reviews from diverse platforms such as Booking.com or Google Hotel Review would enhance the robustness of the findings. Moreover, while this study primarily focused on sentiment analysis, future research could explore more nuanced aspects of reviews, such as specific complaints or praises. 

Despite these acknowledged limitations, this study offers valuable insights into the unprecedented impact of the COVID19 pandemic on hotel satisfaction in major Japanese resort destinations, particularly Beppu City. Through meticulous geographical analysis, the research emphasizes the importance of considering both spatial and temporal dynamics to fully understand customer satisfaction trends within the hospitality sector. The findings highlight the need for nuanced management approaches, especially in response to disruptions like the global pandemic. The implications of this work are significant for tourism stakeholders and hoteliers in Beppu City. Practical guidance emerges for managers, emphasizing the importance of closely monitoring customer feedback to identify areas of dissatisfaction. For downtown hotels in the Kitahama and Cyuou Area, reassessing strategies may be prudent given the shifting priorities of travelers in the post-pandemic era. By leveraging these findings, hotels can tailor their service offerings to match the distinct customer profiles and preferences in different city areas. Moreover, recognizing the potential influences of external factors enables better preparation for future disruptions and more effective recovery strategies. This research advocates for targeted strategies across geographic locations and evolving contexts. Most importantly, it demonstrates the immense potential of sentiment analysis as a tool for gaining insights into the customer experience and supporting data-driven decisions in the hospitality and tourism industry. The spatio-temporal understanding of satisfaction revealed in this study can guide hotels toward more responsive and adaptive management practices. 

9 

HUMANITIES AND SOCIAL SCIENCES COMMUNICATIONS | (2024) 11:1695 | https://doi.org/10.1057/s41599-024-04226-4 

<u>ARTICLE</u> 

HUMANITIES AND SOCIAL SCIENCES COMMUNICATIONS <u>|</u> https://doi.org/10.1057/s41599-024-04226-4 

### Conclusion 

This study demonstrates the significant potential of sentiment analysis and spatio-temporal analysis in revealing the complex dynamics of customer satisfaction within the tourism and hospitality sectors. By leveraging online reviews and advanced natural language processing techniques, our research uncovers valuable insights that contribute to theoretical understanding, methodological advancement, and practical applications for the industry. 

Theoretically, our findings observed variations in satisfaction across different areas of Beppu City and over time, particularly in the context of the COVID-19 pandemic. These results underscore the importance of integrating spatio-temporal dynamics into theoretical models. Furthermore, the study enhances the understanding of cross-cultural differences in customer satisfaction and communication styles, as evidenced by the divergence between international and domestic tourists’ sentiment expressions and ratings. 

Methodologically, this research advances the application of sentiment analysis and interrupted time series analysis in tourism research. By integrating these techniques, we present a nuanced approach to understanding customer experiences and satisfaction levels across diverse contexts. The spatio-temporal analysis employed in this study addresses a significant gap in the literature, offering a promising framework for investigating the interplay between location, time, and customer sentiment-an aspect that has been largely overlooked in previous studies. 

From a practical standpoint, the findings provide valuable insights and actionable strategies for tourism stakeholders and hotel managers. By leveraging sentiment analysis and monitoring customer feedback, hotels can identify areas of dissatisfaction, tailor service offerings based on customer preferences, and adapt their communication approaches to better align with cultural norms and expectations. Additionally, the spatio-temporal analysis approach enables tourism stakeholders to track satisfaction trends across locations and events, identify negative aspects, and respond swiftly to shifting customer priorities, particularly in the face of disruptive events such as the COVID-19 pandemic. 

In summary, this research highlights the significant potential of sentiment analysis and spatio-temporal analysis as powerful tools for gaining comprehensive insights into the customer experience and promoting data-driven decision-making in the hospitality and tourism industry. By bridging the gap between theoretical knowledge, methodological advancements, and practical applications, this study paves the way for a deeper understanding of customer satisfaction dynamics and more informed strategies for enhancing the overall tourism experience. 

### Data availability 

All data generated or analysed during this study are included in this published article and its supplementary information file. The dataset was derived from the following public domain resource: https://www.tripadvisor.jp/. 

Received: 29 January 2024; Accepted: 6 December 2024; 



### References 

- Abubakar AM, Ilkan M (2016) Impact of online WOM on destination trust and intention to travel: a medical tourism perspective. J Destin Mark Manag 5(3):192–201. https://doi.org/10.1016/j.jdmm.2015.12.005 

- Alaei AR, Becken S, Stantic B (2019) Sentiment analysis in tourism: capitalizing on big data. J Travel Res 58(2):175–191. https://doi.org/10.1177/0047287517747753 

Al-Natour S, Turetken O (2020) A comparative assessment of sentiment analysis and star ratings for consumer reviews. Int J Inf Manag 54:102132. https://doi. org/10.1016/j.ijinfomgt.2020.102132 

- Alnawas I, Hemsley-Brown J (2019) Examining the key dimensions of customer experience quality in the hotel industry. J Hosp Mark Manag 28(7):833–861. https://doi.org/10.1080/19368623.2019.1568339 

- Alrawadieh Z, Alrawadieh Z, Cetin G (2021) Digital transformation and revenue management: Evidence from the hotel industry. Tour Econ 27(2):328–345. https://doi.org/10.1177/1354816620901928 

- Alvarez Leon I, Cavallin A, Louzao N (2021) City or beach hotel? Location as a determinant of customer satisfaction and room rate. Int J Tour Cities 7(2):278–293. https://doi.org/10.1108/IJTC-07-2020-0142 

- Ananthakrishnan U, Proserpio D, Sharma S (2023) I hear you: does quality improve with customer voice? Mark Sci 42(6):1143–1161. https://doi.org/10. 1287/mksc.2023.1437 

- Beppu City (2023). Tourism Statistics Annual Survey in Beppu. https://www.city. beppu.oita.jp/sangyou/kankou/sokuhou_01.html 

- Bigne E, Ruiz C, Perez-Cabañero C, Cuenca A (2023) Are customer star ratings and sentiments aligned? A deep learning study of the customer service experience in tourism destinations. Serv Bus 17(1):281–314. https://doi.org/10.1007/ s11628-023-00524-0 

- Butler R (2022) COVID-19 and its potential impact on stages of tourist Destination Development. Curr Issues Tour 25(10):1682–1695. https://doi.org/10.1080/ 13683500.2021.1990223 

- Calero C, Turner LW (2020) Regional economic development and tourism: a literature review to highlight future directions for regional tourism research. Tour Econ 26(1):3–26. https://doi.org/10.1177/1354816619881244 

- Calero-Sanz J, Orea-Giner A, Villacé-Molinero T, Muñoz-Mazón A, FuentesMoraleda L (2022) Predicting A New Hotel Rating System by Analysing UGC Content from Tripadvisor: Machine Learning Application to Analyse Service Robots Influence. Procedia Computer Sci 200:1078–1083. https://doi.org/10. 1016/j.procs.2022.01.307 

- Chang V, Liu L, Xu Q, Li T, Hsu C (2023) An improved model for sentiment analysis on luxury hotel review. Exp Syst 40(2). https://doi.org/10.1111/exsy.12580 

- Cuomo MT, Tortora D, Foroudi P, Giordano A, Festa G, Metallo G (2021) Digital transformation and tourist experience co-design: Big social data for planning cultural tourism. Technol Forecast Soc Change 162:120345. https://doi.org/ 10.1016/j.techfore.2020.120345 

- Fujii M, Tanabe S, Yamada M, Mishima T, Sawadate T, Ohsawa S (2017) Assessment of the potential for developing mini/micro hydropower: a case study in Beppu City, Japan. J. Hydrol. Reg. Stud. 11:107–116. https://doi.org/ 10.1016/j.ejrh.2015.10.007 

- García-Pablos A, Cuadros M, Linaza MT (2016) Automatic analysis of textual hotel reviews. Inf Technol Tour 16(1):45–69. https://doi.org/10.1007/s40558-0150047-7 

- Garner B, Kim D (2022) Analyzing user-generated content to improve customer satisfaction at local wine tourism destinations: an analysis of Yelp and TripAdvisor reviews. Consum Behav Tour Hosp 17(4):413–435. https://doi.org/ 10.1108/CBTH-03-2022-0077 

- Garrido-Moreno A, García-Morales VJ, Martín-Rojas R (2021) Going beyond the curve: Strategic measures to recover hotel activity in times of COVID19. Int. J Hospitality Manag 96:102928. https://doi.org/10.1016/j.ijhm. 2021.102928 

- Garvey C, Maskal C (2020) Sentiment analysis of the news media on artificial intelligence does not support claims of negative bias against artificial intelligence. OMICS: A J Integr Biol 24(5):286–299. https://doi.org/10.1089/omi. 2019.0078 

- Geetha M, Singha P, Sinha S (2017) Relationship between customer sentiment and online customer ratings for hotels - An empirical analysis. Tour Manag 61:43–54. https://doi.org/10.1016/j.tourman.2016.12.022 

- Geewax J (2018) Google Cloud platform in action. In: Google Cloud platform in action. https://www.manning.com/books/google-cloud-platform-in-action?a_ aid=jjg&a_bid=89371512 

- Gharzouli M, Hamama AK, Khattabi Z (2022) Topic-based sentiment analysis of hotel reviews. Curr Issues Tour 25(9):1368–1375. https://doi.org/10.1080/ 13683500.2021.1940107 

- Ghorbani A, Mousazadeh H, Akbarzadeh Almani F, Lajevardi M, Hamidizadeh MR, Orouei M, Zhu K, Dávid LD (2023) Reconceptualizing customer perceived value in hotel management in turbulent times: a case study of Isfahan metropolis five-star hotels during the COVID-19 pandemic. Sustainability 15(8):7022. https://doi.org/10.3390/su15087022 

- Google (2023a). Sentiment Analysis. https://cloud.google.com/natural-language/ docs/basics#interpreting_sentiment_analysis_values 

- Google (2023b, July 3). Language support. https://cloud.google.com/naturallanguage/docs/languages 

- Google (2023c, July 3). Natural Language AI. https://cloud.google.com/naturallanguage 

10 

HUMANITIES AND SOCIAL SCIENCES COMMUNICATIONS | (2024) 11:1695 | https://doi.org/10.1057/s41599-024-04226-4 

<u>ARTICLE</u> 

HUMANITIES AND SOCIAL SCIENCES COMMUNICATIONS <u>|</u> https://doi.org/10.1057/s41599-024-04226-4 

- Hawker C, Koukoumidis E (2023) Google Cloud supercharges NLP with large language models. https://cloud.google.com/blog/products/ai-machinelearning/google-cloud-supercharges-nlp-with-large-language-models?hl=en 

- Hirschberg J, Manning CD (2015) Advances in natural language processing. Science 349(6245):261–266. https://doi.org/10.1126/science.aaa8685 

- Hoshi K, Kasahara H, Makioka R, Suzuki M, Tanaka S (2021) Trade-off between job losses and the spread of COVID-19 in Japan. Jpn Econ Rev 72(4):683–716. https://doi.org/10.1007/s42973-021-00092-w 

- Hu F, Warren J, Exeter DJ (2020) Interrupted time series analysis on first cardiovascular disease hospitalization for adherence to lipid-lowering therapy. Pharmacoepidemiology Drug Saf 29(2):150–160. https://doi.org/10.1002/pds.4916 

- Itakura H (2013) Hedging praise in English and Japanese book reviews. J Pragmat 45(1):131–148. https://doi.org/10.1016/j.pragma.2012.11.003 

- Kuhzady S, Ghasemi V (2019) Factors influencing customers’ satisfaction and dissatisfaction with hotels: a text-mining approach. Tour Anal 24(1):69–79. https://doi.org/10.3727/108354219X15458295631972 

- Kyan A, Takakura M (2022) Socio-economic inequalities in physical activity among Japanese adults during the COVID-19 pandemic. Public Health 207:7–13. https://doi.org/10.1016/j.puhe.2022.03.006 

- Latinopoulos D (2020) Analysing the role of urban hotel location in guests’ satisfaction. Anatolia 31(4):636–650. https://doi.org/10.1080/13032917.2020.1808489 

- Lee C-C, Chen M-P (2022) The impact of COVID-19 on the travel and leisure industry returns: Some international evidence. Tour Econ 28(2):451–472. https://doi.org/10.1177/1354816620971981 

- Leske S, Kõlves K, Crompton D, Arensman E, de Leo D (2021) Real-time suicide mortality data from police reports in Queensland, Australia, during the COVID-19 pandemic: an interrupted time-series analysis. Lancet Psychiatry 8(1):58–63. https://doi.org/10.1016/S2215-0366(20)30435-1 

- Levy SE, Duan W, Boo S (2013) An Analysis of One-Star Online Reviews and Responses in the Washington, D.C., Lodging Market. Cornell Hospitality Q 54(1):49–63. https://doi.org/10.1177/1938965512464513 

- Li KX, Jin M, Shi W (2018) Tourism as an important impetus to promoting economic growth: a critical review. Tour Manag Perspect 26:135–142. https:// doi.org/10.1016/j.tmp.2017.10.002 

- Lo AS, Yao SS (2019) What makes hotel online reviews credible? An investigation of the roles of reviewer expertise, review rating consistency and review valence. Int J Contemp Hospitality Manag 31(1):41–60. https://doi.org/10. 1108/IJCHM-10-2017-0671 

- Lu W, Stepchenkova S (2015) User-generated content as a research mode in tourism and hospitality applications: topics, methods, and software. J Hosp Mark Manag 24(2):119–154. https://doi.org/10.1080/19368623.2014.907758 

- Luo, J. M., Vu, H. Q., Li, G., & Law, R. (2021). Understanding service attributes of robot hotels: A sentiment analysis of customer online reviews. International Journal of Hospitality Management, 98. https://doi.org/10.1016/j.ijhm.2021.103032 

- Ma E, Cheng M, Hsiao A (2018) Sentiment analysis—a review and agenda for future research in hospitality contexts. Int J Contemp Hosp Manag 30(11):3287–3308. https://doi.org/10.1108/IJCHM-10-2017-0704 

- Martínez-Navalón, J.-G., Gelashvili, V., & Gómez-Ortega, A. (2021). Evaluation of User Satisfaction and Trust of Review Platforms: Analysis of the Impact of Privacy and E-WOM in the Case of TripAdvisor. Frontiers in Psychology, 12. https://doi.org/10.3389/fpsyg.2021.750527 

- Martin-Fuentes E, Mateu C, Fernandez C (2020) The more the merrier? Number of reviews versus score on TripAdvisor and Booking.com. Int J Hosp Tour Adm 21(1):1–14. https://doi.org/10.1080/15256480.2018.1429337 

- Mauri AG, Minazzi R (2013) Web reviews influence on expectations and purchasing intentions of hotel potential customers. Int J Hospitality Manag 34:99–107. https://doi.org/10.1016/j.ijhm.2013.02.012 

- McDowall D, McCleary R, Bartos BJ (2019) Interrupted time series analysis. Oxford University Press 

- Mehta MP, Kumar G, Ramkumar M (2023) Customer expectations in the hotel industry during the COVID-19 pandemic: a global perspective using sentiment analysis. Tour Recreat Res 48(1):110–127. https://doi.org/10.1080/ 02508281.2021.1894692 

- Mellinas JP, Martínez María-Dolores S-M, Bernal García JJ (2015) Booking.com: the unexpected scoring system. Tour Manag 49:72–74. https://doi.org/10. 1016/j.tourman.2014.08.019 

- Mellinas JP, Nicolau JL, Park S (2019) Inconsistent behavior in online consumer reviews: The effects of hotel attribute ratings on location. Tour Manag 71:421–427. https://doi.org/10.1016/j.tourman.2018.10.034 

- Moreno-Ortiz A, Salles-Bernal S, Orrequia-Barea A (2019) Design and validation of annotation schemas for aspect-based sentiment analysis in the tourism sector. Inf Technol Tour 21(4):535–557. https://doi.org/10.1007/s40558-019-00155-0 

- Morishita S (2023) Customer satisfaction with tangible and intangible services of ryokans and hotels in the Japanese lodging industry. J Glob Tour Res 8(2):117–124. https://doi.org/10.37020/jgtr.8.2_117 

- Morishita, S. (2021). What is Omotenashi? A Comparative Analysis with Service and Hospitality in the Japanese Lodging Industry. J Adv Manag Sci 88–95. https://doi.org/10.18178/joams.9.4.88-95 

- Nakayama M, Wan Y (2019) The cultural impact on social commerce: A sentiment analysis on Yelp ethnic restaurant reviews. Inf Manag 56(2):271–279. https:// doi.org/10.1016/j.im.2018.09.004 

- Nandwani P, Verma R (2021) A review on sentiment analysis and emotion detection from text. Soc Netw Anal Min 11(1):81. https://doi.org/10.1007/ s13278-021-00776-6 

- Nilashi M, Abumalloh RA, Alghamdi A, Minaei-Bidgoli B, Alsulami AA, Thanoon M, Asadi S, Samad S (2021) What is the impact of service quality on customers’ satisfaction during COVID-19 outbreak? New findings from online reviews analysis. Telemat Inform 64:101693. https://doi.org/10.1016/j.tele.2021.101693 

- O’Donnell A, Anderson P, Jané-Llopis E, Manthey J, Kaner E, Rehm J (2019) Immediate impact of minimum unit pricing on alcohol purchases in Scotland: controlled interrupted time series analysis for 2015-18. BMJ 366:l5274. https://doi.org/10.1136/bmj.l5274 

- Palazzo M, Gigauri I, Panait MC, Apostu SA, Siano A (2022) Sustainable Tourism Issues in European Countries during the Global Pandemic Crisis. Sustainability 14(7):3844. https://doi.org/10.3390/su14073844 

- Pencarelli T (2020) The digital revolution in the travel and tourism industry. Inf Technol Tour 22(3):455–476. https://doi.org/10.1007/s40558-019-00160-3 

- Pham TD, Vo D, Li F, Baker K, Han B, Lindsay L, Pashna M, Rowley R (2020) Natural language processing for analysis of student online sentiment in a postgraduate program. Pac J Technol Enhanc Learn 2(2):15–30. https://doi. org/10.24135/pjtel.v2i2.4 

- Pontiki M, Galanis D, Papageorgiou H, Androutsopoulos I, Manandhar S, ALSmadi M, Al-Ayyoub M, Zhao Y, Qin B, De Clercq O, Hoste V, Apidianaki M, Tannier X, Loukachevitch N, Kotelnikov E, Bel N, Jiménez-Zafra SM, Eryiğit G (2016) SemEval-2016 Task 5: Aspect Based Sentiment Analysis. Proceedings of the 10th International Workshop on Semantic Evaluation (SemEval-2016), 19–30. https://doi.org/10.18653/v1/S16-1002 

- Prime Minister’s Office of Japan. (2023). [COVID-19] Declaration of a State of Emergency in response to the Novel Coronavirus Disease (April 16). https:// japan.kantei.go.jp/ongoingtopics/_00020.html 

- Ray B, Garain A, Sarkar R (2021) An ensemble-based hotel recommender system using sentiment analysis and aspect categorization of hotel reviews. Appl Soft Comput 98:106935. https://doi.org/10.1016/j.asoc.2020.106935 

- Ren L, Zhang HQ, Ye BH (2015) Understanding Customer Satisfaction With Budget Hotels Through Online Comments: Evidence From Home Inns in China. J Qual Assur Hospitality Tour 16(1):45–62. https://doi.org/10.1080/ 1528008X.2015.966299 

- Rita P, Ramos R, Borges-Tiago MT, Rodrigues D (2022) Impact of the rating system on sentiment and tone of voice: a Booking.com and TripAdvisor comparison study. Int J Hosp Manag 104:103245. https://doi.org/10.1016/j.ijhm.2022.103245 

- Schuckert M, Liu X, Law R (2015a) A segmentation of online reviews by language groups: How English and non-English speakers rate hotels differently. Int J Hospitality Manag 48:143–149. https://doi.org/10.1016/j.ijhm.2014.12.007 

- Schuckert M, Liu X, Law R (2015b) Hospitality and tourism online reviews: recent trends and future directions. J Travel Tour Mark 32(5):608–621. https://doi. org/10.1080/10548408.2014.933154 

- So KKF, Wei W, Martin D (2021) Understanding customer engagement and social media activities in tourism: a latent profile analysis and cross-validation. J Bus Res 129:474–483. https://doi.org/10.1016/j.jbusres.2020.05.054 

- Song Y, Liu K, Guo L, Yang Z, Jin M (2022) Does hotel customer satisfaction change during the COVID-19? A perspective from online reviews. J Hospitality Tour Manag 51:132–138. https://doi.org/10.1016/j.jhtm.2022.02.027 

- Tamrakar S, Madhavi BK, Mohan V (2022). Democratizing sentiment analysis of Twitter data using Google Cloud Platform and BigQuery. In: Handbook of intelligent computing and optimization for sustainable development. Wiley. pp. 287–304 

- TripAdvisor.com (2022). Tripadvisor is the world’s largest travel site. https://ir. tripadvisor.com/ 

- Tsukamoto M (2016) Physical and mental treatment of tōji and local touristic strategy in Beppu. Int J Humanit Soc Sci 8(12):4056–4059 

- Vaishar A, Šťastná M (2022) Impact of the COVID-19 pandemic on rural tourism in Czechia Preliminary considerations. Curr Issues Tour 25(2):187–191. https://doi.org/10.1080/13683500.2020.1839027 

- Varkaris E, Neuhofer B (2017) The influence of social media on the consumers’ hotel decision journey. J Hosp Tour Technol 8(1):101–118. https://doi.org/10. 1108/JHTT-09-2016-0058 

- Venkit, P. N., & Wilson, S. (2021). Identification of Bias Against People with Disabilities in Sentiment Analysis and Toxicity Detection Models. http:// arxiv.org/abs/2111.13259 

- Yang Y, Mao Z, Tang J (2018) Understanding guest satisfaction with urban hotel location. J Travel Res 57(2):243–259. https://doi.org/10.1177/0047287517691153 

### Acknowledgements 

This work was supported by JSPS KAKENHI Grant Number 24K21025. 

11 

HUMANITIES AND SOCIAL SCIENCES COMMUNICATIONS | (2024) 11:1695 | https://doi.org/10.1057/s41599-024-04226-4 

<u>ARTICLE</u> 

HUMANITIES AND SOCIAL SCIENCES COMMUNICATIONS <u>|</u> https://doi.org/10.1057/s41599-024-04226-4 

### Author contributions 

Feiyu Hu: conceptualized the research question, designed the methodology, conducted data collection and statistical analysis, drafted and revised the entire manuscript; Jun Pan: shaped the research questions, provided feedback on data analysis strategies, edited and revised the manuscript; Haijun Wang: provided data analysis strategies and revised the manuscript. 

### Competing interests 

The authors declare no competing interests. 

### Ethical approval 

This article does not contain any studies with human participants performed by any of the authors. 

### Informed consent 

This article does not contain any studies with human participants performed by any of the authors. 

### Additional information 

Supplementary information The online version contains supplementary material available at https://doi.org/10.1057/s41599-024-04226-4. 

Reprints and permission information is available at http://www.nature.com/reprints 

Publisher’s note Springer Nature remains neutral with regard to jurisdictional claims in published maps and institutional affiliations. 

Open Access This article is licensed under a Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International License, which permits any non-commercial use, sharing, distribution and reproduction in any medium or format, as long as you give appropriate credit to the original author(s) and the source, provide a link to the Creative Commons licence, and indicate if you modified the licensed material. You do not have permission under this licence to share adapted material derived from this article or parts of it. The images or other third party material in this article are included in the article’s Creative Commons licence, unless indicated otherwise in a credit line to the material. If material is not included in the article’s Creative Commons licence and your intended use is not permitted by statutory regulation or exceeds the permitted use, you will need to obtain permission directly from the copyright holder. To view a copy of this licence, visit http://creativecommons.org/ licenses/by-nc-nd/4.0/. 

© The Author(s) 2024 

Correspondence and requests for materials should be addressed to Jun Pan. 

12 

HUMANITIES AND SOCIAL SCIENCES COMMUNICATIONS | (2024) 11:1695 | https://doi.org/10.1057/s41599-024-04226-4 

