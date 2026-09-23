Asia Pacific Journal of Information Systems Vol. 35 No. 1 (March 2025), 49-72 

ISSN 2288-5404 (Print) / ISSN 2288-6818 (Online) https://doi.org/10.14329/apjis.2025.35.1.49 

# Beyond the Stars: The Impact of Rating-Text Inconsistency on Perceived Review Usefulness 

Boram Kwon<sup>**a,**†</sup> , Junyeong Lee<sup>**b,**†</sup><sup>**,***</sup> , Jinyoung Min<sup>**c**</sup> , Chanhee Kwak<sup>**d**</sup> , HanByeol Stella Choi<sup>**e,***</sup> 

> a _Assistant Professor, College of Business, Chosun University, Korea_ 

> b _Associate Professor, Department of Management Information Systems, Chungbuk National University, Korea_ 

> c _Associate Professor, College of Business & Economics, Chung-Ang University, Korea_ 

> d _Assistant Professor, Department of Artificial Intelligence Convergence, Kangnam University, Korea_ 

> e _Assistant Professor, Department of Management Information Systems, Myongji University, Korea_ 

##### **A B S T R A C T** 

Online reviews have a significant influence on purchasing decisions. Online reviews typically comprise star ratings and text content, both of which consumers consider when evaluating a product to reduce uncertainty. Previous studies have primarily concentrated on the isolated effects of these factors, assuming a strong correlation between star ratings and text context. However, there is a lack of research on the effect of review inconsistency on consumer perceptions, in which the sentiment conveyed in the text differs from the assigned star rating. By arguing that review inconsistency may provide more nuanced insights for consumers and has the potential to be positive in certain situations, this study explored the impact of review inconsistency on the perceived usefulness of reviews. In particular, we investigate the impact of two different inconsistencies between star ratings and review text, namely, degree and direction inconsistencies, by examining the circumstances under which these inconsistencies may stimulate consumer curiosity and prompt more comprehensive information processing. The analysis of data from 41,258 reviews of 183 products on Amazon.com suggests that review inconsistency can be perceived positively depending on contextual factors such as product awareness and review negativity. This study provides novel insights into consumer information processing and review platform design. 

_Keywords:_ Review Usefulness, Rating, Review Text, Inconsistency, Curiosity Theory 

## Ⅰ **. Introduction** 

Online reviews have a significant impact on purchasing decisions. Consumers can alter their purchase 

preferences by reading reviews, which affect their trust in online e-commerce businesses, making it important for both consumers and companies (Zhu and Zhang, 2010). Online reviews consist primarily 

†Co-First Authors 

*Co-Corresponding Authors. E-mail: junyeong.lee@cbnu.ac.kr (J. Lee), hbschoi@mju.ac.kr (HBS Choi) 

Beyond the Stars: The Impact of Rating-Text Inconsistency on Perceived Review Usefulness 

of two elements: star ratings and review texts. Consumers tend to check both star ratings and review texts when exploring reviews. Accordingly, previous studies have explained consumer behavior by focusing on these two elements (Hu and Chen, 2016; Korfiatis et al., 2012). Typically, consumers first look at the star rating and then examine the text content, which helps reduce product uncertainty and increases confidence in purchase decisions based on elaborate narratives about the target product or service (Hong et al., 2017; Kim and Hollingshead, 2015). This is based on the assumption that star ratings and text content share similarities (Tsang and Prendergast, 2009) and that the emotions exhibited in the review text would have a high correlation with the rating (Abedin et al., 2021; Aghakhani et al., 2021). Under such assumptions, many existing studies have shown that rating-text consistency is useful and effective (e.g., Aghakhani et al., 2021), whereas rating-text inconsistency is considered a problem to be solved or a review that does not need to be checked. 

However, the emotions contained in individual review texts may differ even though they have the same star rating (Almansour et al., 2022). For example, by examining product reviews on Amazon, one can find that even among reviews with the same 5-star rating, some users leave extremely satisfactory opinions, whereas others include comments about aspects they found to be lacking. Similarly, a low rating does not always include only negative review sentiments, and vice versa (Hazarika et al., 2021). A unique characteristic of online reviews is that the consistency between review ratings and texts is not guaranteed, because reviewers have their own reference points and thresholds for satisfaction with products or services (Hu et al., 2017). Because review inconsistency is widespread and its effects continue to be questioned (Liu and Karahanna, 2017), recent 

research has focused on the discrepancy between text and star ratings (Fazzolari et al., 2017; Fu et al., 2013; Geierhos et al., 2015). 

We define review inconsistency as the inconsistency between a review text and its attendant star ratings (Abedin et al., 2021; Aghakhani et al., 2021). In reviews composed of star ratings and review text, the review text may or may not contain content consistent with the average text sentiment typically associated with a given star rating. In addition, review texts can provide supplementary context and rationale for assigned star ratings (Mudambi and Schuff, 2010). To illustrate, a consumer might want to know if a 5-star review means satisfaction with all aspects of the product or if it is a glowing endorsement of a particular feature. In this regard, review texts play an important role in helping consumers understand the detailed pros and cons of a product that are difficult to grasp from star ratings (Ghose and Ipeirotis, 2010). Therefore, relying solely on star ratings to communicate review information may have limitations (Chen and Tseng, 2011; Korfiatis et al., 2012; Mudambi and Schuff, 2010), especially in situations where such inconsistencies exist (Fazzolari et al., 2017; Fu et al., 2013). Prior studies on inconsistent reviews between star ratings and text have focused on their existence, their negative effects, and ways to reduce them, showing differences in distribution depending on product type, star rating value, app category, whether the app was free or paid, and whether it was a fake review (Hazarika et al., 2021; Mudambi et al., 2014; Shan et al., 2018). However, it should be noted that inconsistencies in reviews do not necessarily have negative consequences. Indeed, some inconsistencies may pique consumers’ curiosity, prompting them to seek further information. This enables consumers to obtain more detailed information that is beneficial for 

50  Asia Pacific Journal of Information Systems 

Vol. 35 No. 1 

Boram Kwon, Junyeong Lee, Jinyoung Min, Chanhee Kwak, HanByeol Stella Choi 

their decision-making processes. 

Moreover, in the current usefulness voting system, consumers can leave inconsistent reviews with the deliberate intention of increasing their visibility and the number of usefulness votes they receive. Because people primarily pay attention to top-ranked reviews with usefulness votes, inconsistent reviews often gain high usefulness votes. It is, therefore, crucial to understand how consumers perceive rating-text inconsistent reviews and address such inconsistent reviews in a timely manner (Hazarika et al., 2021; Hu et al., 2017). However, substantial research is lacking on the specific conditions or mechanisms that may induce or facilitate these positive effects. Therefore, this study aims to identify the impact of review inconsistencies on consumers’ information processing and review usefulness and to suggest contextual factors that may lead to positive outcomes. In addition, we separate review inconsistency into degree inconsistency, which represents the difference in the average text sentiment score of reviews with the same star rating within a product, and direction inconsistency, which indicates the difference in positive/negative direction between star rating and text, whereas most prior studies have focused on each of the two review inconsistencies separately (Shan et al., 2021; Wang et al., 2023; Zhang et al., 2023). 

We employed the lens of curiosity theory to understand the positive effects and conditions of review inconsistency. Although previous studies have primarily regarded rating-text inconsistency as a negative phenomenon and a challenge to be addressed (Abedin et al., 2021; Aghakhani et al., 2021), curiosity theory posits that inconsistency can stimulate consumers’ curiosity and facilitate more comprehensive information processing (Steur et al., 2022). In certain instances, review inconsistencies may prompt consumers to seek additional information, which could 

facilitate more sophisticated information searches. Accordingly, we sought to elucidate the conditions under which inconsistent reviews influence review usefulness. To examine when and how these two review inconsistencies affect review usefulness, we investigated their interaction effects with two contingency factors, product awareness and review negativity. We analyzed 41,258 reviews of 183 Amazon products using zero-inflated negative binomial regression. Our findings deepen the understanding of consumer review information processing by revealing the mechanisms through which review inconsistencies can be perceived as useful through contextual elements and provide important implications for review platform development and management. 

## Ⅱ **. Conceptual Background** 

### 2.1. Review Usefulness 

Online reviews are utilized as an important guide for decision-making that reduces consumer purchase uncertainty amid an abundance of information (Mudambi and Schuff, 2010), and they also have a significant impact on the sales of products and services (Hong et al., 2017; Ye et al., 2009). Many online platforms have adopted usefulness voting systems to help buyers effectively find useful reviews (Lee et al., 2021). Usefulness is defined as the degree to which people who read the review perceive it as useful (Mudambi and Schuff, 2010). Researchers have shown great interest in review usefulness as an important clue to understanding the consumer decision-making process, and have examined the potential factors that determine it (Racherla and Friske, 2012). Factors that positively influence review useful- 

Asia Pacific Journal of Information Systems 51 

Vol. 35 No. 1 

Beyond the Stars: The Impact of Rating-Text Inconsistency on Perceived Review Usefulness 

ness include review text characteristics (e.g., length and readability), reviewer characteristics (e.g., level of information exposure and previous experience), review context characteristics (e.g., awareness), and product characteristics (e.g., product type) (Choi and Leon, 2020; Hong et al., 2017). 

Among these, star ratings and review texts provide important information that can indicate consumer satisfaction with and attitudes toward products. The literature on online reviews treats these as major influencing factors (Chen and Tseng, 2011; Hu and Chen, 2016; Korfiatis et al., 2012; Mudambi and Schuff, 2010; Pavlou and Dimoka, 2006). For example, high star ratings (Choi and Leon, 2020), rating extremes (Filieri et al., 2018), and differences from average ratings (Baek et al., 2012) affect review usefulness. Review depth (Cao et al., 2011; Chua and Banerjee, 2015), readability (Ghose and Ipeirotis, 2010), and negativity (Park and Lee, 2009; Verhagen et al., 2013) positively affect review usefulness. Previous research has primarily examined the characteristics of star ratings and text (Korfiatis et al., 2012; Singh et al., 2017), assuming that the ratings are a summary of the texts and their valences are consistent (Tsang and Prendergast, 2009). Following these studies, which examined the effects of review text and star ratings on review usefulness, studies that considered both factors simultaneously have also emerged. 

Although many previous studies have revealed that user emotions expressed in text are highly correlated with ratings (Geetha et al., 2017), the existence of inconsistent reviews, in which star ratings and review text imply different meanings, has been continuously confirmed (Shan et al., 2018). Even with the same star rating, the emotions contained in a review can vary, and such reviews can be perceived as sufficiently useful. Accordingly, it is meaningful to compre- 

hensively consider the relationship between review text and star ratings, and examine the effect of inconsistent reviews on review usefulness. 

### 2.2. Review Inconsistency 

Although many studies related to online reviews emphasize that star ratings and review text are important for understanding consumer information processing (Cheung, 2012), they have mainly examined the characteristics of these elements and assumed consistency between star ratings and review text (Chua and Banerjee, 2016; Korfiatis et al., 2012; Mudambi and Schuff, 2010). Although it is assumed that star ratings are a summary of the text and that their values are consistent, the two elements are not necessarily aligned within the review (Islam, 2014). Star ratings may lack validity because they can be biased by consumer perceptions or editorial policies (Steur et al., 2022). Previous literature has confirmed the inconsistencies between star ratings and review text in various contexts, such as applications, e-commerce, and restaurants (Fu et al., 2013; Geierhos et al., 2015; Mudambi et al., 2014). Additionally, research findings suggest that inconsistencies occur more frequently with high star ratings and for experience goods, whereas they tend to occur less frequently with search goods (Mudambi et al., 2014). Fazzolari et al. (2017) revealed that inconsistencies occurred across all star ratings; however, most occurred in 2-star and 4-star reviews. 

Previous studies have defined review inconsistency as either the gap between text sentiment and the average sentiment typically associated with a given star rating (Jin et al., 2023; Shan et al., 2021) or the presence or absence of a contradiction between rating and text sentiment (Aghakhani et al., 2021; Tsang and Prendergast, 2009). Building on the con- 

52  Asia Pacific Journal of Information Systems 

Vol. 35 No. 1 

Boram Kwon, Junyeong Lee, Jinyoung Min, Chanhee Kwak, HanByeol Stella Choi 

cepts of these previous studies, this study aims to examine the different measurements of inconsistency by distinguishing between degree inconsistency and direction inconsistency. The former, which we term degree inconsistency, occurs when the text review of a specific product with a certain star rating differs (either more positive or negative) from the average text sentiment of other reviews with the same star rating (Shan et al., 2021, studies that measured in the same way). In this case, sentiments in the same direction may differ in degree. Degree inconsistency is an important aspect in fake review detection (Shan et al., 2021) and review usefulness (Zhang et al., 2023). They found that as the degree inconsistency increased, the likelihood of a review’s fakeness and usefulness increased. The latter, which we term direction inconsistency, refers to cases in which star ratings and text are directionally contradictory, for example, showing a strong contrast in the difference between ratings and text sentiment (e.g., negative sentiment with positive ratings and positive sentiment with negative ratings). Wang et al. (2023) found a significant moderating role of direction inconsistency in the relationship between review text richness and review helpfulness. Although previous studies have attempted to determine the impact of degree and direction inconsistency, they are limited in their focus to the respective aspects of review inconsistency. This study differs from such studies by simultaneously addressing these two sub-dimensions. 

<Table 1> summarizes the previous studies related to review inconsistencies. Early studies focused on the phenomenon itself and attempted to determine whether or how much review inconsistency occurred in a review system. For example, Park and Kim (2008) confirmed that inconsistencies between star ratings and review text predicted that inconsistencies would negatively affect consumers, citing cognitive fit theory 

and the efficiency of information processing. Because review inconsistency is becoming a common phenomenon, recent studies have focused on the consequences of review inconsistency, attempting to consider different aspects of review inconsistency (Shan et al., 2021; Wang et al., 2023; Zhang et al., 2023). Studies in this stream commonly agree that inconsistency between review text and ratings, or textual inconsistency with other review texts under the same star ratings, affects information processing by attracting consumers’ attention and arousing curiosity (Shan et al., 2021; Shoemaker et al., 1987). Although this leads to uncertainty about information and ambiguous stimuli (Steur et al., 2022), consumers put more effort into minimizing uncertainty when conflicting information exists (Nazlan et al., 2018). Through this process, consumers experience the reward of reducing uncertainty and gaining understanding, which is a key mechanism for increasing the usefulness of online reviews (Liu and Karahanna, 2017). In summary, inconsistent reviews do not simply have a negative impact on consumers but rather play a role in attracting attention and making them examine information more closely. This leads consumers to invest more effort in resolving uncertainty and making more reliable decisions, which can ultimately increase the usefulness of reviews. Because research on inconsistent reviews is still in its early stages, an understanding of the effects of such reviews is necessary. Therefore, we examined the relationship between aspects of review inconsistency and usefulness votes through the lens of curiosity theory. 

### 2.3. Curiosity Theory 

Curiosity theory explains the exploratory desire that people experience when confronted with new information or ambiguous stimuli. Curiosity is the 

Asia Pacific Journal of Information Systems 53 

Vol. 35 No. 1 

Beyond the Stars: The Impact of Rating-Text Inconsistency on Perceived Review Usefulness 

|Findings|Discovered the inconsistencies between user comments and ratings and proposed<br>WisCom, an integrated system to analyze user reviews and detect inconsistencies<br>in reviews.|Found that star rating/review text misalignment occurs more often for experience<br>goods, and goods that receive high star ratings.|Introduced a method to detect inconsistencies between numerical ratings and<br>review texts by evaluating the content of user-generated reviews.|Detected that a misalignment can exist between review text and the score<br>associated with it and argued that by focusing only on those texts associated<br>with a mismatch, consumers could achieve better awareness concerning what<br>has been liked or not about aproduct.|Found that although the ratings and sentiments are highly correlated and<br>visualized abnormal distribution of review sentiments for every rating to<br>statisticallyverifythe existence of inconsistency.|Divided review inconsistency into three categories and demonstrated significant<br>positive effects of review inconsistency on the performance of fake online<br>consumer review detection.|Found the moderating role of direction inconsistency in the relationship between<br>text richness and review helpfulness.|Examined the effect of review novelty and inconsistency on usefulness with the<br>moderatingeffect of review valence, reviewer expertise, and restaurantpopularity.|Investigated the impact of review inconsistency on review usefulness, considering<br>both degree and direction inconsistency.|
|---|---|---|---|---|---|---|---|---|---|
|Data Collection|Google play store<br>(13,286,706 user<br>reviews)|Amazon.com<br>(1,734 randomly<br>selected reviews)|Jameda.de and<br>Docinsider.de<br>(593,633 reviews)|Booking.com and<br>TripAdvisor.com<br>(632,163 reviews)|Yelp.com<br>(24,539 reviews)|Yelp.com<br>(24,539 reviews)|JD.com<br>(9,692 reviews)|Yelp.com<br>(1,744,693 reviews)|Amazon.com<br>(41,258 reviews)|
|Research<br>Methods|Sentiment<br>analysis|Machine<br>learning|Sentiment<br>Analysis|Artificial<br>intelligence|Sentiment<br>Analysis|Machine<br>learning|Artificial<br>intelligence|Deep learning|Sentiment<br>Analysis|
|Inconsistency<br>Types|Direction<br>inconsistency|Direction<br>inconsistency|Degree<br>inconsistency|Direction<br>inconsistency|Degree<br>inconsistency|Degree<br>inconsistency|Direction<br>inconsistency|Degree<br>inconsistency|Degree and<br>direction<br>inconsistencies|
|Theoretical<br>Perspectives|Multi-level system|Elaboration likelihood<br>model (ELM)|Polarity inference|Polarity detection|-|Deception and<br>attitude-behavior<br>consistencytheories|Prospect theory|Heuristic-systematic<br>model|Curiosity Theory|
|Authors|Fu et al.<br>(2013)|Mudambi et al.<br>(2014)|Geierhos et al.<br>(2015)|Fazzolari et al.<br>(2017)|Shan et al.<br>(2018)|Shan et al.<br>(2021)|Wang et al.<br>(2023)|Zhang et al.<br>(2023)|This study|



54  Asia Pacific Journal of Information Systems 

Vol. 35 No. 1 

Boram Kwon, Junyeong Lee, Jinyoung Min, Chanhee Kwak, HanByeol Stella Choi 

motivation to fill information gaps, leading people to seek and understand more information (Berlyne, 1960; Collins et al., 2004; Litman and Jimerson, 2004). This theoretical lens provides important insights into the impact of review inconsistencies on consumer information processing. 

Loewenstein (1994) explained that, when people face new information or complex and ambiguous stimuli, curiosity promotes information-seeking behavior (Hill et al., 2016; Smith and Swinyard, 1988). Research has shown that greater uncertainty is associated with greater curiosity about potential answers (Gottlieb and Oudeyer, 2018; Kidd and Hayden, 2015). This increased curiosity motivates individuals to seek more information to reduce uncertainty (Berlyne, 1955; Litman and Jimerson, 2004). In the context of online reviews, these inconsistencies make it difficult for consumers to form clear and consistent impressions of products and services. Consumers are also uncertain about aspects of trust and how to reconcile different opinions. This state of uncertainty and ambiguity triggers curiosity and motivates consumers to find additional information to resolve inconsistencies and form a more comprehensive understanding (Steur et al., 2022). Consequently, consumers make an effort to read reviews in more detail and seek related reviews to resolve this uncertainty. 

Curiosity is a major driver of information-seeking behavior (Loewenstein, 1994), and satisfying the desire for clarity provides utility gains by filling information gaps (Golman and Loewenstein, 2015). Utility refers to the perceived value or benefit that consumers derive from information. Clarity implies that knowing information is better than not knowing it, indicating that the information itself is a source of utility (Golman and Loewenstein, 2015). Additionally, satisfying curiosity liberates one from 

anxiety (Litman, 2005), and the process of resolving uncertainty is rewarding and provides relief (Litman and Jimerson, 2004; Loewenstein, 1994; Singh and Manjaly, 2021). In the context of online reviews, consumers exploring inconsistent reviews gain a deeper understanding of the product by resolving uncertainty, which increases the perceived usefulness of the review. 

Recent studies have focused on how curiosity affects information exploration and processing (Hill et al., 2016; Laran and Tsiros, 2013), demonstrating that curiosity increases the breadth and quality of information exploration (Menon and Soman, 2002). Research on curiosity has explored the processing of uncertain information in various digital contexts such as emails (Wainer et al., 2011) and news (Scacco and Muddiman, 2020). These studies provide insight that can be applied to online reviews. Similar to how individuals process uncertain information through email or news, reviews with conflicting information confront consumers with uncertainty and stimulate their desire for clarity. Consumers can reduce information gaps and resolve uncertainty through information seeking and processing, leading to increased consumer utility. In the context of online reviews, this increased utility manifests as a higher perceived usefulness of the review as consumers gain a more comprehensive understanding of the product or service being reviewed. 

## Ⅲ **. Hypotheses** 

According to curiosity theory, consumers select and focus on deviant or unusual information (i.e., inconsistent) (Shoemaker et al., 1987). Curiosity refers to an intense “desire to know.” It is activated when people realize that they lack the specific in- 

Asia Pacific Journal of Information Systems 55 

Vol. 35 No. 1 

Beyond the Stars: The Impact of Rating-Text Inconsistency on Perceived Review Usefulness 

formation needed to solve problems or complete their knowledge portfolios (Litman, 2005). Curiosity contributes to focusing strong attention on information and to specific information-seeking and acquisition behaviors (Mussel, 2010; Von Stumm et al., 2011). In other words, inconsistent reviews stimulate curiosity and cause consumers to examine the information more closely. Consumers wonder why such inconsistencies occur, and exert more cognitive effort to minimize the uncertainty caused by conflicting information. They carefully read the review text, which is the source of the inconsistency, compare it with the star rating, and process the information based on specific cues (systematic cues). This aligns with previous research based on the dual-process theory, which suggests that systematic processing occurs when there is a higher level of cognitive processing motivation (Bohner et al., 1995), and systematic processing positively affects the perceived usefulness of the review (Chung et al., 2017; Qahri-Saremi and Montazemi, 2019). This study posits that review inconsistencies influence review usefulness by stimulating curiosity and promoting systematic information processing. Accordingly, we focused on two contingency factors, product awareness and review negativity, to empirically analyze how these factors interact with review inconsistency and how such interactions affect review usefulness. 

First, we consider the context of product awareness. The idea that reviewers may use high or low ratings to attract attention to their reviews among numerous others (Shan et al., 2021) suggests that for products with many reviews (i.e., high awareness products), reviewers may leave reviews exhibiting inconsistency to attract attention. If this intention is realized, review inconsistency may increase its usefulness. When a product has many reviews, consumers face uncertainty in determining which reviews 

to read and which are useful, and thus confront the challenge of selectively reading the necessary reviews (Jabr and Rahman, 2022). In such situations, consumers use selective attention mechanisms to efficiently utilize their limited cognitive resources (Smith et al., 2008). Reviews exhibiting inconsistencies act as unique stimuli that attract attention and gain precedence in information processing. For products with many reviews, there is generally an expectation that most reviews will be positive (Hu et al., 2009). Therefore, reviews exhibiting inconsistencies that differ from this expectation can attract consumer attention and induce deeper processing. Additionally, among many reviews presenting similar opinions, those exhibiting inconsistencies can reveal new perspectives or hidden features of the product, which are perceived as useful information for consumer decision-making. 

- H1: (a) Degree and (b) direction inconsistency of a review has a positive effect on review usefulness, when product awareness is high. 

Next, we consider the moderating role of negative sentiments in the relationship between review inconsistency and usefulness. Previous research has identified various incentives for reviewers to leave negative comments alongside high star ratings, driven by motivations such as altruism, reciprocity, and community building (Mudambi et al., 2014; Valdivia et al., 2019). Studies have also demonstrated negativity bias, whereby reviews with negative sentiments tend to be perceived as more useful (Lee et al., 2017; Sen and Lerman, 2007). Consumers pay more attention to negative reviews during information searches as a mechanism for avoiding risk (Lee et al., 2017). Negative reviews are perceived as having higher informational value than positive sentiments in product 

56  Asia Pacific Journal of Information Systems 

Vol. 35 No. 1 

Boram Kwon, Junyeong Lee, Jinyoung Min, Chanhee Kwak, HanByeol Stella Choi 

evaluation because information reveals potential problems or limitations of the product, which increases the usefulness of the review (Sen and Lerman, 2007). When encountering such reviews, consumers may engage in deeper information processing to reconcile the inconsistency and attempt to infer the reviewer’s motivation (Sen and Lerman, 2007). This increased cognitive effort, combined with the inherent attention-grabbing nature of negative information (Baumeister et al., 2001; Rozin and Royzman, 2001), may cause these reviews to be judged as particularly useful. In other words, we propose that negative sentiment amplifies the effect of inconsistency on review usefulness. 

- H2: (a) Degree and (b) direction inconsistency of a review has a positive effect on review usefulness, when a review has negative sentiment. 

## Ⅳ **. Research Methodology** 

The hypothesis put forth in this study was validated using an Amazon.com review. As of 2023, Amazon has 2.27 billion monthly visitors from across the world according to Statista, an online statistics database. Owing to its widespread use, Amazon has been used as a source of data in numerous earlier studies to examine the factors affecting the review usefulness of online platforms (Mudambi and Schuff, 2010). Reviews were gathered between December 20 and December 27, 2021 using a web crawler created in Python 3.8. Crawlers collected product codes, review texts, usefulness scores, and star ratings. Data with fewer than five total usefulness votes for the product after data collection were omitted to ensure robustness of the analysis (Choi and Leon, 2020; Siering, et al., 2018). The final data included 173 products and 41,258 reviews with an average of 238 reviews per product. <Table 2> presents the descriptive statistics for the products in each category, including the mean and standard deviation corresponding to the star rating. 

### 4.1. Data Collection 

### 4.2. Definition of Variables 

<Table 2> Descriptive Statistics of Each Product Category 

|Product Category|Number of Products|Number of Reviews|Mean of Review Rating|SD of Review Rating|
|---|---|---|---|---|
|Baby|28|6,137|4.19|1.36|
|Electronics|13|4,220|4.01|1.46|
|Games|21|2,670|4.09|1.49|
|Movies|13|3,765|4.33|1.24|
|Music|9|1,766|4.15|1.39|
|Office|24|4,815|4.21|1.32|
|Pet|16|4,740|3.67|1.62|
|Shoes|12|3,458|3.84|1.41|
|Streaming|16|4,365|3.92|1.52|
|Others|21|5,322|4.10|1.36|
|Total|173|41,258|4.05|1.43|



Asia Pacific Journal of Information Systems 57 

Vol. 35 No. 1 

Beyond the Stars: The Impact of Rating-Text Inconsistency on Perceived Review Usefulness 

Degree inconsistency is defined as the absolute difference between the content sentiment and star rating of online reviews of the same products and was measured using the formula for rating sentiment inconsistency by Shan et al. (2021) (see <Equation 1>). Preprocessing, sentiment term extraction, sentiment score calculation, and sentiment score aggregation comprise the four basic steps of the content sentiment analysis process used in the calculation. Tokenization, lemmatization, PoS tagging, and term filtering were the preprocessing procedures. Because of the high accuracy of SentiWordNet 3.0 (Baccianella et al., 2010) over other lexicon-based methods in extracting sentiment, such as Linguistic Inquiry and Word Count (LIWC) (Tausczik and Pennebaker, 2010) and the extended version of the Profile of MoodStates (POMS-ex) (Bollen et al., 2021), this study selected it to calculate the sentiment scores 





<sup></sup> : Inconsistency in the jth review. 

- <sup></sup> , <sup></sup> : z-scores of the rating and sentiment of the jth review. 

<sup></sup> , <sup></sup> : Rating and sentiment of the jth review.  ,<sup></sup>  : Mean values of ratings and sentiments of reviews for the same products. 

-  ,  : The standard deviations of ratings and sentiment score of all reviews. 

#### of the identified term. 

Direction inconsistency refers to the unmatched directions between the sentiment of the review content and its star rating and measures whether the sentiments expressed by the star rating and the contents of the review are opposite. Specifically, positive review content with a star rating of 1 or 2 and negative review content with a star rating of 4 or 5 indicated that the stated sentiment was opposite of the star rating. Product awareness is the number of reviews written for a specific product (Zhang and Lin, 2018). Furthermore, in this study, we measured “review negativity” using the LIWC program (Boyd, 2017). This program calculates the score of negative sentiments in a text by analyzing linguistic features and word usage. 

Finally, review usefulness, the dependent variable in this study, refers to the number of usefulness votes received by the review. Based on previous studies of review usefulness, word count, day lapse, and review photos were considered as control variables. Word count represents the number of words included in the review, and previous studies have argued that the longer the review, the more useful it is (Mudambi and Schuff, 2010). Day lapse refers to the natural logarithm of the number of days between the crawling date and the review date. This variable is controlled because it negatively affects the usefulness vote, since online review systems generally present the latest reviews on the first page, giving them more visibility than older reviews on subsequent pages. A review photo indicates whether the review contains images. Previous studies have shown that images included in reviews have a positive impact on usefulness (Filieri et al., 2018). <Table 3> presents the definitions of the variables. 

<Equation 1> Formula for rating-sentiment 

inconsistency 

### 4.3. Descriptive Statistics 

> 58  Asia Pacific Journal of Information Systems 

Vol. 35 No. 1 

Boram Kwon, Junyeong Lee, Jinyoung Min, Chanhee Kwak, HanByeol Stella Choi 

<Table 3> Definition of Variables 

||Variables|Definition|Instrumentation of Model Variables|
|---|---|---|---|
|Dependent<br>Variable|Review Usefulness|Number of “usefulness” votes in the review|Numerical value (scale)|
||Degree Inconsistency|The absolute difference between review<br>sentiment and star ratingof the same review|<sup>Numerical value (scale)</sup>|
|Independent<br>Variables|Direction Inconsistency|Whether directions between the sentiment of<br>the review content and its star rating are<br>unmatched (e.g., positive sentiment with<br>negative rating or negative sentiment with<br>positive rating)|1 = If the sentiment of the review text is<br>negative with a 4- or 5-star rating; or the<br>sentiment of the review text is positive<br>with a 1- or 2-star rating;<br>0 = Otherwise|
|d|Product Awareness|The number of reviews written for a specific<br>product|Numerical value (scale)|
|Moerators|Review Negativity|The extent of negative emotional tone present<br>in the text|Numerical value (scale)|
||Word Count|Take the natural logarithm of the number of<br>words in the review text|Numerical value (scale)|
|Control<br>Variables|Day Lapse|Take the natural logarithm of the number of<br>days between the crawling date and the review<br>date|Numerical value (scale)|
||Review Photo|Number ofpictures included in the review|Numerical value (scale)|



<Table 4> shows descriptive statistics for the variables. The Amazon reviews collected use an average of 53 words and up to 1,888 words. The average day lapse is 764 days, and the review includes an average of 0.135 photos. The minimum and maximum number of review usefulness are 0 and 875 respectively, and 30,259 out of 41,258 reviews has a review usefulness value of 0. The average number of review usefulness votes is 2.622, whereas the standard deviation of review usefulness is 19.731, which is greater than the average. <u>Degree inconsistency has</u> a value of at least 0.001 to 10.694, and the average is 0.929. Direction inconsistency is denoted as 1 when the direction of the star rating and the sentiment of the review text are different, and 21,783 cases of the total data are included. Product awareness has an average of 497 reviews and up to 957 reviews. Review negativity has an average of -0.130, indicating 

that reviews generally express positive sentiment. This suggests an overall favorable attitude among reviewers toward the evaluated products or services. 

A correlation matrix is provided in <Table 5>. The correlation matrix helps identify potential multicollinearity issues, which are further addressed by variance inflation factor (VIF) analysis. The mean VIF is 1.21 and the highest VIF is 1.60, indicating a low level of multicollinearity among the predictors. Our model does not suffer from severe multicollinearity issues, thereby enhancing the reliability and stability of our regression estimates. 

## Ⅴ **. Data Analysis and Results** 

We employed a zero-inflated negative binomial (ZINB) regression to analyze the factors influencing 

Asia Pacific Journal of Information Systems 59 

Vol. 35 No. 1 

Beyond the Stars: The Impact of Rating-Text Inconsistency on Perceived Review Usefulness 

##### <Table 4> Descriptive Statistics of Variables 

|Variables|Number of<br>Reviews|Mean|SD|Min|Max|
|---|---|---|---|---|---|
|Review Usefulness|41,258|2.622|19.731|0|875|
|Content Inconsistency|41,258|0.929|0.678|0.001|10.694|
|Direction Inconsistency|41,258|0.461|0.498|0|1|
|Product Awareness|41,258|497.967|271.3656|2|957|
|Review Negativity|41,258|-0.130|0.252|-2.934|2.348|
|Word Count|41,258|53.410|71.168|0|1888|
|DayLapse|41,258|764.009|814.737|4|8242|
|Review Photo|41,258|0.135|0.597|0|17|



Note: Before taking the natural logarithm. 

<Table 5> Correlation Matrix 

|Variables|Review<br>Usefulness|Degree<br>Inconsistency|Direction<br>Inconsistency|Product<br>Awareness|Review<br>Negativity|Word Count|Day Lapse|
|---|---|---|---|---|---|---|---|
|Review Usefulness|1.000|||||||
|Degree<br>Inconsistency|0.041***|1.000||||||
|Direction<br>Inconsistency|0.021***|-0.379***|1.000|||||
|Product Awareness|-0.035***|-0.030***|0.007|1.000||||
|Review Negativity|0.004|-0.054***|-0.409***|-0.025***|1.000|||
|Word Count|0.119***|0.042***|0.087***|-0.041***|-0.044***|1.000||
|DayLapse|0.037***|-0.020***|-0.002|-0.034***|-0.052***|0.052***|1.000|
|Review Photo|0.110***|0.016***|0.027***|-0.009|-0.036***|0.153***|-0.042***|



Note: ***p < 0.001 

review usefulness. First, we considered count regression because our dependent variable is a count variable, the number of usefulness votes for reviews. We then chose the more suitable method between the Poisson regression and negative binomial regression. Poisson regression assumes that the variance of the dependent variable is equal to its mean, which can result in biased estimates when applied to over-dispersed data because it tends to underestimate the standard error of the regression coefficients (Cox, 1983). In our dataset, <u>the data ex-</u> 

hibited overdispersion with a variance (19.731) that markedly exceeded the mean (2.622). The value resulting from the likelihood ratio test of alpha was significantly different from zero, indicating that our dependent variables were overdispersed (Cameron and Trivedi, 2013; Long, 1997). Because the dependent variable has a substantially larger variance than its mean, the negative binomial regression model is judged to be more suitable than the Poisson regression model (Yang et al., 2019). Moreover, 73.7% of the observations (30,259 of 41,258) had a value 

60  Asia Pacific Journal of Information Systems 

Vol. 35 No. 1 

Boram Kwon, Junyeong Lee, Jinyoung Min, Chanhee Kwak, HanByeol Stella Choi 

<Table 6> Results of the ZINB Regression 

||Model 1|Model 2|Model 3|Model 4|Model 5|
|---|---|---|---|---|---|
|||Count model (N =|41,258)|||
|Word Count|0.444***<br>(0.051)|0.446***<br>(0.042)|0.449***<br>(0.041)|0.446***<br>(0.042)|0.450***<br>(0.040)|
|Day Lapse|-0.043<br>(0.044)|-0.024<br>(0.043)|-0.022<br>(0.043)|-0.023<br>(0.042)|-0.021<br>(0.042)|
|Review Photo|0.555***<br>(0.076)|0.593***<br>(0.068)|0.600***<br>(0.069)|0.594***<br>(0.068)|0.601***<br>(0.068)|
|Pd A|-0.014|-0.026|-0.040|-0.030|-0.042|
|rouct wareness|(0.039)|(0.038)|(0.038)|(0.036)|(0.037))|
|Review Negativity|0.313**<br>(0.120)|0.580***<br>(0.164)|0.554***<br>(0.160)|0.536**<br>(0.187)|0.530**<br>(0.184)|
|Degree Inconsistency|-|0.475***<br>(0.606)|0.521***<br>(0.070)|0.510***<br>(0.074)|0.562***<br>(0.086)|
|Direction Inconsistency|-|0.583***<br>(0.110)|0.591***<br>(0.117)|0.567***<br>(0.113)|0.562***<br>(0.121)|
|Degree Inconsistency ×<br>Product Awareness|||0.113**<br>(0.047)||0.114*<br>(0.048)|
|Direction Inconsistency ×|||0.196||-0.003|
|Product Awareness|||(0.084)||(0.082)|
|Degree Inconsistency ×<br>Review Negativity||||0.168†<br>(0.087)|0.154<br>(0.088)|
|Direction Inconsistency ×||||-0.053|-0.025|
|Review Negativity||||(0.218)|(0.227)|
|Ctt|-0.199|-1.030**|-1.029**|-1.035***|-1.045**|
|onsan|(0.383)|(0.381)|(0.389)|(0.370)|(0.380)|
|||Inflated model (N|= 30,256)|||
|Word Count|-0.685***<br>(0.033)|-0.685***<br>(0.032)|-0.687***<br>(0.032)|-0.677***<br>(0.031)|-0.677***<br>(0.032)|
|Day Lapse|-0.159***<br>(0.041)|-0.189***<br>(0.043)|-0.189***<br>(0.044)|0.199***<br>(0.042)|-0.199***<br>(0.042)|
||-0.297**|-0.269**|-0.267**|-0.264**|-0.262*|
|Review Photo|(0.101)|(0.099)|(0.100)|(0.100)|(0.103)|
|Product Awareness|0.683***<br>(0.046)|0.685***<br>(0.048)|0.664***<br>(0.049)|0.676***<br>(0.046)|0.659***<br>(0.047)|
||-1.219***|-2.744***|-2.768***|-2.554***|-2.563***|
|Review Negativity|(0.104)|(0.185)|(0.188)|(0.193)|(0.199)|



of zero, indicating a high frequency of zero outcomes. The Vuong test results (p < 0.001 for all models) also confirm that the ZINB model is more appropriate 

than the standard negative binomial model (Faraj et al., 2015; Long, 1997; Vuong, 1989). Given these characteristics, we concluded that it was appropriate 

Asia Pacific Journal of Information Systems 61 

Vol. 35 No. 1 

Beyond the Stars: The Impact of Rating-Text Inconsistency on Perceived Review Usefulness 

<Table 6> Results of the ZINB Regression (Cont.) 

||Model 1|Model 2|Model 3|Model 4|Model 5|
|---|---|---|---|---|---|
|Degree Inconsistency|-|-0.850***<br>(0.068)|-0.805***<br>(0.070)|-0.742***<br>(0.144)|-0.660***<br>(0.176)|
|Direction Inconsistency|-|-0.745**<br>(0.098)|-0.750*<br>(0.103)|-0.837***<br>(0.115)|-0.870***<br>(0.129)|
|Degree Inconsistency ×<br>Product Awareness|-||-0.057<br>(0.051)||-0.081<br>(0.060)|
|Direction Inconsistency ×|||0.356||0.037|
|<br>Product Awareness|-||(0.092)||(0.089)|
|Degree Inconsistency ×||||0.247|0.282|
|Review Negativity||||(0.282)|(0.343)|
|Direction Inconsistency ×||||1.091***|1.214**|
|Review Negativity||||(0.318)|(0.392)|
|Constant|-1.672***<br>(0.432)|-0.670<br>(0.445)|-0.586<br>(0.457)|-0.676***<br>(0.449)|-0.659<br>(0.499)|
|LogLikelihood|-50352.87|-49882.02|-49869.83|-49840.28|-49825.85|
|Waldχ²|133.64|350.54|362.56|366.30|371.70|



Notes: † < 0.1, * p < 0.05, ** p < 0.01, *** p < 0.001 Model 1: Vuong test of ZINB vs. standard negative binomial: z = 11.98 Pr>z = 0.0000 Model 2: Vuong test of ZINB vs. standard negative binomial: z =  13.72 Pr>z = 0.0000 Model 3: Vuong test of ZINB vs. standard negative binomial: z =  13.54 Pr>z = 0.0000 Model 4: Vuong test of ZINB vs. standard negative binomial: z =  14.21 Pr>z = 0.0000 Model 5: Vuong test of ZINB vs. standard negative binomial: z =  14.02 Pr>z = 0.0000 

to use a ZINB regression to test our hypotheses. Model 1 included the control variables, and as we progressed from Model 1 to Model 5, we observed how the inclusion of additional variables and interaction terms affected the relationships of interest (see <Table 6>). 

The results suggest that both inconsistencies are perceived as more useful. Subsequently, we observed a significant interaction between degree inconsistency and product awareness (β = 0.113, p < 0.01 in Model 3), indicating that the effect of degree inconsistency on usefulness is amplified when product awareness is high. However, the interaction between direction inconsistency and product awareness was not significant (β = 0.196, not significant). This finding suggests that the inconsistency does not depend 

on product awareness. Thus, Hypothesis 1 is partially supported. However, the interaction between degree inconsistency and review negativity showed a positive but marginal effect (β = 0.168, p = 0.053 in Model 4), indicating the effect of degree inconsistency on usefulness marginally strengthens when the review has high negative sentiment. The interaction between direction inconsistency and review negativity was insignificant (β = -0.053, n.s. in Model 4). These findings suggest that the effect of inconsistency on usefulness is marginally or insignificantly affected based on the negativity of the review. These results do not support hypothesis 2. Taken together, regarding the interaction effects, reviews with degree inconsistency are useful when product awareness and review negativity are high, whereas reviews with direc- 

62  Asia Pacific Journal of Information Systems 

Vol. 35 No. 1 

Boram Kwon, Junyeong Lee, Jinyoung Min, Chanhee Kwak, HanByeol Stella Choi 

tion inconsistency are not. 

The inflated ZINB model examines the factors influencing the probability of reviews receiving no usefulness votes. Our analysis indicates that a higher degree inconsistency and direction inconsistency, greater word count, the presence of photos, and more negative sentiments have a significantly lower probability of receiving no usefulness votes. This suggests that these characteristics increase the likelihood of a review being perceived as useful by at least a few users. Conversely, reviews of products with many existing reviews and reviews that have remained longer have a higher probability of receiving no usefulness votes, possibly because of the abundance of available information for these items, and thereby less attention. These findings complement our main results by identifying the factors that affect whether a review is considered useful by any user, rather than being entirely overlooked. Interestingly, the interaction between direction inconsistency and review negativity was positively significant, indicating that higher direction inconsistency has a higher probability of receiving no usefulness votes when the review has a more negative sentiment. 

## Ⅵ **. Discussion and Implications** 

### 6.1. Discussion of Findings 

This study examined the relationships between review inconsistency, usefulness, and contextual conditions. Based on an analysis of the ZINB model using 41,258 Amazon reviews, the results provide important insights into this relationship. Our findings demonstrate how various sub-dimensions of review inconsistency (degree and direction inconsistency) impact review usefulness under specific contextual 

conditions, considering product awareness and review negativity. 

First, our results show that both degree and direction inconsistencies positively affect review usefulness. The finding that inconsistencies between review text and star ratings can increase the usefulness of reviews challenges the vague expectation that consistency in reviews is preferred. Review inconsistency arouses consumers’ curiosity and encourages them to read more complex and organized product reviews. In this process, consumers resolve the uncertainty associated with inconsistent reviews and perceive them as useful. 

Second, our findings indicate a significant interaction between the degree inconsistency and product awareness. The effect of degree inconsistency on review usefulness is strengthened by product awareness. This may be because inconsistent reviews stand out more and may reveal new perspectives or hidden characteristics of the product amid many reviews with similar opinions, when there are many reviews. However, the interaction between direction inconsistency and product awareness was not significant. This indicates that direction inconsistency affects usefulness regardless of product awareness. The difference between the interaction effects of each degree inconsistency and direction inconsistency emphasizes the complexity of review inconsistency and its impact. 

Third, this study supports the findings of previous research by confirming that review negativity positively impacts usefulness. However, our results reject the hypothesis regarding the moderating effect of review negativity. This finding indicates that the effect of review inconsistency on usefulness is not significantly affected by review negativity, which suggests that the effects of review inconsistency and negativity on usefulness operate independently rather 

Asia Pacific Journal of Information Systems 63 

Vol. 35 No. 1 

Beyond the Stars: The Impact of Rating-Text Inconsistency on Perceived Review Usefulness 

than synergistically. 

### 6.2. Implications for Research and Practice 

This study has several implications. First, it improves our understanding of review inconsistency within a single review by decomposing review inconsistency into its direction and degree. In previous studies, review inconsistency has been defined and measured differently as either degree or direction inconsistency (Aghakhani et al., 2021; Shan et al., 2021). This study comprehensively examines these two subdimensions of inconsistency, which have been treated separately or as a single factor in previous studies, and provides evidence that the effects of the two types of inconsistency are different in the interaction process. Thus, this study suggests that the types of inconsistencies between star ratings and text sentiment can be distinguished and should be considered simultaneously. Furthermore, contrary to the assumption of previous studies that consistency in reviews is favored (Abedin et al., 2021; Aghakhani et al., 2021), our results show that inconsistencies between review text and star ratings can actually increase the usefulness of reviews under certain conditions. By analyzing the conditions under which inconsistent reviews can be useful, such as high product awareness, we improved our understanding of the mechanisms underlying the usefulness of inconsistent reviews. We believe that this will extend our understanding of the roles and effects of inconsistent reviews, and the dynamics of the review space as a whole. 

This study also applies curiosity theory to the context of online reviews. Curiosity theory is promising for understanding people’s information-seeking behaviors; however, it has not been studied extensively. Although there have been some applications in the 

digital space of email and news (Scacco and Muddiman, 2020; Wainer et al., 2011), we extend the applicability of this theory to the context of online reviews and e-commerce. It can be applied as a new and major theoretical lens to understand user behaviors in online review contexts, beyond the primary theoretical models that have been used, including elaboration likelihood models (Petty et al., 1986) and systematic-heuristic models (Chaiken, 1980). By using the theory of curiosity to confirm the existence and effectiveness of these inconsistencies, we contribute to our understanding of inconsistent reviews. 

Finally, our findings have implications for the literature on online review usefulness. Previous studies have primarily concentrated on the isolated effect of stars and text, when identifying their effect on review usefulness (Chen and Tseng, 2011; Korfiatis et al., 2012; Mudambi and Schuff, 2010). Star ratings provide a straightforward indication of overall satisfaction, whereas text provides detailed feedback on specific aspects of a product (Mudambi and Schuff, 2010). Although some studies have considered their interactive effects (Yin et al., 2016), the present study goes one step further. Beyond the simple interaction between star ratings and text reviews, we combine the two to derive and analyze a variable called review inconsistency. By quantifying the inconsistency between these two factors, the two types of review inconsistency variables can more accurately capture the complex consumer evolution process. Simply analyzing star ratings and text in isolation or in combination limits the ability to fully understand a consumer’s detailed assessment and experience. By exploring the effects of review inconsistency on review usefulness, considering both elements together, our findings can facilitate an understanding of review consumption mechanisms and conditions and the underlying decision-making process that informs purchasing 

64  Asia Pacific Journal of Information Systems 

Vol. 35 No. 1 

Boram Kwon, Junyeong Lee, Jinyoung Min, Chanhee Kwak, HanByeol Stella Choi 

decisions. 

Our findings have important implications for review platforms, companies, and users. First, inconsistent reviews are often viewed as errors or negligible information by platform designers and administrators. However, our findings show that inconsistent reviews can also be perceived as useful; therefore, it is important to pay attention to them. Additionally, platform administrators must ensure that inconsistent reviews do not misrepresent the intended review rating filter or review rating frequency to consumers. In particular, because most platforms sort reviews based on usefulness votes, there is a risk of biasing the review system if inconsistent reviews are read and rated as useful by consumers. Therefore, the two moderators examined in this study can support the management of review space by carefully examining the distribution of inconsistent reviews and how they are rated by consumers. 

Second, when companies utilize review data for analysis or decision-making, they mainly assume that star ratings and text sentiments are consistent. However, these implicit assumptions can lead to incorrect analytical results because review consistency exists, and review inconsistency can be considered useful depending on certain boundary conditions, as shown in this study. Therefore, our findings provide nuanced, evidence-based guidance for companies to effectively manage and respond to product reviews. 

Finally, our findings have important implications for users. Reading inconsistent reviews can provide useful information that is unavailable in other reviews. Therefore, by intentionally seeking inconsistent reviews, readers may reduce the time and cognitive resources required to search for and acquire information. In other words, review writers can intentionally write inconsistent reviews as a tactic to get 

their reviews read more often (Mudambi et al., 2014; Shan et al., 2021), and this can be empirically effective. 

### 6.3. Limitations and Future Research Directions 

This study focuses on review inconsistency and empirically confirms the conditions under which it positively affects review usefulness. However, addressing several limitations could improve and expand our findings. First, although we considered product awareness and review negativity as the conditions, we believe that it would be beneficial to further improve our understanding of inconsistent reviews by considering other factors such as reviewer characteristics (e.g., reputation) and product characteristics (e.g., product type). For example, a future research avenue would be a comparative analysis that considers the moderating effects of product characteristics, because the content of online reviews and reliance on them may vary significantly depending on product characteristics (e.g., experiential goods). The timing of a product release and the duration of its sales period may also significantly influence review usefulness. It would be beneficial for future research to consider factors such as product life cycle, release timing, and sales period to facilitate a more detailed analysis of the effect of review inconsistency. By controlling for these variables or considering them as moderators, researchers will be better positioned to accurately identify trends in review inconsistencies and their effects. Moreover, although this study considers review usefulness as the main dependent variable, utilizing other types of dependent variables (e.g., subsequent review ratings) would expand the understanding of review inconsistency and the review space in general. Finally, although this study was conducted using Amazon reviews, which have been used to 

Asia Pacific Journal of Information Systems 65 

Vol. 35 No. 1 

Beyond the Stars: The Impact of Rating-Text Inconsistency on Perceived Review Usefulness 

understand online reviews in many previous studies (Mudambi and Schuff, 2010), we believe that replicating this study on other platforms (in other countries) would increase the generalizability of the findings, because the effects may vary depending on the review platform and user characteristics. 

## **Acknowledgements** 

This work was supported by the Ministry of Education of the Republic of Korea and the National Research Foundation of Korea (NRF-2019S1A5A2A 03041910). 

## **<References>** 

- [1] Abedin, E., Mendoza, A., and Karunasekera, S. (2021). Exploring the moderating role of readers’ perspective in evaluations of online consumer reviews. Journal of Theoretical and Applied Electronic Commerce Research, 16(7), 3406–3424. https://doi.org/10.3390/jtaer16070184 

- [2] Aghakhani, N., Oh, O., Gregg, D. G., and Karimi, J. (2021). Online review consistency matters: An elaboration likelihood model perspective. Information Systems Frontiers, 23, 1287–1301. https://doi.org/ 10.1007/s10796-020-10030-7 

- [3] Almansour, A., Alotaibi, R., and Alharbi, H. (2022). Text-rating review discrepancy (TRRD): An integrative review and implications for research. Future Business Journal, 8, 1–15. https://doi.org/ 10.1186/s43093-022-00114-y 

- [4] Baccianella, S., Esuli, A., and Sebastiani, F. (2010). SentiWordNet 3.0: An enhanced lexical resource for sentiment analysis and opinion mining. In Proceedings of the Seventh International Conference on Language Resources and Evaluation (LREC'10) (pp. 2200–2204). Valletta, Malta: European Language Resources Association (ELRA). 

- [5] Baek, H. M., Ahn, J. H., and Choi, Y. S. (2012). Helpfulness of online consumer reviews: Readers’ objectives and review cues. International Journal of Electronic Commerce, 17(2), 99–126. https:// doi.org/10.2753/JEC1086-4415170204 

- [6] Baumeister, R. F., Bratslavsky, E., Finkenauer, C., and Vohs, K. D. (2001). Bad is stronger than good. Review of General Psychology, 5(4), 323–370. https://doi.org/10.1037/1089-2680.5.4.323 

- [7] Berlyne, D. E. (1955). The arousal and satiation of perceptual curiosity in the rat. Journal of Comparative and Physiological Psychology, 48(4), 238–246. https://doi.org/10.1037/h0042968 

- [8] Berlyne, D. E. (1960). Conflict, Arousal, and Curiosity. McGraw-Hill Book Company. 

- [9] Bohner, G., Moskowitz, G. B., and Chaiken, S. (1995). The interplay of heuristic and systematic processing of social information. European Review of Social Psychology, 6(1), 33–68. https://doi.org/10.1080/147 92779443000003 

- [10] Bollen, J., Mao, H., and Pepe, A. (2021). Modeling public mood and emotion: Twitter sentiment and socio-economic phenomena. In Proceedings of the International AAAI Conference on Web and Social Media, 5(1), 450–453. https://doi.org/10.1609/icwsm. v5i1.14171 

- [11] Boyd, R. L. (2017). Psychological text analysis in the digital humanities. In S. Hai-Jew (Ed.), Data Analytics in Digital Humanities (pp. 161–189). Springer International Publishing. 

- [12] Cameron, A. C., and Trivedi, P. K. (2013) Regression Analysis of Count Data. Cambridge, UK: Cambridge University Press. 

- [13] Cao, Q., Duan, W., and Gan, Q. (2011). Exploring determinants of voting for the “helpfulness” of online user reviews: A text mining approach. Decision Support Systems, 50(2), 511–521. https://doi.org/10. 1016/j.dss.2010.11.009 

- [14] Chaiken, S. (1980). Heuristic versus systematic information processing and the use of source versus message cues in persuasion. Journal of personality 

66  Asia Pacific Journal of Information Systems 

Vol. 35 No. 1 

Boram Kwon, Junyeong Lee, Jinyoung Min, Chanhee Kwak, HanByeol Stella Choi 

   - and social psychology, 39(5), 752. https://doi.org/ 10.1037/0022-3514.39.5.752 

- [15] Chen, C. C., and Tseng, Y. D. (2011). Quality evaluation of product reviews using an information quality framework. Decision Support Systems, 50(4), 755–768. https://doi.org/10.1016/j.dss.2010.08.023 

- [16] Cheung, C. M. Y., Sia, C. L., and Kuan, K. K. Y. (2012). Is this review believable? A study of factors affecting the credibility of online consumer reviews from an ELM perspective. Journal of the Association for Information Systems, 13(8), 618–635. https://doi. org/10.17705/1jais.00305 

- [17] Chua, A. Y. K., and Banerjee, S. (2015). Understanding review helpfulness as a function of reviewer reputation, review rating, and review depth. Journal of the Association for Information Science and Technology, 66(2), 354–362. https://doi.org/10. 1002/asi.23180 

- [18] Chua, A. Y. K., and Banerjee, S. (2016). Helpfulness of user-generated reviews as a function of review sentiment, product type and information quality. Computers in Human Behavior, 54, 547–554. https://doi.org/10.1016/j.chb.2015.08.057 

- [19] Chung, H. C., Lee, H. A., Koo, C. M., and Chung, N. H. (2017). Which is more important in online review usefulness, heuristic or systematic cue?. In Proceedings of the International Conference in Information and Communication Technologies in Tourism 2017. Rome, Italy, Springer International Publishing, 581–594. 

- [20] Choi, H. S., and Leon, S. (2020). An empirical investigation of online review helpfulness: A big data perspective. Decision Support Systems, 139, 113403. https://doi.org/10.1016/j.dss.2020.113403 

- [21] Collins, R. P., Litman, J. A., and Spielberger, C. D. (2004). The measurement of perceptual curiosity. Personality and Individual Differences, 36(5), 1127– 1141. https://doi.org/10.1016/S0191-8869(03)00205-8 

- [22] Cox, D. R. (1983). Some remarks on overdispersion. Biometrika, 70(1), 269–274. https://doi.org/10.2307/ 2335966 

- [23] Faraj, S., Kudaravalli, S., and Wasko, M. (2015) 

   - Leading collaboration in online communities. MIS Quarterly, 39(2), 393–412. https://doi.org/10.25300/ MISQ/2015/39.2.09 

- [24] Fazzolari, M., Cozza, V., Petrocchi, M., and Spognardi, A. (2017). A study on text-score disagreement in online reviews. Cognitive Computation, 9(5), 689–701. https://doi.org/10.10 07/s12559-017-9496-y 

- [25] Filieri, R., Raguseo, E., and Vitari, C. (2018). When are extreme ratings more helpful? Empirical evidence on the moderating effects of review characteristics and product type. Computers in Human Behavior, 88, 134–142. https://doi.org/10.1016/j.chb.2018.05. 042 

- [26] Fu, B., Lin, J., Li, L., Faloutsos, C., Hong, J., and Sadeh, N. (2013). Why people hate your app: Making sense of user feedback in a mobile app store. In Proceedings of the 19th ACM SIGKDD International Conference on Knowledge Discovery and Data Mining (pp. 1276–1284). 

- [27] Geetha, M., Singha, P., and Sinha, S. (2017). Relationship between customer sentiment and online customer ratings for hotels-An empirical analysis. Tourism Management, 61, 43–54. https://doi.org/ 10.1016/j.tourman.2016.12.022 

- [28] Geierhos, M., Bäumer, F., Schulze, S., and Stuß, V. (2015). “I grade what I get but write what I think.” Inconsistency analysis in patients’ reviews. In Proceedings of the 23rd European Conference on Information Systems (ECIS) (pp. 1–15). 

- [29] Ghose, A., and Ipeirotis, P. G. (2010). Estimating the helpfulness and economic impact of product reviews: Mining text and reviewer characteristics. IEEE Transactions on Knowledge and Data Engineering, 23(10), 1498–1512. https://doi.org/10. 1109/TKDE.2010.188 

- [30] Golman, R., and Loewenstein, G. (2015). Curiosity, information gaps, and the utility of knowledge. Decision, 5(3), 143–164. https://doi.org/10.1037/dec 0000068 

- [31] Gottlieb, J., and Oudeyer, P. Y. (2018). Towards a neuroscience of active sampling and curiosity. 

Asia Pacific Journal of Information Systems 67 

Vol. 35 No. 1 

Beyond the Stars: The Impact of Rating-Text Inconsistency on Perceived Review Usefulness 

   - Nature Reviews Neuroscience, 19(12), 758–770. https://doi.org/10.1038/s41583-018-0078-0 

- [32] Hazarika, B., Chen, K., and Razi, M. (2021). Are numeric ratings true representations of reviews? A study of inconsistency between reviews and ratings. International Journal of Business Information Systems, 38(1), 85–106. https://doi.org/10.1504/IJBIS. 2021.118637 

- [33] Hill, K. M., Fombelle, P. W., and Sirianni, N. J. (2016). Shopping under the influence of curiosity: How retailers use mystery to drive purchase motivation. Journal of Business Research, 69(3), 1028 –1034. https://doi.org/10.1016/j.jbusres.2015.08.015 

- [34] Hong, H., Xu, D., Wang, G. A., and Fan, W. (2017). Understanding the determinants of online review helpfulness: A meta-analytic investigation. Decision Support Systems, 102, 1–11. https://doi.org/10.1016/j. dss.2017.06.007 

- [35] Hu, N., Pavlou, P. A., and Zhang, J. (2009). Why do online product reviews have a J-shaped distribution? Overcoming biases in online wordof-mouth communication. Communications of the ACM, 52(10), 144–147. http://doi.org/10.2139/ssrn. 2380298 

- [36] Hu, N., Pavlou, P. A., and Zhang, J. (2017). On self-selection biases in online product reviews. MIS Quarterly, 41(2), 449–475. http://doi.org/10.25300/ MISQ/2017/41.2.06 

- [37] Hu, Y. H., and Chen, K. (2016). Predicting hotel review helpfulness: The impact of review visibility, and interaction between hotel stars and review ratings. International Journal of Information Management, 36(6), 929–944. https://doi.org/10.10 16/j.ijinfomgt.2016.06.003 

- [38] Islam, M. R. (2014). Numeric rating of Apps on Google Play Store by sentiment analysis on user reviews. In 2014 International Conference on Electrical Engineering and Information & Communication Technology (IEEE), Dhaka, Bangladesh. 

- [39] Jabr, W., and Rahman, M. S. (2022). Online reviews and information overload: The role of selective, 

   - parsimonious, and concordant top reviews. MIS Quarterly, 46(3), 1517–1550. http://doi.org/10.2139/ ssrn.3200803 

- [40] Jin, W., Chen, Y., Yang, S., Zhou, S., Jiang, H., and Wei, J. (2023). Personalized managerial response and negative inconsistent review helpfulness: The mediating effect of perceived response helpfulness. Journal of Retailing and Consumer Services, 74, 103398. https://doi.org/10.1016/j.jretconser.2023.10 3398 

- [41] Kidd, C., and Hayden, B. Y. (2015). The psychology and neuroscience of curiosity. Neuron, 88(3), 449– 460. https://doi.org/10.1016/j.neuron.2015.09.010 

- [42] Kim, Y. J., and Hollingshead, A. B. (2015). Online social influence: Past, present, and future. Annals of the International Communication Association, 39, 163–192. https://doi.org/10.1080/23808985.2015. 11679175 

- [43] Korfiatis, N., García-Bariocanal, E., and SánchezAlonso, S. (2012). Evaluating content quality and helpfulness of online product reviews: The interplay of review helpfulness vs. review content. Electronic Commerce Research and Applications, 11(3), 205– 217. https://doi.org/10.1016/j.elerap.2011.10.003 

- [44] Laran, J., and Tsiros, M. (2013). An investigation of the effectiveness of uncertainty in marketing promotions involving free gifts. Journal of Marketing, 77(2), 112–123. https://doi.org/10.1509/ jm.11.025 

- [45] Lee, M. W., Jeong, M. Y., and Lee, J. S. (2017). Roles of negative emotions in customers’ perceived helpfulness of hotel reviews on a user-generated review website: A text mining approach. International Journal of Contemporary Hospitality Management, 29(2), 762–783. https://doi.org/10.11 08/IJCHM-10-2015-0626 

- [46] Lee, S. Y., Lee, S. R., and Baek, H. M. (2021). Does the dispersion of online review ratings affect review helpfulness?. Computers in Human Behavior, 117, 106670. https://doi.org/10.1016/j.chb.2020.106670 

- [47] Litman, J. (2005). Curiosity and the pleasures of learning: Wanting and liking new information. Cogni 

68  Asia Pacific Journal of Information Systems 

Vol. 35 No. 1 

Boram Kwon, Junyeong Lee, Jinyoung Min, Chanhee Kwak, HanByeol Stella Choi 

tion and Emotion, 19(6), 793–814. https://doi.org/10. 1080/02699930541000101 

- [48] Litman, J. A., and Jimerson, T. L. (2004). The measurement of curiosity as a feeling of deprivation. Journal of Personality Assessment, 82(2), 147–157. https://doi.org/10.1207/s15327752jpa8202_3 

- [49] Liu, Q. B., and Karahanna, E. (2017). The dark side of reviews. MIS quarterly, 41(2), 427–448. https://www.jstor.org/stable/26629721 

- [50] Loewenstein, G. (1994). The psychology of curiosity: A review and reinterpretation. Psychological Bulletin, 116(1), 75–98. https://doi.org/10.1037/00 33-2909.116.1.75 

- [51] Long, J. S. (1997). Regression Models for Categorical and Limited Dependent Variables. Thousand Oaks, CA: Sage Publications. 

- [52] Menon, S., and Soman, D. (2002). Managing the power of curiosity for effective web advertising strategies. Journal of Advertising, 31(3), 1–14. https://doi.org/10.1080/00913367.2002.10673672 

- [53] Mudambi, S. M., and Schuff, D. (2010). What makes a helpful online review? A study of customer reviews on Amazon. com. MIS Quarterly, 34(1), 185–200. https://doi.org/10.2307/20721420 

- [54] Mudambi, S. M., Schuff, D., and Zhang, Z. (2014). Why aren't the stars aligned? An analysis of online review content and star ratings. In System Sciences (HICSS) 2014 47th Hawaii International Conference (pp. 3139–3147). IEEE. 

- [55] Mussel, P. (2010). Epistemic curiosity and related constructs: Lacking evidence of discriminant validity. Personality and Individual Differences, 49(5), 506– 510. https://doi.org/10.1016/j.paid.2010.05.014 

- [56] Nazlan, N. H., Tanford, S., and Montgomery, R. (2018). The effect of availability heuristics in online consumer reviews. Journal of Consumer Behaviour, 17(5), 449–460. https://doi.org/10.1002/cb.1731 

- [57] Park, C., and Lee, T. M. (2009). Information direction, website reputation and eWOM effect: A moderating role of product type. Journal of Business Research, 62(1), 61–67. https://doi.org/10.1016/j. jbusres.2007.11.017 

- [58] Park, D. H., and Kim, S. (2008). The effects of consumer knowledge on message processing of electronic word-of-mouth via online consumer reviews. Electronic Commerce Research and Applications, 7(4), 399–410. https://doi.org/10.1016/ j.elerap.2007.12.001 

- [59] Pavlou, P. A., and Dimoka, A. (2006). The nature and role of feedback text comments in online marketplaces: Implications for trust building, price premiums, and seller differentiation. Information Systems Research, 17(4), 392–414. https://doi.org/10. 1287/isre.1060.0106 

- [60] Petty, R. E., Cacioppo, J. T., Petty, R. E., and Cacioppo, J. T. (1986). The elaboration likelihood model of persuasion (pp. 1–24). Springer New York. 

- [61] Qahri-Saremi, H., and Montazemi, A. R. (2019). Factors affecting the adoption of an electronic word of mouth message: A meta-analysis. Journal of Management Information Systems, 36(3), 969–1001. https://doi.org/10.1080/07421222.2019.1628936 

- [62] Racherla, P., and Friske, W. (2012). Perceived ‘usefulness’ of online consumer reviews: An exploratory investigation across three services categories. Electronic Commerce Research and Applications, 11(6), 548–559. https://doi.org/10.10 16/j.elerap.2012.06.003 

- [63] Rozin, P., and Royzman, E. B. (2001). Negativity bias, negativity dominance, and contagion. Personality and Social Psychology Review, 5(4), 296– 320. https://doi.org/10.1207/S15327957PSPR0504 

- [64] Scacco, J. M., and Muddiman, A. (2020). The curiosity effect: Information seeking in the contemporary news environment. New Media & Society, 22(3), 429–448. https://doi.org/10.1177/146 1444819863408 

- [65] Sen, S., and Lerman, D. (2007). Why are you telling me this? An examination into negative consumer reviews on the web. Journal of Interactive Marketing, 21(4), 76–94. https://doi.org/10.1002/dir.20090 

- [66] Shan, G., Zhang, D., Zhou, L., Suo, L., Lim, J., and Shi, C. (2018). Inconsistency investigation between online review content and ratings. In Twenty-fourth 

Asia Pacific Journal of Information Systems 69 

Vol. 35 No. 1 

Beyond the Stars: The Impact of Rating-Text Inconsistency on Perceived Review Usefulness 

Americas Conference on Information Systems. 

- [67] Shan, G., Zhou, L., and Zhang, D. (2021). From conflicts and confusion to doubts: Examining review inconsistency for fake review detection. Decision Support Systems, 144, 113513. https://doi.org/10. 1016/j.dss.2021.113513 

- [68] Shoemaker, P. J., Chang, T. K., and Brendlinger, N. (1987). Deviance as a predictor of newsworthiness: Coverage of international events in the U.S. media. In M. L. McLaughlin (Ed.), Communication Yearbook 10 (1st ed., pp. 348–365). Beverly Hills, CA: Sage. 

- [69] Siering, M., Muntermann, J., and Rajagopalan, B. (2018). Explaining and predicting online review helpfulness: The role of content and reviewer-related signals. Decision Support Systems, 108, 1–12. https://doi.org/10.1016/j.dss.2018.01.004 

- [70] Singh, A., and Manjaly, J. A. (2021). The effect of information gap and uncertainty on curiosity and its resolution. Journal of Cognitive Psychology, 33(4), 403–423. https://doi.org/10.1080/20445911.2021.19 08311 

- [71] Singh, J. P., Irani, S., Rana, N. P., Dwivedi, Y. K., Saumya, S., and Roy, P. K. (2017). Predicting the “helpfulness” of online consumer reviews. Journal of Business Research, 70, 346–355. https://doi.org/ 10.1016/j.jbusres.2016.08.008 

- [72] Smith, R. E., and Swinyard, W. R. (1988). Cognitive response to advertising and trial: Belief strength, belief confidence and product curiosity. Journal of Advertising, 17(3), 3–14. https://doi.org/10.1080/009 13367.1988.10673118 

- [73] Smith, S. M., Fabrigar, L. R., and Norris, M. E. (2008). Reflecting on six decades of selective exposure research: Progress, challenges, and opportunities. Social and Personality Psychology Compass, 2(1), 464–493. https://doi.org/10.1111/j.1751-9004.2007. 00060.x 

- [74] Steur, A. J., Fritzsche, F., and Seiter, M. (2022). It's all about the text: An experimental investigation of inconsistent reviews on restaurant booking platforms. Electronic Markets, 32, 1187–1220. 

https://doi.org/10.1007/s12525-022-00525-3 

- [75] Tausczik, Y. R., and Pennebaker, J. W. (2010). The psychological meaning of words: LIWC and computerized text analysis methods. Journal of Language and Social Psychology, 29(1), 24–54. https://doi.org/10.1177/0261927X09351676 

- [76] Tsang, A. S. L., and Prendergast, G. (2009). Is a “star” worth a thousand words? The interplay between product‐review texts and rating valences. European Journal of Marketing, 43(11/12), 1269– 1280. https://doi.org/10.1108/03090560910989876 

- [77] Valdivia, A., Hrabova, E., Chaturvedi, I., Luzón, M. V., Troiano, L., Cambria, E., and Herrera, F. (2019). Inconsistencies on TripAdvisor reviews: A unified index between users and Sentiment Analysis Methods. Neurocomputing, 353, 3–16. https://doi. org/10.1016/j.neucom.2018.09.096 

- [78] Verhagen, T., Nauta, A., and Feldberg, F. (2013). Negative online word-of-mouth: Behavioral indicator or emotional release?. Computers in Human Behavior, 29(4), 1430–1440. https://doi.org/10.10 16/j.chb.2013.01.043 

- [79] Von Stumm, S., Hell, B., and Chamorro-Premuzic, T. (2011). The hungry mind: Intellectual curiosity is the third pillar of academic performance. Perspectives on Psychological Science, 6(6), 574–588. https://doi.org/10.1177/1745691611421204 

- [80] Vuong Q. H. (1989) Likelihood ratio tests for model selection and non-nested hypotheses. Econometrica, 57(2), 307–333. https://doi.org/10.2307/1912557 

- [81] Wainer, J., Dabbish, L., and Kraut, R. (2011). Should I open this email? Inbox-level cues, curiosity and attention to email. In Proceedings of the SIGCHI conference on Human Factors in Computing Systems (pp. 3439–3448). https://doi.org/10.1145/ 1978942.1979456 

- [82] Wang, Y., Ngai, E. W. T., and Li, K. (2023) The effect of review content richness on product review helpfulness: The moderating role of rating inconsistency. Electronic Commerce Research and Applications, 61, 101290. https://doi.org/10.1016/ j.elerap.2023.101290 

70  Asia Pacific Journal of Information Systems 

Vol. 35 No. 1 

Boram Kwon, Junyeong Lee, Jinyoung Min, Chanhee Kwak, HanByeol Stella Choi 

- [83] Yang, S., Zhou, Y., Yao, J., Chen, Y., and Wei, J. (2019). Understanding online review helpfulness in omnichannel retailing. Industrial Management & Data Systems, 119(8), 1565–1580. https://doi.org/10. 1108/IMDS-10-2018-0450 

- [84] Ye, Q., Law, R., and Gu, B. (2009). The impact of online user reviews on hotel room sales. International Journal of Hospitality Management, 28(1), 180–182. https://doi.org/10.1016/j.ijhm.2008. 06.011 

- [85] Yin, D., Mitra, S., and Zhang, H. (2016). Research Note: When do consumers value positive vs. negative reviews? An empirical investigation of confirmation bias in online word of mouth. Information Systems Research, 27(1), 131–144. https://doi.org/10.1287/ isre.2015.0617 

- [86] Zhang, Y., and Lin, Z. (2018). Predicting the helpfulness of online product reviews: A multilingual approach. Electronic Commerce Research and Applications, 27, 1–10. https://doi.org/10.1016/j. elerap.2017.10.008 

- [87] Zhang, X., Zhang, X., Liang, S., Yang, Y., and Law, R. (2023). Infusing new insights: How do review novelty and inconsistency shape the usefulness of online travel reviews?. Tourism Management, 96, 104703. https://doi.org/10.1016/j.tourman.2022.104 703 

- [88] Zhu, F., and Zhang, X. (2010). Impact of online consumer reviews on sales: The moderating role of product and consumer characteristics. Journal of Marketing, 74(2), 133–148. https://doi.org/10.15 09/jm.74.2.133 

Asia Pacific Journal of Information Systems 71 

Vol. 35 No. 1 

Beyond the Stars: The Impact of Rating-Text Inconsistency on Perceived Review Usefulness 

## ◆ **About the Authors** ◆ 



##### **Boram Kwon** 

<mark>Boram Kwon</mark> is an assistant professor in the College of Business at Chosun University. She received her Ph.D. in the College of Business Administration at the <mark>Seoul National University. Her research interests include digital strategy, business analytics and human behavior in information systems. Her research articles have been published in academic journals, including International Journal of Human–Computer Interaction, Information Technology for Development and Journal of Computer Information Systems.</mark> 



##### **Junyeong Lee** 

<mark>Junyeong Lee is an associate professor in Department of Management Information Systems at Chungbuk National University, Korea.</mark> He received his Ph.D. in Management Engineering at the KAIST. His research <mark>interests include collective dynamics and human behavior in information systems. His work has appeared</mark> in academic journals including Journal of Management Information Systems, Journal of the Association for Information Systems, Journal of Business Ethics, Strategic Organization, International Journal of Information Management, and Communications of the ACM. 



##### **Jinyoung Min** 

<mark>Jinyoung Min is an associate professor at the College of Business & Economics at Chung-Ang University, South Korea. She received her Ph.D. in Management Engineering at the Korea Advanced Institute of Science and Technology (KAIST). Her research interests include data privacy, social media, and algorithmic automation. Her research articles have been published in academic journals, including Computers in Human Behavior, Journal of the Association for Information Science and Technology, International Journal of Information Management,</mark> and Communications of the ACM. 



##### **Chanhee Kwak** 

Chanhee Kwak is an assistant professor in the Department of Artificial Intelligence Convergence, Kangnam University. He received his Ph.D. in Management Engineering at KAIST. His research interests include data analytics and human interactions with IT artifacts. His research has been published in academic journals including Journal of Management Information Systems, Journal of Business Ethics, Communications of the ACM, International Journal of Information Management, and Journal of Knowledge Management. 



##### **HanByeol Stella Choi** 

<mark>HanByeol Stella Choi is an assistant professor in Department of Management Information Systems, Myongji University. She received her Ph.D. in Management Engineering from the College of Business at KAIST. Her research interest includes business analytics, privacy, information security, and societal impact of information systems. Her research has been published in academic journals including Journal of Management Information Systems, Decision Support Systems, Security Journal and Communications of the ACM.</mark> 

Submitted: September 1, 2024; 1st Revision: December 13, 2024; Accepted: January 15, 2025 

72  Asia Pacific Journal of Information Systems 

Vol. 35 No. 1 

