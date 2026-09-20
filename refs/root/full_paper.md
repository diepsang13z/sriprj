# Unlocking Insights into Customer Sentiment Analysis: Impact of Loyalty on Online Hotel Ratings

> **Bibliographic Information:**
> * **Authors:** Hanh Thi My Le (a,b), Thang Quyet Nguyen (a,*), Binh T. Nguyen (c,d,e)
> * **Affiliations:**
>   * (a) Faculty of Tourism & Hospitality Management, HUTECH University, Ho Chi Minh City, Viet Nam
>   * (b) Faculty of Tourism & Hospitality Management, Ho Chi Minh City University of Economics and Finance, Ho Chi Minh City, Viet Nam
>   * (c) AISIA Research Lab, Ho Chi Minh City, Viet Nam
>   * (d) Faculty of Mathematics & Computer Science, VNU-HCM University of Science, Ho Chi Minh City, Viet Nam
>   * (e) Vietnam National University Ho Chi Minh City, Viet Nam
> * **Journal:** *International Journal of Hospitality Management*, Volume 134, 2026, Article 104574
> * **DOI:** [10.1016/j.ijhm.2026.104574](https://doi.org/10.1016/j.ijhm.2026.104574)
> * **Timeline:** Received 20 March 2025; Revised 4 January 2026; Accepted 20 January 2026; Available online 28 January 2026
> * **Corresponding Authors:** nq.thang@hutech.edu.vn (T.Q. Nguyen), ltm.hanh80@hutech.edu.vn / hanhltm@uef.edu.vn (H.T.M. Le), ngtbinh@hcmus.edu.vn (B.T. Nguyen)

---

## Abstract

Large-scale social data and user-generated text are extensively important for understanding customer sentiment in the hospitality industry. The present study employs BERTopic to extract fine-grained themes from 607,451 Booking.com reviews and 782,584 TripAdvisor reviews, covering more than 13,000 hotels in Vietnam. Unlike traditional models, the BERTopic-based approach demonstrates superior efficacy in uncovering three sentiment expressions and is refined into five novel categories (facility, amenity, service, experience value and loyalty). To enhance construct validity, human-labeled sentiment analysis is combined. Econometric techniques connect aspect-based sentiment with individual ratings within the S-O-R framework. The results show that loyalty-related intentions are strongly associated with higher ratings, which highlights their mediating role between service delivery and brand equity. Managerially, the findings provide granular insights for hoteliers to build loyalty programs, optimize service strategies and strengthen online branding in modern competitive markets. We present theoretical understanding of these novel categories and provide actionable strategies for data-driven brand management.

**Keywords:** Online hotel ratings, Data-driven machine learning, Customer sentiment, Loyalty, BERTopic.

---

## 1. Introduction

### 1.1. Background

Nowadays, online reviews and ratings on platforms such as Booking.com and TripAdvisor have become critical information sources influencing both customer purchasing decisions and managerial decision-making in the hospitality industry (Ahani et al., 2019; Bai et al., 2024). Prior research consistently demonstrated that online reviews significantly shape customers’ satisfaction perceptions, purchase intentions and value assessments (Zhao et al., 2019; Rezaei et al., 2024; Lahsini et al., 2026). In particular, Ahani et al. (2019) highlighted that online hotel reviews provide rich, experience-based information regarding customer satisfaction and preferences, which emphasize their strategic importance for service improvement and brand management. Empirical evidence further confirms systematic links between review sentiment and online ratings. It was indicated that textual content and numerical ratings jointly influence hotel performance and reputation (Geetha et al., 2017; Rezaei et al., 2024). Customers increasingly relied on online reviews to infer service quality and perceived value, while managers used them to monitor experience satisfaction and reinforce digital brand equity (Zhao et al., 2019).

However, the exponential growth of user-generated content has resulted in massive, unstructured and noisy textual data (Li et al., 2018). It makes systematic interpretation challenging when using traditional analytical approaches. To solve this challenge, big data and AI-driven techniques have been widely adopted to extract latent topics, sentiments and behavioral signals from large-scale hotel reviews (Zhao et al., 2019; Chang et al., 2020; Bian et al., 2022; Puh and Bagić Babac, 2023; Zhang and Niu, 2024; Le et al., 2025). For example, Zhao et al. (2019) used large textual datasets from TripAdvisor to predict overall customer satisfaction based on review attributes, while Zhang and Niu (2024) applied deep learning methods to forecast hotel demand from review information. Similarly, Puh and Bagić Babac (2023) employed machine-learning models to predict both sentiment polarity and numerical ratings in tourism reviews.

By predictive modeling, topic modeling and aspect-based sentiment analysis have been extensively applied to identify key experience dimensions and customer preferences in tourism texts. Existing studies examined destination attributes (Schlesinger et al., 2020), service quality and functional attributes as well as emotional and experiential aspects of tourism consumption (Chen et al., 2019; Zhang et al., 2021; Mirzaalian and Halpenny, 2021; Liu et al., 2021; Sanchez-Franco and Rey-Moreno, 2022; Egger and Yu, 2022; Lerksuthirat et al., 2023; Bai et al., 2024; Yoo et al., 2024; Rabadan-Martín et al., 2025). Methodologically, traditional unsupervised approaches such as LDA (Blei et al., 2003), NMF (Lee and Seung, 2000), and Top2Vec (Angelov, 2020) as well as more recent transformer-based models (Dhanal and Ghorpade, 2024) have been used to extract hotel aspects and associated sentiments (Xu and Li, 2016; Calheiros et al., 2017; Hu et al., 2019; Kirilenko et al., 2021; Wu et al., 2023). Recent reviews emphasized the growing potential of AI-enhanced topic modeling for tourism and hospitality research (Kirilenko and Stepchenkova, 2025).

Despite these methodological advances, existing studies exhibit several important limitations. First, much of the prior literature focuses on predicting ratings or extracting topics and sentiments in isolation without embedding these outputs within an integrated behavioral or branding framework. Second, although experience satisfaction and value are widely recognized as key antecedents of customer loyalty, loyalty-related intentions are rarely examined jointly with aspect-level sentiments and individual ratings in online review contexts.

In hospitality research, experience satisfaction is typically conceptualized as an evaluative outcome that precedes and fosters loyalty. Empirical studies demonstrated that perceived value and experience satisfaction exert significant positive effects on customer loyalty and revisit intentions (El-Adly, 2019; Schlesinger et al., 2020). In online review settings, ratings are often interpreted as indicators of experience satisfaction or digital brand equity. Radojević et al. (2017) showed that online ratings are strongly correlated with experiential quality factors such as service, rooms and cleanliness are significantly influenced by hotel star ratings and room prices. These findings suggest that online ratings represent a behavioral outcome of brand valuation in customer perception. They reflect a synthesis of experience quality and experience value, which in turn shapes brand-related perceptions and feelings (Soler and Gémar, 2017). Moreover, online ratings have been shown to function as behavioral expressions of brand-related emotions with strong associations between review sentiment, brand experience and individual ratings (Soler and Gémar, 2017; Kalnaovakul et al., 2025). From a branding perspective, customer-based brand equity (CBBE) reflects experience value, satisfaction and brand positioning accumulated through customer interactions with the brand (Kotler and Keller, 2006; Kim et al., 2021; Piriyakul et al., 2024). Digital review environments further amplify this process, as online reviews actively shape, reinforce or collapse brand image and reputation (Borges-Tiago et al., 2021).

Importantly, loyalty is not only reflected in long-term attitudes but also in behavioral intentions such as revisiting or recommending a hotel. Online reviews, therefore, provide a unique opportunity to observe satisfaction and loyalty simultaneously: numerical ratings capture overall experience evaluations, while textual reviews often contain explicit loyalty-related expressions (e.g., “we will come back”, “highly recommend”, or “never again”). However, prior studies (e.g., Zhao et al., 2019; Liu et al., 2021; Martin-Fuentes et al., 2024; Le et al., 2025) tended to examine these elements separately, which constrains understanding of how multiple experience dimensions, sentiment expressions and loyalty-related intentions jointly translate into observable rating behavior within a coherent S–O–R framework.

To address the above gap, we integrate advanced text-mining techniques with a theory-driven consumer behavior framework. Specifically, BERTopic is employed to capture semantically rich, context-sensitive experience aspects from large-scale hotel reviews, overcoming limitations of traditional topic modeling in handling short and noisy texts. Combined with VADER-based sentiment analysis and human validation, the present approach enables the identification of multi-aspect sentiment variables reflecting affective and cognitive responses of customers. Using a large cross-platform dataset of more than 1.3 million reviews, the study further links aspect-level sentiments and loyalty-related expressions to individual ratings through a weighted multinomial logistic regression model (WMLR). This design allows online ratings to be interpreted as behavioral responses (Response) measured by facilities, amenities and services (Stimulus), and by experience value and loyalty (Organism), within the S–O–R framework. Consequently, our study promotes understanding of how multi-aspect sentiment variables jointly translate into rating behavior. It offers a more integrated explanation of online reviews as observable manifestations of customer-based brand equity in the hospitality sector.

### 1.2. Topic Extraction and Research Gap

Expanding on this context, the study aims to address several interrelated gaps in the hospitality and tourism literature by employing advanced text-mining techniques to examine a theory-driven question about consumer behavior. First, although numerous studies have applied topic modeling and sentiment analysis to online hotel reviews, they typically focus on a limited set of predefined attributes or on global sentiment scores. Prior research often examines service quality, cleanliness, staff behavior or destination attributes in relation to satisfaction or loyalty, but does not systematically integrate multiple experience dimensions with explicit loyalty-related expressions and individual ratings within a single analytical framework (Radojevic et al., 2017; Soler and Gémar, 2017; Situmeang et al., 2020). As a result, how different aspects of the hotel experience jointly translate into rating behavior remains insufficiently explained.

Second, while overall experience satisfaction and loyalty have been extensively studied using survey data and structural models. Few studies exploit large-scale online reviews to examine loyalty-related language embedded in review texts and its co-occurrence with aspect-based sentiments and rating outcomes. This is notable because loyalty has traditionally been treated as a latent construct measured through questionnaires, rather than as an expressed cognitive–affective state revealed through naturally occurring textual data.

Third, from a methodological perspective, existing applications of topic modeling in hospitality mainly rely on traditional models such as LDA or NMF, which have limitations in capturing semantic nuance in short, noisy review texts. Although transformer-based approaches such as BERTopic show considerable promise, they remain underutilised in hotel rating and loyalty research, particularly in studies seeking to connect text-derived insights to consumer behavior theory.

Therefore, our study contributes to three interrelated objectives, clearly distinguishing its theoretical and methodological contributions to consumer behavior. From a consumer behavior perspective, the first objective is to extract fine-grained experience topics from online hotel reviews and group them into five theoretically meaningful categories, namely facility, amenity, service, experience value and loyalty. Although these categories are identified at the textual level, they serve distinct theoretical roles within the S–O–R framework: facility, amenity and service represent service stimuli (S), experience value and loyalty-related sentiments capture internal organismic states (O) and online ratings constitute the behavioral response (R). Notably, identifying loyalty as an emergent category from review texts represents a behavioral contribution as it demonstrates that loyalty-related intentions (e.g., revisit and recommendation) can be observed directly in customer narratives rather than inferred solely from survey instruments. Within the S-O-R framework, loyalty is conceptualized as an internal organismic state that mediates how service-related stimuli are translated into evaluative responses in the form of ratings.

The second objective is to examine how aspect-based sentiments and loyalty-related expressions jointly shape individual ratings on Booking.com and TripAdvisor. By doing so, we explain rating behavior as the outcome of an integrated evaluative process, in which loyalty may amplify positive experiences or attenuate the effects of negative ones, rather than treating ratings as a simple reflection of isolated service attributes.

From a methodological perspective, the third objective is to develop a hybrid analytical pipeline that combines BERTopic for topic discovery, VADER-based sentiment scoring, and human validation to enhance robustness when analyzing large-scale review data. A weighted multinomial logistic regression (WMLR) model is then employed to link aspect-level sentiments and loyalty-related expressions to rating outcomes while addressing class imbalance. This methodological contribution supports, rather than replaces, our primary theoretical aim of explaining consumer behavior.

These objectives are reflected in the following research questions:

- **RQ1:** How do emotional sentiments associated with key hotel service aspects relate to customers’ overall experience evaluation as reflected in their ratings?
- **RQ2:** Which sentiment polarity across these aspects is most strongly associated with higher or lower ratings?
- **RQ3:** How do loyalty-related expressions (revisit and recommendation intentions) interact with aspect-based sentiments in shaping ratings, for example, by amplifying positive experiences or softening the effect of negative ones?

Last but not least, Fig. 1 illustrates the analytical framework and procedural flow of the present work, from data collection and preprocessing to BERTopic-based topic extraction, category grouping, sentiment analysis and customer rating regression with WMLR estimation. The remainder of the paper is organized as follows: Section 2 describes the data collection; Section 3 outlines the aspects-based extraction technique and the novel empirical approach; Section 4 presents the empirical results; Section 5 discusses the findings and implications; and Section 6 closes with the concluding remarks and future work.

> **Fig. 1.** *Analytical framework and research pipeline: Data acquisition -> Data preprocessing -> Aspect extraction (BERTopic) -> Aspect grouping (SentenceBERT + c-TF-IDF) -> Sentiment classification (VADER + Gold standard) -> Econometric estimation via WMLR under S-O-R framework.*

---

## 2. Data Acquisition and Preprocessing

This section introduces a common approach to extract data from hotel review websites using Python web scraping libraries with Selenium and BeautifulSoup. The data collection process begins with specifying the search page's URL, employing Selenium’s WebDriver to execute essential operations such as managing cookies and navigating through dynamic content. BeautifulSoup evaluates the HTML and extracts the hotel’s URLs. Selenium engages with dynamic web elements, while BeautifulSoup is used for parsing static content. The WebDriver retrieves the specific URLs of the hotels to gather comprehensive information from hotel reviews and BeautifulSoup systematically analyses the review data. We present a schematic overview of the implementation to pack the data acquisition process, highlighting the synergy between Selenium and BeautifulSoup, as plotted in Fig. 2.

> **Fig. 2.** *A summary of web scraper architecture combining Selenium and BeautifulSoup.*

Fig. 3 illustrates a data collection review from a specific hotel. In the initial data preprocessing phase, missing temporal data is addressed by identifying and excluding records with absent date entries. The dataset is then refined by removing duplicate reviews and entries with unclear linguistic attributes. The final step in the data cleansing protocol entails removing any commentary that lacks associated hotel information when cross-referenced with the hotel dataset. This approach ensures the integrity and relevance of the data before subsequent analytical procedures.

> **Fig. 3.** *An illustration of the data collection process and sample review record.*

A large dataset contained 607,451 reviews on Booking.com from 2020 to August 2023 and 782,584 ones on TripAdvisor from 2015 to August 2023 (Le et al., 2025). It is found that this dataset significantly exceeds those in prior studies, such as 108,563 reviews from Bogotá hotels and 498,361 reviews from Madrid hotels (Vargas-Calderón et al., 2021), 38,292 reviews from Lisbon hotels (Rita et al., 2022) and 429,000 reviews from major European cities (Leoni and Boto-García, 2023).

Then, we filter the reviews written in English and apply transformations within the data pipeline. These English-language reviews establish the pre-final dataset deemed suitable for analysis within the scope of this study before labeling the aspect. A multi-step pipeline enhances feedback data for topic modeling by removing invalid timestamps, segmenting text into sentences, cleaning characters and whitespaces, filtering non-English content, converting non-ASCII to ASCII, and discarding very short sentences. As a result, the dataset has 902,425 Booking sentences and 3,287,307 TripAdvisor sentences. In addition, the labeled dataset for the present study includes 15,741 English reviews from TripAdvisor and 6,955 from Booking.com. This process makes sure that it is both academically compliant and human-verified, minimizing bias from automation (Cui et al., 2022; Kirilenko and Stepchenkova, 2025; Rabadan-Martín et al., 2025; Lahsini et al., 2026).

---

## 3. Methodology

### 3.1. Topic Modeling with BERTopic

It has been well known that most studies about topic modeling employed Latent Dirichlet Allocation (LDA). Nonetheless, a significant challenge of LDA is that it considers text as a bag-of-words and neglects word order and context, leading to less accurate topic extraction (Egger and Yu 2022; Yoo et al., 2024; Kirilenko and Stepchenkova, 2025). Researchers emphasized that BERTopic is particularly effective with large-scale data, providing more accurate and updated topics than traditional qualitative methods. For instance, while LDA is widely used in cultural mining of tourism data (Egger and Yu, 2022), it often produces broad topics without uncovering semantic nuances or distinct sentiments (Kirilenko and Stepchenkova, 2025). Sanchez-Franco and Rey-Moreno (2022) also highlighted that LDA and PLSA are unsuitable for short texts due to data sparsity.

In contrast, BERTopic can generate more interpretable and representative topics within a continuous semantic space (Grootendorst, 2022). Similarly, Kirilenko and Stepchenkova (2025) evaluated the interpretability of both LDA and BERTopic but confirmed that BERTopic yields richer insights. Other studies, such as Lerksuthirat et al. (2023) on ‘cannabis tourism’ and Egger and Yu (2022) on Twitter data, also demonstrated the effectiveness of combining BERTopic with sentiment analysis. It is clear that BERTopic is not only widely applied in online tourism research but also excels in handling short, noisy, and emotional data, making it suitable for our analysis. For instance, BERTopic can build up to 100 more complex and specific topics. Some unique detected topics are “motorbike noise”, “hard bed”, “loud air conditioner”, “infinity pool” and “friendly host”. The wordcloud graphs are illustrated in Fig. 4. It shows that this machine learning touches the factual, detailed and personal sentiments well. It contributes to overall satisfaction and increases the depth and accuracy of content analysis. In addition, further details on the topic extraction and multi-aspect extraction techniques are provided in the Supplement file at https://github.com/Hanhlevna/Manhos.

> **Fig. 4.** *A visualization of nine fine-grained topics via BERTopic (e.g., swimming pool, noise levels, bike rentals, beach location, bed comfort, air conditioning, host friendliness, family homestay, price value).*

### 3.2. Topic Grouping Technique

An efficient and straightforward technique, so-called topic grouping, is presented to classify topics across the five aforementioned aspects through a multi-step process. The idea is to extract the top $k$ keywords for each topic in BERTopic, effectively defining a keyword list for each aspect. Following this step, embeddings for each keyword are derived using SentenceBERT and cosine distances are calculated to produce a distance matrix ($n \times 5$, where $n$ is the number of topics clustered by BERTopic). The weight of each keyword within each topic is then determined using a $c$-TF-IDF matrix, which is subsequently processed to identify the indices of the top $k$ most significant values, retaining only these positions to represent the most important keywords for each topic. The classification process culminates in multiplying the distance matrix by the keyword weight matrix, yielding a weighted distance matrix. This matrix is necessary to determine the aspect keywords most closely related to each topic. It facilitates the identification of the corresponding aspects as defined earlier. Results are summarized in Tables 1–2 and plotted in Fig. 5.

It is worth noting that the loyalty aspect is characterized by terms such as “revisit”, “back”, “recommend”, “again”, “stay away” and “never again”, which in the loyalty literature are interpreted as revisit and recommendation intentions, i.e., behavioral indicators of attitudinal loyalty. In this study, these expressions are treated as text-based signals of loyalty-related behavioral intentions rather than direct measurements of long-term loyalty status. We show later that loyalty-related keywords have a strong impact on online ratings.

> **Fig. 5.** *Five specific aspects generated through BERTopic analysis: Facility, Amenity, Service, Experience Value, Loyalty.*

#### Table 1: Aspects Associated with Keywords

| Aspect | Keywords |
| :--- | :--- |
| **Facility** | Facility, room, furnishings, bathroom, charging, reception area, restaurant facilities, public equipment, gym, pool, elevator, bed, mattress, water, electricity, configuration, home appliances, article, supplies, utensils, decoration, air conditioner, infrastructure, environment, sanitation, sound insulation, ventilation, natural lighting, landscape, scenery, new, old, complete, antiquated, shabby, wet, dark, dirty, sanitary, clean, tidy, leaky, warm, dusky, bright, moldy, fusty, foul smelly, neat |
| **Amenity** | Amenity, payment method, bill issued, location, transportation, safety, security, lock, fire extinguisher, public service, spa, parking, traffic, place, site, surrounding, vicinity, travel, subway, bus stop, business district, city center, convenient, quick, well-suited |
| **Service** | Service, restaurant service, breakfast, food, beverage, staff, helpful, friendly, care, room services, booking services, room appointment, attitude, customer service, manager, front desk, proprietor, quality, cleaning, reception, sweeping, make up, waiter, service quality, work efficiency, passionate, caring, patiently, indifferent, considerate, thoughtful, kind, observant, meticulous, cordial |
| **Experience value (Experience)** | Atmosphere, noisy, quiet, relaxing, fresh, elegant, lovely, view, panorama, scenery, cultural, highlight, seaview, view, vision, satisfaction, hype, fame, promise, deliver, unsatisfaction, over-rated, overpriced, worth, value, price, fee, room rate, room price, cost-performance, entirety, in short, hotel, apartment, expensive, cheap, cost-effective, price increase, discount, concessional |
| **Loyalty** | Loyalty, revisit, back, recommend, suggest, again, stay away, never again, once is enough, stay elsewhere |

### 3.3. Customer Sentiment

Sentiment analysis aims to uncover insights into customer feedback and hotel services. Geetha et al. (2017) and Rezaei et al. (2024) investigated the link between customer sentiment and individual ratings, finding that sentiment polarity significantly explains rating variations across hotel categories. Notably, sentiments were less positive for luxury than budget hotels, highlighting the need for budget hotel managers to enhance staff performance and services. Sentiment is divided into positive, neutral and negative categories. Each sentiment category is analyzed to reflect specific levels of satisfaction, neutrality or dissatisfaction. It allows for a better understanding of customer behavior instead of relying on traditional research methods. Thus, the model examines how aspect-level sentiments and loyalty-related intentions co-vary with and condition customers’ ratings, rather than assuming that loyalty causally precedes satisfaction. Within this structure, loyalty is viewed as a state that co-develops with experience value and can amplify or attenuate how service experiences are translated into ratings. It is consistent with the idea that loyal customers may react more leniently to minor failures or more strongly to outstanding experiences.

### 3.4. A Novel Empirical Approach via WMLR and S-O-R

This subsection describes the S-O-R framework as the theoretical foundation to explain how customer experience stimuli influence customers’ internal psychological states and subsequently shape their evaluative responses. While the proposed relationships are theoretically grounded in S-O-R, logistic regression is employed as an empirical technique to estimate the likelihood of customers’ overall rating outcomes. To reach this goal, a weighted multinomial logistic regression (WMLR) is employed. It does not require strict assumptions about error distribution or homoscedasticity. Note that unweighted multinomial logistic regression (UMLR) often encounters limitations when handling online evaluation data with high imbalance, in which the positive evaluation group is largely dominant. Inversely, in WMLR, observation weights are proportional to class size to ensure the total weights of classes being equal (Picek et al., 2019). It is described as the probability of customer rating regression ($CoRe$), which can be formed in terms of three sentiment levels as:

$$\begin{aligned}
\log(CoRe) = \beta_0 &+ \beta_{11}AmenityPositive + \beta_{12}AmenityNeutral + \beta_{13}AmenityNegative \\
&+ \beta_{21}FacilityPositive + \beta_{22}FacilityNeutral + \beta_{23}FacilityNegative \\
&+ \beta_{31}ServicePositive + \beta_{32}ServiceNeutral + \beta_{33}ServiceNegative \\
&+ \beta_{41}ExperiencePositive + \beta_{42}ExperienceNeutral + \beta_{43}ExperienceNegative \\
&+ \beta_{51}LoyalPositive + \beta_{52}LoyalNeutral + \beta_{53}LoyalNegative
\end{aligned} \tag{1}$$

where:
- $\beta_0, \beta_{ij}$ ($i = 1 \div 5, j = 1 \div 3$) are arbitrary coefficients and need to be determined through the results.
- The “Positive” variables represent the positive aspects of amenities, experience, facilities, loyalty, and service.
- The “Negative” variables represent the remaining opposite ones.
- The “Neutral” variables represent customers’ neutral attitudes toward the above factors.

Eq. (1) estimates the probability of satisfied and dissatisfied levels based on the labeled sentiment datasets. At Booking.com, we classify a rating below seven as dissatisfied (Martin-Fuentes et al., 2024). For TripAdvisor, a score of 4 and above is labeled “Satisfied” (Taecharungroj and Mathayomchan, 2019; Puh and Bagić Babac, 2023). The present method quantifies how different sentiment aspects, such as service, facilities, or amenities, influence $CoRe$. It also clearly explains how each factor impacts the perceived brand experience. This approach is chosen to test the hypothesis and to predict potential customer purchases. According to Puh and Bagić Babac (2023), analyzing online reviews not only improves service quality but also helps estimate consumer trends. In this context, $CoRe$ serves as an intermediary variable to connect customer sentiment with their behavior and market potential.

Applying the S–O–R model to hospitality, Liu et al. (2021) examined it in P2P accommodation, providing a sound theoretical framework for understanding psychological and behavioral experiences. This framework depicts a chain of interconnected effects in which the customer's perceived experience shapes internal states. It yields evaluation responses, engagement and brand value, involving both rational and emotional components. Also, El-Adly (2019) argued that experience value reflects the customer's subjective assessment of the benefits obtained during interaction with the hotel service quality. Liu et al. (2021) emphasized the significance of the Organism (O) as an internal evaluation process triggered by various environmental factors. Similarly, Şanlıöz-Özgen and Kozak (2023) confirmed that experience quality reflects customer rational perceptions of service performance. It plays a crucial role in creating experience value, engagement and brand-related responses. From a different perspective, Fan et al. (2023) conceptualized customer experience as the Stimulus (S), while experience value measured by pleasure and travel memories is viewed as the Organism (O). They proposed that customer intentions to return and retain services can be seen as Responses (R).

In our work, the S-O-R assesses emotional aspects on the overall rating (see Fig. 6). Herein, facilities, amenities and services are defined as the Stimulus (S). These reflect customers' perceptions of specific service attributes and interactions. The Organism (O) reflects internal cognitive–affective states such as emotions and attachment tendencies that include experience value and loyalty. Responses (R) are operationalized through an overall rating score ($CoRe$), which serves as a quantitative measure of brand equity in the digital era. This rating illustrates how customers synthesize, evaluate and validate brand value through their service experiences. It is also one of the brand equity elements, a core concept in marketing, defined as the perceived value of a brand in consumers' minds (Piriyakul et al., 2024). In addition, experience value and customer loyalty operate as parallel psychological states within the S-O-R framework. Both are influenced by customer experience and simultaneously lead to Brand Equity/customer rating. Therefore, our present model focuses on exploring the direct impact of customer experience on rating and the indirect impact through experience value and customer loyalty. The lack of a direct correlation between the Organism components is consistent with the logic of SOR theory, where Organism states do not necessarily have a causal relationship with each other but can function as parallel mediating mechanisms.

> **Fig. 6.** *Research framework connecting Stimulus (Facility, Amenity, Service), Organism (Experience Value, Loyalty), and Response (Customer Rating / CoRe / Brand Equity).*

#### Table 2: Topic Representations Generated for Each Sentence Within Initial Input

| Input Review | Results (Extracted Sentences -> BERTopic Representations) |
| :--- | :--- |
| *The staff were very kind and helpful. The dog was also a sweetheart. The water pressure in the shower was weak.* | * The staff were very kind and helpful $\\rightarrow$ `room_staff_clean_location`<br>* The dog was also a sweetheart $\\rightarrow$ `dog_cute_puppy_pet`<br>* The water pressure in the shower was weak $\\rightarrow$ `shower_wet_drain_water` |
| *Fantastic location in the tea village, surrounded by the wonderful tea hills. Owners of the homestay are always trying to help and support you and they offer a tasty dinner every evening. Hard bed. But for such a decent price, absolutely no complaints.* | * Fantastic location in the tea village surrounded by the wonderful tea hills $\\rightarrow$ `room_staff_clean_location`<br>* Owners of the homestay are always trying to help and support you and they offer a tasty dinner every evening $\\rightarrow$ `homestay_family_run_home`<br>* Hard bed $\\rightarrow$ `bed_hard_mattress_pillow`<br>* But for such a decent price absolutely no complaints $\\rightarrow$ `value_price_money_worth` |

---

## 4. Empirical Results

### 4.1. Topic Clusters and Visualization

For simplicity, we visualize nine topics as plotted in Fig. 4. It is observed that prominent keywords such as “pool (i.e., swimming pool quality), noise (noise levels), bike (bike rentals), beach (location with beachside), bed (bed comfort), and air (air conditioning)” are the most influential experiences. In addition, phrases such as \"host, helpful, kind, and friendly\" show the influence of employee conduct and service quality on experience satisfaction. Customer revisits and positive eWOM recommendations are strongly correlated with loyalty, as evidenced by keywords like \"definitely, return and recommend, visit soon\". It is noteworthy that these favourable experiences improve brand e-commerce performance and increase hotel online visibility. On the other hand, phrases like \"hard\", which refers to beds and \"hear\", which probably refers to environmental disruptions, highlight discontent among customers. A hotel's online reputation, rankings and customer bookings can all be negatively impacted by negative reviews.

Table 3 illustrates the efficiency of BERTopic in breaking down customer reviews into precise and actionable categories. For example, in the first input, the feedback regarding staff behavior, pet presence, and bathroom issues is accurately classified into topics such as `room_staff_clean_location`, `dog_cute_puppy_pet`, and `shower_wet_drain_water`. This demonstrates the performance of the present model for capturing diverse aspects of guest experiences. Similarly, the second example showcases comprehensive categorization into topics like `room_staff_clean_location` for location quality, `homestay_family_run_home` for hospitality, `bed_hard_mattress_pillow` for bed comfort, and `value_price_money_worth` for price satisfaction. This detailed analysis effectively highlights positive aspects, such as friendly staff and good value for money, while identifying negative issues like uncomfortable beds and bathroom issues.

#### Table 3: Keywords Associated with Weights for Symbolic Topics

| Aspect | Topic | Key representation (Weights) | Document representation (Sample Reviews) |
| :--- | :--- | :--- | :--- |
| **Facility** | Apartment<br>spacious<br>equip<br>bedroom | [0.312*‘apartment’ + 0.023*‘spacious’ + 0.018*‘equip’ + 0.017*‘bedroom’ + 0.016*‘clean’ + 0.013*‘kitchen’ + 0.012*‘view’ + 0.012*‘furnish’ + 0.012*‘modern’ + 0.011*‘studio’] | - The apartment itself was clean and comfortable<br>- The apartment is lovely and spacious<br>- Clean and well equipped apartment<br>- Very comfortable 2 bedroom apartment<br>- The apartment is clean and modern very convenient |
| **Amenity** | walk<br>city<br>distance<br>attraction | [0.101*‘walk’ + 0.090*‘city’ + 0.081*‘distance’ + 0.081*‘attraction’ + 0.065*‘center’ + 0.043*‘tourist’ + 0.037*‘main’ + 0.037*‘centre’ + 0.034*‘far’ + 0.032*‘location’] | - Its a good location to many attractions all less than 515 mins walk<br>- Perfect location to get to discover the city<br>- Fantastic location being walking distance to many attractions<br>- Good location near to all the main attractions and restaurants<br>- Very well located at walking distance from the main tourist destinations and attractions |
| **Service** | host<br>helpful<br>kind<br>friendly | [0.261*‘host’ + 0.029*‘helpful’ + 0.028*‘kind’ + 0.027*‘friendly’ + 0.022*‘welcome’ + 0.019*‘super’ + 0.017*‘family’ + 0.017*‘amazing’ + 0.016*‘responsive’ + 0.015*‘help’] | - Hosts were very kind and helpful<br>- The host and his staff are very kind and helpful<br>- Very friendly host and accommodating<br>- The hosts were very welcoming and helpful<br>- The host is a super friendly, helpful, and chill |
| **Experience value** | stay<br>overall<br>enjoy<br>pleasant | [0.155*‘stay’ + 0.096*‘overall’ + 0.078*‘enjoy’ + 0.054*‘pleasant’ + 0.035*‘wonderful’ + 0.035*‘love’ + 0.029*‘really’ + 0.029*‘happy’ + 0.024*‘enjoyable’ + 0.022*‘amazing’] | - The stay was way above my expectations<br>- We had a good stay overall<br>- Really enjoyed stay there<br>- Really pleasant stay<br>- It was an enjoyable stay |
| *(Exp. Value Cont.)* | picture<br>photo<br>exactly<br>look | [0.283*‘picture’ + 0.213*‘photo’ + 0.101*‘exactly’ + 0.094*‘look’ + 0.057*‘reality’ + 0.053*‘like’ + 0.042*‘match’ + 0.036*‘website’ + 0.031*‘different’ + 0.030*‘mislead’] | - Everything is just like on the pictures<br>- It was totally different from the photos on the internet<br>- It looks exactly like the pictures and easy to find<br>- The place looks nothing like the pictures<br>- The photos and the name clearly do not reflect the reality |
| **Loyalty** | homestay<br>family<br>run<br>recommend | [0.254*‘homestay’ + 0.021*‘family’ + 0.018*‘run’ + 0.012*‘recommend’ + 0.012*‘lovely’ + 0.011*’beautiful’ + 0.011*‘owner’ + 0.010*‘home’ + 0.010*‘locate’ + 0.010*‘experience’] | - I highly recommend this homestay and we sincerely hope to come back to see you all soon. We just wished we could have stayed longer but hopefully we will come back one day.<br>- We highly recommend this homestay very authentic and great value for money<br>- We can recommend the homestay without reservation.<br>- A lovely family run homestay made to feel very welcome and would highly recommend.<br>- Definitely comeback to this homestay when I travel to Can Tho. I really love it. |

### 4.2. Detected Topics

An analysis of reviews, as summarized in Table 4, reveals keywords describing the topics. Regarding a term of Facility, the most popular keyword is “apartment’’. Words like “spacious”, “kitchen” and “modern” accurately reflect their features. The keywords for each aspect such as Amenities, are clearly expressed through keywords like “location”, “walk” and “center” indicating the convenience that the hotel’s location brings to them. Interestingly, comments mentioning “picture”, “photo”, “website”, “match” and “exactly” suggest the photos accurately represent the apartments, building trust and a strong brand image through brand experience. The experience is also evident through high-weighted keywords such as “happy”, “pleasure”, “glad” and “enjoy”.

The number of sentences for each aspect in each dataset is shown in Fig. 7. Based on our observations, hotel facilities consistently emerge as the top concern for guests. Loyalty does not have a significant place in customers’ minds.

> **Fig. 7.** *The distribution of sentences in each aspect over years (2015–2023): Facility dominates with ~70% across all years, followed by Service, Experience, Amenity, and Loyalty.*

#### Table 4: An Illustration of Labeling Aspects and Sentence Sentiment Analysis

**Input Customer Review:**
> *“Beautiful place Ak the karaoke around. Every day whole day listening to karaoke from houses around. Crazy loud.”*

**Token-Level Aspect & Sentiment Assignment:**
```python
[
  ('Beautiful place', ['Experience']),
  ('Beautiful place', ['Positive']),
  ('Crazy loud', ['Experience']),
  ('Crazy loud', ['Negative']),
  ('Every day whole day listening to karaoke from houses around', ['Experience']),
  ('Every day whole day listening to karaoke from houses around', ['Negative']),
  ('the karaoke around', ['Amenity']),
  ('the karaoke around', ['Negative'])
]
```

### 4.3. Sentiment Analysis

In our current work, BERTopic divides text into smaller pieces and combines sentiment analysis using VADER (Valence Aware Dictionary and sentiment Reasoner) to establish data-driven persona creation, with coherence topics. It gets better at interpreting online reviews and informing management strategies, providing a more comprehensive assessment (Díaz and Rodríguez, 2018; Borges-Tiago et al., 2021). For example, as shown in Table 4 and Table 5, a customer review stated *“Beautiful place Ak the karaoke around. Every day whole day listening to karaoke from houses around. Crazy loud”.* It is labeled into two specific aspects, i.e, “Experience” and “Amenity”. Also, sentence sentiment analysis is assigned to the polarity items, i.e, “Positive” and “Negative”.

VADER uses a large sentiment lexicon with words assigned sentiment scores ranging from a deeply negative −1 to a highly positive +1. It utilizes a compound score to categorize reviews into positive, neutral and negative sentiments. A neutral sentiment label is assigned to reviews with a compound score of 0. Reviews are classified as negative when the compound score has a negative value. Conversely, reviews are considered positive when the compound score is positive. Our sentiment analysis revealed that a predominantly positive sentiment distribution is present within the review data. Positive reviews made up the most significant proportion, followed by neutral reviews. Negative reviews were the least frequent category, representing a small part of the dataset.

Table 5 reveals the sentiment statistics for each aspect within each dataset. The results show positive reviews with a rate of over 50%. Customer comments primarily focused on facilities, accounting for approximately 70%. Of these, 68% were positive, confirming this as a key strength, although around 10% negative ones indicate improvements. Services also received significant attention, achieving 12.85% on Booking and 9.45% on TripAdvisor. Such positive experience was reflected in 69.84% and 74% of responses. However, negative reviews of 11% on Booking and 7% on TripAdvisor suggest the need for improvements. This aligns with the work of Leite-Pereira et al. (2019) which emphasizes "facilities" and "services" as primary factors influencing hotel choices in both academia and enterprise. Similarly, Luo et al. (2021) showed that facilities often receive more positive than negative feedback. Amenity reviews comprised only 5–7% of total feedback, with an over 60% positivity rate and 30% neutral ones suggesting satisfaction, generating less negative attention and complaints.

On the other hand, the experience value had a higher negative feedback rate of 12% on Booking and 9% on TripAdvisor, indicating a need for improvement to enhance the perceived cost-benefit, cultural experience, or brand experience perceived balance for customers. Conversely, loyalty achieved the highest positive rates of 77.26% on Booking and 64.31% on TripAdvisor, with the lowest negative rates of approximately 6% on both platforms, reflecting customer loyalty to the brand's reputation. The study also revealed customer feedback concerns about facilities, amenities and services. It also highlights that hotels rarely receive negative feedback, impacting their image when customers focus on expected quality. For comprehensive improvement, prioritizing the reduction of negative feedback, especially regarding the overall experience, is crucial while maintaining the strengths in facilities, services and brand image.

Additionally, Table 6 shows the results of the sentence polarity analysis. We observe a variety of customer reviews with positive, negative, and neutral sentiments. Positive comments include phrases like "The breakfast was great and filling" and "I would love to return here again." These indicate that customers are satisfied with the breakfast and overall experience. However, negative sentiments such as "The bed mat was also hard, so it was hard for me to sleep" and "It was the most stressful experience" highlight areas for improvement, especially in bedding comfort and managing stressful situations. The neutral review, "Cheap 5 min from the beach," suggests that while the location is highly valued, there is no strong emotional connection to the hotel.

#### Table 5: The Distribution of Sentiments Across Five Aspects

| Platform / Aspect | Positive | Neutral | Negative | Total | % Positive | % Negative |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Booking.com** | | | | | | |
| Facility | 404,431 | 128,672 | 72,923 | 606,026 | 67% | 12% |
| Amenity | 40,109 | 18,621 | 6,880 | 65,610 | 61% | 10% |
| Service | 81,003 | 22,568 | 12,347 | 115,918 | 70% | 11% |
| Experience | 58,675 | 20,664 | 11,137 | 90,476 | 65% | 12% |
| Loyalty | 18,832 | 4,096 | 1,451 | 24,379 | 77% | 6% |
| **Booking.com Total** | **603,050** | **194,621** | **104,738** | **902,409** | **67%** | **12%** |
| **TripAdvisor** | | | | | | |
| Facility | 1,656,139 | 547,399 | 222,062 | 2,425,600 | 68% | 9% |
| Amenity | 129,539 | 59,417 | 15,894 | 204,850 | 63% | 8% |
| Service | 212,584 | 52,385 | 20,550 | 285,519 | 74% | 7% |
| Experience | 197,656 | 62,568 | 25,671 | 285,895 | 69% | 9% |
| Loyalty | 52,636 | 26,668 | 6,139 | 85,443 | 62% | 7% |
| **TripAdvisor Total** | **2,248,554** | **748,437** | **290,316** | **3,287,307** | **68%** | **9%** |

#### Table 6: Results of Overall Sentiment Analysis

| Document (Sample Review Sentence) | Compound score | Negative score | Neutral score | Positive score | Sentiment label from compound score |
| :--- | :--- | :--- | :--- | :--- | :--- |
| *The bed mat was also hard so it was hard for me to sleep* | -0.2023 | 0.189 | 0.811 | 0.000 | Negative |
| *Breakfast was great and filling* | 0.6249 | 0.000 | 0.494 | 0.506 | Positive |
| *Cheap 5 min from the beach* | 0.0000 | 0.000 | 1.000 | 0.000 | Neutral |
| *It was the most stressful experience* | -0.5563 | 0.418 | 0.582 | 0.000 | Negative |
| *I’d love to come back here again* | 0.6369 | 0.000 | 0.588 | 0.412 | Positive |
| *Everything was ok for 5 star accommodation* | 0.2960 | 0.000 | 0.694 | 0.306 | Positive |

### 4.4. Analyzing the Strong Impact of Loyalty on Ratings

In this study, we combine both methods: topic sentiment analysis using machine learning and manual labeling by experts. Topic sentiment analysis relies on BERTopic and VADER, which facilitate the processing of large datasets and quickly estimate the ratio of positive and negative aspect sentiments. It serves as a reference data, reduces workload, minimizes potential bias and enhances labeling consistency. However, it is often limited by context, negativity and new word trends (Liu, 2023). Therefore, we built a set of manually labeled data by experts as a “gold standard” for reference and validation of topic sentiment’s accuracy. It also ensures the reliability of WMLR. This combination aligns with the recommendation that human labeling remains irreplaceable even in the LLMs (Liu, 2023; Kejriwal et al., 2024; Yoo et al., 2024; Lahsini et al., 2026). Recent experiments have also demonstrated the “AI label effect” where humans still prefer human-generated data even when the objective quality is equivalent (Zhang et al., 2025). Thus, aspect-based sentiment manual annotation is essential and applied to better support machine-derived insights, strengthening reliability and interpretive depth.

Next, the model fitting assessment needs to be considered. Results listed in Table 7 show that our present approach is statistically significant overall and explains a substantial portion of the dependent variable customer rating variation. The results have a very high explanation compared to the practical research. In Booking.com, the Pseudo $R^2$ (McFadden) is 0.4617; in TripAdvisor, it is 0.5898. It is known in social and economic research that Pseudo $R^2$ values are often low due to complex and highly variable data. Values from 0.10 to 0.50 are acceptable if some or most explanatory variables are statistically significant. Particularly, values between 0.1 and 0.2 are still acceptable because they accurately reflect the inherently unpredictable nature of human behavior and economic phenomena (Ozili, 2023). And the model fitting strongly explains most of the variation in the dependent variable.

The Chi-square test $\chi^2$ of 1642.92 and 12131, respectively; $df = 15; p < 0.001$ confirms that the overall model has high statistical significance and practical value, significantly improving the predictive ability compared to the null model. The results confirm that customer experience, experience value and loyalty factors all play a decisive role in forming $CoRe$. The WMLR model achieved very high pseudo R-squared (McFadden) values, 0.4617 for Booking.com data and 0.5898 for TripAdvisor data, far exceeding the usual acceptance threshold (0.1–0.2) in social science research. The Likelihood Ratio test also yielded large chi-square statistics ($\chi^2 = 1642.92$ and $12131; p < 0.001$), confirming the model's superior explanatory power relative to the empty model.

In addition, the classification performance metric on Booking.com indicates a high level of sentiment classification, but also clearly reflects the imbalanced data distribution. On this dataset, the overall accuracy is 88%, slightly lower than the 91% observed in the TripAdvisor dataset. However, the results remain reliable for identifying trends of satisfaction and dissatisfaction. In particular, for the satisfied group, the assessment on Booking.com achieves near-perfect precision (0.98) and a recall of 0.88. These results are similar to those on TripAdvisor (precision 0.98, F1-score 0.95), showing the ability to identify this perfect group. On the other hand, the dissatisfied ones provide a clear difference between the two platforms with precision at 0.43 compared to 0.63 and recall (0.86, compared to 0.89). This shows that the model captures most dissatisfied cases but frequently confuses them with the satisfied group. This difference is likely due to the label imbalance, where satisfied responses dominate the underlying datasets (Le et al., 2025), which biases the learning model and reduces the accuracy of the minority group. This result confirms the outperformance of the present model in classifying positive emotions and points to improvements for more accurate recognition of negative experiences, an important factor for improving service quality.

Furthermore, to assess predictive performance, we examine the confusion matrices for the datasets. Fig. 8a shows TripAdvisor’s strong performance, with a clear “Satisfied” classification. The model achieved high accuracy in both sentiment classes (58.70% of comments were consistent). This result is consistent with that of Borges-Tiago et al. (2021), who found that platform users tend to use a positive tone, express their emotions clearly, and recount detailed experiences, making it easier for the model to distinguish between positive and negative feedback. This is the main difference between the two platforms, resulting in distinct writing styles. Booking.com ones (Fig. 8b) recorded a higher confusion rate in the “Unsatisfied” class. Although satisfied reviews were still accurately predicted, many negative reviews were misclassified as positive. Comments are short, informative, and often mix positive and negative elements in the same sentence (e.g., “Great location, but small and noisy room”). This is consistent with the previous work by Borges-Tiago et al. (2021), which showed that Booking.com users share positive experiences and report disputes or complaints. Despite using a positive-biased qualitative rating scale (Borges-Tiago et al., 2021; Leoni and Boto-García, 2023), Booking.com’s actual positive review rate is lower than TripAdvisor’s, with a consistency of only 37.18%. The combination of mixed sentiment and low consistency makes it difficult for the model to identify negative reviews accurately. Thereby, it made a prediction misunderstanding in the “Unsatisfied” class.

However, Booking.com is considered more trustworthy thanks to its user verification system, which only allows stayed visitors to post reviews, ensuring the authenticity of the feedback content (Vargas-Calderón et al., 2021; Leoni and Boto-García, 2023). But the complex language nature with hidden meanings, semantic ambiguity and the mixing of praise and criticism in the same review has created significant challenges for algorithms in categorizing emotions clearly (Bi et al., 2024; Le et al., 2025).

The Kernel density estimation (KDE) (see Fig. 9) exhibits a clear continuous distribution of predicted values. Both satisfaction classes have a high peak at 0.99 with densities of 10.71 and 12.63, indicating strong concentration. The real data show that satisfied customers have mostly rated close to perfect, and the distribution of these ratings is not widely dispersed. This is a reliable indication that customers are satisfied with the quality. The hotels have created a mostly positive experience. And the dissatisfied ones have a lower peak at 0.8 and 0.05 with densities of 1.13 and 1.75, with significant overlap in the range of 0.0–0.4 for Booking and to a lesser extent for TripAdvisor. This further explains some of the mislabeling in the confusion matrix. The WMLR model was effective in broadening the gap between the two extremes, improving the classification ability. The results of the KDE metric on manually labeled data and automatic sentiment analysis using VADER in Table 6 show a clear positive trend in customer experience on Booking.com, which is a testament to the overall quality view of hotels in Vietnam. The high density of satisfaction rates corresponds to the dominant positive feedback ratio in VADER, showing the relative consistency between the two methods. Overall, the KDE results have a fairly high reliability in overall classification, and there are certain limitations at the border between the two classes.

The results of the WMLR model in Python, following parameter tuning and model validation as described in Eq. (1), enable us to estimate the probability of a customer rating. We obtain an explicit form of $\log(CoRe)$ according to Booking.com (Eq. (2a)) and TripAdvisor (Eq. (2b)), with a focus on statistically significant variables ($p$-value $< 0.05$) as follows:

$$\begin{aligned}
\log(CoRe) = 1.9179 &+ 2.7410 LoyalPositive - 1.6632 LoyalNegative \\
&+ 1.1748 ExperiencePositive - 1.0367 ExperienceNegative \\
&+ 0.8956 ServicePositive - 0.8586 ServiceNegative \\
&+ 0.8424 FacilityPositive - 1.0778 FacilityNegative \\
&+ 0.4150 AmenityPositive - 0.4854 AmenityNegative
\end{aligned} \tag{2a}$$

$$\begin{aligned}
\log(CoRe) = 0.9143 &+ 1.7844 LoyaltyPositive - 2.0086 LoyaltyNegative \\
&+ 0.8229 ServicePositive - 0.7224 ServiceNeutral - 1.1069 ServiceNegative \\
&+ 0.7121 ExperiencePositive - 0.5466 ExperienceNeutral - 0.9516 ExperienceNegative \\
&+ 0.4459 FacilityPositive - 0.5403 FacilityNeutral - 1.1661 FacilityNegative \\
&+ 0.2692 AmenityPositive - 0.6887 AmenityNegative
\end{aligned} \tag{2b}$$

> **Fig. 8.** *Confusion matrix of logistic regression model: (a) TripAdvisor showing 58.70% consistency; (b) Booking.com showing 37.18% consistency with higher confusion in the Unsatisfied class.*
> **Fig. 9.** *Distribution function of the predicted values (Kernel Density Estimation - KDE) showing high concentration peaks at 0.99 for satisfied customers across both platforms.*

#### Table 7: Model Fitting Assessment

| Platform | Test | DF | p-value | Chi-square ($\chi^2$) | Pseudo $R^2$ (McFadden) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Booking.com** | Likelihood Ratio Test | 15 | < 0.001 | 1,642.92 | 0.4617 |
| **TripAdvisor** | Likelihood Ratio Test | 15 | < 0.001 | 12,131.00 | 0.5898 |

#### Table 8: The Classification Performance Metric

| Platform | Label | Precision | Recall | F1-Score | Support |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Booking.com** | 0 (unsatisfy) | 0.43 | 0.86 | 0.57 | 127 |
| | 1 (satisfy) | 0.98 | 0.88 | 0.93 | 1,264 |
| | *Accuracy* | | | 0.88 | 1,391 |
| | *Macro Avg* | 0.71 | 0.87 | 0.75 | 1,391 |
| | *Weighted Avg* | 0.93 | 0.88 | 0.91 | 1,391 |
| **TripAdvisor** | 0 (unsatisfy) | 0.63 | 0.89 | 0.73 | 392 |
| | 1 (satisfy) | 0.98 | 0.92 | 0.95 | 2,523 |
| | *Accuracy* | | | 0.91 | 2,915 |
| | *Macro Avg* | 0.80 | 0.90 | 0.84 | 2,915 |
| | *Weighted Avg* | 0.93 | 0.91 | 0.92 | 2,915 |

Our regression results reveal clear differences between two platforms. On Booking.com, the higher Positive coefficient indicates that favorable reviews are highly amplified, while negative feedback carries less weight-consistent with rating inflation. In contrast, TripAdvisor shows a stronger Negative coefficient, where critical reviews markedly reduce $\log(CoRe)$, reflecting stricter and more reality-oriented customer evaluations. These observations are consistent with previous studies (Taecharungroj and Mathayomchan, 2019; Rita et al., 2022; Leoni and Boto-García, 2023; Kalnaovakul et al., 2025) and are further validated.

It is seen that Loyalty has the strongest impact on $CoRe$, with a $p$-value $< 0.001$. It has the highest sensitivity in reducing $CoRe$ and provides a forecast of a large brand equity value loss if customers lose trust or are no longer loyal. Customer loyalty acts as an intermediary, linking customer factors with brand equity, so increasing brand strength and performance in the 4–5 star hotels (Camilleri and Filieri, 2023). The results obtained are similar to those of Borges-Tiago et al. (2021), Wilk et al. (2021), and France et al. (2025). They concluded that positive interactions in digital communities from brand trust and loyalty will contribute positively to brand co-creation. In addition, the impact of $FacilityNegative$, with $\beta = -1.0778$ and $-1.1661$, on the two platforms significantly affects $CoRe$ when it is not up to standard, second only to Loyalty. It shows that facilities are an important indicator of $CoRe$. This result is consistent with Martin-Fuentes et al. (2024), where facilities are the most influential factor on overall satisfaction, which is an important indicator to predict the downward trend in customer ratings. In addition, Experience and Service also have a significant positive impact and agree with the observation from Kalnaovakul et al. (2025). Although being an S variable in the S–O–R framework, amenities play only a supporting and indirect role with relatively low impact. And loyalty exerts the strongest influence, serving as the key intermediary linking experiences to brand values. It demonstrates that loyalty acts as a mediator, partially transmitting the effects of facilities, services, and amenities on $CoRe$ and reflecting customers' assessment and long-term attitude toward a brand. This, in turn, directly influences brand strength, performance, and equity (Franky and Syah, 2023; Piriyakul et al., 2024). It confirms that loyalty, as the Organism in the S-O-R framework, is the most significant factor in driving customer engagement and brand-related outcomes.

The regression results show that loyalty-related intentions have the largest coefficients in absolute value among the modeled aspects. This means that reviews containing strong revisit or recommendation signals are closely associated with higher satisfaction ratings ($CoRe$). This pattern supports the view that when guests express clear loyalty intentions in their reviews, they typically also report a high level of satisfaction and that a loss of such loyalty intentions is associated with markedly lower ratings and, consequently, weaker perceived brand performance.

In addition, some neutral factors have $p$-values greater than 0.05 and are not statistically significant. This indicates that neutral feedback is not strong enough to significantly influence overall ratings, unlike positive and negative feedback, which convey emotions more clearly. A valuable finding is the strong impact of negative reviews, via the large regression coefficients. It indicates a high sensitivity and a significant impact on brand equity. This highlights the importance of perfect customer experience management to limit negative attitudes and transform neutral ones into positive ones, thereby improving brand evaluation and brand performance (Martin-Fuentes et al., 2024). It is interesting that the key strategies should focus on strengthening loyalty with customer relationship management (CRM), improving hotel quality, designing unique experiences, and maintaining and equipping the unique local facilities and amenities to make a brand signature. Managing neutral feedback also plays an important role in optimizing review ratings and strengthening brand equity. It is consistent with previous articles emphasizing the leverage role of loyalty in improving brand image and review ratings (Piriyakul et al., 2024). In the hospitality industry, online reviews directly impact digital brand equity and attract new customers. The positive and negative effects reflect the individual sensitivity of each aspect: investing in the right strategies creates a competitive advantage, while a lack of control can become a serious weakness. KDE analysis shows that the majority of customer reviews are positive. But small amounts of negative feedback still have a strong impact. It emphasizes the importance of controlling touchpoints, especially in Loyalty, Experience value and Facility.

---

## 5. Findings and Discussion

### 5.1. Findings

This study identifies five key aspects reflected in online hotel reviews: facility, amenity, service, experience, and loyalty, together with customer sentiment. Customer reviews on Booking.com and TripAdvisor are primarily focused on amenities and services. They indicate that these dimensions dominate customers’ evaluative attention. Overall, positive sentiment outweighs negative sentiment across all aspects, suggesting that customer experiences generally meet or exceed expectations. Among these dimensions, higher ratings are most strongly associated with loyalty-related expressions, followed by sentiments toward service, experience and facilities. Reviews containing positive loyalty intentions, such as recommendations or intentions to return, consistently correspond to higher ratings, whereas lower ratings are strongly linked to negative loyalty expressions (e.g., “never again” or “stay away”).

### 5.2. Theoretical Implications

This study demonstrates the originality of the S–O–R framework by integrating sentiment analysis across five experiential aspects: facility, amenity, service, experience value and loyalty using large-scale online review data. The findings indicate that customer sentiment associated with each aspect serves as a distinct stimulus (S), rather than a general emotional evaluation. We show that loyalty-related expressions strongly shape individual ratings. Loyalty exhibits the strongest association with rating outcomes, reinforcing its role as an organismic state (O) within the S-O-R framework. Rather than assuming a causal sequence in which loyalty precedes satisfaction, the results suggest that loyalty co-develops with experiential evaluations and amplifies or attenuates how service-related stimuli are translated into ratings. By conceptualizing overall ratings as the response (R), this study provides a theoretical interpretation of ratings as quantitative manifestations of brand-related outcomes rather than simple proxies for satisfaction. This clarification enhances the internal consistency of the S–O–R framework in the context of online hotel reviews.

The WMLR results further strengthen this theoretical interpretation by mitigating the dominance of majority positive classes inherent in UMLR models. The weighted model captures negative experiential signals more sensitively, allowing organismic responses related to dissatisfaction and loyalty-related intentions to be more accurately reflected in rating behavior. In general, by combining BERTopic-based aspect extraction with sentiment and loyalty-related analysis, the proposed study extends the S–O–R framework to digital review platforms. It is suitable to explain consumer evaluation behavior in large-scale, imbalanced datasets.

### 5.3. Practical Implications

The present work brings practical implications to hoteliers by providing actionable insights derived from big data analytics, BERTopic, and weighted multinomial logistic regression. The study highlights customers’ key concerns related to facilities, service quality and experience value. It is useful for hoteliers to identify critical issues, detect emerging trends and make data-driven decisions to improve service delivery and online branding. By unifying sentiment analysis within hotel management strategies, the present work facilitates targeted managerial actions aimed at enhancing customer satisfaction and loyalty.

In particular, negative feedback points out the importance of improving room comfort, especially bedding quality. It reduces stressful service encounters. Conversely, hotels can use positive reviews by promoting breakfast services and encouraging repeat visits through loyalty programs. Enhancing the overall customer experience through personalized touches and consistent service excellence may also help convert neutral reviews into positive ones, therefore strengthening online reputation and revisit intentions. Importantly, the findings suggest that brand strengthening cannot rely solely on improving basic services or optimizing isolated touchpoints. Instead, hoteliers need to develop strategies that foster and sustain loyalty through emotional engagement, brand trust and personalized experiences, which form the foundation for long-term brand value creation, particularly in an increasingly competitive and dynamic digital environment.

At the same time, the strong influence of negative experiences on overall ratings signals a major risk to brand equity. It emphasizes the priority of minimizing and promptly addressing negative feedback. Accordingly, effective customer relationship management (CRM), continuous quality improvement and the design of unique experiences supported by distinctive local facilities and amenities can help hotels establish a recognizable brand signature and translate service quality into sustained brand equity.

---

## 6. Conclusion

This study analyzed over 1.3 million reviews from both Booking.com and TripAdvisor using BERTopic, refined with human-labeled sentiment and econometric techniques. Our work identified five fine-grained novel categories: facility, amenity, service, experience and loyalty, beyond traditional classifications. The present work provides a more diverse view of brand perception and customer experience. It enriches the existing literature on online reviews and sentiment modeling. Among these, loyalty emerged as the most influential factor, mediating the relationship between service delivery and overall ratings. From a managerial perspective, our study promotes actionable insights for hotel managers to build loyalty programs, optimize service delivery and strengthen online branding in competitive hospitality markets.

Our findings also extend previous research by empirically showing that:
1. Aspect-based emotional sentiments significantly influence rating behavior, with customer loyalty mediating this relationship;
2. Negative sentiments have a disproportionately larger impact compared to positive ones, confirming an asymmetry effect; and
3. Loyalty not only mediates but also amplifies the sentiment–rating connection, making it the main driver of overall evaluations.

These insights emphasize the dual role of loyalty as both a result of experience and a behavioral amplifier, yielding new theoretical and practical implications for hospitality research. The results indicate that loyalty-related intentions are tightly intertwined with aspect-based sentiments and satisfaction ratings: they are strongest when aspect sentiments are positive and weakest when experiences are negative. Rather than treating loyalty as a separate causal driver, our findings demonstrate that loyalty-related intentions co-evolve with satisfaction and appear to amplify the impact of positive (or negative) aspect experiences on the final rating.

However, some disadvantages still exist. The data originate from an emerging-market context, which limits their generalizability. Future research should extend the analysis to other destinations and cultural settings. Moreover, the imbalance in topic distribution suggests a need for advanced clustering or balancing techniques. In future, we will examine the model in depth, focusing on relevant impact variables through SEM and a suitable hypothesis framework to assess their impact on the overall rating.

---

## CRediT Authorship Contribution Statement

- **Nguyen Binh Thanh:** Writing – review & editing, Methodology, Supervision, Resources, Data curation.
- **Thang Quyet Nguyen:** Supervision, Funding acquisition, Conceptualization.
- **Le Hanh Thi My:** Writing – original draft, Visualization, Software, Methodology, Investigation, Formal analysis, Writing – review & editing, Validation, Data curation, Conceptualization.

## Declaration of Competing Interest

The authors declare that they have no known competing financial interests or personal relationships that could have appeared to influence the work reported in this paper.

## Acknowledgments

This research is funded by the Vietnam National Foundation for Science and Technology Development (NAFOSTED) under grant number `504.99–2024.12`. The authors would like to thank the AISIA Research Team and Mr Truong Phu Le for their assistance.

## Data Availability

The data and Python codes generated from this work are provided in the author’s GitHub repository: [https://github.com/Hanhlevna/Manhos](https://github.com/Hanhlevna/Manhos). Reviewers have requested that this repository be made public.

---

## References

1. Ahani, A., Nilashi, M., Yadegaridehkordi, E., Sanzogni, L., Tarik, A.R., Knox, K., Ibrahim, O., 2019. Revealing customers’ satisfaction and preferences through online review analysis: the case of Canary Islands hotels. *J. Retail. Consum. Serv.* 51, 331–343.
2. Angelov, D., 2020. Top2vec: Distributed representations of topics. *arXiv preprint* arXiv:2008.09470.
3. Bai, S., He, H., Han, C., Yang, M., Yu, D., Bi, X., Panigrahi, P.K., 2024. Exploring thematic influences on theme park visitors' satisfaction: an empirical study on Disneyland China. *J. Consum. Behav.* 23 (1), 90–106.
4. Bi, J.W., Zhu, X.E., Han, T.Y., 2024. Text analysis in tourism and hospitality: a comprehensive review. *J. Travel Res.* 63 (8), 1847–1869. https://doi.org/10.1177/00472875241247318.
5. Bian, Y., Ye, R., Zhang, J., Yan, X., 2022. Customer preference identification from hotel online reviews: a neural network based fine-grained sentiment analysis. *Comput. Ind. Eng.* 172, 108648.
6. Blei, D.M., Ng, A.Y., Jordan, M.I., 2003. Latent Dirichlet allocation. *J. Mach. Learn. Res.* 3, 993–1022.
7. Borges-Tiago, M.T., Arruda, C., Tiago, F., Rita, P., 2021. Differences between TripAdvisor and Booking.com in branding co-creation. *J. Bus. Res.* 123, 380–388.
8. Calheiros, A.C., Moro, S., Rita, P., 2017. Sentiment classification of consumer-generated online reviews using topic modeling. *J. Hosp. Mark. Manag.* 26 (7), 675–693.
9. Camilleri, M.A., Filieri, R., 2023. Customer satisfaction and loyalty with online consumer reviews: factors affecting revisit intentions. *Int. J. Hosp. Manag.* 114, 103575.
10. Chang, Y.C., Ku, C.H., Chen, C.H., 2020. Using deep learning and visual analytics to explore hotel reviews and responses. *Tour. Manag.* 80, 104129.
11. Chen, Y., Zhang, H., Liu, R., Ye, Z., Lin, J., 2019. Experimental explorations on short text topic mining between LDA and NMF based schemes. *Knowl. Based Syst.* 163, 1–13.
12. Cui, C., Wei, M., Che, L., Wu, S., Wang, E., 2022. Hotel recommendation algorithms based on online reviews and probabilistic linguistic term sets. *Expert Syst. Appl.* 210, 118503. https://doi.org/10.1016/j.eswa.2022.118503.
13. Dhanal, R.J., Ghorpade, V.R., 2024. Aspect-based sentiment-analysis using topic modelling and machine-learning. *Int. J. Electr. Comput. Eng.* 14 (6).
14. Díaz, M.R., Rodríguez, T.F.E., 2018. Determining the reliability and validity of online reputation databases for lodging: Booking.com, TripAdvisor, and HolidayCheck. *Journal of Vacation Marketing*, 24, pp. 261–274.
15. Egger, R., Yu, J., 2022. A topic modeling comparison between LDA, NMF, Top2Vec, and Bertopic to Demystify Twitter posts. *Front. Sociol.* 7, 886498.
16. El-Adly, M.I., 2019. Modelling the relationship between hotel perceived value, customer satisfaction, and customer loyalty. *J. Retail. Consum. Serv.* 50, 322–332.
17. Fan, Y., Isa, S.M., Yang, S., Goh, E., 2023. Please stay with us again: investigating the mediating roles of hedonic well-being and tourism autobiographical memory in customer retention at Chinese resorts. *J. Hosp. Tour. Manag.* 56, 410–419. https://doi.org/10.1016/j.jhtm.2023.08.005.
18. France, S.L., Davcik, N.S., Kazandjian, B.J., 2025. Digital brand equity: the concept, antecedents, measurement, and future development. *J. Bus. Res.* 192, 115273. https://doi.org/10.1016/j.jbusres.2025.115273.
19. Franky, F., Syah, T.Y.R., 2023. The effect of customer experience, customer satisfaction, and customer loyalty on brand power and willingness to pay a price premium. *Quant. Econ. Manag. Stud.* 4 (3), 437–452.
20. Geetha, M., Singha, P., Sinha, S., 2017. Relationship between customer sentiment and online customer ratings for hotels-An empirical analysis. *Tour. Manag.* 61, 43–54.
21. Grootendorst, M., 2022. BERTopic: Neural topic modeling with a class-based TF-IDF procedure. *arXiv preprint* arXiv:2203.05794.
22. Hu, N., Zhang, T., Gao, B., Bose, I., 2019. What do hotel customers complain about? Text analysis using structural topic model. *Tour. Manag.* 72, 417–426.
23. Kalnaovakul, K., Balasubramanian, K., Chuah, S.H.W., 2025. Service quality, customer sentiment and online ratings of beach hotels: an analysis of moderating factors. *J. Hosp. Tour. Insights* 8 (3), 988–1009.
24. Kejriwal, M., Santos, H., Shen, K., Mulvehill, A.M., McGuinness, D.L., 2024. A noise audit of human-labeled benchmarks for machine commonsense reasoning. *Sci. Rep.* 14 (1), 8609.
25. Kim, E.J., Baloglu, S., Henthorne, T.L., 2021. Signaling effects of branded amenities on customer-based brand equity. *J. Hosp. Mark. Manag.* 30 (4), 508–527. https://doi.org/10.1080/19368623.2021.1846651.
26. Kirilenko, A.P., Stepchenkova, S., 2025. Facilitating topic modeling in tourism research: comprehensive comparison of new AI technologies. *Tour. Manag.* 106, 105007.
27. Kirilenko, A.P., Stepchenkova, S.O., Dai, X., 2021. Automated topic modeling of tourist reviews: does the Anna Karenina principle apply? *Tour. Manag.* 83, 104241.
28. Kotler, P., Keller, K.L., 2006. Marketing Management. Pearson.
29. Lahsini, B.E., Ranjan, R.P., Gorge, A., 2026. Do managerial responses influence traveller retention. *Tour. Manag.* 112, 105243. https://doi.org/10.1016/j.tourman.2025.105243.
30. Le, H.T.M., Phan-Thi, T.A., Nguyen, B.T., Nguyen, T.Q., 2025. Mining online hotel reviews using big data and machine learning: an empirical study from an emerging country. *Ann. Tour. Res. Empir. Insights* 6 (1), 100170.
31. Lee, D., Seung, H.S., 2000. Algorithms for non-negative matrix factorization. *Adv. Neural Inf. Process. Syst.* 13.
32. Leite-Pereira, F., Brandão, F., Costa, R., 2019. Role of breakfast in hotel selection: systematic review. *Int. J. Cult. Tour. Hosp. Res.* 13 (2), 204–217.
33. Leoni, V., Boto-García, D., 2023. ‘Apparent’ and actual hotel scores under Booking.com new reviewing system. *Int. J. Hosp. Manag.* 111, 103493. https://doi.org/10.1016/j.ijhm.2023.103493.
34. Lerksuthirat, T., Srisuma, S., Ongphiphadhanakul, B., Kueanjinda, P., 2023. Sentiment and topic modeling analysis on twitter reveals concerns over cannabis-containing food after cannabis legalization in Thailand. *Healthc. Inform. Res.* 29 (3), 269–279.
35. Li, J., Xu, L., Tang, L., Wang, S., Li, L., 2018. Big data in tourism research: a literature review. *Tour. Manag.* 68, 301–323.
36. Liu, Y., 2023. The importance of human-labeled data in the era of LLMs. *arXiv preprint* arXiv:2306.14910.
37. Liu, F., Lai, K.H., Wu, J., Duan, W., 2021. Listening to online reviews: a mixed-methods investigation of customer experience in the sharing economy. *Decis. Support Syst.* 149, 113609. https://doi.org/10.1016/j.dss.2021.113609.
38. Luo, J., Huang, S., Wang, R., 2021. A fine-grained sentiment analysis of online guest reviews of economy hotels in China. *J. Hosp. Mark. Manag.* 30 (1), 71–95.
39. Martin-Fuentes, E., Mellinas, J.P., Mateu, C., 2024. Understanding Booking.com’s rating drop in the context of online hotel reviews. *Tour. Hosp. Res.* 14673584241283901.
40. Mirzaalian, F., Halpenny, E., 2021. Exploring destination loyalty: application of social media analytics in a nature-based tourism setting. *J. Destin. Mark. Manag.* 20, 100598.
41. Ozili, P.K., 2023. The acceptable R-square in empirical modelling for social science research. In *Social research methodology and publishing results: A guide to non-native English speakers* (pp. 134–143). IGI global.
42. Picek, S., Heuser, A., Jovic, A., Bhasin, S., Regazzoni, F., 2019. The curse of class imbalance and conflicting metrics with machine learning for side-channel evaluations. *IACR Trans. Cryptogr. Hardw. Embed. Syst.* 209–237.
43. Piriyakul, I., Kunathikornkit, S., Piriyakul, R., 2024. Evaluating brand equity in the hospitality industry: Insights from customer journeys and text mining. *Int. J. Inf. Manag. Data Insights* 4 (2), 100245.
44. Puh, K., Bagić Babac, M., 2023. Predicting sentiment and rating of tourist reviews using machine learning. *J. Hosp. Tour. Insights* 6 (3), 1188–1204.
45. Rabadán-Martín, I., Barcos-Redín, L., Pereira-Delgado, J., Aguado-Correa, F., Padilla-Garrido, N., 2025. Topic-based engagement analysis: focusing on hotel industry Twitter accounts. *Tour. Manag.* 106, 104981.
46. Radojević, T., Stanišić, N., Stanić, N., 2017. Inside the rating scores: a multilevel analysis of the factors influencing customer satisfaction in the hotel industry. *Cornell Hosp. Q.* 58 (2), 134–164. https://doi.org/10.1177/1938965516686114.
47. Rezaei, F., Raeesi Vanani, I., Jafari, A., Kakavand, S., 2024. Identification of influential factors and improvement of hotel online user-generated scores: a prescriptive analytics approach. *J. Qual. Assur. Hosp. Tour.* 25 (4), 1070–1109. https://doi.org/10.1080/1528008X.2022.2146620.
48. Rita, P., Ramos, R., Borges-Tiago, M.T., Rodrigues, D., 2022. Impact of the rating system on sentiment and tone of voice: a Booking.com and TripAdvisor comparison study. *Int. J. Hosp. Manag.* 104, 103245.
49. Sánchez-Franco, M.J., Rey-Moreno, M., 2022. Do travelers' reviews depend on the destination? An analysis in coastal and urban peer-to-peer lodgings. *Psychol. Mark.* 39 (2), 441–459.
50. Şanlıöz-Özgen, H.K., Kozak, M., 2023. Positioning five-star hotels in city destinations: the case of Istanbul, Turkey. *Tourism Hospital. Res.* 23 (2), 239–253.
51. Schlesinger, W., Cervera-Taulet, A., Pérez-Cabañero, C., 2020. Exploring the links between destination attributes, quality of service experience and loyalty in emerging Mediterranean destinations. *Tour. Manag. Perspect.* 35, 100699.
52. Situmeang, F., de Boer, N., Zhang, A., 2020. Looking beyond the stars: A description of text mining technique to extract latent dimensions from online product reviews. *Int. J. Mark. Res.* 62 (2), 195–215. https://doi.org/10.1177/1470785319863619.
53. Soler, I.P., Gémar, G., 2017. Brand equity research using online customer ratings of Spanish hotels. *Int. J. Tour. Res.* 19 (2), 191–202. https://doi.org/10.1002/jtr.2096.
54. Taecharungroj, V., Mathayomchan, B., 2019. Analysing TripAdvisor reviews of tourist attractions in Phuket, Thailand. *Tour. Manag.* 75, 550–568.
55. Vargas-Calderón, V., Moros Ochoa, A., Castro Nieto, G.Y., Camargo, J.E., 2021. Machine learning for assessing quality of service in the hospitality sector based on customer reviews. *Inf. Technol. Tour.* 23 (3), 351–379.
56. Wilk, V., Soutar, G.N., Harrigan, P., 2021. Online brand advocacy and brand loyalty: a reciprocal relationship. *Asia Pac. J. Mark. Logist.* 33 (10), 1977–1993. https://doi.org/10.1108/APJML-05-2020-0303.
57. Wu, L., Yang, W., Gao, Y., Ma, S., 2023. Feeling luxe: a topic modeling × emotion detection analysis of luxury hotel experiences. *J. Hosp. Tour. Res.* 47 (8), 1425–1452.
58. Xu, X., Li, Y., 2016. The antecedents of customer satisfaction and dissatisfaction toward various types of hotels: a text mining approach. *Int. J. Hosp. Manag.* 55, 57–69.
59. Yoo, J.W., Park, J., Park, H., 2024. The impact of AI-enabled CRM systems on organizational competitive advantage: a mixed-method approach using BERTopic and PLS-SEM. *Heliyon* 10 (16).
60. Zhang, J., Lu, X., Liu, D., 2021. Deriving customer preferences for hotels based on aspect-level sentiment analysis of online reviews. *Electron. Commer. Res. Appl.* 49, 101094.
61. Zhang, D., Niu, B., 2024. Leveraging online reviews for hotel demand forecasting: a deep learning approach. *Inf. Process. Manag.* 61 (1), 103527.
62. Zhang, W., Xie, C., Jiang, L., Yang, L., Hu, Z., Hao, N., 2025. Neural correlates of evaluative bias against artificial intelligence-labeled versus human-labeled artworks. *Soc. Cogn. Affect. Neurosci.* 20 (1), nsaf071.
63. Zhao, Y., Xu, X., Wang, M., 2019. Predicting overall customer satisfaction: big data evidence from hotel online textual reviews. *Int. J. Hosp. Manag.* 76, 111–121.
