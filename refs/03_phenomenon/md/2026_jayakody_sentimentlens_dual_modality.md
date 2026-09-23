# SentimentLens: Reconciling Sentiment and Ratings via Dual-Modality in the Hospitality Sector 

Dineth Jayakody, Pasindu Thenahandi, Sampath Jayarathna 

Department of Computer Science 

Old Dominion University 

Norfolk, Virginia, USA 

**_Abstract_ —Online travel platforms generate vast volumes of user-generated hotel reviews, offering rich opportunities to understand traveler experiences at scale. However, transforming unstructured textual feedback into structured, actionable insights remains a challenging task. This paper presents** **_SentimentLens_ , a scalable analysis system based on Aspect-Based Sentiment Analysis that performs knowledge extraction from unstructured hotel reviews and organizes them into interpretable service categories. SentimentLens integrates aspect term extraction, aspect sentiment classification, semantic category assignment, and multilevel analytical modules to support region-level, hotel-level, and category-level evaluation. The system is designed to operate across different geographic contexts and hospitality settings. To demonstrate its practical utility, we apply SentimentLens to a large real-world dataset of over 10,000 publicly available hotel reviews. Through extensive analysis, the framework reveals how traveler sentiment varies across regions, service categories, and hotel archetypes. We further implement a cross-modal reconciliation of textual sentiment and numerical ratings to identify latent operational conflicts, structural inconsistencies in service quality, and high-impact improvement opportunities using importance–performance and entropy-based analyses. The results show that SentimentLens effectively transforms largescale unstructured reviews into actionable intelligence, supporting data-driven decision-making for hospitality management and tourism policy. While demonstrated using a national case study, the proposed system is generalizable to other destinations and review-driven service domains.** 

**_Index Terms_ —Information Fusion, Information Integration, Aspect-Based Sentiment Analysis, Decision Support Systems, Knowledge Discovery** 

## I. INTRODUCTION 

Online travel platforms produce large volumes of usergenerated hotel feedback in two complementary forms: (i) unstructured textual reviews describing guest experiences in detail, and (ii) structured metadata such as star ratings and trip types. Star ratings provide a quick summary of overall satisfaction but often hide the specific reasons behind positive or negative experiences, while textual reviews contain rich explanations yet are difficult to analyze systematically at scale. Therefore, an effective tourism analytics system should jointly leverage both modalities to produce reliable, interpretable, and actionable insights [1]. Aspect-Based Sentiment Analysis (ABSA) is a widely adopted approach for extracting finegrained opinions from review text by identifying specific aspects and predicting the sentiment expressed toward each 

one [2], [3]. However, many ABSA-driven studies stop at producing predictions, without integrating them into a broader workflow that supports region-level comparison, hotel benchmarking, and decision-making. Moreover, relying solely on either modality risks missing patterns that only become visible when both signals are combined. 

In this work, we present SentimentLens, a scalable information integration framework that performs multimodal fusion across two heterogeneous data streams: (i) a text-based pipeline that applies ABSA to extract aspect-level sentiment and organizes aspects into standardized service categories, and (ii) a rating-based pipeline that analyzes star rating distributions and traveler trip types with province-wise comparisons and statistical significance testing. A fusion layer then reconciles insights across both modalities, highlighting agreements and discrepancies. To demonstrate its practical utility, we conduct a large-scale case study using more than 10,000 publicly available hotel reviews covering hotels across the nine provinces of Sri Lanka, illustrating how SentimentLens uncovers province-level satisfaction differences, category-level strengths and weaknesses, hotel archetypes, and targeted improvement opportunities. 

The main contributions of this paper are: 

- We propose _SentimentLens_ , a unified cross-modal reconciliation framework that integrates hotel review text and structured ratings to extract actionable insights at scale. 

- We introduce a systematic approach for aligning aspectlevel sentiment with numerical rating signals, enabling the identification of inconsistencies, latent service gaps, and hidden performance issues across modalities. 

- We develop an end-to-end analytical pipeline that combines ABSA-based aspect extraction, semantic category alignment, and multi-level aggregation across provinces, hotels, and service categories for interpretable analysis. 

- We validate the proposed framework through a large-scale real-world case study, demonstrating that cross-modal integration improves interpretability and reveals insights that are not observable from single-modality analysis alone. 

While this paper focuses on hotels, the proposed system generalizes to other review-driven service domains (e.g., restaurants, attractions, airlines) where both text feedback and numerical ratings are available. 

## II. LITERATURE REVIEW 

Prior research consistently identifies a common set of service dimensions that drive customer satisfaction in the hotel industry including room quality staff and reception services food and beverage offerings location convenience and value for money [4], [5]. While these attributes significantly influence satisfaction and loyalty empirical studies show that their performance is often uneven with critical factors such as cleanliness reliability and restaurant services frequently underperforming despite their high importance [5]. This highlights persistent structural gaps in hotel service delivery and the need for targeted improvement strategies. 

Recent advances in automated text analysis have enabled large-scale exploitation of online hotel reviews. Studies show that negative reviews concentrate on a few key issues such as cleanliness, staff behavior, and pricing, while positive reviews span a wider range of experiences. Moreover, negative sentiment has a disproportionately strong impact on perceived service quality and behavioral intentions [6]. To capture such finegrained insights, aspect-based sentiment analysis (ABSA) has emerged as a dominant approach, linking sentiment polarity to specific hotel attributes such as service, food, cleanliness, and location [7]. Although recent work highlights rapid progress in transformer-based ABSA and improved handling of implicit aspects [8], limitations remain, including fragmented pipelines, weak integration with rating metadata, and limited focus on managerial decision support. 

Deep learning approaches now dominate ABSA in the hospitality domain. Models such as Convolutional Neural Networks and Bidirectional Long Short-Term Memory networks outperform traditional methods for aspect extraction and sentiment classification [7]. More recent studies leverage transformer embeddings with clustering and semantic similarity to improve implicit aspect detection and contextual understanding [8]. Emerging work also integrates ABSA into decision support systems, including dashboards, recommender systems, and multi-criteria models, to assist managers in identifying strengths, weaknesses, and investment priorities. 

However, these decision-support applications remain limited in scope. Most ABSA studies still focus on isolated modeling tasks or single-platform analyses and rarely perform systematic regional or cross-hotel aggregation, which restricts their practical utility for hotel chains and destination-level strategy development. Although recent advances in locationspecific modeling, hotel similarity clustering via aspect-aware embeddings, and cross-language/multi-agent frameworks have begun to address these limitations by uncovering hidden service patterns across geographies and languages, unified end-to-end analytical systems capable of seamlessly integrating textual sentiment, numerical ratings, and multi-level (regional/hotel/aspect) insights are still scarce [9]–[11]. 

In summary, although ABSA is well established for extracting fine-grained insights from hotel reviews [4], [7], it is often treated as an isolated modeling task. The absence of unified, end-to-end frameworks that integrate textual sentiment 

with numerical ratings and enable systematic regional and cross-hotel aggregation continues to limit the translation of these insights into actionable strategies. This persistent gap motivates the development of system-oriented approaches such as _SentimentLens_ , which aim to bridge modeling accuracy with practical, data-driven decision making in the hospitality sector. 

## III. METHODOLOGY 

## _A. Raw Data Sources_ 

Raw hotel reviews are collected using Apify [12], a webscraping platform that provides reliable tools for extracting publicly available online content. Reviews are gathered from two major online travel platforms, Google Reviews and TripAdvisor [13], [14]. These platforms were selected due to their widespread use and the availability of both textual feedback and structured rating information. The scraping process extracts only content that users have voluntarily shared publicly on the respective platforms. No private, sensitive, or personally identifiable user data are collected. Each record includes structured attributes such as hotel name, city, province, star rating, and traveler trip type (when available), along with unstructured free-text reviews. The dataset covers hotels from all nine provinces of Sri Lanka, with more than ten hotels per province. For each hotel, the latest 100 reviews are collected, resulting in a corpus of over 10,000 raw hotel reviews. This geographically balanced dataset supports region-level and hotel-level analysis. 

## _B. Data Preprocessing_ 

The collected data are initially stored as raw CSV files for each province. Preprocessing steps include extracting only relevant fields, eliminating empty records, removing duplicate reviews, and merging them into a single unified dataset. Reviews with missing essential metadata or unusable text are discarded. The resulting cleaned dataset is then passed through the text-based and rating-based analytical pipelines. 

## _C. Aspect-Based Sentiment Analysis Framework_ 

The foundational integration layer of the proposed system is a custom ABSA pipeline that integrates Aspect Term Extraction (ATE) and Aspect Sentiment Classification (ASC) into a unified workflow. The entire pipeline is self-hosted and operates locally, without reliance on third-party large language model APIs, enabling scalable, cost-free, and privacypreserving analysis. 

ABSA is performed using _Instruct-DeBERTa_ [15], a hybrid instruction-based framework that jointly handles aspect extraction and sentiment classification. The model uses instructiondriven prompts to identify both explicit and implicit aspect terms from review text and simultaneously predicts the corresponding sentiment polarity (positive, negative, or neutral) for each extracted aspect. This unified approach enables coherent modeling of fine-grained opinions by linking aspect detection and sentiment interpretation within a single framework. This enables context-aware sentiment prediction when multiple aspects occur in the same review. To support higher-level analysis, aspect terms are mapped to semantic categories 



Fig. 1: **System architecture of** **_SentimentLens_ .** The framework ingests raw review text together with structured metadata, performs aspect extraction and aspect-level sentiment classification, maps extracted aspects into standardized service categories, and then aggregates the outputs into province-level, hotel-level, and cross-modal analytical views for downstream reconciliation. 

(Facilities, Food and Dining, Room Quality, Staff, Location, Booking Process) using centroid-based embedding prototypes. Aspect terms and category keywords are embedded using GIST Sentence Transformers [16], and each aspect is assigned to the category with the highest cosine similarity above a threshold. The pipeline is applied to over 10,000 reviews, producing structured triples _(aspect: category: sentiment)_ stored in CSV format for downstream analysis. 

## _D. Analytical Representation of Aspect-Level Sentiment_ 

Each raw hotel review is decomposed into multiple aspectlevel sentiment entries of the form 



After filtering invalid, missing, or generic categories, each remaining entry represents a single opinion toward a concrete service dimension. This produces an aspect-level dataset _D_ with one row per aspect mention, enabling aggregation across hotels, provinces, and categories. 

Sentiment polarity is mapped to a numerical score 



where _si_ denotes the sentiment score of the _i_ -th aspect mention. Let _A_ be the set of all aspect mentions, _Ac_ the 

subset belonging to category _c_ , _Ap_ the subset originating from province _p_ , and _Ac,p_ the subset corresponding jointly to category _c_ in province _p_ . 

## _E. Category- and Province-Level Sentiment Aggregation_ 

Category importance is defined as the relative frequency with which a category is mentioned: 



where _wc_ is the importance weight of category _c_ . 

Average sentiment per category is computed as 



Overall sentiment per province is computed as 



To analyze regional variation across service dimensions, a province–category sentiment matrix is defined as 



where _s_ ¯ _c,p_ is the mean sentiment of category _c_ in province _p_ . For profile-based comparisons, each province is represented by the vector 



where _C_ is the number of standardized service categories. 

## _F. Comparative Indices and Stability Measures_ 

For each category _c_ , the best-performing province is defined as 



Inter-provincial variability for category _c_ is measured using the standard deviation 



where _P_ is the number of provinces and _µc_ is the mean sentiment of category _c_ across all provinces. 

To integrate category importance with performance, a Province Competitiveness Index (PCI) is defined as 



This index gives greater emphasis to categories that travelers mention more frequently. 

_G. Co-occurrence, Entropy, and Hotel Archetype Discovery_ 

Let _Nc_ 1 _,c_ 2 denote the number of reviews in which categories _c_ 1 and _c_ 2 co-occur. These values form a category cooccurrence matrix **C** that is used to study interactions among service dimensions. 

To quantify uncertainty in category-level experience, sentiment entropy is computed as 



where _P_ ( _s_ = _k | c_ ) denotes the probability that sentiment class _k_ occurs within category _c_ . 

For hotel archetype analysis, each hotel _h_ is represented by a category-level sentiment vector 



After standardization, K-Means clustering is applied by minimizing 



where _Ck_ and **_µ_** _k_ denote cluster _k_ and its centroid, respectively. The selected number of clusters is determined using the elbow method. 

_H. Opportunity Gap Formulation_ 

To compare category importance against performance on a common scale, sentiment is normalized to [0 _,_ 1] as 



An opportunity score is then defined as 



where high values indicate categories that are heavily discussed but underperform relative to guest expectations. 

_I. Rating- and Trip-Type-Based Analysis_ 

In parallel with the text-based pipeline, the structured ratings dataset is cleaned by removing invalid or missing trip-type entries. Province-level mean rating is computed as 



where _Np_ is the number of ratings available for province _p_ . To assess regional differences in ratings, a one-way ANOVA is performed under the null hypothesis 



Pairwise post-hoc comparisons are subsequently examined using Tukey’s HSD test. To analyze the association between province and trip type, a chi-square test of independence is used with statistic 



where _Oij_ and _Eij_ denote observed and expected counts, respectively. 

## _J. Cross-Modal Conflict Identification_ 

To reconcile textual sentiment with numerical ratings, SentimentLens identifies latent conflicts between the normalized rating signal and aspect-level sentiment. A conflict set is defined as 



where _h_ denotes a hotel, _c_ a service category, _R_ norm the normalized overall rating, _Sa_ the category-level sentiment score, and _τ_ an empirically selected discrepancy threshold. This formulation captures cases in which high overall ratings mask recurring category-specific weaknesses. 

## IV. RESULTS 

This section presents the empirical findings obtained from 46,565 aspect-level sentiment mentions extracted from 100 hotels distributed across the nine provinces of Sri Lanka. 

_A. Sentiment-Based Analysis of Traveler Reviews_ 



Fig. 2: **Global category importance versus average sentiment.** The figure shows which service categories dominate traveler discourse and how positively they are perceived on average. _Staff_ occupies the strongest performance region, while _Booking Process_ and _Room Quality_ appear as comparatively weaker categories despite their importance, highlighting where operational weaknesses persist. 

At the global category level, _the_ guest discourse is dominated by staff, _Food and dining_ and _Room Quality_ (Fig.2). _Staff_ achieves the strongest sentiment performance, suggesting that interpersonal service is a national strength. In contrast, _Booking Process_ and _Room Quality_ receive weaker sentiment despite being frequently discussed, indicating persistent operational weaknesses in high-visibility service dimensions. 

At the province level, Eastern, Central, Western, and Southern Provinces show the strongest overall sentiment (Fig.3b), consistent with more mature tourism ecosystems, while Northern Province records the weakest, reflecting persistent issues in service consistency and accommodation quality. When examined jointly with service category, _Staff_ sentiment remains consistently high across most provinces, whereas _Room Quality_ , _Facilities_ , and _Booking Process_ show strong regional 



(a) Province–category sentiment heatmap 





<!-- Start of picture text -->
(b) Average overall rating by province<br><!-- End of picture text -->

Fig. 3: Regional sentiment structure across service categories. (a) The heatmap makes cross-province strengths and weaknesses immediately visible and shows that _Staff_ remains relatively strong across most regions, whereas _Room Quality_ , _Facilities_ , and _Booking Process_ vary more sharply by province. (b) Average overall ratings by province show that Eastern, Central, and Western Provinces achieve the highest scores, while Northern Province records the lowest, a pattern that closely mirrors the sentimentbased provincial ranking. **Together, these panels confirm that regional performance differences are multidimensional and consistent across both textual and numerical feedback modalities.** 

disparities, suggesting that physical infrastructure and operational reliability vary more substantially than staff-related experiences. 

The category-wise leader analysis (Fig.3a) shows that no single province dominates every dimension. Central Province performs especially well in _Location_ , _Facilities_ , and _Booking Process_ , while Eastern Province leads in _Staff_ and _Food and Dining_ . Variation analysis confirms that _Room Quality_ and _Facilities_ are the least stable categories across provinces, whereas _Staff_ and _Location_ function as broad national assets. The province competitiveness analysis ranks Eastern Province as the strongest overall performer and Northern Province last, consistent with both category-level and province-level observations. 

The co-occurrence analysis reveals that _Staff_ is strongly linked with _Food and Dining_ and _Room Quality_ , suggesting that service experiences are not perceived in isolation. The entropy analysis further shows that _Booking Process_ and _Room Quality_ exhibit the highest experiential uncertainty, while _Staff_ remains the most consistently positive dimension. Hotellevel clustering identifies three archetypes, premium, mid-tier, and struggling, with low-performing hotels concentrated in Northern and Sabaragamuwa Provinces and stronger hotels in Eastern, Central, Southern, and Western Provinces. Finally, the importance–performance analysis highlights _Room Quality_ and _Food and Dining_ in Northern, North Central, and Sabaragamuwa Provinces as the clearest high-priority opportunity gaps. 

## _B. Rating- and Trip-Type-Based Analysis_ 

The rating distribution is strongly skewed toward the upper end of the scale, indicating that most hotels receive favorable overall evaluations. However, this apparent positivity does not eliminate meaningful differences across provinces. Southern, Central, and Eastern Provinces achieve the highest average ratings, while Northern Province records the lowest. This 

mirrors the province-level sentiment ranking and suggests that the structured rating signal is broadly aligned with the sentiment extracted from text. 

Trip-type analysis shows that average ratings vary only slightly across traveler categories, indicating that hotels in the dataset tend to deliver broadly similar overall satisfaction to families, couples, solo travelers, and business travelers. In contrast, the distribution of trip types across provinces is not uniform. Leisure-oriented provinces show stronger concentrations of families and couples, whereas Western Province has a comparatively larger share of business travelers. This indicates that while traveler composition differs geographically, the average rating signal itself remains comparatively stable across traveler types. 

The inferential analysis reinforces these descriptive observations. Province-level differences in ratings are statistically significant, confirming that regional quality differences are not due to random fluctuation. Post-hoc comparisons identify Northern Province as significantly lower-rated than most other provinces, while Southern and Uva Provinces appear among the stronger performers. By contrast, ratings do not differ significantly across trip types, supporting the descriptive finding that satisfaction is relatively uniform across traveler groups. The chi-square analysis further confirms that province and trip type are associated, meaning that different regions attract different mixes of travelers even when their average rating levels by traveler type remain similar. 

## _C. Cross-Modal Conflict Identification_ 

To enable systematic reconciliation between textual sentiment and numerical ratings, we identify latent conflicts as discrepancies between the normalized rating signal and aggregated aspect-level sentiment. Intuitively, a conflict arises when overall satisfaction remains high while specific service dimensions exhibit weaker sentiment. 

The overall rating is normalized to the [0 _,_ 1] range using min–max scaling over the original [1 _,_ 5] scale, ensuring direct comparability with sentiment scores. For example, an average rating of 4 _._ 24 corresponds to a normalized value of 0 _._ 81, as observed in the Northern Province. 

Conflicts are identified at the province–category level by comparing normalized ratings with category-level sentiment scores, as defined in Equation (15). Larger gaps indicate stronger disagreement between overall satisfaction and finegrained service experience. 

TABLE I: Examples of cross-modal conflicts. Larger gaps indicate stronger disagreement between rating and sentiment. 

|**Province**|**Category**|_R_norm|_Sa_|**Gap**|
|---|---|---|---|---|
|Northern Province|Room Quality|0.81|0.40|0.41|
|Northern Province|Facilities|0.81|0.46|0.35|
|Sabaragamuwa Province|Food|0.85|0.61|0.24|



_a) Illustrative examples.:_ These examples reveal _latent service gaps_ , where relatively strong overall ratings mask weaker performance in specific categories. For instance, in the Northern Province, despite a normalized rating of 0 _._ 81, sentiment toward _Room Quality_ drops to 0 _._ 40, indicating recurring dissatisfaction that is not reflected in the aggregate rating. Similar discrepancies are observed for _Facilities_ in the same province and _Food and Dining_ in Sabaragamuwa Province. 

Such patterns highlight a key limitation of rating-only analysis. While ratings capture broad impressions, they often obscure category-specific weaknesses. By contrast, aspectlevel sentiment provides fine-grained visibility into operational performance. The proposed cross-modal conflict identification mechanism therefore enables detection of targeted improvement areas that remain hidden when relying on a single modality. 

## V. DISCUSSION AND CONCLUSION 

The _SentimentLens_ framework reveals clear geographic disparities in hotel performance across Sri Lankan provinces, highlighting consistent national strengths in _Staff_ and _Location_ alongside structural weaknesses in _Room Quality_ , _Facilities_ , and _Booking Process_ , while also uncovering latent inconsistencies where strong overall ratings may mask weaker categorylevel experiences, thereby emphasizing the importance of cross-modal analysis in identifying targeted improvement opportunities, particularly in _Room Quality_ and _Food and Dining_ in underperforming regions, while maintaining core service strengths. These findings demonstrate that integrating textual sentiment with numerical ratings provides a more comprehensive and reliable basis for data-driven decision-making in the hospitality sector. 

Overall, this study introduced _SentimentLens_ , a scalable framework that integrates Aspect-Based Sentiment Analysis (ABSA) with structured rating analytics to generate interpretable, multi-level insights from large-scale hotel reviews. Using over 10,000 publicly available reviews across all nine 

provinces of Sri Lanka, the framework demonstrates strong capability in identifying actionable service gaps, regional disparities, and hidden performance issues. Although evaluated in a national tourism context, the approach is generalizable, scalable, and adaptable to other regions and multilingual settings. 

Future work will focus on extending the framework with real-time data integration, predictive modeling, intelligent recommendation mechanisms, and cross-domain generalization with deeper multimodal fusion to support more robust, proactive, and adaptive decision-making in dynamic environments. 

## CODE AVAILABILITY 

The full implementation of _SentimentLens_ will be made publicly available upon acceptance. 

## REFERENCES 

- [1] Y. Chen, Y. Zhong, S. Yu, Y. Xiao, and S. Chen, “Exploring bidirectional performance of hotel attributes through online reviews based on sentiment analysis and kano-ipa model,” _Applied Sciences_ , vol. 12, no. 2, p. 692, 2022. 

- [2] W. Zhang, X. Li, Y. Deng, L. Bing, and W. Lam, “A survey on aspect-based sentiment analysis: Tasks, methods, and challenges,” _IEEE Transactions on Knowledge and Data Engineering_ , vol. 35, no. 11, pp. 11 019–11 038, 2022. 

- [3] D. Jayakody, K. Isuranda, A. Malkith, N. De Silva, S. R. Ponnamperuma, G. Sandamali, and K. Sudheera, “Aspect-based sentiment analysis techniques: A comparative study,” in _2024 Moratuwa Engineering Research Conference (MERCon)_ . IEEE, 2024, pp. 205–210. 

- [4] J. Shin, J. Joung, and C. Lim, “Determining directions of service quality management using online review mining with interpretable machine learning,” _International journal of hospitality management_ , vol. 118, p. 103684, 2024. 

- [5] V. Perdomo-Verdecia, P. Garrido-Vega, and M. Sacrist´an-D´ıaz, “An fsQCA analysis of service quality for hotel customer satisfaction,” _International Journal of Hospitality Management_ , vol. 122, p. 103793, 2024. 

- [6] W. Xu, Z. Yao, Y. Ma, and Z. Li, “Understanding customer complaints from negative online hotel reviews: A BERT-based deep learning approach,” _International Journal of Hospitality Management_ , vol. 126, p. 104057, 2025. 

- [7] R. A. Charisma, N. A. P. Masaling, A. Maulina, F. R. Tambunan, L. A. Y. Caesar, and R. C. Chow, “A comparative study of transformerbased models for aspect-based sentiment analysis on indonesian hotel reviews,” in _2025 8th International Seminar on Research of Information Technology and Intelligent Systems (ISRITI)_ . IEEE, 2025, pp. 221–226. 

- [8] I. C. Sahin and C. Eyupoglu, “Aspect-based sentiment analysis for hospitality industry applications:: A systematic literature review,” _Applied Computer Systems_ , vol. 30, no. 1, pp. 53–67, 2025. 

- [9] T. K. Tran and P. Tran, “Aspect-based sentiment analysis in ho chi minh city hotel reviews using aspect-conditioned bilstm with crossaspect attention and ordinal regression,” _IEEE Access_ , 2026. 

- [10] A. C. Ozt¨urk<sup>¨</sup> and F. Soygazi, “Revealing hotel similarities via aspectbased sentence embedding of guest reviews,” _PeerJ Computer Science_ , vol. 12, p. e3713, 2026. 

- [11] X. Han, “Cross-language hotel review sentiment analysis via multiagent federated learning with heterogeneous graph attention networks,” _Scientific Reports_ , 2026. 

- [12] “Apify web scraping platform,” https://apify.com/, accessed: 2026-04. 

- [13] “Google reviews,” https://www.google.com/maps, accessed: 2026-04. 

- [14] “Tripadvisor,” https://www.tripadvisor.com, accessed: 2026-04. 

- [15] D. Jayakody, A. Malkith, K. Isuranda, V. Thenuwara, N. de Silva, S. R. Ponnamperuma, G. Sandamali, and K. Sudheera, “Instruct-deberta: A hybrid approach for aspect-based sentiment analysis on textual reviews,” _The International Journal on Advances in ICT for Emerging Regions_ , vol. 18, no. 2, 2025. 

- [16] A. V. Solatorio, “GISTembed: Guided in-sample selection of training negatives for text embedding fine-tuning,” _arXiv preprint arXiv:2402.16829_ , 2024. 

## **APPENDIX** 

## VI. MODEL AND DATA INITIALIZATION 

## _A. Dataset Collection and Geographic Coverage_ 

The dataset used in this study consists of hotel reviews collected from properties distributed across all regions of Sri Lanka. To ensure geographic diversity and reduce locationspecific bias, a total of 100 hotels were selected to represent different provinces and tourism zones within the country. 

To validate the spatial distribution of the dataset, we visualize the geographic locations of all selected hotels on a map of Sri Lanka. This visualization demonstrates that the dataset is well-distributed across the country, covering coastal, urban, and inland regions, thereby enabling a comprehensive analysis of hospitality trends at a national level. 



Fig. 4: Geographic distribution of the selected hotel dataset across Sri Lanka. Each point represents a hotel included in the study, illustrating broad national coverage across multiple regions. 

## _B. Aspect Categorization via Semantic Prototypes_ 

While the main paper describes the _Instruct-DeBERTa_ framework for aspect-based sentiment analysis, we further 

extend the pipeline by introducing a semantic category assignment mechanism for extracted aspects. 

We define a set of domain-specific aspect categories relevant to the hospitality industry, such as _Facilities_ , _Food and Dining_ , _Room Quality_ , and _Staff_ . Each category is represented using a curated set of representative keywords. 

To enable robust semantic matching, each keyword is encoded into a normalized embedding vector using a sentence transformer model. A centroid prototype is then computed for each category by aggregating the embeddings of its associated keywords. 

Given an extracted aspect, it is projected into the same embedding space and compared against all category prototypes using cosine similarity. The aspect is assigned to the most similar category when the similarity exceeds a predefined confidence threshold; otherwise, it is categorized as _other_ . This approach enables flexible and semantically consistent mapping from extracted aspects to higher-level categories. 

## _C. t-SNE Visualization of Category Embeddings_ 

To analyze the semantic structure of the defined categories, we visualize the embedding space of all category keywords using t-distributed Stochastic Neighbor Embedding (t-SNE). Each keyword is embedded using the same model and projected into a two-dimensional space. 

The resulting visualization shows clear clustering behavior, where semantically related keywords group together according to their assigned categories. Each category is represented using a distinct color, and individual words are annotated to enhance interpretability. 



Fig. 5: t-SNE visualization of category keyword embeddings. Each point represents a keyword, colored by its assigned aspect category. The clustering demonstrates strong semantic coherence within categories and clear separation across different categories. 

TABLE III: Average sentiment scores across categories. 

|**Category**|**Avg Sentiment**|**Interpretation**|
|---|---|---|
|Staff|0.864|Extremely positive hospitality|
|Location|0.836|Strong scenic appeal|
|Food and Dining|0.712|Generally positive but variable|
|Facilities|0.690|Moderate satisfaction|
|Room Quality|0.638|Mixed experiences|
|Booking Process|0.556|Lowest satisfaction|



## _D. Model Inference Pipeline_ 

The aspect-based sentiment analysis framework described in the main paper is applied to the entire dataset to extract structured aspect-level insights. For each review, the pipeline performs aspect extraction, sentiment classification, and semantic category assignment. 

This process is executed across all reviews, producing structured outputs consisting of aspect terms, sentiment polarity, and corresponding semantic categories. The resulting representations enable large-scale analysis of hospitality trends with interpretable, category-level granularity. 

## _E. Example Output_ 

An example of the model output for a single review is shown below to illustrate the complete pipeline: 

**Review:** Beautiful hotel. Extremely clean and tidy. Very good food and great service. Meeting facilities were also excellent. My housekeepers were fantastic both weeks. 

**Extracted Aspects:** food, service, meeting facilities, housekeepers 

**food** _→_ positive (Food and Dining) 

**service** _→_ positive (Staff) **meeting facilities** _→_ positive (Facilities) 

**housekeepers** _→_ positive (Cleanliness) 

This process is applied consistently across the entire dataset, enabling scalable and interpretable analysis of user-generated reviews. 

## VII. REVIEW ANALYSIS 

## _A. Category-Level Summary of Mentions and Sentiment_ 

The dataset contains a total of **46,565 aspect–category mentions** extracted from hotel reviews spanning all **9 provinces** and **100 hotels** in Sri Lanka. Each mention corresponds to a specific opinion about a particular aspect of a hotel stay, mapped into one of six standardized categories. 

The considered categories are: _Staff_ , _Food and Dining_ , _Room Quality_ , _Location_ , _Facilities_ , and _Booking Process_ . These categories represent the primary dimensions of the hospitality experience and form the basis for subsequent analysis. Sentiment polarity is encoded numerically as _positive_ = 1, _neutral_ = 0, and _negative_ = -1. Therefore, aggregated sentiment scores may take values in the range [ _−_ 1 _,_ 1]. 

TABLE II: Category-wise distribution of aspect mentions across the dataset. 

|**Category**|**Mentions**|**Interpretation**|
|---|---|---|
|Staff|12,685|Most discussed; service quality is central|
|Food and Dining|12,478|Major role in tourism experience|
|Room Quality|9,784|Comfort and cleanliness emphasized|
|Location|5,797|Scenic value varies by region|
|Facilities|4,423|Amenities vary across hotels|
|Booking Process|1,398|Least discussed; often neutral|



_1) Category Importance:_ **Insight:** Guest discussions are dominated by _Staff_ , _Food_ , and _Room Quality_ , highlighting that human interaction and core comfort elements are central to the traveler experience. 

_2) Category Sentiment:_ **Insight:** While _Staff_ and _Location_ consistently receive high sentiment, _Room Quality_ and _Booking Process_ represent key areas for improvement. 

## _B. Province-Level Sentiment Analysis_ 

To understand geographic variations in traveler satisfaction, we aggregate aspect-level sentiments at the provincial level. 

TABLE IV: Province-level average sentiment and number of mentions. 

|**Province**<br>**Avg **|**Sentiment**|**Mentions**|
|---|---|---|
|Eastern Province|0.821|5,450|
|Central Province|0.817|4,360|
|Western Province|0.809|4,907|
|Southern Province|0.800|4,717|
|North Western Province|0.777|5,348|
|Uva Province|0.757|5,129|
|North Central Province|0.701|5,978|
|Sabaragamuwa Province|0.678|5,619|
|Northern Province|0.580|5,057|



**Insight:** Eastern, Central, and Western Provinces exhibit the highest overall satisfaction, while Northern and Sabaragamuwa Provinces show comparatively lower sentiment, indicating potential gaps in service consistency or infrastructure. 

## _C. Province–Category Sentiment Patterns_ 

A more granular view reveals how each province performs across different categories. 

## **Key Observations:** 

- Central and Eastern Provinces show strong performance in _Staff_ and _Location_ . 

- Southern and Western Provinces demonstrate balanced performance across most categories. 

- Northern Province consistently exhibits lower scores across multiple categories. 

**Insight:** While hospitality ( _Staff_ ) and natural appeal ( _Location_ ) remain strengths across most regions, categories related to infrastructure such as _Room Quality_ and _Facilities_ show greater variability. 

## _D. Best Performing Provinces per Category_ 

**Insight:** Central Province emerges as the strongest overall performer, while Eastern Province excels in service and foodrelated categories. Western Province leads in room quality, reflecting stronger infrastructure. 

TABLE V: Top-performing province for each category based on average sentiment. 

|**Category**|**Province**|**Avg Sentiment**|
|---|---|---|
|Booking Process|Central Province|0.680|
|Facilities|Central Province|0.823|
|Food and Dining|Eastern Province|0.801|
|Location|Central Province|0.908|
|Room Quality|Western Province|0.775|
|Staff|Eastern Province|0.907|



## _E. Province Competitiveness Index_ 

Average sentiment alone does not fully capture provincial performance, because not all categories contribute equally to traveler satisfaction. Categories such as _Staff_ , _Food and Dining_ , and _Room Quality_ appear far more frequently in reviews than _Booking Process_ or _Facilities_ . To account for this, we define a province-level competitiveness index that combines category sentiment with category importance, where importance is determined by the relative frequency of guest mentions. 

TABLE VI: Province competitiveness ranking based on importance-weighted sentiment. 

|**Rank**|**Province**|**Competitiveness Score**|
|---|---|---|
|1|Eastern Province|0.818|
|2|Central Province|0.814|
|3|Western Province|0.805|
|4|Southern Province|0.793|
|5|North Western Province|0.776|
|6|Uva Province|0.754|
|7|North Central Province|0.706|
|8|Sabaragamuwa Province|0.684|
|9|Northern Province|0.598|



This ranking provides a more realistic view of regional competitiveness because it emphasizes performance in the categories that matter most to guests. Eastern Province emerges as the strongest overall province, driven by excellent results in highly discussed categories such as _Staff_ , _Food and Dining_ , _Room Quality_ , and _Location_ . Central Province follows closely with a highly balanced profile, especially in _Staff_ , _Location_ , and _Food and Dining_ . Western Province ranks third, supported by stronger _Room Quality_ and _Facilities_ , which reflect relatively mature hotel infrastructure. 

Southern Province also performs strongly and consistently across major categories, while North Western and Uva Provinces remain in the middle tier due to mixed performance across room-related and facility-related dimensions. North Central and Sabaragamuwa Provinces score lower because of recurring weaknesses in room standards, facilities, and booking experiences. Northern Province ranks last, reflecting weaker sentiment across several high-importance categories, particularly _Room Quality_ , _Facilities_ , and _Booking Process_ . 

Overall, the province competitiveness index highlights which regions deliver the most complete hospitality experience when both quality and guest priorities are considered. 

## _F. Category Interaction Analysis_ 

To better understand how travelers structure their feedback, we analyze how frequently different aspect categories are mentioned together within the same review. This reveals which parts of the hotel experience are cognitively linked in guest narratives and helps identify broader experience clusters rather than isolated service dimensions. 



Fig. 6: Category co-occurrence heatmap showing how frequently pairs of hotel experience categories are mentioned together within the same review. 

The strongest co-occurrence is observed between _Food and Dining_ and _Staff_ , with 5,793 co-mentions, indicating that dining experiences are strongly shaped by service quality. _Room Quality_ and _Staff_ also exhibit a strong association, with 4,508 co-mentions, suggesting that housekeeping, room preparation, and front-desk support are tightly linked to perceptions of room comfort. Similarly, _Food and Dining_ and _Room Quality_ appear together 4,049 times, showing that guests often evaluate these two core elements jointly when forming their overall impression of a hotel. 

Other notable links include _Location_ with _Staff_ (3,337), _Food and Dining_ with _Location_ (2,977), and _Facilities_ with _Staff_ (2,524). These patterns suggest that staff performance influences nearly every part of the guest experience, while physical infrastructure and environmental appeal also interact closely in shaping satisfaction. 

Taken together, the co-occurrence structure reveals three broad experience clusters. First, a _service cluster_ centered on _Staff_ , which connects strongly to all major categories. Second, a _core hospitality cluster_ formed by _Room Quality_ , _Food and Dining_ , and _Location_ . Third, an _infrastructure cluster_ linking _Facilities_ , _Room Quality_ , and _Food and Dining_ . These relationships suggest that improvements in one category may generate positive spillover effects in others, making cooccurrence analysis valuable for identifying bundled intervention opportunities. 

TABLE VII: Sentiment entropy by category. Higher values indicate more mixed and less predictable guest reactions. 

|**Category**|**Entropy**|
|---|---|
|Booking Process|0.746|
|Facilities|0.672|
|Food and Dining|0.649|
|Room Quality|0.649|
|Location|0.450|
|Staff|0.308|



## _G. Category Stability Across Provinces_ 

Beyond average sentiment, it is important to understand how stable each category is across provinces. Some categories may perform well nationwide, while others may vary substantially from region to region. To illustrate this, we examine the provincial distribution of sentiment for each category. 



Fig. 7: Distribution of category-level sentiment across provinces. Wider distributions indicate greater geographic variability, while tighter distributions indicate more stable performance. 

The _Staff_ category is the most stable and consistently positive category, with sentiment concentrated in a narrow highvalued range across provinces. This indicates that Sri Lanka’s hospitality culture is strong nationwide and remains one of the country’s most reliable competitive strengths. _Location_ is also both strong and stable, reflecting the fact that natural beauty, scenery, and cultural surroundings are appreciated across most parts of the country. 

_Food and Dining_ exhibits moderate variation. While most provinces receive favorable dining sentiment, the spread is wider than for _Staff_ and _Location_ , suggesting uneven culinary consistency across regions. _Facilities_ show even larger variability, indicating strong differences between well-developed hotels and less-equipped properties. _Room Quality_ has the largest spread among all categories, marking it as the most inconsistent dimension of the guest experience. This aligns with earlier findings that room comfort, cleanliness, and maintenance differ substantially across provinces. 

_Booking Process_ remains one of the weakest and less stable categories. Although it is discussed less frequently, its distribution indicates uneven performance and recurring issues in reservation handling, check-in efficiency, and communication. Overall, this analysis shows that categories tied to hospitality 

and environment are relatively stable nationwide, whereas infrastructure-related categories remain much more uneven. 

## _H. Sentiment Entropy Across Categories_ 

To further assess experience consistency, we analyze sentiment entropy for each category. Entropy captures the degree of uncertainty or unpredictability in guest sentiment: higher values indicate more mixed reactions, while lower values indicate more uniform experiences. 

_Booking Process_ has the highest entropy, making it the most unpredictable category in the dataset. This suggests that guest experiences with reservations, confirmations, and check-in procedures vary widely across hotels and provinces. _Facilities_ also display high entropy, reflecting substantial differences in infrastructure quality and amenity availability. _Food and Dining_ and _Room Quality_ both exhibit high entropy as well, indicating that these aspects generate mixed reactions and are less reliably delivered across the country. 

By contrast, _Location_ has comparatively low entropy, showing that guests consistently value the natural and cultural appeal of Sri Lankan destinations. The lowest entropy is observed for _Staff_ , confirming that service quality is not only highly rated but also highly predictable. This makes _Staff_ the most dependable category in the entire analysis. 

These entropy results reinforce the broader findings of this study. Categories such as _Room Quality_ , _Facilities_ , and _Booking Process_ remain priority areas for quality improvement because they are both weaker and more inconsistent. In contrast, _Staff_ and _Location_ represent stable national strengths that form the foundation of Sri Lanka’s hospitality advantage. 

## _I. Hotel Archetype Clustering_ 

To identify broader structural patterns in hotel performance across Sri Lanka, we group hotels into a small number of archetypes based on their average sentiment across six core categories: _Booking Process_ , _Facilities_ , _Food and Dining_ , _Location_ , _Room Quality_ , and _Staff_ . This moves the analysis beyond individual reviews and enables a higher-level view of the national hospitality landscape. 

The clustering process begins by constructing a hotel-level representation in which each hotel is described by its mean sentiment score in each category. These category-wise features are then standardized so that no single dimension dominates the clustering simply due to scale. We then examine candidate cluster counts and select the final number of clusters based on the elbow trend in within-cluster variation. 

_1) Selection of the Number of Archetypes:_ To determine the appropriate number of hotel archetypes, we inspect the elbow curve over a range of cluster counts. 

The elbow pattern shows a clear reduction in within-cluster variance up to three clusters, after which the improvement becomes much smaller. This suggests that **three archetypes** provide a good balance between descriptive power and interpretability. Accordingly, all subsequent clustering results are reported with _k_ = 3. 

TABLE VIII: Average sentiment profile of each hotel archetype across the six categories. 

|**Cluster**|**Booking **|**Facilities**|**Food**|**Location **|**Room**|**Staff**|
|---|---|---|---|---|---|---|
|Archetype|0<br>0.287|0.566|0.635|0.786|0.528|0.807|
|Archetype|1<br>0.191|0.116|0.313|0.582|-0.022|0.241|
|Archetype|2<br>0.753|0.765|0.789|0.879|0.807|0.926|





Fig. 8: Elbow plot used to determine the number of hotel archetypes. The curve shows a clear bend at _k_ = 3, indicating that three clusters capture the major structural differences in hotel performance. 



Fig. 9: Two-dimensional visualization of hotel archetypes. Each point represents a hotel, and colors indicate the assigned cluster. The separation suggests the presence of three distinct tiers of hotel performance. 

_2) Visualization of the Archetypes:_ To visually inspect the learned grouping structure, the hotel representations are projected into two dimensions and plotted according to their assigned cluster. 

The visualization shows meaningful separation between the three groups. One cluster forms a compact high-performing region, indicating a set of hotels with consistently strong sentiment across categories. A second cluster occupies a broader middle region, representing hotels with moderate and relatively balanced performance. The third cluster lies farther apart and corresponds to low-performing or inconsistent ho- 

tels with weaker guest sentiment across multiple dimensions. This separation supports the interpretation that the discovered clusters reflect substantive differences in the overall guest experience. 

_3) Cluster Profiles:_ To interpret each archetype, we compute the mean sentiment score per category within each cluster. These results reveal three clearly interpretable hotel archetypes. 

_a) Archetype 0: Balanced Mid-Range Hotels:_ The first group shows moderate performance across all categories. Sentiment is relatively strong for _Staff_ and _Location_ , while _Food and Dining_ , _Facilities_ , and especially _Booking Process_ are more moderate. _Room Quality_ is positive but not particularly strong. Overall, this archetype represents dependable hotels that provide a satisfactory and reasonably consistent experience without standing out as premium properties. This group can be viewed as the broad middle tier of the Sri Lankan hotel market. 

_b) Archetype 1: Low-Performing or Inconsistent Hotels:_ The second group records the weakest sentiment across nearly all categories. _Room Quality_ is particularly poor, even falling slightly below zero on average, indicating clearly negative guest reactions. _Facilities_ , _Food and Dining_ , and _Staff_ also perform poorly, while _Location_ remains the least weak dimension but is still substantially below the other clusters. This archetype appears to capture hotels with persistent service or infrastructure problems, likely corresponding to struggling, poorly maintained, or inconsistent properties. 

_c) Archetype 2: Premium High-Satisfaction Hotels:_ The third group performs strongly across all six categories and represents the top tier of the market. _Staff_ achieves the highest sentiment overall, followed by excellent scores for _Location_ , _Room Quality_ , _Food and Dining_ , and _Facilities_ . Unlike the other two clusters, this archetype also performs well in _Booking Process_ , suggesting a more polished and complete guest experience. This cluster therefore represents premium, high-satisfaction hotels that consistently outperform the rest of the market. 

_4) Interpretation of the Archetypes:_ The clustering analysis highlights a clear three-tier structure in Sri Lanka’s hotel landscape: a premium tier, a mid-range dependable tier, and a weaker inconsistent tier. Several patterns are especially notable. 

First, _Staff_ is a major discriminator between clusters. The premium archetype reaches a very high staff sentiment, the mid-range group remains strong but lower, and the lowperforming cluster drops sharply. This indicates that service quality is one of the clearest markers of overall hotel quality. 

Second, _Room Quality_ strongly separates the clusters. It is highly positive in the premium group, moderate in the midrange group, and negative in the weakest group. This suggests that room comfort, maintenance, and cleanliness are among the most visible factors that distinguish high-performing hotels from low-performing ones. 

Third, _Booking Process_ remains relatively weak except in the premium cluster. Even hotels in the middle tier do 

not achieve high sentiment in this category, indicating that booking and check-in procedures remain a broader operational challenge across much of the market. 

Finally, _Location_ remains comparatively strong even outside the premium cluster, showing that natural and geographic appeal contributes positively across Sri Lanka. However, location alone is not enough to offset weaknesses in service, rooms, or facilities. 

Overall, hotel archetype clustering provides a compact and interpretable summary of the Sri Lankan hospitality landscape. It reveals that hotels do not form a continuous spectrum of quality, but instead group naturally into distinct performance profiles. This makes the archetype view useful for benchmarking, strategic planning, and identifying where service upgrades are likely to have the greatest effect. 

## _J. Province-wise Distribution of Hotel Archetypes_ 

To further understand how hotel performance varies geographically, we analyze the distribution of the three identified archetypes across provinces. This provides insight into how different regions balance premium, mid-range, and lowperforming properties. 



Fig. 10: Distribution of hotel archetypes across provinces. Each province is represented by the proportion of hotels belonging to each cluster, illustrating regional differences in hospitality performance tiers. 

The results reveal several important geographic patterns. High-performing hotels (Archetype 2) dominate most provinces, indicating that a significant portion of Sri Lanka’s hospitality sector delivers consistently strong guest experiences. This dominance is particularly evident in major tourism regions such as Western, Southern, Central, Eastern, and Uva Provinces, where better infrastructure and higher tourist inflow likely contribute to improved service quality. 

The mid-range archetype (Archetype 0) is present in all provinces and generally forms the second-largest group. These hotels typically perform well in categories such as _Staff_ and _Location_ , but show moderate or inconsistent performance in _Room Quality_ , _Facilities_ , and _Booking Process_ . This group represents the backbone of the tourism sector, consisting of reliable but non-premium properties. 

The lowest-performing archetype (Archetype 1) appears only in a limited number of provinces, primarily in Northern and Sabaragamuwa regions. The relatively small presence of this cluster suggests that severely underperforming hotels are not widespread, but tend to be concentrated in regions with less-developed tourism infrastructure. These findings indicate that regional disparities in infrastructure and service delivery still play a role in shaping guest experiences. 

Overall, the province-wise archetype distribution highlights that while Sri Lanka has a strong base of high-performing hotels, targeted improvements in specific regions could further enhance nationwide consistency in hospitality quality. 

## _K. Tourism Opportunity Analysis_ 

While previous analyses focused on performance and variation, it is equally important to identify where improvements would have the greatest impact. To achieve this, we analyze the gap between how frequently guests discuss a category and how positively they evaluate it. Categories that are both highly discussed and relatively weaker in sentiment represent the most critical opportunities for improvement. 

TABLE IX: Top province–category opportunity areas based on importance and sentiment gap. 

|**Rank**|**Province**|**Category**|
|---|---|---|
|1|Northern Province|Room Quality|
|2|Sabaragamuwa Province|Food and Dining|
|3|Northern Province|Food and Dining|
|4|North Central Province|Food and Dining|
|5|Sabaragamuwa Province|Room Quality|
|6|North Central Province|Room Quality|
|7|Uva Province|Room Quality|
|8|North Western Province|Food and Dining|
|9|Northern Province|Staff|
|10|Central Province|Food and Dining|



_1) Top Opportunity Areas Across Provinces:_ The results reveal several consistent patterns across provinces. 

**Room Quality** emerges as the most critical opportunity area, particularly in Northern, Sabaragamuwa, North Central, and Uva Provinces. In these regions, guests frequently discuss rooms, but sentiment remains comparatively weaker. This suggests that improvements in cleanliness, maintenance, and comfort would have a strong impact on overall satisfaction. 

**Food and Dining** is the second major opportunity category. It appears across multiple provinces, including Sabaragamuwa, Northern, North Central, North Western, and even Central Province. Although food is a central part of the travel experience, its quality and consistency vary across regions, indicating strong potential for improvement through better menu design, service quality, and dining experiences. 

TABLE X: Average hotel ratings by trip type. 

|**Trip Type**|**Avg Rating**|
|---|---|
|Family|4.64|
|Couples|4.64|
|Solo|4.62|
|Friends|4.60|
|Business|4.57|



The **Northern Province** appears multiple times among the top opportunity areas, highlighting it as the most underserved region relative to guest expectations. This suggests that targeted investments in room quality, food services, and staff performance could significantly improve overall hospitality perception in this region. 

In contrast, provinces such as Western, Southern, and Eastern do not appear among the top opportunity areas. This indicates that their most frequently discussed categories are already aligned with high sentiment, reflecting more mature and balanced hospitality ecosystems. 

_2) Overall Interpretation:_ The opportunity analysis provides a strategic perspective on where improvements can yield the highest returns in guest satisfaction. It highlights that not all weaknesses are equally important; instead, priority should be given to areas that guests care about most. 

Across Sri Lanka, infrastructure-related categories such as _Room Quality_ and _Food and Dining_ represent the largest opportunities for improvement. Enhancing these dimensions can significantly reduce variability in guest experiences and elevate overall service standards. At the same time, maintaining strengths in _Staff_ and _Location_ is essential, as these remain the country’s most consistent and defining advantages. 

This analysis therefore serves as a practical guide for tourism stakeholders, helping identify high-impact interventions at both provincial and national levels. 

VIII. DATA ANALYSIS ON RATINGS AND TRIP TYPES 

This section analyzes numerical hotel ratings and traveler types to complement the sentiment-based findings. Specifically, we examine (i) rating variation across provinces, (ii) differences across trip types, and (iii) statistical relationships between geography, traveler profiles, and satisfaction. 

## _A. Average Rating by Province_ 

Hotel ratings show clear variation across provinces, reflecting differences in infrastructure, service quality, and tourism maturity. 

Central Province records the highest average rating (4.79), driven by well-established tourism destinations and a strong presence of mid-range and premium accommodations. Southern (4.77) and Eastern (4.74) Provinces also achieve high ratings, supported by coastal tourism, resort-style hospitality, and leisure-focused experiences. 

In contrast, Northern Province records the lowest average rating (4.24). This likely reflects relatively underdeveloped tourism infrastructure, fewer established hotel chains, and 

greater variability in service standards. However, the region shows growth potential as tourism continues to expand. 

Overall, these results indicate that provinces with stronger tourism ecosystems tend to achieve higher and more consistent ratings. 

## _B. Rating Patterns by Trip Type_ 

Ratings remain consistently high across all trip types, with only minor differences. Family and couple travelers report the highest satisfaction, suggesting that hotels are well-aligned with leisure-oriented needs such as comfort, amenities, and personalized service. Solo travelers also report positive experiences, though slightly lower, potentially due to fewer social or community-oriented features. 

Groups of friends show moderate satisfaction, indicating potential opportunities to enhance shared experiences and recreational offerings. Business travelers report the lowest ratings, which may reflect varying availability of work-friendly amenities such as connectivity, workspace, and convenience. 

Overall, the small differences suggest that hotel performance is broadly consistent across traveler segments. 

## _C. Province × Trip Type Distribution_ 



Fig. 11: Distribution of trip types across provinces. The figure highlights how different traveler groups are concentrated in different regions of Sri Lanka. 

The distribution of trip types varies significantly across provinces. Family travelers dominate across most regions, particularly in Eastern and Southern Provinces, reflecting their popularity as coastal leisure destinations. Couples are also highly represented, especially in scenic provinces such as Uva and Sabaragamuwa, which are known for nature-oriented and romantic tourism. 

Business travelers are concentrated primarily in Western Province, highlighting the importance of urban and commercial hubs. Friend groups and solo travelers are more moderately distributed, with higher presence in Western and Central regions, likely due to better accessibility and urban amenities. 

These patterns suggest that different provinces attract distinct traveler profiles, influenced by geography, infrastructure, and tourism positioning. 

_D. Statistical Analysis: Province vs Rating_ 

To formally evaluate whether hotel ratings differ across provinces, we performed a one-way analysis of variance (ANOVA), treating _province_ as the grouping factor and _rating_ as the response variable. The ANOVA result indicates a statistically significant difference in mean ratings across provinces, with a large test statistic and a near-zero _p_ -value. This shows that provincial differences in hotel ratings are unlikely to be due to random variation alone. 

TABLE XI: One-way ANOVA summary for province versus hotel rating. 

|**Statistic**|**Value**|**Interpretation**|
|---|---|---|
|F-statistic|50.934|Strong between-province variation|
|_p_-value|_<_0_._001|Statistically significant difference|



Since the overall ANOVA was significant, we conducted Tukey’s honestly significant difference (HSD) post-hoc test to determine which province pairs differed significantly in mean rating. The pairwise comparisons show that _Northern Province_ stands out as the lowest-performing region, with significantly lower ratings than Central, Eastern, North Western, Sabaragamuwa, Southern, Uva, and Western Provinces. _North Central Province_ also shows several significant differences, especially when compared with higher-rated provinces such as Southern, Uva, and Western. _Sabaragamuwa Province_ occupies a lowermiddle position, performing significantly below Southern, Uva, and Western Provinces, but above Northern Province. 

By contrast, several of the top-performing provinces do not significantly differ from one another. For example, Central, Eastern, Southern, and Western Provinces show no statistically significant pairwise differences in several comparisons, suggesting a relatively similar upper tier of performance. 

TABLE XII: Key significant Tukey HSD comparisons (province vs rating). 

|**Prov. 1**|**Prov. 2**|**Result**|
|---|---|---|
|Northern|Central|Lower|
|Northern|Eastern|Lower|
|Northern|Southern|Lower|
|Northern|Uva|Lower|
|Northern|Western|Lower|
|North Central|Southern|Lower|
|North Central|Uva|Lower|
|North Central|Western|Lower|
|Sabaragamuwa|Southern|Lower|
|Sabaragamuwa|Western|Lower|
|Central|Northern|Higher|
|Central|North Central|Higher|



Overall, the province-level rating differences are both statistically significant and substantively meaningful. The findings indicate that traveler satisfaction is not uniform across Sri Lanka. Provinces such as Southern, Uva, and Western occupy the higher end of the rating spectrum, while Northern and North Central Provinces perform more weakly. This supports the broader interpretation that tourism maturity, infrastructure quality, and service consistency vary across regions. 

_E. Statistical Analysis: Trip Type vs Rating and Province Interaction_ 

To evaluate whether hotel ratings vary across traveler segments, we performed a one-way analysis of variance (ANOVA) using _trip type_ as the grouping factor and _rating_ as the response variable. 

TABLE XIII: One-way ANOVA summary for trip type versus hotel rating. 

|**Statistic**|**Value**|**Interpretation**|
|---|---|---|
|F-statistic|1.199|Weak between-group variation|
|_p_-value|0.309|Not statistically significant|



Since the _p_ -value exceeds 0.05, we fail to reject the null hypothesis, indicating that average ratings do not differ significantly across trip types. This suggests that travelers—whether families, couples, solo visitors, or business guests—report broadly similar satisfaction levels. The relatively low F- statistic further confirms that between-group differences are small compared to within-group variation. 

These findings indicate that hotel ratings are influenced more strongly by regional and hotel-specific factors than by the purpose of travel. 

_1) Chi-Square Analysis: Province vs Trip Type:_ To examine whether traveler types are distributed differently across provinces, we conducted a Chi-square test of independence between _province_ and _trip type_ . The result was statistically significant, indicating a strong association between geographic location and traveler composition. 

The large Chi-square statistic (approximately 623.72) and a near-zero _p_ -value confirm that the observed differences in triptype distribution across provinces are far greater than expected by chance. This implies that different provinces attract distinct types of travelers. 

_2) Post-hoc Analysis of Province Differences:_ To identify which provinces differ most in traveler composition, pairwise Chi-square tests were conducted with Bonferroni correction. 

TABLE XIV: Top significant province pair differences in triptype distribution (Chi-square post-hoc). 

|**Province Pair**|**Interpretation**|
|---|---|
|Sabaragamuwa vs Northern|Strong difference|
|Uva vs Northern|Strong difference|
|Eastern vs Western|Distinct traveler mix|
|Uva vs Western|Leisure vs urban contrast|
|Sabaragamuwa vs Western|Different traveler patterns|
|Western vs Southern|Urban vs leisure contrast|
|North Central vs Northern|Distinct distributions|
|North Central vs Western|Different traveler mix|
|Eastern vs Northern|More diverse in Eastern|
|Western vs Central|Urban vs scenic contrast|



The results highlight several key patterns. The _Northern Province_ exhibits the most distinct traveler profile, differing significantly from nearly all other regions. This suggests a less diverse or more constrained tourism base. The _Western_ 

_Province_ also shows a unique distribution, likely influenced by business and urban travel demand. 

In contrast, _Southern_ , _Uva_ , and _Eastern Provinces_ are more strongly associated with leisure-oriented travelers such as families and couples, reflecting their appeal as scenic and recreational destinations. 

_3) Overall Interpretation:_ Taken together, these results show that while hotel ratings remain consistent across traveler types, the _composition of travelers varies significantly by province_ . This indicates that geography plays a central role in shaping tourism demand patterns. 

Regions such as Uva, Southern, and Eastern Provinces function primarily as leisure destinations, attracting families and couples, whereas Western and Northern Provinces exhibit more distinct or specialized traveler profiles. These differences are statistically significant and highlight the importance of aligning regional tourism strategies with dominant visitor segments. 

CODE AVAILABILITY 

The full implementation of _SentimentLens_ is available and will be released publicly upon acceptance. 

