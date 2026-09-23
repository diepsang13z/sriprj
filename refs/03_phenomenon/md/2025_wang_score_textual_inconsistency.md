International Journal of Hospitality Management 130 (2025) 104271 



Contents lists available at ScienceDirect 

# International Journal of Hospitality Management 

journal homepage: www.elsevier.com/locate/ijhm 



### Full length article 

## Beyond the stars: Unpacking the impact of score-textual inconsistency of online reviews on hotel performance 



Ping Wang<sup>a,1</sup> , Hailin Zhang<sup>b,1</sup> , Xina Yuan<sup>a,1,*</sup> , Xiulin Zhang<sup>c</sup> 

a _Marketing Department, School of Management, Xiamen University, 422 Siming South Road, Xiamen, Fujian 361005, China_ b _School of Cultural Industries and Tourism, Xiamen University of Technology, No.600 Ligong Road, Xiamen, Fujian 361024, China_ c _Huawei Technologies Co., Ltd., Huawei Base, Bantian, Longgang District, Shenzhen 518129, China_ 

A R T I C L E I N F O A B S T R A C T _Keywords:_ Online reviews Score-textual inconsistency Heuristic-systematic model Schema incongruity theory Hotel performance 

Merchants often implement strategies to secure high ratings for their products. However, consumers consider more than just rating scores, placing significant emphasis on the sentiment conveyed in review texts when making purchase decisions. This study examines the nuanced interplay between product rating, review inconsistency (i.e., high review scores paired with low textual sentiments), and product sales. Analysing a dataset of 299,975 online reviews from 300 hotels on Ctrip.com, the findings indicate that while product rating is positively associated with product sales, review inconsistency exerts a negative impact. Additionally, this research highlights the moderating roles of reviewer anonymity, image number, and managerial response in these relationships. The results suggest that consumers engage in both heuristic and systematic processing modes when evaluating online reviews. 

#### **1. Introduction** 

In the contemporary landscape of digital commerce, the significance of online consumer reviews has grown substantially, becoming a crucial determinant of purchasing behaviours (Nielsen, 2015). A large majority of online shoppers (87 %) research their purchases online, with 77 % specifically seeking out websites that provide ratings and reviews (PowerReviews, 2023). This trend is even more critical in the tourism and hospitality sector, given the intangible and uncertain nature of its offerings (Liu and Park, 2015). Existing literature confirms that positive reviews significantly enhance customer trust, brand perception, and financial performance (Sparks and Browning, 2011; Ye et al., 2009). For instance, Anderson and Magruder (2012) demonstrated that a marginal increase of half a star in online ratings can lead to a 19 % rise in restaurant bookings. 

Recognizing the crucial role of online reviews, businesses have adopted various strategies to improve their online image and reputation, often focusing on boosting rating scores (Costa et al., 2019). Some establishments even resort to artificially inflating their rating scores to increase consumer engagement and profitability (Zhang et al., 2022). However, such strategies frequently neglect the qualitative aspects of reviews. Despite emphasizing numerical rating scores, the sentiment 

conveyed in review texts does not always align with these scores (Bigne et al., 2023). For example, Wu et al. (2024) reported that over 40 % of data exhibit inconsistencies between sentiment polarity and rating scores. For various reasons, consumers may leave high review scores accompanied by negative feedback or vice versa (McGregor, 2019; Kassem et al., 2024). This discrepancy suggests that rating scores alone may not provide a comprehensive indicator of customer feedback, raising an essential question: Are high rating scores sufficient by themselves? The phenomenon of high rating scores paired with low content sentiments challenges conventional views on the efficacy of high ratings and underscores the need for businesses and researchers to investigate review mechanisms more deeply. 

To the best of our knowledge, the impact of score-textual inconsistency on potential consumers has not been comprehensively explored. Previous research has focused primarily on (1) the impact of such discrepancy on the performance of fake review detection algorithms (Shan et al., 2021); (2) the interaction between review text and star ratings in influencing product demand (Cho et al., 2022); and (3) how review inconsistency moderates the relationship between personalized managerial responses and consumer perceptions (Jin et al., 2023). However, there remains a gap in understanding the specific influence of high rating scores paired with low textual sentiments on product sales, 

* Corresponding author. 

_E-mail addresses:_ pingwang@stu.xmu.edu.cn (P. Wang), zhang@xmut.edu.cn (H. Zhang), zinayuan@xmu.edu.cn (X. Yuan), a2016112651@163.com (X. Zhang). 

> 1 These authors are co-first authors who equally contributed to this work. 

https://doi.org/10.1016/j.ijhm.2025.104271 

Received 25 April 2024; Received in revised form 19 November 2024; Accepted 4 May 2025 Available online 12 May 2025 

0278-4319/© 2025 Elsevier Ltd. All rights are reserved, including those for text and data mining, AI training, and similar technologies. 

_International Journal of Hospitality Management 130 (2025) 104271_ 

_P. Wang et al._ 

particularly in the context of tourism management. Addressing this gap is essential for comprehending the implications of score-textual inconsistency for market performance. 

In the realm of online tourism reviews, the heuristic-systematic model explains that consumers use a dual-processing approach. They rely not only on heuristic cues, such as product ratings but also on detailed analysis of review texts to evaluate the overall impact of these elements (Park and Nicolau, 2015; Zhao et al., 2019). While numerical rating scores serve as initial heuristic cues indicating product or service quality, review texts offer in-depth information, enabling consumers to form more well-rounded evaluations (Dhar and Bose, 2022; Shan et al., 2021). These texts capture genuine consumer experiences and detailed judgments, which numerical ratings alone cannot convey (Taecharungroj and Mathayomchan, 2019). Schema incongruity theory, which posits that conflicting information can create cognitive dissonance, helps explain the impact of encountering reviews with high rating scores paired with low content sentiments. This discrepancy between expected (high rating scores) and actual (low textual sentiments) information disrupts cognitive processing fluency, making it more difficult for consumers to interpret and positively assess the information. Consequently, these inconsistencies can lead to adverse evaluations, delaying or even deterring purchasing decisions. This underscores the importance of consistency between review scores and review text to facilitate smoother information processing and more favourable consumer responses. 

Our study makes three key contributions to the hospitality marketing field. First, we precisely define score-textual inconsistent reviews and employ natural language processing and machine learning for sentiment analysis to examine their impact on hotel room sales. To our knowledge, this is among the first empirical studies to investigate this specific inconsistency. Second, by integrating theories from consumer information processing, such as the heuristic-systematic model and schema incongruity theory, along with concepts of cognitive dissonance and cognitive processing fluency, we present a comprehensive framework for understanding online reviews in the hospitality industry. Third, we analyse the moderating effects of reviewer anonymity, image number, and managerial response, revealing boundary conditions that influence how product rating and review inconsistency impact hotel sales. Our study not only sheds light on these complex dynamics but also offers practical insights for businesses to refine their strategies and improve their competitive advantage in the hospitality market. 

#### **2. Literature review** 

#### _2.1. Review inconsistency_ 

The concept of review inconsistency has been extensively examined in recent studies, confirming its widespread presence in online reviews (Valdivia et al., 2019). Scholars have employed various terms to describe this phenomenon, such as review incoherence (Yin et al., 2023), misalignment (Bigne et al., 2023), review discrepancy (Sadiq et al., 2021), conflicting reviews (Siddiqi et al., 2020), review incongruence (Hong and Pittman, 2020), and review disagreement (Fazzolari et al., 2017). Review inconsistency can generally be categorized into external inconsistency—where a review’s information conflicts with other reviews (Choi et al., 2023; Yin et al., 2023)—and internal inconsistency, which occurs when there are conflicting elements within a single review (Wang et al., 2021). Specifically, various forms of inconsistency among review text, ratings, and images have been explored, such as topic alignment between review texts (Aghakhani et al., 2023; Kim et al., 2023; Zhou et al., 2023), rating variations (Lee et al., 2021; Ying et al., 2023), mismatches between rating scores and textual content (Jin et al., 2023; Li et al., 2024), and inconsistencies between review text and images (Liu et al., 2024; Yang et al., 2023). This study focuses on internal inconsistency, specifically Score-Textual Inconsistency, where a high rating score conflicts with a low textual sentiment. 

To investigate review inconsistency, researchers have utilized a range of methods, including secondary data analysis, surveys, and experiments (Jin et al., 2023; Siddiqi et al., 2020). Sentiment analysis, particularly lexicon-based sentiment classifiers, has been widely used to assess sentiment in review texts (Geetha et al., 2017; Shan et al., 2021). More recently, machine learning models, particularly deep learning techniques, have become prominent for analysing sentiment because of their superior ability to recognize contextual nuances and specific situations (Cho et al., 2022). These advanced methods have proven highly effective in identifying sentiment inconsistencies, especially in large datasets from tourism platforms (Luo and Xu, 2021). For example, when deep learning is combined with natural language processing, Bigne et al. (2023) demonstrated that sentiment valence in the tourism reviews of Venice attractions does not always align with star ratings. 

The implications of review inconsistency, as documented in the literature, are significant and primarily affect experience evaluation, review helpfulness, and purchase intention (Aghakhani et al., 2021; Kim et al., 2023; Li et al., 2023). Two main perspectives have emerged. One argues that review inconsistency undermines perceived credibility (Chakraborty, 2019; Hong and Pittman, 2020), fosters ambivalence (Akhtar et al., 2019; Wang et al., 2021), and increases cognitive processing costs (Yang et al., 2021). For example, Wang et al. (2021) found that discrepancies between primary and supplementary reviews reduce purchase intention by creating ambivalence. The opposing view suggests that inconsistency can have positive effects, offering higher informational value (Hung et al., 2023) and appealing to individuals’ interest in deviations (Choi et al., 2023). Cultural factors, such as a preference for individualism, also play a role in how consumers perceive and accept inconsistency (Aghakhani et al., 2021). For instance, Choi et al. (2023) analysed 514,929 job reviews and reported that internal inconsistency positively correlates with review helpfulness, whereas external inconsistency has a negative relationship. Beyond these two streams, Liu et al. (2024) further demonstrated a nonlinear, inverted U-shaped relationship between consistency (i.e., between photo and review text) and tourist ratings, suggesting that a moderate level of inconsistency may enhance consumer evaluations. 

Despite advancements in understanding review inconsistency, several critical gaps remain. First, most research has focused either on rating inconsistency or text inconsistency. The heuristic-systematic model suggests that examining score-textual inconsistency can provide deeper insights into consumer decision-making processes, particularly for experience goods such as hotel bookings. As shown in Table 1, Li et al. (2024) found that rating inconsistency increases the perceived helpfulness of reviews for experience goods compared with search goods. Second, research on score-textual inconsistency is limited and has focused primarily on the magnitude rather than the directional nature of inconsistency (Hong and Pittman, 2020; Li et al., 2024). Prospect theory indicates that consumer behaviour varies on the basis of emotional context, whether positive or negative (Wang et al., 2023). Therefore, different types of inconsistency—such as high ratings with low sentiments versus low ratings with high sentiments—may have distinct effects. Given the dominance of positive ratings in online reviews (Hu et al., 2009; Zheng et al., 2021), our study focuses on high-rated but low-sentiment inconsistency. Furthermore, while prior research has often examined the effect of inconsistency on review helpfulness, few studies have directly linked review inconsistency to product sales, a crucial metric for the hotel industry. This study aims to address these research gaps by using machine learning-based sentiment analysis to explore the interplay between review sentiment and rating scores. Specifically, we investigate how review inconsistency (i.e., high-rated but low-sentiment) affects product sales. 

#### _2.2. Heuristic-systematic model_ 

The heuristic-systematic model (HSM) of information processing, initially proposed by Chaiken (1980) and subsequently explored in 

2 

_P. Wang et al.                                                                                                                                                                                                                                   International Journal of Hospitality Management_ 

_International Journal of Hospitality Management 130 (2025) 104271_ 

**Table 1** 

Overview of key recent studies on internal review inconsistency. 

|**Authors**|**Data Source**|**Key DVs**|**Definition of Review Inconsistency**|**Relevant Findings**|
|---|---|---|---|---|
|Fazzolari et al.|TripAdvisor|None|Mismatch between the review content and the actual|The text-score disagreement conveniently conveys to the user a|
|(2017)|Booking||score|summary of positive and negative features of the review target.|
|Chi et al.<br>(2020)|xiaozhu.com|Rental<br>purchase|Consistency between picture colour cues and textual<br>cues|The consistency of picture colour cues and textual cues related<br>to colour is found to have a significant impact on rental<br>decisions.|
|Hong and|Experiment|Perceived|Incongruent valence between star ratings and product|Consistent argument valence will result in higher perceived|
|Pittman<br>(2020)||credibility|reviews|credibility of online reviews.|
|Siddiqi et al.<br>(2020)|Survey|Purchase<br>intention|Conflicting review star ratings from different reviewers|Conflicting ratings are positively associated with attitude<br>ambivalence (mediator) and then decrease purchase<br>intentions.|
|Aghakhani<br>et al. (2021)|Yelp.com|Review<br>usefulness|Consistency between a review text and the<br>corresponding numerical rating|Review consistency and rating inconsistency positively affects<br>review usefulness.|
|Shan et al.<br>(2021)|Yelp.com|None|Inconsistency between ratings and review sentiments|Inconsistencies are more salient in fake reviews than in<br>authentic reviews.|
|Wang et al.<br>(2021)|Experiment|Intention to<br>buy|Inconsistency between primary and supplementary<br>review sentiments|Inconsistent reviews result in less favourable intention to buy<br>through engendering ambivalence.|
|Zhou et al.<br>(2023)|TripAdvisor|Review<br>helpfulness|Consistency between manager responses and<br>corresponding reviews|Topic consistency positively affects review helpfulness.|
|Choi et al.<br>(2023)|Jobplanet. co.<br>kr|Review<br>helpfulness|Inconsistency among rating, title, recommendation, and<br>growth|Internal inconsistency is positively related to review<br>helpfulness, while external inconsistency is negatively related<br>to review helpfulness.|
|Hung et al.<br>(2023)|Survey|eWOM<br>usefulness|Consistency of the review contents|Review consistency negatively correlates with informational<br>influence.|
|Jin et al.<br>(2023)|TripAdvisor<br>Experiment|Review<br>helpfulness|Inconsistency between a review textual sentiment and<br>related rating|l<br>Review inconsistency positively moderates the effect of<br>personalized managerial response on negative review<br>helpfulness.|
|Li et al. (2024)|Amazon.com|Perceived<br>helpfulness|Review consistency between the review text and the<br>numerical rating; rating inconsistency between the<br>individual review ratings and the average rating|Review consistency positively affects perceived helpfulness,<br>while rating inconsistency positively affect perceived<br>helpfulness in reviews of experience goods rather than search<br>goods.|
|Yang et al.<br>(2023)|JD.com|Review<br>helpfulness|Consistency between images and text|Consistency prompts review helpfulness for search products,<br>while the effect is negative for experience products.<br>i|
|Liu et al.<br>(2024)|Qunar.com|Hotel rating|Fit between photo and review text|<br>Photo-text fit is associated with tourists’ratings with the<br>relationship typified by an inverted U-shaped pattern.|
|Wang et al.<br>(2024)|TripAdvisor|Forwarding<br>behaviour|Sentiment dissimilarity between review content and<br>review title|i<br>Negative sentiment dissimilarity dampens the positive effect of<br>negative sentiment on forwarding behaviour.|
|Our study|Ctrip.com|Product sales|Review inconsistency with high scores but low<br>sentiments|Review inconsistency negatively affects product sales.|



various studies (e.g., Qahri-Saremi and Montazemi, 2019; Zhang et al., 2014; Zhang et al., 2023), presents a dual-route framework through which individuals process information via either systematic or heuristic pathways. Systematic processing entails in-depth engagement with information, where individuals thoroughly examine each element of the content, dedicating significant cognitive effort to forming well-reasoned judgments. In contrast, heuristic processing involves a more surface-level approach, where judgments are based on a limited set of cues, thereby reducing cognitive expenditure. An individual’s preference for either processing mode is influenced by their motivation to engage in cognitive effort and their capacity for information elaboration. 

Notably, heuristic and systematic processing are not mutually exclusive; individuals can engage in both modes simultaneously, particularly when the need for information elaboration is high (Chaiken and Maheswaran, 1994; Darke et al., 1998). This concurrent use allows for interaction between text-based systematic processing and nontextual heuristic cues, where heuristic influences may be moderated—or attenuated—under rigorous systematic scrutiny. Thus, consumers may initially rely on heuristic cues to make quick judgments, followed by a more detailed systematic review to refine their understanding and inform decision-making. 

In digital environments, the relevance of dual-process models is further emphasized by findings that both textual (systematic) and nontextual (heuristic) cues significantly shape users’ information processing and behavioural intentions on online review platforms (Kim et al., 2017; Zhang et al., 2014). Accordingly, we propose that when navigating online reviews, consumers adopt a dual-processing approach, quickly 

forming preliminary judgments through heuristic cues and then engaging in a deeper, systematic analysis to increase the quality of their purchasing decisions. These insights underscore the multifaceted nature of online information processing, highlighting the need to consider both the textual content and the contextual cues of online reviews in shaping consumer perceptions and actions. 

Through this lens, our study contributes to the growing literature on hospitality marketing and consumer decision-making by offering a comprehensive framework to dissect the mechanisms underpinning online review evaluation and its subsequent impact on consumer attitudes and behaviours. 

#### _2.3. Schema incongruity theory_ 

Schema incongruity theory, developed by Mandler (1982), posits that individuals experience varying degrees of congruence between external stimuli and their existing cognitive schemas. This theory describes how discrepancies between expected and actual experiences stimulate cognitive and affective processes to reconcile incongruity (Halkias and Kokkinaki, 2014). Specifically, moderate incongruities may be assimilated into existing schemas, enhancing engagement and evaluation due to their novelty and challenge (Meyerslevy and Tybout, 1989). In contrast, significant incongruities may necessitate schema accommodation, requiring substantial cognitive effort to adjust existing schemas or create new ones, thereby impacting attitudes and behaviour (Stayman et al., 1992). 

Schema incongruity theory has been widely applied in marketing, particularly in advertising, where moderate incongruity has been shown 

3 

_International Journal of Hospitality Management 130 (2025) 104271_ 

_P. Wang et al._ 

to enhance message engagement and evaluation (Peng et al., 2023). Extending this theory to the context of online reviews, this study examines how consumers process and react to inconsistencies between rating scores and textual content, referred to as score-textual inconsistency. 

Applying schema incongruity theory to online review analysis introduces a nuanced perspective for exploring consumer responses to score-textual inconsistency. This phenomenon represents a unique form of schema incongruity, challenging consumers’ expectations and prompting a reevaluation of their preconceived notions about a product or service. This theoretical framework highlights the complexity of consumer information processing, emphasizing the role of cognitive and affective mechanisms in navigating inconsistencies in online reviews. 

#### **3. Research hypotheses** 

#### _3.1. Effect of the product rating_ 

Building on the understanding that numerical ratings encapsulate consumer evaluations and serve as platform-endorsed indicators of quality (Park and Nicolau, 2015), this study proposes that such ratings significantly shape consumer purchasing behaviour. Typically, presented as a star system, numerical ratings distil complex consumer sentiments into a straightforward, quantifiable metric that provides a quick snapshot of product quality and value (Li and Hitt, 2010; Yin et al., 2016). Empirical studies have highlighted the substantial influence of product rating on sales, with Jabr and Zheng (2014) and Moe and Trusov (2011) demonstrating both direct and indirect effects on market performance. Ratings act not only as heuristic cues simplifying product assessment but also as guides for consumer attitudes and decisions, particularly in experiential purchases such as hotel bookings, where objective evaluation criteria are limited. In these contexts, consumers often rely on the aggregated wisdom embedded in ratings to reduce cognitive effort and enhance decision quality, drawing on perceived endorsements from both experts and peers (Tsang and Prendergast, 2009). On the basis of this rationale, we hypothesize the following: 

**Hypothesis 1** . Product rating is positively associated with product sales. 

#### _3.2. Effect of review inconsistency_ 

According to the heuristic-systematic model, consumers typically navigate online reviews through a dual-processing approach: initially relying on heuristic cues for efficiency and, if needed, engaging in more elaborate systematic processing (Chaiken, 1980). Schema incongruity theory further informs this process by suggesting that incongruities between expected and actual stimuli prompt individuals to resolve the discrepancy, often requiring a shift from heuristic to more effortful systematic processing (Mandler, 1982). 

In the context of online reviews, high rating scores accompanied by low review sentiments create schema incongruity, disrupting the expectation that higher ratings correspond with more positive feedback (Cho et al., 2022). This incongruity challenges consumers’ cognitive schemas, prompting a shift from heuristic to systematic processing to address the inconsistency. In other words, the divergence between the heuristic cue (review score) and the systematic cue (review text) unsettles consumers’ cognitive equilibrium, compelling them to engage in deeper processing to reconcile the discrepancy. 

Since consumers are cognitive misers who generally prefer strategies that conserve mental resources, the additional cognitive effort required to process inconsistent reviews can induce cognitive dissonance and frustration (Yin et al., 2023). This increased cognitive load, combined with potential difficulty in reconciling conflicting information, is likely to result in negative product evaluations, reducing purchase intentions and consequently adversely impacting product sales. 

Empirical studies reinforce the importance of review consistency for consumer perceptions and behaviours. For instance, Tsang and Prendergast (2009) highlight the strong impact of consistent and diagnostic reviews on purchase intentions, illustrating the value of review coherence. When consistency is disrupted, however, the diagnostic value of reviews declines, diminishing their effectiveness in guiding consumer decisions (Lee and Ma, 2012). The systematic processing induced by review inconsistency not only increases cognitive effort but also erodes the credibility and perceived usefulness of reviews, ultimately reducing their informational value in consumer decision-making. Therefore, we propose the following hypothesis: 

**Hypothesis 2** . Score-textual review inconsistency is negatively associated with product sales. 

#### _3.3. Moderating effect of reviewer anonymity_ 

In the digital landscape of consumer feedback, the interplay of source credibility, attribution theory, and the accessibility-diagnosticity model offers a comprehensive framework for examining the nuanced effects of reviewer anonymity on the relationships among product rating, review inconsistency, and sales performance. Extensive research has emphasized the importance of source characteristics, such as reviewer expertise, identity disclosure, and perceived trustworthiness, in establishing the credibility of online reviews (Cheung et al., 2012). Attribution theory further suggests that consumers tend to infer motivations behind reviewers’ contributions, with anonymity often casting doubt on the intent and authenticity of the feedback (Dyussembayeva et al., 2020; Liu et al., 2019). Additionally, the accessibility-diagnosticity model posits that information’s impact on judgments is strengthened when it is both readily accessible and considered diagnostic—relevant and useful for evaluative purposes (Feldman and Lynch, 1988; Schwarz, 2004). 

Anonymity, as marked by a reviewer’s choice to conceal personal identifiers, serves a dual function within online platforms: it promotes a sense of freedom in expression but simultaneously reduces accountability, which may undermine the perceived trustworthiness of reviews (Parameswaran et al., 2023; Racherla and Friske, 2012). From a source credibility perspective, disclosed identities enhance the trustworthiness of reviews by reducing informational ambiguity and simplifying the consumer’s information processing (Forman et al., 2008; Liu and Park, 2015). However, when reviewers choose to remain anonymous, particularly in cases of review inconsistency, consumers are likely to engage in attribution processes, becoming more sceptical of the review’s authenticity and reducing its influence on purchase decisions. 

Reviewer anonymity also affects both the accessibility and the perceived diagnosticity of review content. Although reviews from anonymous sources are often widespread and easily encountered, their diagnostic value for decision-making may be questioned, leading consumers to doubt their reliability and relevance. Based on these considerations, we propose the following hypotheses: 

**Hypothesis 3a** . **.** The positive effect of product rating on product sales will be weakened when reviewer anonymity is relatively high. 

**Hypothesis 3b** . **.** The negative effect of review inconsistency on product sales will be mitigated when reviewer anonymity is relatively high. 

#### _3.4. Moderating effect of the image number_ 

The increasing incorporation of visual elements, such as product images, has been recognized for enhancing the informativeness and perceived helpfulness of online reviews, especially for experiential products (Luo et al., 2021). Visuals act as powerful heuristic cues, providing tangible insights into product quality and user experiences, which complement and enrich the textual content of reviews (Chi et al., 2022; Li et al., 2022; Liu and Park, 2015). 

4 

_International Journal of Hospitality Management 130 (2025) 104271_ 

_P. Wang et al.                                                                                                                                                                                                                                   International Journal of Hospitality Management_ 

The inclusion of images in reviews extends beyond mere aesthetic appeal, serving as a medium for conveying richer, more detailed information (Yu and Egger, 2021). These visual elements not only enhance the credibility and readability of reviews but also offer a more immersive understanding of the product or service experience. As a result, reviews featuring a greater number of images are often perceived as more credible and useful, making them more influential in shaping consumer perceptions and decisions (Zhao et al., 2023). 

Based on this perspective, we posit that the presence of images in online tourism reviews significantly impacts their diagnostic value and, consequently, their effectiveness in influencing product sales. Specifically, an increase in the image number within a review is expected to strengthen the positive impact of product ratings on sales. This is due to the additional, specific content that images provide, which makes the review more engaging and informative, thus amplifying the diagnostic power of product ratings. Moreover, a greater number of images may intensify the perceived thoroughness of the review, potentially accentuating the negative impact of review inconsistency on sales. Visual evidence provided by images can highlight discrepancies between the rating score and review text, thereby heightening the effects of review inconsistency. Accordingly, we propose the following hypotheses: 

**Hypothesis 4a** . The positive effect of product rating on product sales will be strengthened when the image number is relatively high. 

**Hypothesis 4b** . The negative effect of review inconsistency on product sales will be magnified when the image number is relatively high. 

#### _3.5. Moderating effect of managerial response_ 

In the realm of online travel platforms, the interaction between consumer reviews and managerial responses plays a crucial role in shaping consumer perceptions and purchasing decisions (Yhee et al., 2023). Within the hotel booking process, where experiential products are often subject to subjective evaluations, managerial responses extend beyond mere service recovery by adding diagnostic information that complements reviews. This not only enhances the perceived helpfulness of reviews but also reinforces hotel credibility, fostering trust among potential guests (Li et al., 2017). 

Drawing from the customer relationship management literature, managerial response is vital in influencing how consumers interpret review ratings. According to Xie et al. (2014), managerial response can moderate the impact of review ratings on customer perceptions by providing additional context. For instance, a thoughtful response to a low rating can alleviate its negative impact by addressing customer concerns and demonstrating corrective actions. Similarly, responses to high ratings can reinforce positive perceptions, amplifying their effect on consumer attitudes. This interactive approach fosters trust and credibility, ultimately influencing purchase decisions (Shin et al., 2020). 

Building upon the information processing literature and service recovery theory, we further propose that managerial response serves as a key cue in shaping potential consumers’ decision-making processes, particularly in the presence of review inconsistency. Managerial response, aimed at addressing customer feedback, reflects a customeroriented service recovery strategy. These responses signal a commitment to customer satisfaction and enhance a brand’s image as responsive and trustworthy (Gong et al., 2022; van Noort and Willemsen, 2012). Effective managerial responses, especially in cases of conflicting reviews, help clarify ambiguities, and reduce uncertainty and ambivalence among potential consumers (Palese et al., 2021). The quality of these responses—characterized by the relevance, reliability, clarity, and sufficiency of information—becomes instrumental in guiding potential customers through their prepurchase evaluation, offering a clearer understanding of hotel attributes and addressing concerns arising from conflicting reviews (Filieri, 2016; Lee et al., 2008). 

Therefore, managerial response is expected not only to strengthen the positive effect of favourable rating but also to reduce the negative 

impact of review inconsistency by enhancing transparency, reducing ambiguity, and demonstrating a commitment to customer satisfaction. Accordingly, we propose the following hypotheses: 

**Hypothesis 5a** . **.** The positive effect of product rating on product sales will be amplified when managerial response is relatively high. 

**Hypothesis 5b** . **.** The negative effect of review inconsistency on product sales will be mitigated when managerial response is relatively high. 

In conclusion, this study proposes a theoretical model, as illustrated in Fig. 1, to systematically examine the relationships between product rating, review inconsistency, and their moderating factors on product sales. 

#### **4. Methodology** 

#### _4.1. Data collection_ 

This study utilized the extensive database of online hotel reviews available on Ctrip.com, China’s leading online travel agency (OTA) platform, which held a market share of 36.3 % in 2021, significantly outpacing its competitors. Ctrip.com offers a comprehensive range of hotel reservation services across more than 200 countries and regions, encompassing over 1.7 million hotels in more than 90,000 cities. Given the platform’s large and diverse dataset, Ctrip.com was identified as an ideal data source for this research. The analysis specifically focused on hotels rated between 2-star and 5-star, covering a wide range of price points and consumer preferences. 

The study further narrowed its scope to the top 10 tourist cities in China, which were selected on the basis of their popularity and representativeness as major travel destinations. These cities—Chongqing, Shanghai, Beijing, Wuhan, Xi’an, Chengdu, Guiyang, Tianjin, Hangzhou, and Kunming—were used as keywords to extract relevant hotel review data from Ctrip.com. In each city, the top 30 hotels, as ranked by Ctrip’s natural recommendation algorithm (which reflects common consumer search and selection patterns), were selected as the sample set for analysis. 

Using Python for web crawling, the study systematically collected data on hotel characteristics (name, star rating, and location), reviewer demographics (username, check-in time, and reviewing history), and detailed review content (scores, textual and visual feedback, helpfulness votes, and managerial responses). An example of the collected data is illustrated in Fig. 2. 

Data collection was conducted over a one-week period from November 12–18, 2022, resulting in an initial dataset of 301,489 reviews from 300 hotels across the selected cities. After a meticulous preprocessing stage, which involved removing incomplete or irrelevant entries, the dataset was refined to 299,975 valid online reviews for 



<!-- Start of picture text -->
Reviewer  Image<br>Anonymity Number<br>H3a H3b H4a H4b<br>Product  H1<br>Rating<br>Product Sales<br>Review  H2<br>Inconsistency<br>H5a H5b<br>Managerial<br>Response<br><!-- End of picture text -->

**Fig. 1.** Research Model. 

5 

_P. Wang et al.                                                                                                                                                                                                                                   International Journal of Hospitality Management_ 

_International Journal of Hospitality Management 130 (2025) 104271_ 



**Fig. 2.** An example of hotel online reviews. 

comprehensive analysis. 

#### _4.2. Variable measurement_ 

This study defines product sales as the key dependent variable. Since Ctrip.com does not disclose direct hotel sales data, this study, following established research practices (Ye et al., 2009; Lee et al., 2011), uses the number of online reviews as a proxy for hotel sales. This approach rests on the premise that reviews indicate consumer engagement and, by extension, consumption experience. Given that Ctrip.com requires users to complete their stay before posting a review, the review count serves as a reasonable proxy for estimating product sales, although it is acknowledged that not all customers leave reviews. 

For the independent variables, this study primarily uses hotel rating as a measure of product rating, supplemented by a robustness check using the average review score. To capture score-textual inconsistency, we examine the specific inconsistency that is high-rated but lowsentiment (i.e., the review rating score is higher than the textual sentiment score). Machine learning was applied to perform sentiment analysis, categorizing reviews into positive, neutral, and negative categories to quantify review text sentiments. 

Specifically, advanced machine learning techniques were employed to analyse sentiment in review texts, classifying each sentiment as positive (1), neutral (0), or negative (-1). This analysis was conducted on the MODELSAIL platform (www.mosail.cn), developed by Qingbo Intelligent Technology Co., Ltd. (www.gsdata.cn), which leverages big data and artificial intelligence technologies. The sentiment analysis model utilized the bidirectional encoder representations from transformers (BERT) framework, which is known for its contextual embedding 

capabilities in natural language processing. 

To ensure accuracy, a curated dataset of 1103 hotel reviews annotated by three marketing professors was uploaded to the MODELSAIL platform for model training. This annotated set—comprising 51.04 % positive, 26.38 % neutral, and 22.58 % negative reviews—provided sufficient volume for effective training. After rigorous verification, the model demonstrated high accuracy in categorizing review sentiment. Table 2 presents the evaluation metrics (F1 score, precision, and recall) across sentiment categories. To account for potential sentiment measurement errors, such as variability in the annotation sample size during model training, additional robustness checks were conducted. The model was retrained using various sample sizes (e.g., 3000 and 6000 labelled samples) on the basis of a supervised deep learning approach. These checks aimed to ensure that the sentiment analysis results remained consistent and reliable across varying annotation sample size (Cho et al., 2022). For further details on the supervised machine learning-based approach, please refer to Appendix A1. 

Following sentiment analysis, a comparison was made between the sentiment scores and corresponding review scores, categorizing each review score as positive, neutral, or negative. On the basis of Bigne et al. (2023) and common consumer perceptions of online reviews, rating scores between [4,5] were classified as positive (coded as “1”), ratings in 

**Table 2** 

Sentiment analysis evaluation indicators. 

|Indicators|Positive|Neutral|Negative||
|---|---|---|---|---|
|f1_score|92.86 %|75.86 %|88.46 %|86.97 %|
|precision|89.66 %|84.62 %|85.19 %|87.20 %|
|recall|96.30 %|68.75 %|92.00 %|87.39 %|



6 

_International Journal of Hospitality Management 130 (2025) 104271_ 

_P. Wang et al.                                                                                                                                                                                                                                   International Journal of Hospitality Management_ 

the [3, 4) range as neutral (coded as “0”), and those in the [1, 3) range as negative (coded as “-1”). This coding scheme enabled a structured examination of the alignment between review text sentiment and the rating score. Table 3 provides an overview of the distribution of review sentiments and scores in the sample. Thus, score-textual inconsistency includes three scenarios: review rating scores of 1 paired with textual sentiments of 0 or − 1, and review rating scores of 0 paired with textual sentiment of − 1. The concordance between a review’s rating score and textual sentiment was marked as “0” (indicating consistency), whereas it was labelled “1” (indicating inconsistency). 

For this study, we focus on the proportion of reviews with high review scores but low textual sentiments to quantify review inconsistency within each hotel’s reviews. 

In examining moderating effects, reviewer anonymity was measured as the proportion of anonymous reviews relative to total reviews (Parameswaran et al., 2023). The image number was calculated as the average number of images per review, representing visual content (Lee et al., 2008). Managerial response was assessed as the ratio of reviews receiving direct responses from hotel management, reflecting the level of merchant engagement with reviews (Li et al., 2017). 

To control for potential confounding variables, this analysis includes both hotel-specific and review-specific factors. Among the hotel-specific controls, city popularity, which is coded from 1 to 10, reflects the ranking of the ten most popular tourist cities where the hotels are located (Xie et al., 2017), and hotel star ratings, ranging from 2 to 5 stars, were encoded accordingly (Huang et al., 2021). Review-specific controls include text length, which is calculated as the average word count per review to indicate content richness (Lee et al., 2008), and useful votes, which are measured by the average helpfulness votes per review (Hu and Chen, 2016). Table 4 summarizes the descriptions of all the variables. 

#### **5. Empirical results** 

#### _5.1. Descriptive analysis_ 

As shown in Table 5, the average product rating is 4.634 out of 5, indicating a generally high level of satisfaction across the sampled hotels. Additionally, the average level of review inconsistency is 0.166, reflecting a notable occurrence of reviews where high scores are accompanied by low textual sentiments. 

The correlation analysis reveals a positive correlation between product rating and product sales, supporting the intuitive link between higher rating and increased sales. Conversely, review inconsistency is significantly negatively correlated with product sales, highlighting the adverse impact of score-textual inconsistency on sales performance. These findings align with our hypothesized relationships, which are further validated in the subsequent sections through rigorous model testing. 

**Table 3** 

Distribution of review sentiments and scores for the sample data. 

|Review sentiments|Review scores|Review number|Percentage|
|---|---|---|---|
|1|1|233,902|77.97 %|
||0|1571|0.52 %|
||−1|115|0.04 %|
|0|1|37,207|12.40 %|
||0|6363|2.12 %|
||−1|1191|0.40 %|
|−1|1|4930|1.64 %|
||0|5997|2.00 %|
||−1|8699|2.90 %|
|Sum|-|299,975|100 %|



**Table 4** 

Description of all variables. 

|Variable|Description|
|---|---|
|**Dependent variable**||
|Product sales|The quantity of online reviews of the hotel.|
|**Independent**<br>**variables**||
|Product rating|The hotel rating on the product page.|
|Review|The percentage of inconsistent reviews with high review|
|inconsistency|scores but low textual sentiments.|
|**Moderators**||
|Reviewer|The percentage of anonymous reviews which do not disclose|
|Anonymity|user names.|
|Image number|The average number of images per review.|
|Managerial response|The percentage of reviews responded by the merchant.|
|**Control variables**||
|City popularity|The rank of the tourism city where the hotel is located|
|Hotel star|The hotel level shown on the product page.|
|Text length|The average word count per review.|
|Useful votes|The average helpfulness votes per review.|



#### _5.2. Empirical results_ 

Tables 6 and 7 present the results of the regression analyses, with logtransformed product sales as the dependent variable (Zhang et al., 2019, 2023). The variance inflation factor (VIF) values for each model are below 5, indicating that there are no multicollinearity issues among the predictor variables (Xu and Zhao, 2022). For brevity, only the maximum VIF value for each regression model is reported; a full list of VIF values is available in Appendix A2.3. Table 6 begins with Model M0, which includes only control variables. M1 then introduces the main effects, showing a positive and statistically significant coefficient for product rating (β = 0.489, p _<_ 0.01), thereby supporting Hypothesis 1. 

Further analysis explores the moderating roles of reviewer anonymity, image number, and managerial response. Contrary to Hypothesis 3a, M2 shows a non-significant negative coefficient for the interaction between product rating and reviewer anonymity (β = − 4.638, p _>_ 0.10). In contrast, Model M3 indicates a significant positive effect for the interaction effect between product rating and image number on product sales (β = 1.618, p _<_ 0.01), supporting Hypothesis 4a. This suggests that a greater number of images enhances the positive effect of product rating on sales. Additionally, Model M4 supports Hypothesis 5a, showing a significant positive moderating effect of managerial response on this relationship (β = 1.370, p _<_ 0.10), indicating that higher response rates increase sales. 

In Table 7, Model M1 confirms Hypothesis 2, showing a significant negative impact of review inconsistency on product sales (β = − 1.112, p _<_ 0.05). The moderating effects analysis reveals a significant positive interaction between review inconsistency and reviewer anonymity in M2 (β = 34.312, p _<_ 0.05), suggesting that higher anonymity mitigates the negative impact of review inconsistency, which is consistent with Hypothesis 3b. Conversely, M3 shows a significant negative interaction between review inconsistency and image number (β = − 2.831, p _<_ 0.10), reinforcing the adverse effect of inconsistency on sales and supporting Hypothesis 4b. Unexpectedly, Model M4 indicates a negative moderating effect of managerial response on the relationship between review inconsistency and product sales (β = − 5.280, p _<_ 0.10), thus not supporting Hypothesis 5b. 

#### _5.3. Robustness checks_ 

Additional analyses aimed at validating the consistency and reliability of our initial results. Firstly, to refine the measurement of hotel product rating, an alternative approach was adopted by utilizing the average score from all reviews of a hotel, diverging from the reliance on the platform-displayed overall rating. The results of this methodological adjustment are comprehensively documented in Table 8. The analysis 

7 

_International Journal of Hospitality Management 130 (2025) 104271_ 

**Table 5** 

Results of the correlation analysis among the variables. 

|Variables|(1)|(2)|(3)|(4)|(5)|(6)|(7)|(8)|(9)|(10)|
|---|---|---|---|---|---|---|---|---|---|---|
|(1) Product sales|1||||||||||
|(2) Product rating|0.210 * **|1|||||||||
|(3) Review inconsistency|−0.126 * *|−0.644 * **|1||||||||
|(4) Reviewer Anonymity|−0.151 * **|0.257 * **|−0.396 * **|1|||||||
|(5) Image number|0.113 * *|0.229 * **|−0.321 * **|0.152 * **|1||||||
|(6) Managerial response|0.015|0.140 * *|−0.079|−0.028|0.068|1|||||
|(7) City popularity|−0.168 * **|−0.156 * **|0.060|−0.038|−0.050|0.126 * *|1||||
|(8) Hotel star|0.315 * **|0.255 * **|−0.020|0.013|0.143 * *|0.046|−0.167 * **|1|||
|(9) Text length|0.141 * *|0.235 * **|−0.264 * **|0.089|0.669 * **|−0.022|−0.150 * **|0.431 * **|1||
|(10) Useful votes|−0.05|0.063|0.030|0.006|0.058|−0.011|−0.035|0.190 * **|0.140 * *|1|
|Mean|1601.37|4.634|0.166|0.07|0.453|0.967|5.5|3.017|35.142|0.17|
|SD|1065.42|0.187|0.058|0.038|0.357|0.136|2.877|0.894|10.347|0.608|
|Min|499|4|0.044|0.008|0.079|0.018|1|2|20.008|0|
|Max|7798|4.9|0.347|0.182|3.141|1|10|5|94.857|7.914|



_Notes_ : N = 300; *** _p <_ 0.01, ** _p <_ 0.05, * _p <_ 0.10. 

**Table 6** 

Empirical results of the effects of product rating on product sales. 

|DV: Product sales (log)|M0|M1|M2|M3|M4|
|---|---|---|---|---|---|
|Product rating||0.489 * **|0.638 * **|0.685 * **|0.560 * **|
|||(0.167)|(0.174)|(0.185)|(0.172)|
|Reviewer Anonymity|||−3.518 * **<br>(0.817)|||
|Image number||||−0.045<br>(0.128)||
|Managerial response|||||0.062<br>(0.243)|
|Rating×anonymity|||−4.638<br>(4.653)|||
|Rating×image||||1.618 * **<br>(0.586)||
|Rating×response|||||1.370 *<br>(0.789)|
|City popularity|−0.029 * **|−0.025 * *|−0. 026 * *|−0.023 * *|−0.023 * *|
||(0.011)|(0.011)|(0.010)|(0.011)|(0.011)|
|Hotel star|0.192 * **|0.174 * **|0. 163 * **|0.181 * **|0.169 * **|
||(0.038)|(0.038)|(0.037)|(0.039)|(0.038)|
|Text length|0.001|−0.001|−0.000|−0.003|−0.001|
||(0.003)|(0.003)|(0.003)|(0.004)|(0.003)|
|Useful votes|−0.109 * *|−0.11 * *|−0.110 * *|−0.108 * *|−0.110 * *|
||(0.051)|(0.050)|(0.048)|(0.049)|(0.050)|
|Constant|6.784 * **|4.597 * **|4.173 * **|3.755 * **|4.209 * **|
||(0.150)|(0.762)|(0. 780)|(0.845)|(0.804)|
|F|11.501 * **|11.148 * **|11.806 * **|9.361 * **|8.456 * **|
|R-squared|0.135|0.159|0.221|0.183|0.169|
|Max VIF|1.27|1.30|1.31|2.42|1.32|



_Notes:_ N = 300; Log denotes the logarithmic transformation of the original variables; Standard errors are in parentheses; *** p _<_ 0.01, ** p _<_ 0.05, * p _<_ 0.10. reveals a high degree of consistency with the initial findings reported in response quality of hotel managers. This aspect, calculated as the Table 6, affirming the robust nature of our results across different average word count of responses per review, delves into the substantive operationalizations of product rating. content of managerial feedback, which is posited to influence consumer 

response quality of hotel managers. This aspect, calculated as the average word count of responses per review, delves into the substantive content of managerial feedback, which is posited to influence consumer perceptions of review usefulness (Li et al., 2017). A comprehensive textual engagement from management, as indicated by longer responses, is presumed to enhance the perceived utility of the reviews, aiding consumers in forming more informed evaluations of the services offered. The findings, detailed in M5 of Tables 8 and 9, indicate that response length significantly moderates the relationship between product rating and sales in a manner consistent with Hypothesis H5a, yet does not lend support to Hypothesis H5b. This divergence suggests that the efficacy of service recovery efforts is contingent upon the appropriateness of the remedial actions undertaken, with ineffective recoveries potentially exacerbating customer grievances and fostering negative sentiment (Liu and Xu, 2023; Yang et al., 2022). 

Secondly, the study revisited the operationalization of review inconsistency. Acknowledging the variability in consumer perceptions of what constitutes a high-rated review, we adapted our categorization in line with observations from Ctrip’s hotel review platform, where scores of 4.5 and above are explicitly recognized as positive through descriptors such as “good,” “very good,” or “excellent.” Consequently, reviews rated between [4.5, 5] were classified as positive (coded as 1), those within [3, 4.5) as neutral (coded as 0), and [1, 3) as negative (coded as − 1). This recalibrated approach to categorizing review scores was applied, and the revised calculations of review inconsistency were reflected in the analysis, as shown in Table 9. The results across models M1, M2, M3, and M4 maintain their direction and significance, closely aligning with the findings from Table 7, thereby reinforcing the credibility of our revised methodological framework. 

Fourthly, we examined the impact of sentiment measurement error on our findings. To test for robustness, we compared the sentiment prediction results based on the initial 1103 annotated dataset with those of a deep learning-based model. Despite minor differences (e.g., the 

Thirdly, managerial response was further examined through the lens of response length, providing an additional dimension to evaluate the 

8 

_International Journal of Hospitality Management 130 (2025) 104271_ 

_P. Wang et al.                                                                                                                                                                                                                                   International Journal of Hospitality Management_ 

**Table 7** 

Empirical results of review inconsistency on product sales. 

|DV: Product sales (log)|M1|M2|M3|M4|
|---|---|---|---|---|
|Review inconsistency|−1.112 * *|−2.104 * **|−1.133 * *|−1.309 * *|
||(0.542)|(0.563)|(0.554)|(0.553)|
|Reviewer Anonymity||−3.311 * **<br>(0.902)|||
|Image number|||−0.020<br>(0.139)||
|Managerial response||||0.053<br>(0.229)|
|Inconsistency||34.312 * *|||
|×anonymity||(14.477)|||
|Inconsistency×image|||−2.831 *<br>(1.528)||
|Inconsistency||||−5.280 *|
|×response||||(2.824)|
|City popularity|−0.028 * **|−0.030 * **|−0.027 * *|−0.026 * *|
||(0.011)|(0.010)|(0.011)|(0.011)|
|Hotel star|0.200 * **|0.209 * **|0.214 * **|0.197 * **|
||(0.038)|(0.036)|(0.039)|(0.038)|
|Text length|−0.001|−0.002|−0.003|−0.002|
||(0.003)|(0.003)|(0.004)|(0.003)|
|Useful votes|−0.104 * *|−0.102 * *|−0.095 *|−0.102 * *|
||(0.050)|(0.048)|(0.050)|(0.050)|
|Constant|7.008 * **|7.456 * **|7.012 * **|7.014 * **|
||(0.185)|(0.202)|(0.184)|(0.283)|
|F|10.141 * **|12.354 * **|7.941 * **|7.786 * **|
|R-squared|0.147|0.228|0.160|0.157|
|Max VIF|1.35|1.41|2.77|1.37|



_Notes_ : N = 300; Log denotes the logarithmic transformation of the original variables; Standard errors are in parentheses; *** _p <_ 0.01, ** _p <_ 0.05, * _p <_ 0.10. 

MODELSAIL platform’s recall value for positive reviews was 96.3 % versus 92 % in the retrained deep learning model), the regression results were consistent. Further robustness checks involved retraining the model on larger annotation sets (3000 and 6000 reviews), yielding 

improved model performance yet no substantial changes in model error (see Appendix Table A1). Importantly, the regression coefficients remained consistent in direction and significance across varying annotation sizes (see Appendix Tables A5 and A7), underscoring the robustness of our conclusions. 

Finally, acknowledging potential endogeneity issues due to the cumulative number of reviews as a proxy for sales, we conducted additional tests. We created a duration-based control variable by calculating the interval between each hotel’s earliest review and the data collection date (November 12, 2022). Incorporating this control variable into the regression models did not alter our primary conclusions (see Appendix Tables A9 and A10). 

#### **6. Discussions** 

#### _6.1. Conclusions_ 

This study leverages an extensive dataset of 299,975 online reviews from 300 hotels on Ctrip.com to investigate the effects of product rating and review inconsistency—representing heuristic and systematic cues, respectively—on product sales. Additionally, it examines the moderating roles of reviewer anonymity, image number, and managerial response within the heuristic-systematic model framework. The key findings are summarized as follows: 

First, consistent with prior research, product rating positively influences product sales, underscoring its role as a heuristic cue (Geetha et al., 2017; Yoon et al., 2019). Conversely, review inconsistency has a negative impact on sales, suggesting that high inconsistency fosters consumer scepticism regarding review quality and authenticity, thereby weakening the influence of positive ratings and scores (Aghakhani et al., 2021; Cho et al., 2022; Valdivia et al., 2019). 

Second, reviewer anonymity positively moderates the effect of review inconsistency on sales, indicating that anonymity diminishes perceived reviewer credibility, making consumers cautious about 

**Table 8** 

Robustness check: Alternative measure of product rating. 

|DV: Product sales (log)|M1|M2|M3|M4|M5|
|---|---|---|---|---|---|
|Average review score|0.490 * *|0.659 * **|0.690 * **|0.583 * **|0.552 * **|
||(0.195)|(0.202)|(0.218)|(0.202)|(0.204)|
|Reviewer anonymity||−3.297 * **<br>(0.876)||||
|Image number|||−0.025<br>(0.130)|||
|Managerial response||||0.123<br>(0.257)||
|Managerial responselength|||||0.001 *|
||||||(0.001)|
|Score×anonymity||−7.426<br>(5.588)||||
|Score×image|||1.695 * *<br>(0.698)|||
|Score×response||||1.735 *<br>(0.933)||
|Score×responselength|||||0.006 *<br>(0.003)|
|City popularity|−0.027 * *|−0.029 * **|−0.025 * *|−0.025 * *|−0.024 * *|
||(0.011)|(0.010)|(0.011)|(0.011)|(0.011)|
|Hotel star|0.175 * **|0.162 * **|0.186 * **|0.169 * **|0.181 * **|
||(0.038)|(0.037)|(0.039)|(0.038)|(0.038)|
|Text length|−0.001|−0.000|−0.004|−0.001|−0.002|
||(0.003)|(0.003)|(0.004)|(0.003)|(0.003)|
|Useful votes|−0.106 * *|−0.103 * *|−0.102 * *|−0.104 * *|−0.101 * *|
||(0.050)|(0.049)|(0.050)|(0.050)|(0.050)|
|Constant|4.577 * **|4.053 * **|3.689 * **|4.027 * **|4.166 * **|
||(0.890)|(0.908)|(0.999)|(0.939)|(0.929)|
|F|10.631 * **|11.420 * **|8.704 * **|8.162 * **|8.682 * **|
|R-squared|0.153|0.215|0.173|0.164|0.172|
|Max VIF|1.31|1.32|2.44|1.42|1.32|



_Notes_ : N = 300; Log denotes the logarithmic transformation of the original variables; Standard errors are in parentheses; *** _p <_ 0.01, ** _p <_ 0.05, * _p <_ 0.10. 

9 

_International Journal of Hospitality Management 130 (2025) 104271_ 

**Table 9** 

Robustness check: Alternative measure of review inconsistency. 

|DV: Product sales (log)|M1|M2|M3|M4|M5|
|---|---|---|---|---|---|
|Review inconsistency (4.5)|−1. 457 * *|−2.667 * **|−1.343 *|−1.688 * *|−1.440 * *|
||(0.700)|(0.715)|(0.707)|(0.712)|(0.698)|
|Reviewer Anonymity||−3.260 * **<br>(0.876)||||
|Image number|||−0.006|||
||||(0.137)|||
|Managerial response||||0.017<br>(0.225)||
|Managerial responselength|||||0.001 *<br>(0.001)|
|Inconsistency×anonymity||40.779 * *<br>(18.511)||||
|Inconsistency×image|||−3.451 *<br>(1.905)|||
|Inconsistency×response||||−6.602 *<br>(3.739)||
|Inconsistency×responselength|||||−0.015<br>(0.012)|
|City popularity|−0.027 * *|−0.028 * **|−0.030 * **|−0.027 * *|−0.027 * *|
||(0.011)|(0.011)|(0.010)|(0.011)|(0.011)|
|Hotel star|0.175 * **|0.206 * **|0.221 * **|0.219 * **|0.212 * **|
||(0.038)|(0.038)|(0.037)|(0.039)|(0.038)|
|Text length|−0.001|−0.001|−0.002|−0.003|−0.003|
||(0.003)|(0.003)|(0.003)|(0.004)|(0.003)|
|Useful votes|−0.106 * *|−0.101 * *|−0.098 * *|−0.090 *|−0.103 * *|
||(0.050)|(0.051)|(0.048)|(0.051)|(0.050)|
|Constant|4.577 * **|7.000 * **|7.408 * **|6.980 * **|6.904 * **|
||(0.890)|(0.182)|(0.196)|(0.182)|(0.190)|
|F|10.631 * **|10.171 * **|11.949 * **|7.948 * **|8.126 * **|
|R-squared|0.153|0.147|0.223|0.160|0.163|
|Max VIF|1.31|1.35|1.36|2.67|1.40|



_Notes:_ N = 300; Log denotes the logarithmic transformation of the original variables; Standard errors are in parentheses; *** _p <_ 0.01, ** _p <_ 0.05, * _p <_ 0.10. 

reviews regardless of valence (Parameswaran et al., 2023). However, the expected effect of anonymity on the positive relationship between product rating and sales (H3a) was not supported, potentially because consumers prioritize rating information over reviewer identity in decision-making (Siddiqi et al., 2020). 

Third, the image number in online reviews both enhances the positive relationship between product rating and sales and intensifies the negative impact of review inconsistency on sales. This finding highlights the complementary role of visual content in enhancing the diagnostic value of reviews, offering consumers tangible insights into the product and strengthening review credibility (Sayfuddin and Chen, 2021). 

Finally, while managerial response amplifies the positive effect of product rating on sales, it unexpectedly exacerbates the negative impact of review inconsistency on sales. This suggests that not all service recovery efforts through managerial responses are effective; in some cases, they may even worsen consumer dissatisfaction (Tsang and Prendergast, 2009). This result may be attributed to the prevalent use of generic, template-based responses on the platform, which often fail to address consumer concerns adequately or provide meaningful information (Hong and Pittman, 2020). 

#### _6.2. Theoretical implications_ 

Our study contributes to the tourism marketing literature in three key ways, introducing novel insights that distinguish it from existing research. 

Firstly, by rigorously defining and investigating review inconsistency, this study specifically examines the effects of discrepancies where high review scores conflict with low textual sentiments and the consequent impact on hotel sales. While review inconsistency has been explored in prior studies, our research uniquely focuses on score-textual inconsistency and its direct influence on business performance, particularly sales—a facet often overlooked. This analysis reveals a critical gap in current online reputation management practices, advocating for a 

balanced approach that considers both numerical rating scores and textual feedback to gain a more comprehensive understanding of consumer experiences and perceptions. 

Secondly, this study integrates foundational theories from consumer information processing, including the heuristic-systematic model, schema incongruity theory, cognitive dissonance, and cognitive processing fluency, to create a comprehensive framework for analysing review inconsistency. This theoretical integration provides the hospitality research community with a robust framework for interpreting online reviews, offering insights into how consumers process and respond to the interplay between review scores and text. By incorporating these theories, our study enhances the understanding of consumer behaviour in response to review inconsistency, an area that remains underexplored in the current literature. 

Thirdly, by examining the moderating effects of reviewer anonymity, image number, and managerial response, this study identifies boundary conditions that clarify the dynamics of score-textual inconsistency on hotel room sales. This contributes to existing research by expanding the understanding of the factors shaping the impact of online reviews and by providing a nuanced perspective on how hotels can strategically mitigate the negative effects associated with review inconsistency. By highlighting the roles of identity disclosure, visual content and managerial response, our study offers actionable insights that directly inform reputation management strategies in the hospitality industry. 

#### _6.3. Practical implications_ 

First, it is essential for hotels to look beyond rating scores and focus on valuable insights within the textual content of reviews. Our findings underscore the risks of “high rating scores with low sentiments” inconsistency, which can undermine review credibility and reduce their diagnostic value. Hotels should encourage guests to provide detailed feedback explaining the context behind their ratings, enabling more actionable insights and helping to identify both strengths and areas 

10 

_International Journal of Hospitality Management 130 (2025) 104271_ 

_P. Wang et al._ 

needing improvement. 

In addition, fostering a culture that encourages non-anonymous contributions can enhance the credibility of online reviews. Providing incentives, such as rewards or recognition, can motivate reviewers to share genuine and detailed experiences, increasing the trustworthiness of their feedback. The inclusion of visual content alongside textual reviews also enhances the diagnostic value, as images provide tangible insights that assist future guests in making informed decisions. 

Finally, our findings emphasize the importance of personalized managerial response, especially when addressing discrepancies between rating scores and textual sentiments. Rather than using generic, template-based replies, tailored responses that directly address the content of reviews are more effective in mitigating the negative impacts of inconsistency and fostering customer loyalty. This approach allows service recovery efforts to go beyond operational tasks, transforming them into strategic opportunities to reinforce trust and enhance the hotel’s reputation, particularly in cases of service failure. 

#### _6.4. Limitations and future research_ 

This study still has some limitations. First, the use of review count as a proxy for sales data introduces a degree of abstraction from actual sales performance. Future research could benefit from incorporating precise sales figures to increase the validity and applicability of our findings. Second, since reviewers decide to post content based on individual motivations, preferences, and expectations, there is potential for selfselection bias. Future studies could address this issue by employing experimental or longitudinal designs to reduce bias and increase generalizability. Finally, future research could delve further into the content, tone, and responsiveness of managerial feedback via advanced text analysis techniques. This would provide valuable insights into how different aspects of managerial engagement influence consumer perceptions and decision-making. 

#### **CRediT authorship contribution statement** 

**Wang Ping:** Writing – review & editing, Writing – original draft, Validation, Formal analysis, Conceptualization. **Zhang Xiulin:** Methodology, Investigation, Formal analysis. **Yuan Xina:** Writing – review & editing, Writing – original draft, Supervision, Funding acquisition, Conceptualization. **Zhang Hailin:** Writing – review & editing, Writing – original draft, Project administration, Methodology, Formal analysis, Conceptualization. 

#### **Declaration of Competing Interest** 

The authors declare that they have no known competing financial interests or personal relationships that could have appeared to influence the work reported in this paper. 

#### **Acknowledgements** 

This work was supported by Fujian Provincial Federation of Social Sciences (福建省社会科学基金), Grant ID: FJ2021B162. 

#### **Appendix A. Supporting information** 

Supplementary data associated with this article can be found in the online version at doi:10.1016/j.ijhm.2025.104271. 

#### **Data availability** 

Data will be made available on request. 

#### **References** 

|Aghakhani, N., Oh, O., Gregg, D.G., Jain, H., 2023. How review quality and source|
|---|
|credibility interacts to affect review usefulness: an expansion of the elaboration|
|likelihood model. Inf. Syst. Front. 25 (4), 1513–1531.|
|Aghakhani, N., Oh, O., Gregg, D.G., Karimi, J., 2021. Online review consistency matters:<br>|
|an elaboration likelihood model perspective. Inf. Syst. Front. 23 (5), 1287–1301.|
|Akhtar, N., Sun, J., Akhtar, M.N., Chen, J., 2019. How attitude ambivalence from<br>l|
|conflicting online hotel reviews affects consumers’behavioural responses: the<br>moderating role of dialecticism. J. Hosp. Tour. Manag. 41, 28–40.|
|Anderson, M., Magruder, J., 2012. Learning from the crowd: regression discontinuity<br>estimates of the effects of an online review database. Econ. J. 122 (563), 957–989.|
|Bigne, E., Ruiz, C., Perez-Cabanero, C., Cuenca, A., 2023. Are customer star ratings and|
|sentiments aligned? A deep learning study of the customer service experience in|
|tourism destinations. Serv. Bus. 17 (1), 281–314.|
|Chaiken, S., 1980. Heuristic versus systematic information-processing and the use of|
|source versus message cues in persuasion. J. Personal. Soc. Psychol. 39 (5), 752–766.|
|Chaiken, S., Maheswaran, D., 1994. Heuristic processing can bias systematic processing -|
|effects of source credibility, argument ambiguity, and task importance on attitude<br>judgment. J. Personal. Soc. Psychol. 66 (3), 460–473.|
|Chakraborty, U., 2019. Perceived credibility of online hotel reviews and its impact on<br>hotel booking intentions. Int. J. Contemp. Hosp. Manag. 31 (9), 3465–3483.|
|Cheung, C.M.Y., Sia, C.L., Kuan, K.K.Y., 2012. Is this review believable? A study of|
|factors affecting the credibility of online consumer reviews from an ELM perspective.<br>J. Assoc. Inf. Syst. 13 (8), 618–635.|
|Chi, M.M., Pan, M.Y., Huang, R., 2020. Examining the direct and interaction effects of<br>picture color cues and textual cues related to color on accommodation-sharing|
|platform rental purchase. Int. J. Hosp. Manag. 99, 103066.|
|Cho, H.S., Sosa, M.E., Hasija, S., 2022. Reading between the stars: understanding the|
|effects of online customer reviews on product demand. Manuf. Serv. Oper. Manag.<br>24 (4), 1977–1996.|
|Choi, J., Yoo, S.H., Lee, H., 2023. Two faces of review inconsistency: the respective|
|effects of internal and external inconsistencies on job review helpfulness. Comput.|
|Hum. Behav. 140, 107570.|
|Costa, A., Guerreiro, J., Moro, S., Henriques, R., 2019. Unfolding the characteristics of|
|incentivized online reviews. J. Retail. Consum. Serv. 47, 272–281.|
|Darke, P.R., Chaiken, S., Bohner, G., Einwiller, S., Erb, H.P., Hazlewood, J.D., 1998.|
|Accuracy motivation, consensus information, and the law of large numbers: Effects|
|on attitude judgment in the absence of argumentation. Personal. Soc. Psychol. Bull.<br>24 (11), 1205–1215.|
|Dhar, S., Bose, I., 2022. Walking on air or hopping mad? Understanding the impact of|
|emotions, sentiments and reactions on ratings in online customer reviews of mobile|
|apps. Decis. Support Syst. 162, 113769.|
|<br>Dyussembayeva, S., Viglia, G., Nieto-Garcia, M., Invernizzi, A.C., 2020. It makes me feel|
|<br>vulnerable! The impact of public self-disclosure on online complaint behavior.  Int. J.|
|Hosp. Manag. 88, 102512.|
|Fazzolari, M., Cozza, V., Petrocchi, M., Spognardi, A., 2017. A study on text-score|
|disagreement in online reviews. Cogn. Comput. 9 (5), 689–701.|



- Feldman, J.M., Lynch, J.G., 1988. Self-generated validity and other effects of measurement on belief, attitude, intention, and behavior. J. Appl. Psychol. 73 (3), 421–435. 

- Filieri, R., 2016. What makes an online consumer review trustworthy? Ann. Tour. Res. 58, 46–64. 

- Forman, C., Ghose, A., Wiesenfeld, B., 2008. Examining the relationship between reviews and sales: the role of reviewer identity disclosure in electronic markets. Inf. Syst. Res. 19 (3), 291–313. 

- Geetha, M., Singha, P., Sinha, S., 2017. Relationship between customer sentiment and online customer ratings for hotels - an empirical analysis. Tour. Manag. 61, 43–54. 

- Gong, C.Y., Liu, J.W., Law, R., Ye, Q., 2022. Exploring the effects of official-structured managerial responses on hotel online popularity. Int. J. Hosp. Manag. 106, 103293. 

- Halkias, G., Kokkinaki, F., 2014. The degree of ad-brand incongruity and the distinction between schema-driven and stimulus-driven attitudes. J. Advert. 43 (4), 397–409. 

- Hong, S., Pittman, M., 2020. eWOM anatomy of online product reviews: interaction effects of review number, valence, and star ratings on perceived credibility. Int. J. Advert. 39 (7), 892–920. 

- Hu, N., Pavlou, P.A., Zhang, J., 2009. Overcoming the J-shaped Distribution of Product Reviews. Commun. Acm 52 (10), 144–147. 

- Hu, Y.H., Chen, K.C., 2016. Predicting hotel review helpfulness: the impact of review visibility, and interaction between hotel stars and review ratings. Int. J. Inf. Manag. 36 (6), 929–944. 

- Huang, Y.L., Jin, Y., Huang, J.H., 2021. Impact of Managerial responses on product sales: examining the moderating role of competitive intensity and market position. J. Assoc. Inf. Syst. 22 (2), 544–570. 

- Hung, S.W., Chang, C.W., Chen, S.Y., 2023. Beyond a bunch of reviews: the quality and quantity of electronic word-of-mouth. Inf. Manag. 60 (3), 103777, 12. 

- Jabr, W., Zheng, Z.Q., 2014. Know yourself and know your enemy: an analysis of firm recommendations and consumer reviews in a competitive environment. MIS Q. 38 (3), 635–654. 

- Jin, W.Y., Chen, Y.A., Yang, S.Q., Zhou, S.S., Jiang, H., Wei, J.E., 2023. Personalized managerial response and negative inconsistent review helpfulness: the mediating effect of perceived response helpfulness. J. Retail. Consum. Serv. 74, 103398. 

- Kassem, M.A., Abohany, A.A., El-Mageed, A.A.A., Hosny, K.M., 2024. A novel deep learning model for detection of inconsistency in e-commerce websites. Neural Comput. Appl. 36, 10339–10353. 

- Kim, E., Ding, M.Q., Wang, X., Lu, S.J., 2023. Does topic consistency matter? A study of critic and user reviews in the movie industry. J. Mark. 87 (3), 428–450. 

11 

_International Journal of Hospitality Management 130 (2025) 104271_ 

_P. Wang et al._ 

- Kim, K., Park, O.J., Yun, S., Yun, H., 2017. What makes tourists feel negatively about tourism destinations? Application of hybrid text mining methodology to smart destination management. Technol. Forecast. Soc. Change 123, 362–369. 

- Lee, H.H., Ma, Y.J., 2012. Consumer perceptions of online consumer product and service reviews: Focusing on information processing confidence and susceptibility to peer influence. J. Res. Interact. Mark. 6 (2), 110–132. 

- Lee, J., Park, D.H., Han, I., 2008. The effect of negative online consumer reviews on product attitude: an information processing view. Electron. Commer. Res. Appl. 7 (3), 341–352. 

- Lee, J., Lee, J.N., Shin, H., 2011. The long tail or the short tail: the category-specific impact of eWOM on sales distribution. Decis. Support Syst. 51 (3), 466–479. 

- Lee, S., Lee, S., Baek, H., 2021. Does the dispersion of online review ratings affect review helpfulness? Comput. Hum. Behav. 117 (11), 106670. 

- Li, C.Y., Cui, G., Peng, L., 2017. The signaling effect of management response in engaging customers: a study of the hotel industry. Tour. Manag. 62, 42–53. 

- Li, H.Y., Ji, H.P., Liu, H.B., Cai, D.T., Gao, H.C., 2022. Is a picture worth a thousand words? Understanding the role of review photo sentiment and text-photo sentiment disparity using deep learning algorithms. Tour. Manag. 92, 104559. 

- Li, Q.L., Park, J., Kim, J., 2024. Impact of information consistency in online reviews on consumer behavior in the e-commerce industry: a text mining approach. Data Technol. Appl. 58 (1), 132–149. 

- Li, X.X., Hitt, L.M., 2010. Price effects in online product reviews: an analytical model and empirical analysis. MIS Q. 34 (4), 809–831. 

- Li, Y., He, Z.Y., Li, Y.P., Huang, T., Liu, Z.Y., 2023. Keep it real: Assessing destination image congruence and its impact on tourist experience evaluations. Tour. Manag. 97, 104736. 

- Liu, J., Xu, X.A., 2023. Humor type and service context shape AI service recovery. Ann. Tour. Res. 103, 103668. 

- Liu, X.W., Liu, J.W., Law, R., Liang, S., 2019. Power of profile name in online sharing. Int. J. Hosp. Manag. 81, 30–33. 

- Liu, X.X., Zhang, Z.Q., Law, R., Zhang, Z.L., 2024. Words meet photos: How visual content impact rating. Int. J. Hosp. Manag. 123, 103945. 

- Liu, Z.W., Park, S., 2015. What makes a useful online review? Implication for travel product websites. Tour. Manag. 47, 140–151. 

- Luo, Y., Xu, X.W., 2021. Comparative study of deep learning models for analyzing online restaurant reviews in the era of the COVID-19 pandemic. Int. J. Hosp. Manag. 94, 102849. 

- Luo, Y., Tang, L., Kim, E., 2021. A picture is worth a thousand words: The role of a cover photograph on a travel agency’s online identity. Int. J. Hosp. Manag. 94, 102801. 

- Mandler, G., 1982. The structure of value: accounting for taste. In: Margaret Sydnor Clark, Fiske, Susan T. (Eds.), Affect and Cognition: The Seventeenth Annual Carnegie Symposium on Cognition. Erlbaum, Hillsdale, NJ, pp. 3–36. 

- McGregor, C. (2019). How to Leverage Reviews for Voice of the Customer Analysis. 〈https://learn.g2.com/leverage-reviews-for-voice-of-the-customer〉. (Accessed March 11, 2024). 

- Meyerslevy, J., Tybout, A.M., 1989. Schema congruity as a basis for product evaluation. J. Consum. Res. 16 (1), 39–54. 

- Moe, W.W., Trusov, M., 2011. The value of social dynamics in online product ratings forums. J. Mark. Res. 48 (3), 444–456. 

- Nielsen. (2015). Global trust in advertising. 〈https://www.nielsen.com/insights/2015/g lobal-trust-in-advertising/〉. (Accessed March 11, 2024). 

- van Noort, G., Willemsen, L.M., 2012. Online Damage Control: The Effects of Proactive Versus Reactive Webcare Interventions in Consumer-generated and Brand-generated Platforms. J. Interact. Mark. 26 (3), 131–140. 

- Palese, B., Piccoli, G., Lui, T.W., 2021. Effective use of online review systems: Congruent managerial responses and firm competitive performance. Int. J. Hosp. Manag. 96, 102976. 

- Parameswaran, S., Mukherjee, P., Valecha, R., 2023. I Like My Anonymity: An Empirical Investigation of the Effect of Multidimensional Review Text and Role Anonymity on Helpfulness of Employer Reviews. Inf. Syst. Front. 25 (2), 853–870. 

- Park, S.W., Nicolau, J.L., 2015. Asymmetric effects of online consumer reviews. Ann. Tour. Res. 50, 67–83. 

Peng, X.X., Xing, Y., Tian, Y., Fei, M.Q., Wang, Q.Z., 2023. Nonmonetary rewards of referral reward programs and recommendation intention: The role of rewardproduct congruity. Decis. Support Syst. 173, 113999. 

PowerReviews. (2023). Survey: The Ever-Growing Power of Reviews (2023 Edition). 〈https://www.powerreviews.com/research/power-of-reviews-2023/〉. (Accessed March 11, 2024). 

Qahri-Saremi, H., Montazemi, A.R., 2019. Factors Affecting the Adoption of an Electronic Word of Mouth Message: A Meta-Analysis. J. Manag. Inf. Syst. 36 (3), 969–1001. Racherla, P., Friske, W., 2012. Perceived ’usefulness’ of online consumer reviews: An exploratory investigation across three services categories. Electron. Commer. Res. Appl. 11 (6), 548–559. 

Sadiq, S., Umer, M., Ullah, S., Mirjalili, S., Rupapara, V., Nappi, M., 2021. Discrepancy detection between actual user reviews and numeric ratings of Google App store using deep learning. Expert Syst. Appl. 181, 115111. 

Sayfuddin, A.T.M., Chen, Y., 2021. The signaling and reputational effects of customer ratings on hotel revenues: evidence from TripAdvisor. Int. J. Hosp. Manag. 99, 103065. 

- Schwarz, N., 2004. Metacognitive experiences in consumer judgment and decision making. J. Consum. Psychol. 14 (4), 332–348. 

Shan, G.H., Zhou, L.A., Zhang, D.S., 2021. From conflicts and confusion to doubts: Examining review inconsistency for fake review detection. Decis. Support Syst. 144, 113513. 

- Shin, H., Perdue, R.R., Pandelaere, M., 2020. Managing customer reviews for value cocreation: an empowerment theory perspective. J. Travel Res. 59 (5), 792–810. 

- Siddiqi, U.I., Sun, J., Akhtar, N., 2020. The role of conflicting online reviews in consumers’ attitude ambivalence. Serv. Ind. J. 40 (13-14), 1003–1030. 

- Sparks, B.A., Browning, V., 2011. The impact of online reviews on hotel booking intentions and perception of trust. Tour. Manag. 32 (6), 1310–1323. 

- Stayman, D.M., Alden, D.L., Smith, K.H., 1992. Some effects of schematic processing on consumer expectations and disconfirmation judgments. J. Consum. Res. 19 (2), 240–255. 

- Taecharungroj, V., Mathayomchan, B., 2019. Analysing TripAdvisor reviews of tourist attractions in Phuket, Thailand. Tour. Manag. 75, 550–568. 

- Tsang, A.S.L., Prendergast, G., 2009. Is a "star" worth a thousand words? The interplay between product-review texts and rating valences. Eur. J. Mark. 43 (11-12), 1269–1280. 

- Valdivia, A., Hrabova, E., Chaturvedi, I., Luzon, M.V., Troiano, L., Cambria, E., Herrera, F., 2019. Inconsistencies on TripAdvisor reviews: a unified index between users and Sentiment Analysis Methods. Neurocomputing 353, 3–16. 

- Wang, Y.G., Tariq, S., Alvi, T.H., 2021. How primary and supplementary reviews affect consumer decision making? Roles of psychological and managerial mechanisms. Electron. Commer. Res. Appl. 46, 101032. 

- Wang, Y.Q., Ngai, E.W.T., Li, K., 2023. The effect of review content richness on product review helpfulness: the moderating role of rating inconsistency. Electron. Commer. Res. Appl. 61, 101290. 

- Wang, Y.Q., Ngai, E.W.T., Li, K., 2024. Effects of sentiment quantity, dispersion, and dissimilarity on online review forwarding behavior: an empirical analysis. J. Retail. Consum. Serv. 81, 103978. 

- Wu, H.Q., Guo, G.B., Yang, E.N., Luo, Y.D., Chu, Y.B., Jiang, L.Y., Wang, X.W., 2024. PESI: Personalized Explanation recommendation with Sentiment Inconsistency between ratings and reviews. Knowl. -Based Syst. 283, 111133. 

- Xie, K., Kwok, L., Wang, W., 2017. Monetizing managerial responses on TripAdvisor: performance implications across hotel classes. Cornell Hosp. Q. 58 (3), 240–252. 

- Xie, K.L., Zhang, Z.L., Zhang, Z.Q., 2014. The business value of online consumer reviews and management response to hotel performance. Int. J. Hosp. Manag. 43, 1–12. 

- Xu, X., Zhao, Y.B., 2022. Examining the influence of linguistic characteristics of online managerial response on return customers’ change in satisfaction with hotels. Int. J. Hosp. Manag. 102, 103146. 

- Yang, H.Y., Xu, H., Zhang, Y., Liang, Y., Lyu, T., 2022. Exploring the effect of humor in robot failure. Ann. Tour. Res. 95, 103425. 

- Yang, S.Q., Zhou, C.M., Chen, Y.G., 2021. Do topic consistency and linguistic style similarity affect online review helpfulness? An elaboration likelihood model perspective. Inf. Process. Manag. 58 (3), 102521. 

- Yang, Y., Wang, Y.J., Zhao, J.C., 2023. Effect of user-generated image on review helpfulness: Perspectives from object detection. Electron. Commer. Res. Appl. 57, 101232. 

- Ye, Q., Law, R., Gu, B., 2009. The impact of online user reviews on hotel room sales. Int. J. Hosp. Manag. 28 (1), 180–182. 

- Yhee, Y., Kim, H., Kim, J., Koo, C., 2023. Trust in managerial response offsets negative review. Ann. Tour. Res. 102 (18), 103641. 

- Yin, D.Z., Mitra, S., Zhang, H., 2016. When do consumers value positive vs. negative reviews? An empirical investigation of confirmation bias in online word of mouth. Inf. Syst. Res. 27 (1), 131–144. 

- Yin, D.Z., de Vreede, T., Steele, L.M., de Vreede, G.J., 2023. Decide now or later: making sense of incoherence across online reviews. Inf. Syst. Res. 34 (3), 1211–1227. 

- Ying, H., Peng, X.S., Zhao, X.D., & Chen, Z. (2023). The effects of signaling blockchainbased track and trace on consumer purchases: Insights from a quasi-natural experiment. Production and Operations Management. (Early Access). 

- Yoon, Y., Kim, A.J., Kim, J., Choi, J., 2019. The effects of eWOM characteristics on consumer ratings: evidence from TripAdvisor.com. Int. J. Advert. 38 (5), 684–703. 

- Yu, J.N., Egger, R., 2021. Color and engagement in touristic Instagram pictures: a machine learning approach. Ann. Tour. Res. 89, 103204. 

- Zhang, K.Z.K., Zhao, S.J., Cheung, C.M.K., Lee, M.K.O., 2014. Examining the influence of online reviews on consumers’ decision-making: a heuristic-systematic model. Decis. Support Syst. 67, 78–89. 

- Zhang, X., Zhang, X.X., Liang, S., Yang, Y., Law, R., 2023. Infusing new insights: how do review novelty and inconsistency shape the usefulness of online travel reviews. Tour. Manag. 96, 104703. 

- Zhang, Z.L., Liang, S., Li, H.Y., Zhang, Z.Q., 2019. Booking now or later: do online peer reviews matter? Int. J. Hosp. Manag. 77, 147–158. 

- Zhang, Z.Q., Li, Y.S., Li, H.Y., Zhang, Z.L., 2022. Restaurants’ motivations to solicit fake reviews: a competition perspective. Int. J. Hosp. Manag. 107, 103337. 

- Zhao, L., Zhang, M.L., Ming, Y.X., Niu, T., Wang, Y., 2023. The effect of image richness on customer engagement: evidence from Sina Weibo. J. Bus. Res. 154, 113307. 

- Zhao, Y.B., Xu, X., Wang, M.S., 2019. Predicting overall customer satisfaction: Big data evidence from hotel online textual reviews. Int. J. Hosp. Manag. 76, 111–121. 

- Zheng, T.X., Wu, F.R., Law, R., Qiu, Q.H., Wu, R., 2021. Identifying unreliable online hospitality reviews with biased user-given ratings: a deep learning forecasting approach. Int. J. Hosp. Manag. 92, 102658. 

- Zhou, C.M., Yang, S.Q., Chen, Y.G., Zhou, S.S., Li, Y.X., Qazi, A., 2023. How does topic consistency affect online review helpfulness? The role of review emotional intensity. Electron. Commer. Res. 23 (4), 2943–2978. 

**Ping Wang** is a Ph.D. student of Xiamen University. His research interests include tourism e-commerce and social media marketing. 

**Hailin Zhang** is an assistant professor at Xiamen University of Technology. His research focuses on word-of-mouth communication, new media marketing. 

12 

_P. Wang et al.                                                                                                                                                                                                                                   International Journal of Hospitality Management_ 

_International Journal of Hospitality Management 130 (2025) 104271_ 

**Xina Yuan** is a professor of marketing at Xiamen University. Her research interests include marketing strategy, and digital marketing. 

**Xiulin Zhang** is an account manager at Huawei Technologies Co., Ltd. 

13 

