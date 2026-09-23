

_Article_ 

# **A Two-Stage Nonlinear User Satisfaction Decision Model Based on Online Review Mining: Considering Non-Compensatory and Compensatory Stages** 

**Shugang Li**<sup>**1**</sup> **, Boyi Zhu**<sup>**1**</sup> **, Yuqi Zhang**<sup>**2**</sup> **, Fang Liu**<sup>**1,**</sup> *** and Zhaoxu Yu**<sup>**3**</sup> 

- 1 School of Management, Shanghai University, Shanghai 200444, China; westside_li@163.com (S.L.); boyi_star@163.com (B.Z.) 

- 2 College of Business, Jiaxing University, Jiaxing 314001, China; yuqi_2019@163.com 

- 3 Department of Automation, East China University of Science and Technology, Shanghai 200237, China; yu_yyzx@163.com 

- Correspondence: fiona_liu1996@163.com 

**Citation:** Li, S.; Zhu, B.; Zhang, Y.; Liu, F.; Yu, Z. A Two-Stage Nonlinear User Satisfaction Decision Model Based on Online Review Mining: Considering Non-Compensatory and Compensatory Stages. _J. Theor. Appl. Electron. Commer. Res._ **2024** , _19_ , 272–296. https://doi.org/ 10.3390/jtaer19010015 

Academic Editors: Chao Wen, Jiaming Fang and Benjamin George 

Received: 27 July 2023 Revised: 26 December 2023 Accepted: 16 January 2024 Published: 1 February 2024 



**Copyright:** © 2024 by the authors. Licensee MDPI, Basel, Switzerland. This article is an open access article distributed under the terms and conditions of the Creative Commons Attribution (CC BY) license (https:// creativecommons.org/licenses/by/ 4.0/). 

**Abstract:** Mining user satisfaction decision stages from online reviews is helpful for understanding user preferences and conducting user-centered product improvements. Therefore, this study develops a two-stage nonlinear user satisfaction decision model (USDM). First, we use word2vec technology and lexicon-based sentiment analysis to mine the sentiment polarity of each product attribute in the reviews. Then, we develop KANO mapping rules using utility functions to classify consumer preferences based on attribute importance. Based on this, a two-stage nonlinear USDM is developed to describe post-purchase evaluation behavior. In the first non-compensatory stage, consumers determine their initial satisfaction level based on the performance of basic attributes. If the performance of these attributes is poor, it is almost impossible for users to be satisfied. In the compensatory stage, the performance of the remaining attributes collectively affects final satisfaction through participation in user utility calculation. With the use of reviews from JD.com, we develop a genetic algorithm to determine feasible solutions for the USDM and verify its validity and robustness. The USDM is proven to be effective in predicting user satisfaction compared to other classic models and machine learning algorithms. This study provides a universal pattern for user satisfaction decisions and extends the study on preference analysis. 

**Keywords:** user satisfaction; satisfaction decision behavior; evaluation decision rules; preference mining; online reviews 

## **1. Introduction** 

User satisfaction is an indicator used to measure whether and to what extent consumers’ needs are met during the shopping experience, and it is the basis of users’ repeated purchase behaviors [1]. As a result of post-purchase product evaluation, the promoting effects of user satisfaction on expanding brand influence [2,3], cultivating customer loyalty [4,5], and improving product sales [6,7] have been confirmed by numerous studies. In the increasingly fierce market [8], whether enterprises can gain a competitive advantage depends on users’ satisfaction with their products and services. Practical evidence shows that the higher the user satisfaction, the stronger the product competitiveness, the larger the market share, and the better the enterprise’s income [9]. This makes it of great economic and social significance to explore the influencing factors and behavior mechanisms of user satisfaction decisions. Based on an in-depth understanding of user satisfaction decisionmaking behavior, enterprises can accurately analyze users’ differentiated preferences and their emphasis on product attributes [10], so as to realize user-centered product development. Traditionally, interviews, questionnaires, and behavioral experiments [11] are usually applied to observe the user satisfaction decision process, investigate feedback on products 

_J. Theor. Appl. Electron. Commer. Res._ **2024** , _19_ , 272–296. https://doi.org/10.3390/jtaer19010015 

https://www.mdpi.com/journal/jtaer 

_J. Theor. Appl. Electron. Commer. Res._ **2024** , _19_ 

273 

or services, and further provide support to product development and improvement. For example, Ding et al. [12] empirically analyzed the effect of the environment on hotel customer satisfaction. The results showed that tourists may maximize their satisfaction by choosing destinations that provide a good environment. Although these methods provide a direct understanding of user needs and behaviors, with good internal validity, they require more time and higher costs, and the quantity and characteristics of experimental samples are relatively limited. 

With the popularization of e-commerce, the internet has become the main carrier of shopping behaviors, and online reviews have emerged and converged into a new type of word-of-mouth marketing. As pieces of real feedback after purchasing, online reviews not only include more accessible information channels but also contain abundant information helpful to analyze user preferences [13], influencing factors, and mechanisms behind satisfaction decisions [14]. Phillips et al. [15] found through analyzing online review data from 442 hotels that hotel attributes such as room quality, internet availability, and infrastructure had the greatest impact on hotel performance, and positive reviews had the most influence on customer demand. Tang et al. [16] explored the factors influencing e-commerce website conversion rates from two aspects: the affective content and the communication style of online customer reviews. Levy et al. [17] analyzed 946,225 one-star online reviews of a certain hotel and identified front desk staff, bathroom issues, room cleanliness, and room noise as key factors leading to negative customer feedback. Online reviews are valuable sources of information for enterprises. Analyzing consumers’ preferences based on online reviews offers some important insights to understanding user needs and satisfaction decision mechanisms, and helps enterprises carry out product development activities. Hence, extracting user preferences and corresponding satisfaction levels from online reviews, excavating the decision-making stages and rules of evaluation behavior, and constructing a quantitative user satisfaction decision model have become promising research directions. 

Li et al. [18] identified the factors that influence hotel customer satisfaction through analyzing online reviews, and analyzed the importance of these factors and their relationship with customer satisfaction levels when booking luxury and economy hotels. Singh et al. [19] compared the perceptions of different hotel service quality attributes among travelers in religious and commercial destinations, as well as the impact of these attributes on customer satisfaction. Alhamad and Singh [20] researched the significant and minor factors influencing online hotel ratings in consumer reviews to enhance online ratings and customer satisfaction. Although existing research has provided ideas for building models of the impact of product or service attributes on user satisfaction, on one hand, these studies focus on exploring the factors influencing user satisfaction [21,22], with little attention being paid to the stages and processes of consumer satisfaction evaluation behavior. On the other hand, related research generally investigates the linear impact of product attributes, brand, and enterprise services on consumer satisfaction outcomes [23,24]. However, existing research has already established the existence of both non-compensatory and compensatory decision rules in consumer behavior. This means that consumers do not consider all attributes of a product in a comprehensive manner to compensate linearly for satisfaction decisions. Once certain attributes do not meet consumer expectations, even if other attributes perform well, consumers may feel disappointed. Singh and Alhamad [25] utilized the two-factor theory to uncover the key factors impacting online hotel ratings. They hypothesize that both satisfying and dissatisfying factors would influence a hotel’s rating, but satisfiers had a slightly greater effect than dissatisfiers. Furthermore, Zhang and von Dran [26] divided website design factors into two factors: hygiene factors, whose presence made a website functional and serviceable and whose absence caused user dissatisfaction, and motivator factors, which, on the other hand, were those that added value to the website by contributing to user satisfaction. They found that dissatisfaction with hygiene factors directly affected participants’ judgments of motivator factors. Zhang and von Dran [26] considered the interplay between two factors, but lacked a quantitative measurement of the impact of these factors on user satisfaction. Therefore, further exploration is needed on 

_J. Theor. Appl. Electron. Commer. Res._ **2024** , _19_ 

274 

how to quantitatively characterize the nonlinear impact of factors from the product and brand on user satisfaction. 

To fill this research gap, this study uses online review data to extract user needs, preferences, and satisfaction information from a large amount of unstructured text, while considering the nonlinear effects of relevant factors and analyzing the stages and decision principles of user satisfaction. From the perspective of evaluating decision-making behavior, the objective of our study is to excavate the mechanism behind user satisfaction decisions and establish a quantitative model reflecting the evaluation process of consumers. Taking an electronic product, namely smartphones, as an example, a two-stage nonlinear user satisfaction decision model (USDM) considering consumer preference is presented. Our main work includes the following steps. 

Firstly, in order to fully extract consumers’ sentiment intensity in relation to product attributes, an online review semantic mining method is designed using word2vec technology and lexicon-based sentiment analysis methods, and the sentiment vectors of each online review are calculated accordingly. Secondly, for the sake of describing consumers’ preferences for product attributes, we apply the utility function to develop the KANO mapping rules, through which product attributes are classified into various categories according to the importance users attach to them. Thirdly, as the key work of this study, a two-stage nonlinear USDM is developed to depict the post-purchase evaluation behavior accurately and comprehensively and analyze the impact of attribute performance on user satisfaction. We divide the user satisfaction decision into two stages and assume that they follow the non-compensatory decision rule and the compensatory decision rule, respectively. In the first non-compensatory stage, consumers decide on their initial satisfaction level based on the performance of the product’s basic attributes. If the performance of these attributes is poor, it is almost impossible for users to be satisfied with the product. In the second compensatory stage, the performance of the remaining attributes will collectively affect the final user satisfaction by participating in the user’s utility computing. Finally, a genetic algorithm (GA) is designed to adaptively find feasible solutions for the USDM, based on which the validity and robustness of the USDM are verified according to review data collected from JD.com. In order to prove the effectiveness of the UDSM in predicting user satisfaction, the USDM is compared with other classical models and machine learning algorithms, and the experimental results support the rationality of our proposed user satisfaction decision-making process and its rules. Our study makes an important contribution to the field of post-purchase evaluation and satisfaction decisions and sheds new light on the sentiment analysis of online reviews and user-centered product improvement. 

The remainder of this study is organized as follows. Section 2 reviews the relevant literature on user satisfaction, user preferences, and consumer decision making. Section 3 presents the framework of our study. In Section 4, the data processing and user preference analysis are performed. Section 5 describes a two-stage USDM, and Section 6 tests its robustness and validity. Further discussion and implications are provided in Section 7. Section 8 closes the paper with the conclusions, limitations, and future research. 

## **2. Literature Review** 

## _2.1. User Satisfaction and User Preferencess_ 

## 2.1.1. User Satisfaction 

As an evaluation indicator measuring whether and to what extent consumers’ established preferences are met [1], user satisfaction is not only the psychological state of pleasure or disappointment generated within users by commodities or services [27] but is also the result of consumers’ post-purchase evaluation behavior [28,29]. A considerable number of studies have proven that user satisfaction has a positive impact on promoting repurchasing [30], improving market share and profitability of organizations [6], building customer loyalty [4], and strengthening brand equity [31]. 

Previous studies have explored the influencing factors of user satisfaction to provide references for product development and improvement [13,29]. The earliest studies utilized 

_J. Theor. Appl. Electron. Commer. Res._ **2024** , _19_ 

275 

traditional empirical research methods such as questionnaires, interviews, and behavioral experiments. For example, McNamara and Kirakowski [32] constructed a user satisfaction system for e-commerce platforms and proposed a comprehensive model based on product quality, price, after-sales service, and other factors. Cohen et al. [33] measured user satisfaction along with several consumer behavior factors (e.g., emotion, loyalty, and trust). These methods allow for a direct understanding of user needs and behaviors and have good internal validity. However, they require greater costs and time, and the sample size for experiments is relatively limited [11]. 

With the rapid development of the internet and the gradual rise of online shopping platforms, the volume of user review data has dramatically increased. As massive and information-rich sources of data, user reviews are becoming an important research focus for more and more enterprises. Some scholars have attempted to study user satisfaction through online review data. Zhang et al. [23] explored the asymmetric effects of attribute performance (value, cleanliness, location, etc.) on the satisfaction of users with different geographic and cultural backgrounds using review data from hotels. Alhamad and Singh [21] utilized data mining techniques to extract important factors that influence consumer satisfaction from online hotel reviews, including comfort, cleanliness, and location. However, these studies only consider factors that influence consumer satisfaction and do not take into account consumer satisfaction (or dissatisfaction) when evaluating their purchase. Furthermore, existing research generally assumes linear effects of product attributes, brand, and enterprise services on satisfaction outcomes [23,24], ignoring that consumers may not comprehensively consider the advantages and disadvantages of all attributes to make compensatory linear satisfaction decisions. Research has shown that even if other attributes perform well, consumers will feel disappointed if certain attributes do not meet their expectations [26], leading to immediate negative actions. The quantification of the impact of product attributes and other influencing factors on user satisfaction and the characterization of the nonlinear effects of product and brand factors on user satisfaction are still areas that require further research. 

## 2.1.2. User Preferences 

The fundamental determinant of user satisfaction is whether user preferences are met by the products and services [1]. User preference refers to the degree of interest and importance that users show for certain things [34]. It is a comprehensive result of users’ inner weighing of commodities or services based on their own cognition and has a crucial influence on individual behavior and decision making. In the era of a demand-driven economy, companies must consider the market needs for product innovation and provide more comprehensive and unique products than competitors to meet user preferences [35]. Identifying user preferences from online reviews to form user portraits plays a key role in user analysis [36], product development [37], and marketing [38]. 

Numerous pieces of evidence suggest that consumers have various preferences for different attributes, that is, consumers pay different degrees of attention to product attributes [10]. Scholars have proposed a series of theories and models to characterize the different preferences of users towards products and attributes. Among them, Herzberg et al. [39] originally proposed the classic two-factor theory to explain the relationship between job satisfaction and motivation. The theory suggests that job satisfaction and motivation are influenced by two factors: hygiene factors and motivator factors. The former represents individuals’ basic needs and essential conditions for satisfaction, and its impact on job satisfaction and motivation is relatively limited. The latter includes factors such as achievement, recognition, and the nature of the work itself, which have a more positive impact on individual satisfaction and intrinsic motivation. Soliman [40] also indicated that when the environment (organization) adequately satisfied various needs, motivator factors became a stronger source of satisfaction compared to hygiene factors. If the environment deprived people of their various needs, hygiene factors would be more influential in causing dissatisfaction than motivator factors. Subsequently, Maddox [41] 

_J. Theor. Appl. Electron. Commer. Res._ **2024** , _19_ 

276 

further confirmed the validity of the two-factor theory. He argued that satisfaction and dissatisfaction are independent constructs, caused by different facets of interaction between a stimulus (job or product) and individuals. As these constructs are unrelated, individuals might feel both very satisfied and very dissatisfied at the same time. Koncar et al. [42] applied the two-factor theory to online employer–employee review data to study the factors influencing employee satisfaction. Singh and Alhamad [25] utilized two-factor theory (satisfiers and dissatisfiers) to uncover key factors influencing hotel ratings in online review data. They subsequently extended the theory to the four-factor theory (satisfiers, dissatisfiers, critical factors, and neutral factors) and predicted key factors impacting online hotel ratings through online consumer review data [43]. Although the two-factor theory and the four-factor theory, which comprehensively consider and explain work motivation and satisfaction, can provide a basic framework to characterize user preferences from the perspectives of basic needs and emotional value, they overlook the periodicity of user evaluation decision-making behavior and the nonlinearity and complexity of user preferences, making it difficult to fully explain and predict user complex preferences. 

The KANO model provides another perspective to explain user preferences [44]. The KANO model categorizes product attributes based on how much consumers value each attribute [45]. It classifies user preferences into five types: must-be, attractive, onedimensional, indifferent, and reverse [46–48]. Qi et al. [49] applied the joint analysis method and the KANO model to classify the attributes of laptop computers and obtain product improvement strategies. Zhao et al. [50] developed a strength–frequency KANO (SF-KANO) model, which considered the interaction between strength and frequency, to classify the demands expressed by different travelers in online reviews with the goal of maximizing traveler satisfaction at the lowest cost. Jiang and Li [51] proposed a method based on multi-dimensional sentiment analysis and the KANO model to quantify customer satisfaction by mining customer demand data from online reviews. 

Compared to the broader preference categorization method used in the two-factor theory, the KANO model emphasizes placing the user at the core of the analysis and provides a more detailed feature categorization. This helps to understand user needs, attribute priorities, and improvement directions more accurately. Additionally, by identifying expected attributes and attractive attributes, the KANO model offers more innovative directions for products or services to gain competitive advantages. Therefore, it is more suitable for user preference and product or service feature analysis [52]. Based on this, this study develops a KANO mapping rule to extract consumer demands, preferences, and satisfaction information regarding different product attributes from large amounts of unstructured text (online review data). It also considers the nonlinear impact of factors that influence consumer satisfaction and analyzes the stages and decision principles of the user satisfaction process. 

## _2.2. Post-Purchase Evaluation Decision-Making Behavior_ 

Consumer evaluation decision making belongs to the field of consumer behavior, which is a series of activities that consumers take to acquire, use, and process a good or service, and includes their decision-making behavior before and after these activities [53]. Due to the invisibility of individual psychological activities, user decision making is a part of the black box of consumers [54]. Generally speaking, consumer decisions refer to the purchase decisions of consumers. The American Marketing Association (AMA) states that consumer decision making comprises consumers making a detailed evaluation of the attributes of certain products, brands, or services, and making rational choices to complete the process of purchasing a product or service that meets their specific needs at the lowest cost [55]. Consumer evaluation refers to the satisfaction level given by consumers after using products based on the degree to which their demands are satisfied by the product and ancillary services [56]. And consumer evaluation decision making is the process through which consumers generate emotions for products and make satisfaction evaluations, which is an invisible consumer black box problem [35]. 

_J. Theor. Appl. Electron. Commer. Res._ **2024** , _19_ 

277 

From the perspective of consumers’ bounded rationality, decision-making rules are adopted by consumers according to the complexity and importance of decisions to be made in order to simplify the decision-making process. Consumer decision-making rules are divided into compensatory and non-compensatory decision rules [57]. To be specific, compensatory decision rules are a method of decision making based on utility computing [58], such as the simple additive rule and weighted additive rule [59]. The utility of optional product attributes is summarized as the total utility, and then the total utility of all optional products is compared [60]. The bad performance of some attributes can be compensated for by the good performance of other attributes under the compensatory decision rules, that is, a product can offset its deficiencies so that consumers can consider all optional products more comprehensively. Under the non-compensatory decision rules, consumers set restrictive requirements to simplify the decision-making process, excluding all optional products that do not meet their specific requirements [61]. Lexicographic rule, conjunctive rule, elimination by aspects (EBA) rule, etc., are typical non-compensatory decision rules. Among them, EBA is applied by the vast majority of existing literature to analyze consumer decisions [62]. According to EBA, consumers firstly select the most significant attributes in light of the perceived importance of product attributes, and then set a minimum required standard for each attribute, that is, the psychological threshold [63]. All optional products are screened under the same criteria, and products whose attribute performances are below the psychological thresholds are excluded. Consumers then apply other rules to evaluate the remaining products in the considered set. Although there are abundant studies on consumer decision-making theory, the decision-making process is still an unverifiable black box problem [64], and there is a lack of models and methods to comprehensively and accurately depict the decision-making processes of consumers. 

An evaluation decision is a type of consumer thinking decision. Individual cognitive science provides theoretical support for analyzing post-purchase evaluation behavior [65]. In cognitive psychology, the holistic–analytical cognitive model has been widely recognized [66]. The holistic cognitive model and analytical cognitive model are different information processing strategies [67]. The former treats the group as a whole and conducts analysis based on the internal relations between individuals. The latter identifies individual bodies in a group and analyzes their basic properties. Accordingly, under evaluation decision behavior, the holistic cognitive model states that consumers consider all of a product’s attributes to make decisions based on the overall impression of the product; that is, users evaluate the product following the compensatory decision rules. However, the analytical cognitive model is based on consumers’ use of independent judgment of a product’s attributes to determine their satisfaction level, which motivates users to adopt non-compensatory decision rules. Therefore, we infer that when users evaluate a product, they should first generate an overall impression of the product according to a holistic cognitive model, and then make a final decision on their satisfaction based on the consideration of the performance of different attributes. Specifically, in the first stage, users adopt non-compensatory rules and focus on the attributes they value most, based on which they decide whether they are basically satisfied or dissatisfied with the product. In the second stage, users adopt compensatory rules and fine-tune their satisfaction level by comprehensively considering other attributes on the basis of the first stage. However, existing research has seldom explored the behavioral mechanisms underlying the generation of satisfaction outcomes, neglecting the staged and procedural nature of product evaluation behaviors. There is also a lack of exploration into the decision principles for satisfaction at different stages. 

To fill these gaps, this study considers the nonlinear impact of product attributes on user satisfaction and analyzes the stages and decision principles involved in the process of user satisfaction generation. We design an online review semantic mining method to mine consumers’ preferences for different product attributes combine it with the utility function and KANO model. Subsequently, the non-compensatory and compensatory rules of purchase decisions are applied to evaluation behaviors, and a quantitative nonlinear 

_J. Theor. Appl. Electron. Commer. Res._ **2024** , _19_ 

278 

USDM is constructed that solves the black box caused by the invisibility of the product evaluation process. 

## **3. Research Framework** 

Mining users’ satisfaction decision behavior from online reviews can support usercentered product development. The objective of this study is to explore the mechanism of user satisfaction decisions and establish a quantitative model reflecting the evaluation process of consumers. Our study framework is shown in Figure 1. 



**Figure 1.** Research framework. 

Firstly, this work takes smartphones as the study object and crawls Chinese online reviews of various types of smartphones on JD.com as the data source. Therefore, it is necessary to transform the unstructured text into structured data for further analysis, which is the foundation of our study. As shown in part I of Figure 1, data crawling, lexicon construction (attribute lexicon, sentiment lexicon), and sentiment analysis are carried out to filter the reviews with low helpfulness through fine lexicon matching, and the sentiment vectors of the remaining reviews are calculated to reflect the user’s sentiment intensity for each product attribute. 

Secondly, to preliminary explore the relationship between the quality and performance of different attributes and user satisfaction, this study first develops a utility function model to obtain the degree of impact of positive and negative sentiments towards each attribute on the overall satisfaction. Then, the KANO mapping rules are designed according to KANO theory and the regression coefficients of the utility function; through these mapping rules, all smartphone attributes are divided into different categories based on user preferences, as shown in part II of Figure 1. 

Thirdly, in order to accurately describe the process and rules of satisfaction decisions and quantitatively analyze how each product attribute affects the overall satisfaction of users, the non-compensatory and compensatory decision theories are introduced, and a USDM in line with the individual thinking mode is proposed, which is also the focus of this study. Specifically, the decision-making process of user satisfaction is divided into the stage of non-compensatory EBA and the stage of compensatory utility calculation. The classification results of the KANO mapping rules are applied to determine which stage each attribute plays a role in. Through the integration of two decision-making stages, various attributes are comprehensively considered to form the final satisfaction level. Finally, a GA 

_J. Theor. Appl. Electron. Commer. Res._ **2024** , _19_ 

279 

is developed to adaptively train the function expressions and parameters of the UDSM, and the parameter analysis and model comparison are conducted to verify the robustness and effectiveness of the proposed model (see part III in Figure 1). 

## **4. Data Processing and User Preference Analysis** 

## _4.1. Data Collection_ 

The data collection work was carried out in September 2020. We obtained our data from JD.com, one of the largest e-commerce platforms in China. JD sells an enormous variety of products and primarily focuses on digital products. Our data concentrated on the smartphone market, and 93,612 online reviews of 50 different smartphone products were collected (reviews were published from 1 January 2020 to 1 September 2020). For each record, in addition to the product review text and corresponding star-rating (i.e., the satisfaction level), we also collected information such as users’ IP addresses, publicly available personal profiles, and product parameter information. Based on the preliminary analysis of this information, we found that (1) the reviews were posted by users of different types, including different ages, genders, and regions; (2) the 50 smartphones were from 12 mainstream phone brands, and there were significant differences in parameters and prices; (3) the number of reviews for each phone was between 1500 and 2000, and there was no imbalance in quantity; (4) the distribution of satisfaction ratings showed a skewed distribution, and highly satisfied (5-star reviews) and highly dissatisfied (1-star reviews) users were more frequent, with satisfied reviews accounting for 67%. This is also consistent with Ullah et al.’s [68] observation that “the distribution of satisfaction polarity in online reviews shows a bimodal distribution”. Excluding default system reviews and reviews with empty content, a total of 91,544 reviews were included in the subsequent data preprocessing. 

## _4.2. Data Processing_ 

Natural language processing (NLP) techniques are applied to determine the sentiment attitudes towards the product attributes for further analysis. The dictionary-based approach is a common NLP technique that uses pre-defined topic dictionaries or sentiment lexicons to extract keywords, identify named entities, and perform sentiment analysis from text [69]. However, this approach relies on pre-defined dictionaries and may not directly apply to sentiment analysis in specific domains lacking mature dictionaries [70]. The Word2Vec technique partially addresses the limitations of this approach. It is a neural network-based word-embedding model that learns the contextual relationships in large corpora and maps words to continuous vector spaces, enabling the comparison of word associations and similarity [71,72]. It can discover new words that are not covered by dictionary-based methods. Therefore, this study uses both pre-defined dictionaries and Word2Vec models to extract new vocabularies in specific domains, fully incorporating the semantic relationships of the context. We constructed attribute and sentiment dictionaries that cover all product attributes and emotional colors in the smartphone domain. Based on these dictionaries, we can accurately mine the polarity of user sentiment towards smart product attributes in online reviews. 

Firstly, data preprocessing was conducted. After cleaning the raw review data by removing unnecessary punctuation marks, special characters, HTML tags, and spelling errors, the Jieba word segmentation technology was used for word segmentation, and POS (part-of-speech) tagging was performed on the segmented words. Then, a pre-defined stop word list was used to filter out common meaningless words in the text. Subsequently, the word frequency and part of speech were counted, and the candidate lexicon ranked according to word frequency was formed. 

Secondly, word2vec technology [71,72], an open-source tool for word vector calculation, was adopted to construct the attribute lexicon of smartphones. It computes the word vector of the center word by calculating the probability of its co-occurrence with a background word in a certain word window and then compares their semantic simi- 

_J. Theor. Appl. Electron. Commer. Res._ **2024** , _19_ 

280 

larity by calculating the cosine similarity of their word vectors. Using online reviews as input, a word2vec model for comparing word similarity was established. By interviewing professional smartphone developers and referring to the literature on mobile phone products [8,57], the attributes of smartphones were classified into 12 categories: signal, battery, sound quality, storage, processor, camera, screen, network, system, unlock method, appearance, and brand. As shown in Table 1, seed words for each attribute with frequencies greater than 500 were selected from the candidate lexicon. To identify all attribute words of smartphones from online reviews, we applied the word2vec model to obtain words with high similarity with seed words (i.e., the cosine similarity between them is greater than 0.7), after which the attribute lexicon (including 12 kinds of attributes and 429 specific attribute words) was constructed. 

**Table 1.** Attribute classification and seed words of each attribute. 

|**Attribute**|**Seed Words**|**Attribute**|**Seed Words**|
|---|---|---|---|
|Signal|signal; baseband; call, etc.|Screen|screen; resolution; display; clarity, etc.|
|Battery|battery; standby; power, etc.|Network|WI-FI; internet; wireless, etc.|
|Sound quality<br>Storage|sound effects; voice; horn, etc.<br>memory; 256 GB; storage capacity, etc.|System<br>Unlock<br>method|system; iOS, etc.<br>unlock; fingerprint; facial recognition, etc.|
|Processor|chip; CPU; A12, etc.|Appearance|appearance; color; size, etc.|
|Camera|camera; photo; pixel, etc.|Brand|iPhone; Apple, etc.|



Thirdly, a sentiment lexicon was constructed based on the Hownet lexicon and the word2vec model [73]. Specifically, first of all, the candidate lexicon was scanned to identify the words existing in the Hownet lexicon and add them to the sentiment lexicon. In order to make the sentiment words more suitable to the characteristics of smartphones, the semantic similarity between the remaining words in the candidate lexicon and the existing words in the sentiment lexicon was calculated. Finally, the sentiment lexicon containing 536 positive-sentiment words and 364 negative-sentiment words was formed. 

Finally, user sentiment intensity with product attributes in each review was analyzed by matching the attribute words and sentiment words. The following structural processing was conducted for each unstructured online review: 

Step 1: Segment the review text and identify all attribute words according to the attribute lexicon. 

Step 2: For each attribute word, determine the corresponding description text in the review. 

Step 3: Search for sentiment words within the corresponding description text of each attribute, and make a semantic judgment based on negative or positive words. _Xj_<sup>_pos_</sup> and _Xj_<sup>_neg_</sup> represent the value of positive and negative sentiment, respectively, on attribute _j_ . If users have positive feelings towards attribute _j_ , _Xj_<sup>_pos_</sup> = 1, _Xj_<sup>_neg_</sup> = 0. If users have negative feelings towards attribute _j_ , _Xj_<sup>_pos_</sup> = 0, _Xj_<sup>_neg_</sup> = 1. If users do not evaluate an attribute, both _Xj_<sup>_pos_</sup> and _Xj_<sup>_neg_</sup> will be equal to 0. Step 4: Summarize the positive and negative sentiment of 12 attributes in this review to form its sentiment vector ( _X_ 1<sup>_pos_</sup> , _X_ 1<sup>_neg_</sup> , . . . . . . , _X_ 12<sup>_pos_,</sup><sup>_X_</sup> 12<sup>_neg_).</sup> 

If all elements in the sentiment vector of a review are 0, it is deemed that the review does not provide valuable information, and thus should be excluded from the data. Therefore, 89,768 valid review pieces were finally included in our subsequent analysis. This ensures that the subsequent study is based on review data containing rich attribute and sentiment information. 

## _4.3. User Preference Analysis_ 

To analyze how much users value different product attributes and extract the features of consumer preferences, the utility function and the KANO mapping rules are developed based on all the sentiment vectors of online reviews, through which the product attributes are classified according to consumer preferences. 

_J. Theor. Appl. Electron. Commer. Res._ **2024** , _19_ 

281 

## 4.3.1. The Consumer Utility Function Model 

The utility function is established first to explore the impact of different attribute performances on user satisfaction. In general, the utility function depicts the quantitative relationship between the utility perceived by consumers and the combination of products purchased and measures the satisfaction level that consumers obtain through consuming behavior [49,74]. In our study, consumers’ positive and negative sentiments for each attribute are used to represent attribute performance, and the star-rating of each review reflects their level of satisfaction with the product. The definition of the utility function model is as follows: 



where _y_ is the value of satisfaction and is measured by a star-rating, ranging from 1 to 5. As illustrated in Section 4.2, _Xj_<sup>_pos_</sup> and _Xj_<sup>_neg_</sup> denote the positive and negative sentiment of attribute _j_ , respectively, in the corresponding review. _β_<sup>_pos_</sup> _j_ and _β_<sup>_neg_</sup> _j_ are the coefficients of positive sentiment and negative sentiment, respectively, which can be used to analyze the consumer preference for attribute _j_ . 

It is worth noting that the regression coefficients of the utility function can only represent the importance of product attributes from a linear perspective, without considering the nonlinear features of consumer preferences for product attributes, for example, curved decreasing or increasing trends or saturation effects. These nonlinear relationships remind us to fully consider consumers’ perceptions and emotional responses to different attributes in product design and improvement in order to better meet their needs and enhance product satisfaction. Therefore, in order to comprehensively and accurately characterize user preferences and capture nonlinear relationships, we quantify consumer preferences for product attributes based on the KANO theory and the regression coefficients of utility function. 

## 4.3.2. The KANO Mapping Rules 

In this section, consumer preferences for product attribute performance are analyzed, and product attributes are subsequently classified by the established KANO mapping rules. The KANO model, proposed by Noriaki KANO, reflects the nonlinear relationship between product quality and user satisfaction based on the analysis of consumer needs [46–48]. In Figure 2, according to the relationship between attribute quality (namely attribute performance) and user satisfaction, product attributes are divided into five categories: 

- (1) Must-be Attribute: This corresponds to the basic functions of products. When the attribute’s performance is inadequate, users will be unsatisfied. However, if the attribute is improved after it is qualified, the user will not be more satisfied. 

- (2) Attractive Attribute: When the attribute’s performance is insufficient, user satisfaction will not decrease significantly. But, as the quality of this attribute improves, user satisfaction will increase significantly. 

- (3) One-dimensional Attribute: User satisfaction is approximately proportional to attribute performance. 

- (4) Indifferent Attribute: No matter how the attribute’s performance changes, user satisfaction will not be affected. 

- (5) Reverse Attribute: User satisfaction decreases if the attribute’s performance is improved. According to the above definitions, the KANO mapping rules are designed based on 

- _β_<sup>_pos_</sup> _j_ and _β_<sup>_neg_</sup> _j_ , as calculated by the utility function. 

_J. Theor. Appl. Electron. Commer. Res._ **2024** , _19_ 

282 



**Figure 2.** The KANO model [46]. 

Classification rules are shown in Figure 3 and Table 2, where _ϑ_ and _σ_ are two positive hyperparameters greater than 0. _ϑ_ is set to measure the significance of _β_<sup>_pos_</sup> and _β_<sup>_neg_</sup> . When _β_ is lower than _ϑ_ , it is considered to be close to 0. _σ_ is set to estimate the similarity between the impact of positive and negative attribute performances on user satisfaction, namely _β_<sup>_pos_</sup> and _β_<sup>_neg_</sup> . For example, for attribute j, _β_<sup>_pos_</sup> _j_ = 0.03, _β_<sup>_neg_</sup> _j_ = 0.045. If _σ_ = 2 and _β_<sup>_pos_</sup> _j > σ_<sup><u>1</u></sup><sup>_βneg_</sup> _j_ , it can be concluded that _β_<sup>_pos_</sup> _j_ and _β_<sup>_neg_</sup> _j_ have similar values; that is, user satisfaction is proportional to attribute performance, indicating attribute j should be one-dimensional. But if _σ_ = 1.1, the difference between _β_<sup>_pos_</sup> _j_ and _β_<sup>_neg_</sup> _j_ is considered large, and attribute j should be a must-be attribute. Questionable attributes refer to the value ranges in Figure 3, which cannot be reasonably explained in reality. For instance, values in the fourth quadrant denote that user satisfaction increases regardless of whether the attribute’s performance improves or degrades. 



**Figure 3.** The KANO mapping rules. 

_J. Theor. Appl. Electron. Commer. Res._ **2024** , _19_ 

283 

**Table 2.** The KANO mapping rules based on the regression coefficients of positive and negative sentiment. 

|**Mapping Rule**|**Attribute Category**|
|---|---|
|_β_<sup>_pos _</sup>_> ϑ_&_β_<sup>_neg _</sup>_> ϑ_&_β_<sup>_neg _</sup>_>_ <sup>1</sup><br>_σ _<sup>_βpos_&</sup><sup>_βneg < σβpos_</sup>|One-dimensional|
|_β_<sup>_pos _</sup>_< −ϑ_&_β_<sup>_neg _</sup>_< ϑ_;_−ϑ < β_<sup>_pos _</sup>_< ϑ_&_β_<sup>_neg _</sup>_< −ϑ_;<br>|Reverse|
|_β_<sup>_pos _</sup>_> ϑ_&_|β _<sup>_neg_��</sup>�_< ϑ_;_β_<sup>_neg _</sup>_> ϑ_&_β_<sup>_neg _</sup>_<_ <sup>1</sup><br>_σ _<sup>_βpos_</sup>|Attractive|
|_|β_<sup>_pos_</sup>_| < θ_&_β_<sup>_neg _</sup>_> θ_;_β_<sup>_pos _</sup>_> ϑ_&_β_<sup>_neg _</sup>_> σβ_<sup>_pos_</sup><br>_|β_<sup>_pos_</sup>_| < ϑ_&_|β_<sup>_neg_</sup>_| < ϑ_|Must-be<br>Indifferent|
|_β_<sup>_pos _</sup>_< −ϑ_&_β_<sup>_neg _</sup>_> ϑ_;_β_<sup>_pos _</sup>_> ϑ_&_β_<sup>_neg _</sup>_< −ϑ_;|Questionable|



Overall, KANO mapping rules provide a quantitative way to finely identify consumers’ preferences for different product attributes based on their importance. However, the above KANO model can only characterize the impact of a single attribute on consumer satisfaction evaluation decisions. In fact, when making satisfaction evaluation decisions, consumers often consider multiple attributes in a comprehensive manner. Therefore, relying solely on KANO mapping cannot fully capture the impact of product attributes on consumer satisfaction. Based on this, we propose a two-stage USDM which uses the KANO model to classify attributes and provide consumers with an overall satisfaction evaluation decision in each stage. 

## 4.3.3. Experimental Results 

In this section, we regressed the utility function model with the sentiment vectors and star-ratings of 89,768 valid reviews to calculate the regression coefficients _β_<sup>_pos_</sup> _j_ and _β_<sup>_neg_</sup> _j_ . Based on this, all attributes were mapped into five categories according to the KANO mapping rules. Taking _ϑ_ = 0.001 and _σ_ = 4.5, the regression coefficients and attribute classification results were determined as shown in Table 3. 

**Table 3.** The regression coefficients of the utility function and attribute classification results. 

|**Attribute**|**_β_**<sup>**_pos_**</sup><br>**_j_**|**_p_ Value**|**_β_**<sup>**_neg_**</sup><br>**_j_**|**_p_ Value**|**Category**|
|---|---|---|---|---|---|
|Signal|0.0019|0.135|0.2446|***|Must-be|
|Battery|_−_0.0002|**|0.1439|***|Must-be|
|Sound quality|0.0040|*|0.0168|***|One-dimensional|
|<br>Storage|0.0143|***|0.0000|0.326|Attractive|
|Processor|0.0101|***|0.0653|***|Must-be|
|Camera|0.0069|**|0.0352|**|Must-be|
|Screen|0.0102|***|0.0667|***|Must-be|
|Network|0.0187|***|0.1437|***|Must-be|
|System|0.0123|***|0.1106|***|Must-be|
|Unlock method|0.0124|***|0.00272|*|Attractive|
|Appearance|0.0105|***|0.1315|***|Must-be|
|Brand|0.0122|***|0.1234|***|Must-be|



Note: ***, **, and * are statistically significant at the 0.001, 0.01, and 0.05 level, respectively. 

It can be seen from Table 3 that the 12 smartphone attributes are classified into must-be attributes, one-dimensional attributes, and attractive attributes. As developed products, it is reasonable to conclude that there are no indifferent or reverse attributes for smartphones. All 12 attributes have positive effects on use satisfaction, although consumers attach different levels of importance to them. 

So far, 12 attributes of smartphones have been divided into five categories. Since consumers attach different levels of importance to these five categories, we use the categories of the attributes to represent user preferences in the following study. 

## **5. A Two-Stage USDM** 

In this section, the sum of positive sentiment _X_<sup>_pos_</sup> and negative sentiment _X_<sup>_neg_</sup> is calculated and labeled as _x_ to represent the performance of attribute j, and the star-rating is used to denote user satisfaction. To depict the user satisfaction decision process and analyze the influence of consumer preferences with different attributes, we divide the post-purchase evaluation decision into two stages and apply the non-compensatory and compensatory rules of purchase decisions, respectively, through which the USDM is proposed and trained 

_J. Theor. Appl. Electron. Commer. Res._ **2024** , _19_ 

284 

by a GA, overcoming the problem that classical optimization methods cannot generate precise expressions in complex nonlinear space comprehensively and accurately. 

## _5.1. The Framework of the USDM_ 

## 5.1.1. The Concept of the USDM 

The non-compensatory and compensatory rules are commonly used to describe a consumer’s two-stage decision-making process [75,76]. Therefore, this study considers the user post-purchase evaluation behavior as a two-stage satisfaction decision-making process and integrates the two kinds of decision rules to form the USDM, as shown in Figure 4. 



**Figure 4.** The concept of the USDM. 

In the first stage, consumers decide their initial level of user satisfaction. Generally speaking, this process is based on non-compensatory rules; that is, the disadvantages of some attributes cannot be compensated by the advantages of other attributes when consumers evaluate a product [75,76]. As a typical non-compensatory rule, the EBA rule can effectively characterize the process [62]. In EBA, consumers select some basic attributes of the products according to their perceived importance and set minimum standards for them (i.e., the satisfaction threshold of each attribute). 

The basic attributes of a product are directly related to the product’s function. Zhang and von Dran [26] suggested that basic attributes were the minimum user expectations of a product, and if these attributes were lacking or failed to meet the user’s threshold, the user would be dissatisfied or even refuse to use the product. The studies conducted by Alhamad and Singh [20] and Singh and Alhamad [25] also confirmed that the importance of different product attributes on consumer satisfaction varied. In KANO theory, must-be attributes refer to the minimum requirements and basic expectations that users have for a product which do not significantly promote user satisfaction if met but will result in extreme dissatisfaction if they are not met [46–48]. Hence, these basic attributes correspond to the must-be attributes in Section 4.3, which are the attributes or functions that users deem necessary for the product to have. 

Therefore, we propose that in the process of user satisfaction decisions, consumers adopt the EBA rule to determine the initial level of satisfaction ( _ωEBA_ ) according to the performance of must-be attributes first. Among all must-be attributes, if the performance of one is too low to reach users’ psychological threshold, even if other attributes perform well, users will still be dissatisfied with the product. 

In the second stage, consumers comprehensively consider the other four categories of attributes to give the final satisfaction decision. Another consumer purchasing decision rule, the compensatory decision rule, is a decision-making method based on utility computing, in which the advantages and disadvantages of product attributes can compensate each other, and consumers take various attributes of a product into comprehensive consideration [61]. We believe that after consumers evaluate the must-be product attributes based on the EBA 

_J. Theor. Appl. Electron. Commer. Res._ **2024** , _19_ 

285 

rule and generate preliminary satisfaction evaluation, they will comprehensively consider the performance of the other attributes to determine their perceived utility and finally decide their final satisfaction level. In this stage, consumers combine their preferences for the remaining four KANO attributes, including attractive attributes, one-dimensional attributes, indifferent attributes, and reverse attributes, to calculate the compensatory effect of the performance of these attributes on their perceived utility, resulting in the satisfaction level of this stage ( _ωutility_ ). 

It should be noted that this two-stage USDM is particularly suitable for high-value and innovative products, which tend to have more attributes and involve a more complex decision-making process for consumers. For low-value products or products with fewer attributes that consumers habitually purchase, there is no need to use the two-stage USDM. Judgments and decisions can be made based on the first stage of the model alone. 

## 5.1.2. The Expressions of Five KANO Attributes 

In this part, to build a quantitative model of user satisfaction decisions, a series of basic mathematical expressions are designed for five KANO attributes (see Section 4.3) to describe the relationship between the performance of product attributes (i.e., user sentiment, ~~labeled as~~ _~~x~~_ ~~) and user satisfaction (i.e., the utility, labeled as~~ _~~φ~~_ ~~). As shown in Table 4, the~~ curves between the performance of product attributes and user satisfaction include a ~~logarithmic function, power function, exponential function, linear function, and constant~~ function. Among them, <u>p1, p2, and p3 are the coefficients that make the curves conform to the relationship between an attribute’s performance x and user’s satisfaction with the current attribute</u> _<u>φ</u>_ <u>according to KANO theory.</u> 

**~~Table 4.~~** ~~The curves and expressions between the performance of different attributes and user satisfaction.~~ 

|**Attribute**|**Graph of Curve**|**Expressions**|
|---|---|---|
||Satisfied||
|Must-be<br>attribute|Sufficient|Logarithmic function: _φ_= _p_1_ln_(_x_+_p_2),_p_1 _>_0,_x > −p_2<br>Power function: _φ_= _p_1<br>�<br>_x −p_3)<sup>_p_2</sup>,_x > p_3,_p_1 _<_0,_p_2 _<_0<br>~~Exponential function:~~ _φ_~~=~~ _~~p~~_1_~~p~~_2<sup>_~~−x~~_</sup>~~,~~_~~p~~_1 _~~<~~_~~0,~~_~~p~~_2 _~~>~~_~~1~~|
||~~Satisfied~~||
|Attractive<br>attribute|Sufficient|Power function: _φ_= _p_1<br>�<br>_x −p_3)<sup>_p_2</sup>,_x < p_3,_p_1 _>_0,_p_2 _<_0<br>Exponential function: _y_= _p_1_p_2<sup>_x_</sup>,_p_1 _>_0,_p_2 _>_1|
||~~Satisfied~~||
|One-dimensional<br>attribute|Sufficient|Linear function: _φ_= _p_1_x_,_p_1 _>_0|



_J. Theor. Appl. Electron. Commer. Res._ **2024** , _19_ 

286 

**~~Table 4.~~** _~~Cont.~~_ 

|**Attribute**|**Graphof Curve**|**Expressions**|
|---|---|---|
||Satisfied||
|Indifferent<br>attribute|Sufficient|Constant function: _φ_= _p_1|
|Reverse<br>attribute|5.1.3. The Quantitative form o<br>~~After introducing the con~~<br>sponding to the five KANO a     i<br>first stage using the EBA rule,<br>attributes’ performances in thi|Logarithmic function: _φ_= _p_1_ln_(_x_+_p_2), _p_1 _<_0,_x_+_p_2 _>_0<br>Power function: _φ_= _p_1<br>�<br>_x −p_3)<sup>_p_2</sup>,_x < p_3,_p_1 _<_0,_p_2 _<_0<br>Exponential function: _φ_= _p_1_p_2<sup>_−x_</sup>, _p_2 _>_1,_p_1 _>_0 or<br>_y_= _p_1_p_2<sup>_x_</sup>, _p_2 _>_1,_p_1 _<_0<br>Linear function: _φ_= _p_1_x_, _p_1 _<_0<br>f the USDM<br>~~cept of the USDM and the mathematical expressions corre-~~<br>i  ttributes, the two-stage USDM is quantified. Firstly, in the<br>i      the initial level of user satisfaction (_ωEBA_) with all must-be<br>s stage is calculated as follows:|
||_ωEB_|_A_ =<br>�_Q_1,_∀φi ≥qi_ ,_i ∈must −be_<br>_Q_2,_∃φi < qi_ ,_i ∈must −be_<br>(2)|



~~After introducing the concept of the USDM and the mathematical expressions corre-~~ sponding to the five KANO attributes, the two-stage USDM is quantified. Firstly, in the first stage using the EBA rule, the initial level of user satisfaction ( _ωEBA_ ) with all must-be attributes’ performances in this stage is calculated as follows: 

In Formula (2), _φi_ is the user satisfaction level with the performance of the must-be attribute _i_ and is calculated by the optimal expression trained from the expressions of must-be attributes (in Table 4). _qi_ is the satisfaction threshold of attribute _i_ . Only when all must-be attributes satisfy _φi ≥ qi_ will consumers make a higher evaluation _Q_ 1, reflecting that they are mostly satisfied. If the performance of attribute _i_ fails to meet the threshold, that is, _φi < qi_ , consumers will give a lower, unsatisfactory evaluation _Q_ 2. Given that the final satisfaction ranges from 1 to 5 and is the combined result of the two-stage decision process, the values of _Q_ 1 and _Q_ 2 should be set between [0, 5] and _Q_ 1 _< Q_ 2. That is, when a must-be attribute performs poorly, no matter how sufficiently the other attributes perform, it is quite difficult for the product to obtain a rating of 5. 

Next, in the second stage, according to the compensatory utility computing rule, consumers’ satisfaction with the other four categories of attributes, _ωutility_ , is calculated by using the following linear formula to add up the satisfaction with each attribute: _ωutility_ = ∑ _i∈one−dimensional φi_ + ∑ _i∈attractive φi_ + ∑ _i∈indi f f erent φi_ + ∑ _i∈reverse φi_ + _α_ (3) 

where _φi_ is the user satisfaction level for the performance of attribute _j_ and is determined according to its best-fit expression trained from the optimal expressions of this kind of attribute (in Table 4) by GA. _ωutility_ is the sum of _φi_ for the attributes that participate in utility computing. _α_ is a constant. 

Finally, by adding the results of these two stages, the final user satisfaction with the product is obtained, as shown in Formula (4): 



In Formula (4), y is the result of the satisfaction decision, measured by the reviewer’s star-rating, and has a range of [1, 5]. At this point, the two-stage quantitative USDM is constructed. 

_J. Theor. Appl. Electron. Commer. Res._ **2024** , _19_ 

287 

## _5.2. The GA of the USDM_ 

The GA is applied to train the USDM and search for the optimal setting and parameters of the model that best fit the actual data. The GA, which is commonly used to search for the best solution by simulating natural evolution, is independent of local minimum problems [77]. In this study, the GA encodes feasible solutions into chromosomes with a certain genetic structure. A mixed encoding of symbols and float encoding is applied. The chromosome encoding is shown in Figure 5. 



**Figure 5.** The chromosome of GA. 

In Figure 5, _m_ represents the number of product attributes, _n_ is the number of must-be attributes, and the length of a chromosome is 4 _m_ + _n_ + 3. The first part of the chromosome, with a length of _m_ , contains the expression symbols corresponding to each attribute. Symbol encoding is used in this part and the range of _fi_ is [a, b, c, d, e], indicating that the expression of this attribute in the position is a logarithmic, power, exponential, linear, or constant function, respectively. The rest of the chromosome applies float encoding to represent the parameters of the expressions and the model. Specifically, the second part comprises the expression parameters of _m_ attributes. The length of this part is 3 m because each expression takes no more than three parameters according to Table 4. The third part is the threshold of must-be attributes, so the length is n, and each position corresponds to a threshold _qi_ . The fourth part is the evaluation result of the first stage, which contains two elements, which are _Q_ 1 and _Q_ 2 in Section 5.1.3. The fifth part is the constant term _α_ in stage 2. 

In order to reduce the error between the actual value and predicted value, a fitness function is constructed based on mean squared error (MSE). The definition of MSE is shown in Formula (5), and the fitness function is shown in Formula (6). 





The process of the GA for generating precise expressions of the USDM is as follows: Step 1: Initialization. Generate chromosomes randomly and ensure that each initial chromosome is a feasible solution that conforms to the type of expressions and parameter value range. Set the crossover and mutation probability. 

Step 2: Calculate the fitness of individuals in this population. 

Step 3: Selection. Selection is a process of survival of the fittest based on fitness. This study selects random roulette methods for selection and sets an elite retention strategy to retain the best-performing individuals. 

Step 4: Crossover and mutation. A new generation of the population is generated through single-point crossover, multi-point crossover, and mutation, and the values of the last four parts of chromosomes vary within a reasonable range. 

Step 5: Termination. The algorithm terminates when it iterates the specified number of times. If not, repeat steps 2–4. 

## _5.3. Experimental Results_ 

In this section, the USDM was validated with 89,768 pieces of online reviews collected from JD.com. After performing the utility function regression and KANO-based product 

_J. Theor. Appl. Electron. Commer. Res._ **2024** , _19_ 

288 

attribute mapping, consumer preferences were identified, based on which the USDM was trained. 

We developed a GA program through MATLAB. We randomly selected 80% of the 89,768 valid online reviews as the training data and the remaining 20% were used as test data to train the USDM. In the GA, the population size was set as 100; the crossover and mutation probability were 0.3 and 0.1, respectively; and the program was terminated after 1000 iterations. By minimizing the MSE of the training process, the mathematical expression for quantifying the user satisfaction decision was finally determined. We found that the most appropriate expressions of signal, battery, processor, system, appearance, and brand were in logarithmic form; the sound quality was a linear function; and storage, camera, screen, and unlock method were suitably described by the exponential form. On this basis, the parameters of each expression were trained. In addition, the thresholds of nine must-be attributes, the initial level of user satisfaction in the first stage _Q_ 1 and _Q_ 2, and the constant term _α_ in Formula (3) were determined. The MSE of this trained USDM was 0.000509 on the training set and 0.000556 on the test set. 

## **6. Model Tests** 

In order to verify the effectiveness of the UDSM in predicting user satisfaction and further support the rationality of our proposed user satisfaction decision-making process and rules, an analysis of the parameters was carried out, and a series of machine learning models and regression models were selected for comparison with USDM in this section. 

## _6.1. Parameter Analysis_ 

The values of _ϑ_ and _σ_ in the KANO mapping rules directly impact the classification of product attributes, which in turn affects the choice of curve form and coefficient between attribute performance and satisfaction. This parameter sensitivity ultimately leads to differences in the fitting results of the model. Therefore, by referring to existing research [78,79], we conducted a parameter analysis for _ϑ_ and _σ_ to verify the robustness/sensitivity of the model training results at different levels of _ϑ_ and _σ_ . 

If the values of _ϑ_ and _σ_ in the KANO mapping rules change, the attribute classification results will change accordingly. In this section, the training set and test set in Section 4.3 were used to train the USDM through the GA. Ranging the value of _ϑ_ from 0.0005 to 0.005 and setting _σ_ = 4.5, Figure 6 describes the changes in the USDM’s performance over the range of _ϑ_ values. Similarly, by increasing the value of _σ_ from 1.5 to 6 and keeping _ϑ_ = 0.001, the effect of _σ_ on the USDM’s performance is shown in Figure 7. 



**Figure 6.** The impact of _ϑ_ on the performance of USDM. 

_J. Theor. Appl. Electron. Commer. Res._ **2024** , _19_ 

289 



**Figure 7.** The impact of _σ_ on the performance of USDM. 

In Figure 6, the MSE of the training sets and the MSE of the test sets are identical when _ϑ_ is between 0.0005 and 0.004. We focus on the reason for the gradual increase in MSE as _ϑ_ exceeds 0.004, and analyze the method of selecting parameters to avoid special cases. Firstly, we sequentially set _ϑ_ to values ranging from 0.0005 to 0.004, and find that the KANO mapping results are consistent with the corresponding types of each attribute shown in Table 3. However, when _ϑ_ is set to 0.0045 and 0.005, the change in the KANO classification of some attributes causes the GA to have different selections of expressions and weights during training, leading to an increase in the MSE. Similarly, the change in _σ_ in Figure 7 causes a change in the KANO mapping results, which in turn results in a change in the MSE. Moreover, even with the special case of bimodal distribution in the satisfaction data used in this study, the MSE values for both the training and test sets are lowest when _σ_ = 4.5. 

Therefore, on the one hand, this proves that the USDM can achieve the best performance when _ϑ_ = 0.001 and _σ_ = 4.5, indicating that the attribute classification results are reasonable. On the other hand, the robustness and adaptability of USDM are confirmed, as the MSE does not fluctuate much over _ϑ_ and _σ_ . More importantly, the special phenomenon of a sudden increase in MSE suggests that the robustness and predictive validity of the USDM mainly depend on the accuracy of the KANO mapping results. In other words, the accuracy of predicting user satisfaction should be based on accurately identifying consumer preferences for product attributes. And the effectiveness of user preference analysis can be verified by validating the MSE of the model training in reverse. 

## _6.2. Models Comparison_ 

To validate whether the two-stage USDM proposed in this study can effectively predict user satisfaction, similar to Chen et al. [80], we employed a model comparison method to compare the fitting and error levels of the USDM with commonly used machine learning models and regression models. Specifically, we compared our model with 12 machine learning models and regression models. These machine learning models were composed of back-propagation neural networks (BPNNs) [78], general regression neural networks (GRNNs) [79], strict and approximate radial basis function neural networks (RBFNNs) [80], and support vector machine (SVM) [81]. Seven types of regression models were selected: multiple linear regression (MLR), log-linear models RG1-RG3 (the differences between RG1-RG3 are shown in Table 5), reciprocal linear model RG4, and polynomial regression models PR1-PR2 (PR1 is a quadratic polynomial and PR2 is cubic). 

_J. Theor. Appl. Electron. Commer. Res._ **2024** , _19_ 

290 

**Table 5.** _R_<sup>2</sup> and MSE of models. 

|**Models**|**USDM**|**BPNN**|**GRNN**|**Strict RBFNN**|**Approximate RBFNN**|
|---|---|---|---|---|---|
|R<sup>2</sup>|0.052719|0.460879|0.180084|0.455696|0.455696|
|Training MSE|0.000516|0.006996|0.000470|0.000311|0.000311|
|Test MSE|0.000538|0.006893|0.000556|0.001110|0.001110|
|**Models**|**SVM regression**|**MLR**|**RG1:**<br>**ln**(1/**_y_**) =**_a_**+**_blnx_**|**RG2:**<br>**ln****_y_**=**_a_**+**_bx_**|**RG3:**<br>**_y_**=**_a_**+**_blnx_**|
|R<sup>2</sup>|0.234577|0.033737|0.035314|0.033747|0.005082|
|Training MSE|0.001117|0.000553|0.000553|0.000553|0.000570|
|<br>Test MSE|0.001126|0.000581|0.000580|0.000581|0.000592|
|**Models**|**RG4:**<br>1/**_y_**=**_a_**+**_be_**<sup>(1/</sup><sup>**_x_**)</sup>|**PR1:**<br>**_y_**=**_a_**+**_bx_**+**_cx_**<sup>2</sup>|**PR2:**<br>**_y_**=**_a_**+**_bx_**+**_cx_**<sup>2 </sup>+**_dx_**<sup>3</sup>|||
|R<sup>2</sup>|0.031751|0.054268|0.080678|||
|Training MSE|0.000554|0.000542|0.000527|||
|<br>Test MSE|0.000579|0.000579|0.000582|||



The star-ratings and the sentiment vectors of 89,768 valid online reviews were used as data. We applied MATLAB to train the GA to solve the USDM and the other 12 comparison models with the same training set and test set (80% as training data and the remaining 20% as test data). During training, the models were estimated by minimizing the training error. In the training of machine learning models, we used stochastic gradient descent (SGD) to fine-tune the parameters of the BPNN. The learning rate was dynamically adjusted using learning rate decay (between 0.001 and 0.1). An L2 regularization parameter was also used to balance the model’s fitting ability and generalization ability [78]. Since the GRNN does not have an explicit parameter-tuning process, to avoid model overfitting and underfitting, we compared results multiple times and set the bandwidth parameter to 0.8 [79]. When training the RBFNNs, the number of radial basis functions was set to three, with the mean of the training samples as the center of the radial basis functions, and the width was set to one to balance the model’s complexity and fitting ability [80]. For SVM training, the regularization parameter C was set to 5 through cross-validation, and the kernel function parameter Gamma was set to 0.1 [81]. 



The _R_<sup>2</sup> and the MSE of USDM and comparison models are shown in Table 5. The _R_<sup>2</sup> of our model is superior to other models, except for GRNN, strict RBFNN, approximate RBFNN, PR1, and PR2. In addition, the MSE of the USDM is lower than the GRNN in the training set but better than the GRNN in the test set. More importantly, the MSE of our model in the test set is the lowest among the 13 models, indicating that the proposed USDM performs best in prediction accuracy. 

## **7. Discussion and Implications** 

## _7.1. Discussion_ 

This study developed a two-stage nonlinear USDM based on online product reviews to provide a comprehensive analysis of user preferences and aid in product improvements. 

One important contribution of this study is the combination of word2vec technology and lexicon-based sentiment analysis methods to extract the sentiment polarity of each product attribute from consumer reviews. Previous research on mining consumer attitudes towards product attributes mainly relied on either lexicon-based matching methods or Word2Vec technology [82,83]. However, these methods are not applicable for extracting 

_J. Theor. Appl. Electron. Commer. Res._ **2024** , _19_ 

291 

review words in emerging domains where mature dictionaries are lacking. Therefore, this study simultaneously used pre-defined lexicons and Word2Vec models to extract new domain-specific vocabularies by fully integrating the contextual semantic relationships. This integrated approach helps improve the accuracy and precision of analyzing user attitudes towards product attributes. 

Additionally, we introduced utility-based KANO mapping rules to classify consumer preferences for product attributes. Compared to broad preference categorizations like the two-factor and four-factor theories, the KANO model provides a more detailed attribute classification and has been widely applied in consumer preference analysis studies (e.g., Oh et al. [52] and Zhao et al. [50]). However, these studies only capture the influence of a single attribute on consumer satisfaction evaluation decisions. In reality, consumers consider multiple attributes rather than just a single factor when making satisfaction evaluation decisions. Therefore, we propose a two-stage USDM that uses the KANO model to classify attributes at each stage of the decision-making process to provide overall satisfaction evaluation decisions for consumers. 

The two-stage USDM accurately describes post-purchase evaluation behavior. In the first non-compensatory stage, consumers’ initial satisfaction is determined by the performance of basic attributes. In the compensatory stage, the remaining attributes collectively influence the final user satisfaction through utility calculation. This study’s approach of dividing consumer evaluation mechanisms into two stages is similar to Zhang’s and von Dran’s [26] viewpoint. However, their research only considers the linear impact of product attributes on consumer satisfaction, lacks a consideration of the nonlinear impact of attribute preferences on consumer satisfaction, and overlooks the procedural nature of evaluation decision behavior. The proposed model in this study not only reflects consumer decision-making processes but also provides a practical tool for predicting user satisfaction. 

## _7.2. Implications_ 

## 7.2.1. Theoretical Implications 

First of all, our work contributes to the fields of user post-purchase evaluation and satisfaction decisions. There is abundant research on consumer buying behavior, but little work has been devoted to post-purchase evaluation and user satisfaction decisions. Taking massive amounts of online reviews as data, this study offers new insights into the black box of user satisfaction decisions. This study defines two stages of post-purchase product evaluation: In the first stage, the non-compensatory rule is applied to evaluate the must-be attributes. If these attributes perform poorly, it will be difficult to achieve high user satisfaction. In the second stage, other attributes affect the final satisfaction level through compensatory utility calculation; that is, there is a complementary relationship between these attributes. This study enriches the relevant research on modeling user decision-making behavior from a stage-based and procedural perspective. 

Second, this study is conducive to extracting and analyzing the sentiment and preferences from online reviews. Different from other studies, we innovatively combine word2vec technology with dictionary-based sentiment analysis methods to construct attribute dictionaries and sentiment dictionaries. By mining user sentiments towards product attributes in a fine-grained manner, we provide a new text mining approach for sentiment analysis. In addition, the classic KANO theory is considered to develop the consumer preference identification method combined with the utility function (USDM), through which the users’ emphasis on product attributes is measured. This provides a new method for mining user preferences. 

## 7.2.2. Practical Implications 

The conclusions of this study have significant practical implications for online platforms, enterprises, and consumers. 

For platform designers, by mining the process and rules of user satisfaction decisionmaking, they can better understand users’ preferences, needs, and factors affecting their 

_J. Theor. Appl. Electron. Commer. Res._ **2024** , _19_ 

292 

purchase decisions during the shopping process. Platform designers can apply these rules to personalized recommendation systems and customized services, providing more customized product searches, product displays, and review displays based on each user’s preferences for product attributes. They can also optimize the review-liking and consumer interaction functions of the platform, enabling consumers to more intuitively obtain comprehensive and authentic product-related evaluation information. This improves the smoothness and comfort of online shopping while enhancing platform competitiveness and user retention rates. 

For enterprises, this study provides a method for understanding user needs and preferences in depth. Enterprises can understand user preferences and import product attributes, accurately locate target users, and develop more targeted personalized marketing strategies. Similarly, enterprises can identify the product and service attributes most valued by users and which factors have the greatest impact on user satisfaction. Through precise optimization and improvement of products and services, enterprises can improve user satisfaction, increase user purchase intentions and loyalty, increase user repurchase rates and word-of-mouth publicity, and promote long-term business development. 

For consumers, this study provides a universal model to help them better understand their own needs and preferences, more accurately evaluate product performance and attributes, and make more satisfying purchase decisions, reducing post-purchase regrets. This helps consumers reduce impulse purchases, save on shopping time, improve shopping efficiency, and enhance their shopping experience. 

## **8. Conclusions, Limitation, and Future Research** 

## _8.1. Conclusions_ 

In this study, we develop a novel two-stage, nonlinear USDM that utilizes online product reviews to offer an in-depth analysis of user preferences and potential avenues for product enhancement. 

The study’s foremost contribution is the innovative integration of word2vec technology with lexicon-based sentiment analysis methods. This fusion enables the precise extraction of sentiment polarities for distinct product attributes from consumer reviews. This method surpasses the limitations of prior research that primarily depended on either lexicon-based methods or word2vec technology in isolation, particularly in emerging domains lacking established lexical resources. By leveraging both pre-defined lexicons and word2vec models, our study captures new domain-specific vocabularies through contextual semantic relationships, thus enhancing the accuracy of analyzing user attitudes toward product attributes. 

Furthermore, we introduce utility-based KANO mapping rules to categorize consumer preferences for product attributes more granularly. Unlike conventional broad preference categorizations, the KANO model offers a nuanced attribute classification and has been adopted in numerous consumer preference analysis studies. Our approach recognizes that consumers evaluate multiple attributes in tandem when forming satisfaction judgments, as opposed to considering a single factor in isolation. The proposed two-stage USDM leverages the KANO model’s classification capability to inform each stage of the decisionmaking process, culminating in a comprehensive satisfaction evaluation. 

The two-stage USDM presents an accurate characterization of consumers’ post-purchase evaluation behaviors, distinguishing between an initial non-compensatory stage where satisfaction is influenced by basic attributes and a subsequent compensatory stage wherein a collective assessment of the remaining attributes is factored through utility calculations. Our methodology further acknowledges the procedural nature of evaluation decision behavior. 

In conclusion, our model not only offers a theoretical framework that encapsulates the consumer decision-making process but also serves as a practical tool for businesses to forecast and enhance user satisfaction. By applying the insights gained from this research, enterprises can prioritize product attribute improvements and tailor marketing strategies 

_J. Theor. Appl. Electron. Commer. Res._ **2024** , _19_ 

293 

to align with consumer preferences, ultimately fostering an increase in user satisfaction and loyalty. 

## _8.2. Limitations and Future Research_ 

Although current research provides relevant theoretical and practical foundations for understanding consumer demands and preferences for product attributes, and accordingly developing and improving products, this study still has some limitations, which in turn can be suggestions for future research directions. Firstly, existing research has indicated that consumers with different characteristic attributes (such as language, country, or personality) perceive the attributes of services and products differently, leading to differences in satisfaction ratings [84]. Therefore, future research can explore how to integrate consumers’ individual characteristics to provide more personalized and fine-grained satisfaction decision modeling. Secondly, this study does not consider the changes in consumer satisfaction decision-making behaviors over time and other dynamic factors. Therefore, future research should extend the study of user satisfaction decision models to different time periods and different product lifecycles, exploring the dynamic changes in user satisfaction with product attributes and providing more comprehensive, full-cycle user satisfaction prediction and product improvement recommendations. Finally, in special situational factors such as promotional activities, new product launches, and special holidays, enterprises often achieve higher sales in a short period of time through marketing strategies like scarcity marketing, product bundling, and limited-time offers. Consumers may make impulsive purchases influenced by these marketing strategies, so it is necessary to explore the mechanisms behind consumers’ decision making for post-purchase satisfaction when they experience significant emotional fluctuations while shopping in the future. 

**Author Contributions:** Conceptualization, S.L.; methodology, F.L.; software, F.L.; validation, B.Z. and Y.Z.; formal analysis, Z.Y.; investigation, F.L.; resources, S.L.; data curation, F.L.; writing—original draft preparation, F.L. and Z.Y.; writing—review and editing, B.Z.; visualization, F.L. and B.Z.; supervision, S.L. and Z.Y. All authors have read and agreed to the published version of the manuscript. 

**Funding:** This work was supported by the Chinese National Natural Science Foundation (No. 72271155 and No. 71871135). 

**Institutional Review Board Statement:** Not applicable. 

**Informed Consent Statement:** Not applicable. 

**Data Availability Statement:** The data presented in this study are available on request from the corresponding author. 

**Conflicts of Interest:** The authors declare no conflict of interest. 

## **References** 

1. Prayag, G.; Hassibi, S.; Nunkoo, R. A systematic review of consumer satisfaction studies in hospitality journals: Conceptual development, research approaches and future prospects. _J. Hosp. Mark. Manag._ **2019** , _28_ , 51–80. [CrossRef] 

2. Yoo, J.; Park, M. The effects of e-mass customization on consumer perceived value, satisfaction, and loyalty toward luxury brands. _J. Bus. Res._ **2016** , _69_ , 5775–5784. [CrossRef] 

3. Wang, Y.L.; Tzeng, G.H. Brand marketing for creating brand value based on a MCDM model combining DEMATEL with ANP and VIKOR methods. _Expert Syst. Appl._ **2012** , _39_ , 5600–5615. [CrossRef] 

4. Ji, C.L.; Prentice, C. Linking transaction-specific satisfaction and customer loyalty—The case of casino resorts. _J. Retail. Consum. Serv._ **2021** , _58_ , 10. [CrossRef] 

5. Pomirleanu, N.; Chennamaneni, P.R.; Krishen, A.S. Easy to please or hard to impress: Elucidating consumers’ innate satisfaction. _J. Bus. Res._ **2016** , _69_ , 1914–1918. [CrossRef] 

6. Jang, S.; Chung, J.; Rao, V.R. The importance of functional and emotional content in online consumer reviews for product sales: Evidence from the mobile gaming market. _J. Bus. Res._ **2021** , _130_ , 583–593. [CrossRef] 

7. Gallego, M.D.; Bueno, S.; Lopez-Jimenez, D. Impact of B2C e-commerce codes of conduct on sales volume: Lessons from the Spanish perspective. _J. Bus. Ind. Mark._ **2016** , _31_ , 381–392. [CrossRef] 

_J. Theor. Appl. Electron. Commer. Res._ **2024** , _19_ 

294 

8. Lee, W.J.; Shin, S. Effects of Product Smartness on Satisfaction: Focused on the Perceived Characteristics of Smartphones. _J. Theor. Appl. Electron. Commer. Res._ **2018** , _13_ , 1–14. [CrossRef] 

9. Chang, S.C.; Chou, P.Y.; Lo, W.C. Evaluation of satisfaction and repurchase intention in online food group-buying, using Taiwan as an example. _Br. Food J._ **2014** , _116_ , 44–61. [CrossRef] 

10. Sann, R.; Lai, P.C.; Liaw, S.Y.; Chen, C.T. Predicting online complaining behavior in the hospitality industry: Application of big data analytics to online reviews. _Sustainability_ **2022** , _14_ , 1800. [CrossRef] 

11. Pizam, A.; Shapoval, V.; Ellis, T. Customer satisfaction and its measurement in hospitality enterprises: A revisit and update. _Int. J. Contemp. Hosp. Manag._ **2016** , _28_ , 2–35. [CrossRef] 

12. Ding, C.; Guo, Q.; Rehman, A.; Zeeshan, M. Impact of Environment on Hotel Customer Satisfaction in Southeast Asia: A Study of Online Booking Site Reviews. _Front. Environ. Sci._ **2022** , _10_ , 978070. [CrossRef] 

13. Xiao, S.S.; Wei, C.P.; Dong, M. Crowd intelligence: Analyzing online product reviews for preference measurement. _Inf. Manag._ **2016** , _53_ , 169–182. [CrossRef] 

14. Changchit, C.; Klaus, T. Determinants and Impact of Online Reviews on Product Satisfaction. _J. Internet Commer._ **2020** , _19_ , 82–102. [CrossRef] 

15. Phillips, P.; Barnes, S.; Zigan, K.; Schegg, R. Understanding the Impact of Online Reviews on Hotel Performance: An Empirical Analysis. _J. Travel Res._ **2017** , _56_ , 235–249. [CrossRef] 

16. Tang, L.; Wang, X.; Kim, E. Predicting Conversion Rates in Online Hotel Bookings with Customer Reviews. _J. Theor. Appl. Electron. Commer. Res._ **2022** , _17_ , 1264–1278. [CrossRef] 

17. Levy, S.E.; Duan, W.; Boo, S. An analysis of one-star online reviews and responses in the Washington, DC, lodging market. _Cornell Hosp. Q._ **2013** , _54_ , 49–63. [CrossRef] 

18. Li, H.; Ye, Q.; Law, R. Determinants of Customer Satisfaction in the Hotel Industry: An Application of Online Review Analysis. _Asia Pac. J. Tour. Res._ **2013** , _18_ , 784–802. [CrossRef] 

19. Singh, H.P.; Alshallaqi, M.; Altamimi, M. Predicting Critical Factors Impacting Hotel Online Ratings: A Comparison of Religious and Commercial Destinations in Saudi Arabia. _Sustainability_ **2023** , _15_ , 11998. [CrossRef] 

20. Alhamad, I.A.; Singh, H.P. Decoding Significant and Trivial Factors Influencing Online Hotel Ratings: The Case of Saudi Arabia’s Makkah City. _Int. Trans. J. Eng. Manag. Appl. Sci. Technol._ **2021** , _12_ , 12A7H. [CrossRef] 

21. Alhamad, I.A.; Singh, H.P. Predicting Key Factors Impacting Online Hotel Ratings Using Data Mining Approach: A Case Study of the Makkah City of Saudi Arabia. _Int. Trans. J. Eng. Manag. Appl. Sci. Technol._ **2021** , _12_ , 12A2N. [CrossRef] 

22. Guo, Y.; Barnes, S.J.; Jia, Q. Mining meaning from online ratings and reviews: Tourist satisfaction analysis using latent dirichlet allocation. _Tour. Manag._ **2017** , _59_ , 467–483. [CrossRef] 

23. Zhang, W.T.; Choi, I.Y.; Hyun, Y.J.; Kim, J.K. Hotel Service Analysis by Penalty-Reward Contrast Technique for Online Review Data. _Sustainability_ **2022** , _14_ , 7340. [CrossRef] 

24. Albayrak, T.; Caber, M.I. Prioritisation of the hotel attributes according to their influence on satisfaction: A comparison of two techniques. _Tour. Manag._ **2015** , _46_ , 43–50. [CrossRef] 

25. Singh, H.P.; Alhamad, I.A. Deciphering Key Factors Impacting Online Hotel Ratings through the Lens of Two-Factor Theory: A Case of Hotels in the Makkah City of Saudi Arabia. _Int. Trans. J. Eng. Manag. Appl. Sci. Technol._ **2021** , _12_ , 12A8M. [CrossRef] 

26. Zhang, P.; von Dran, G.M. Satisfiers and dissatisfiers: A two-factor model for Website design and evaluation. _J. Am. Soc. Inf. Sci._ **2000** , _51_ , 1253–1268. [CrossRef] 

27. Lee, J.-S.; Back, K.-J.; Chan, E.S. Quality of work life and job satisfaction among frontline hotel employees: A self-determination and need satisfaction theory approach. _Int. J. Contemp. Hosp. Manag._ **2015** , _27_ , 768–789. [CrossRef] 

28. Johnson, M.D.; Fornell, C. A framework for comparing customer satisfaction across individuals and product categories. _J. Econ. Psychol._ **1991** , _12_ , 267–286. [CrossRef] 

29. Li, S.G.; Liu, F.; Zhang, Y.Q.; Peng, K.X.; Yu, Z.X. Research on Personalized Product Integration Improvement Based on Consumer Maturity. _IEEE Access_ **2022** , _10_ , 39487–39501. [CrossRef] 

30. Corrada, M.S.; Flecha, J.A.; Lopez, E. The gratifications in the experience of the use of social media and its impact on the purchase and repurchase of products and services. _Eur. Bus. Rev_ **2020** , _32_ , 297–315. [CrossRef] 

31. Pappu, R.; Quester, P. Does customer satisfaction lead to improved brand equity? An empirical examination of two categories of retail brands. _J. Prod. Brand Manag._ **2006** , _15_ , 4–14. [CrossRef] 

32. McNamara, N.; Kirakowski, J. Measuring user-satisfaction with electronic consumer products: The Consumer Products Questionnaire. _Int. J. Hum. Comput. Stud_ **2011** , _69_ , 375–386. [CrossRef] 

33. Cohen, S.A.; Prayag, G.; Moital, M. Consumer behaviour in tourism: Concepts, influences and opportunities. _Curr. Issues Tour._ **2014** , _17_ , 872–909. [CrossRef] 

34. Karumur, R.P.; Nguyen, T.T.; Konstan, J.A. Personality, User Preferences and Behavior in Recommender systems. _Inf. Syst. Front_ **2018** , _20_ , 1241–1265. [CrossRef] 

35. Li, S.G.; Liu, F.; Lu, H.Y.; Zhang, Y.Q.; Li, Y.M.; Yu, Z.X. Product family lean improvement based on matching deep mining of customer group preference. _Res. Eng. Des._ **2021** , _32_ , 469–488. [CrossRef] 

36. Allen, J.; Munoz, J.C.; Ortuzar, J.D. Understanding public transport satisfaction: Using Maslow’s hierarchy of (transit) needs. _Transp. Policy_ **2019** , _81_ , 75–94. [CrossRef] 

_J. Theor. Appl. Electron. Commer. Res._ **2024** , _19_ 

295 

37. Cao, H.H.; Jiang, J.H.; Oh, L.B.; Li, H.; Liao, X.W.; Chen, Z.W. A Maslow’s hierarchy of needs analysis of social networking services continuance. _J. Serv. Manag._ **2013** , _24_ , 170–190. [CrossRef] 

38. Barnes, S.J.; Pressey, A.D. Who needs cyberspace? Examining drivers of needs in Second Life. _Internet Res._ **2011** , _21_ , 236–254. [CrossRef] 

39. Herzberg, F.B.; Mausner, B.B.; Snyderman, B.B. _The Motivation to Work_ , 2nd ed.; John Wiley & Sons: New York, NY, USA, 1959. 40. Soliman, H.M. Motivation-hygiene theory of job attitudes: An empirical investigation and an attempt to reconcile both the one-and the two-factor theories of job attitudes. _J. Appl. Psychol._ **1970** , _54_ , 452–461. [CrossRef] 

41. Maddox, R.N. Two-factor Theory and Consumer Satisfaction: Replication and Extension. _J. Consum. Res._ **1981** , _8_ , 97–102. [CrossRef] 

42. Koncar, P.; Santos, T.; Strohmaier, M.; Helic, D. On the application of the Two-Factor Theory to online employer reviews. _J. Data Inf. Manag._ **2022** , _4_ , 1–23. [CrossRef] 

43. Singh, H.P.; Alhamad, I.A. A Novel Categorization of Key Predictive Factors Impacting Hotels’ Online Ratings: A Case of Makkah. _Sustainability_ **2022** , _14_ , 16588. [CrossRef] 

44. Mikulic, J.; Prebezac, D. A critical review of techniques for classifying quality attributes in the Kano model. _Manag. Serv. Qual._ **2011** , _21_ , 46–66. [CrossRef] 

45. Chen, D.D.; Zhang, D.W.; Liu, A. Intelligent Kano classification of product features based on customer reviews. _Cirp Ann. Manuf. Technol._ **2019** , _68_ , 149–152. [CrossRef] 

46. Kano, M.; Ohno-Shosaku, T.; Hashimotodani, Y.; Uchigashima, M.; Watanabe, M. Endocannabinoid-Mediated Control of Synaptic Transmission. _Physiol. Rev._ **2009** , _89_ , 309–380. [CrossRef] [PubMed] 

47. Matzler, K.; Hinterhuber, H.H. How to make product development projects more successful by integrating Kano’s model of customer satisfaction into quality function deployment. _Technovation_ **1998** , _18_ , 25–38. [CrossRef] 

48. Tan, K.C.; Shen, X.X. Integrating Kano’s model in the planning matrix of quality function deployment. _Total Qual. Manag._ **2000** , _11_ , 1141–1151. [CrossRef] 

49. Qi, J.Y.; Zhang, Z.P.; Jeon, S.M.; Zhou, Y.Q. Mining customer requirements from online reviews: A product improvement perspective. _Inf. Manag._ **2016** , _53_ , 951–963. [CrossRef] 

50. Zhao, M.; Liu, M.; Xu, C.; Zhang, C. Classifying travellers’ requirements from online reviews: An improved Kano model. _Int. J. Contemp. Hosp. Manag._ **2023** , _36_ , 91–112. [CrossRef] 

51. Jiang, K.; Li, Y. Mining customer requirement from online reviews based on multi-aspected sentiment analysis and Kano model. In Proceedings of the 2020 16th Dahe Fortune China Forum and Chinese High-Educational Management Annual Academic Conference (DFHMC), Zhengzhou, China, 4–6 December 2020; pp. 150–156. [CrossRef] 

52. Oh, M.; Kim, T.; Im, E. Modeling Customer Satisfaction based on Kano Model from Online Reviews: Focused on Deep Learning Natural Language Processing. In Proceedings of the 2022 IEEE/ACIS 7th International Conference on Big Data, Cloud Computing, and Data Science (BCD), Danang, Vietnam, 4–6 August 2022; pp. 22–26. [CrossRef] 

53. Lazaroiu, G.; Negurita, O.; Grecu, I.; Grecu, G.; Mitran, P.C. Consumers’ Decision-Making Process on Social Commerce Platforms: Online Trust, Perceived Risk, and Purchase Intentions. _Front. Psychol._ **2020** , _11_ , 7. [CrossRef] 

54. Kenning, P.; Linzmajer, M. Consumer neuroscience: An overview of an emerging discipline with implications for consumer policy. _J. Verbrauch. Leb._ **2011** , _6_ , 111–125. [CrossRef] 

55. Hult, G.T.M.; Sharma, P.N.; Morgeson, F.V.; Zhang, Y.F. Antecedents and Consequences of Customer Satisfaction: Do They Differ across Online and Offline Purchases? _J. Retail._ **2019** , _95_ , 10–23. [CrossRef] 

56. Huang, N.; Burtch, G.; Hong, Y.; Polman, E. Effects of multiple psychological distances on construal and consumer evaluation: A field study of online reviews. _J. Consum. Psychol._ **2016** , _26_ , 474–482. [CrossRef] 

57. Park, J.; Han, S.H.; Kim, H.K.; Oh, S.; Moon, H. Modeling user experience: A case study on a mobile device. _Int. J. Ind. Erg._ **2013** , _43_ , 187–196. [CrossRef] 

58. Lago, N.C.; Marcon, A.; Ribeiro, J.L.D.; de Medeiros, J.F.; Briao, V.B.; Antoni, V.L. Determinant attributes and the compensatory judgement rules applied by young consumers to purchase environmentally sustainable food products. _Sustain. Prod. Consum._ **2020** , _23_ , 256–273. [CrossRef] 

59. You, T.; Zhang, J.; Fan, Z. Method for Selecting Desirable Product(s) Based on Online Rating Information and Customers Aspirations. _Chin. J. Manag. Sci._ **2017** , _25_ , 94–102. 

60. He, J.J.; Chen, L.H.; Li, J.X.; Liu, S.M. An Empirical Investigation of the Online Commentary Behavior Dynamics Based on the Marginal Utility Theory. _Int. J. Enterp. Inf. Syst_ **2020** , _16_ , 92–106. [CrossRef] 

61. Lima, F.R.; Osiro, L.; Carpinetti, L.C.R. A fuzzy inference and categorization approach for supplier selection using compensatory and non-compensatory decision rules. _Appl. Soft. Comput._ **2013** , _13_ , 4133–4147. [CrossRef] 

62. Tversky, A.; Shafir, E. Choice under conflict: The dynamics of deferred decision. _Psychol. Sci._ **1992** , _3_ , 358–361. [CrossRef] 

63. Wang, M.; Gu, B.; Ye, Q. Elimination by Aspects in Electronic Commerce—Evidence from Online Marketplace and Implications for Empirical Model Specification. In Proceedings of the 47th Annual Hawaii International Conference on System Sciences, Waikoloa, HI, USA, 6–9 January 2014; pp. 4142–4147. [CrossRef] 

64. Stankevich, A. Explaining the consumer decision-making process: Critical literature review. _J. Int. Bus. Res. Mark._ **2017** , _2_ , 7–14. [CrossRef] 

_J. Theor. Appl. Electron. Commer. Res._ **2024** , _19_ 

296 

65. Graffeo, M.; Polonio, L.; Bonini, N. Individual differences in competent consumer choice: The role of cognitive reflection and numeracy skills. _Front. Psychol._ **2015** , _6_ , 15. [CrossRef] 

66. Gani-zade, D.S.; Zakharov, I.M.; Menshikova, G.Y. Brain mechanisms of face perception: Holistic and analytical processes. _Vopr. Psikhologii_ **2021** , _67_ , 121–134. 

67. Apanovich, V.V.; Tishchenko, A.G.; Znakov, V.V.; Alexandrov, Y.I. Construction of blocks of analytical and holistic problems and their empirical verification. _Vopr. Psikhologii_ **2020** , _13_ , 52–71. 

68. Ullah, R.; Amblee, N.; Kim, W.; Lee, H. From valence to emotions: Exploring the distribution of emotions in online product reviews. _Decis. Support Syst._ **2016** , _81_ , 41–53. [CrossRef] 

69. Burnap, P.; Rana, O.F.; Avis, N.; Williams, M.; Housley, W.; Edwards, A.; Morgan, J.; Sloan, L. Detecting tension in online communities with computational Twitter analysis. _Technol. Forecast. Soc. Change_ **2015** , _95_ , 96–108. [CrossRef] 

70. Salawu, S.; He, Y.; Lumsden, J. Approaches to Automated Detection of Cyberbullying: A Survey. _IEEE Trans. Affect. Comput._ **2020** , _11_ , 3–24. [CrossRef] 

71. Mikolov, T.; Chen, K.; Corrado, G.; Dean, J. Efficient estimation of word representations in vector space. _arXiv_ **2013** , arXiv:1301.3781. [CrossRef] 

72. Goldberg, Y.; Levy, O. word2vec Explained: Deriving Mikolov et al.’s negative-sampling word-embedding method. _arXiv_ **2014** , arXiv:1402.3722. [CrossRef] 

73. Fu, X.; Liu, G.; Guo, Y.; Wang, Z. Multi-aspect sentiment analysis for Chinese online social reviews based on topic modeling and HowNet lexicon. _Knowl. Based Syst._ **2013** , _37_ , 186–195. [CrossRef] 

74. Du, X.H.; Jiao, J.X.; Tseng, M.M. Understanding customer satisfaction in product customization. _Int. J. Adv. Manuf. Technol._ **2006** , _31_ , 396–406. [CrossRef] 

75. Arana, J.E.; Leon, C.J. Understanding the use of non-compensatory decision rules in discrete choice experiments: The role of emotions. _Ecol. Econ._ **2009** , _68_ , 2316–2326. [CrossRef] 

76. Scheibehenne, B.; von Helversen, B. Selecting decision strategies: The differential role of affect. _Cogn. Emot._ **2015** , _29_ , 158–167. [CrossRef] 

77. Goldberg, D.E.; Holland, J.H. Genetic algorithms and machine learning. _Mach. Learn._ **1988** , _3_ , 95–99. [CrossRef] 

78. Wang, L.; Zeng, Y.; Chen, T. Back propagation neural network with adaptive differential evolution algorithm for time series forecasting. _Expert Syst. Appl._ **2015** , _42_ , 855–863. [CrossRef] 

79. Li, H.-z.; Guo, S.; Li, C.-j.; Sun, J.-q. A hybrid annual power load forecasting model based on generalized regression neural network with fruit fly optimization algorithm. _Knowl. Based Syst._ **2013** , _37_ , 378–387. [CrossRef] 

80. Chen, C.L.P.; Wen, G.-X.; Liu, Y.-J.; Wang, F.-Y. Adaptive Consensus Control for a Class of Nonlinear Multiagent Time-Delay Systems Using Neural Networks. _IEEE Trans. Neural Netw. Learn. Syst._ **2014** , _25_ , 1217–1226. [CrossRef] 

81. Chang, C.-C.; Lin, C.-J. LIBSVM: A Library for Support Vector Machines. _ACM Trans. Intell. Syst. Technol._ **2011** , _2_ , 1–27. [CrossRef] 82. Alshari, E.M.; Azman, A.; Doraisamy, S.; Mustapha, N.; Alkeshr, M. Effective method for sentiment lexical dictionary enrichment based on Word2Vec for sentiment analysis. In Proceedings of the 2018 Fourth International Conference on Information Retrieval and Knowledge Management (CAMP), Kota Kinabalu, Malaysia, 26–28 March 2018; pp. 1–5. [CrossRef] 

83. Deepa, D.; Tamilarasi, A. Sentiment analysis using feature extraction and dictionary-based approaches. In Proceedings of the 2019 Third International Conference on I-SMAC (IoT in Social, Mobile, Analytics and Cloud) (I-SMAC), Palladam, India, 12–14 December 2019; pp. 786–790. [CrossRef] 

84. Liu, Y.; Teichert, T.; Rossi, M.; Li, H.; Hu, F. Big data for big insights: Investigating language-specific drivers of hotel satisfaction with 412,784 user-generated reviews. _Tour. Manag._ **2017** , _59_ , 554–563. [CrossRef] 

**Disclaimer/Publisher’s Note:** The statements, opinions and data contained in all publications are solely those of the individual author(s) and contributor(s) and not of MDPI and/or the editor(s). MDPI and/or the editor(s) disclaim responsibility for any injury to people or property resulting from any ideas, methods, instructions or products referred to in the content. 

