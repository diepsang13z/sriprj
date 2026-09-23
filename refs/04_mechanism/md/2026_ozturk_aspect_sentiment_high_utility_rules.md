

Received 10 February 2026, accepted 5 March 2026, date of publication 10 March 2026, date of current version 16 March 2026. _Digital Object Identifier 10.1109/ACCESS.2026.3672490_ 

# Discovering Aspect–Sentiment Drivers of Hotel Review Ratings With Interpretable High-Utility Rules 

## AHMET CUMHUR ÖZTÜRK 

Department of Database, Network Design and Management, Söke Vocational School, Aydın Adnan Menderes University, Söke, 09200 Aydın, Türkiye e-mail: cumhur.ozturk@adu.edu.tr 

- **ABSTRACT** Online review ratings provide a convenient summary of guest satisfaction, but a single score does not reveal which aspect-level strengths and weaknesses drove the evaluation. This study proposes an interpretable, rule-based framework to discover rating-specific aspect–sentiment driver patterns from review text. The empirical analysis uses TripAdvisor reviews from 14 five-star hotels in a major coastal resort destination in Turkey. A sentence-level pipeline encodes review sentences with transformer embeddings, clusters them into fine-grained micro-aspects, and merges them into interpretable macro-aspects. Sentencelevel sentiment polarity is then obtained via the OpenAI GPT API using a standardized prompt and fixed inference settings. The resulting aspect–sentiment pairs are transformed into a transactional representation. Then a rating-specific High-Utility Itemset Mining (HUIM) procedure is applied to identify utility-bearing patterns that best differentiate rating levels. The discovered rules identify characteristic combinations for each star level, revealing systematic asymmetries between negative and positive signals and uncovering multi-aspect interaction effects. Specifically, low ratings stem from co-occurring negatives, while midrange scores reflect trade-offs where strengths offset weaknesses. In contrast, high ratings combine multiple positives with value-added experiences like entertainment. The discriminative value of these drivers is further validated by benchmarking the HUIM-based framework against established rating prediction baselines. 

**INDEX TERMS** Aspect-based sentiment analysis, sentence embedding, GPT-based sentiment labeling, high-utility rule mining, rating driver analysis. 

### **I. INTRODUCTION** 

Online review platforms such as TripAdvisor and Google Reviews allow travelers to share their experiences via free-text reviews and star ratings. Consequently, this usergenerated content has become a key information source for both travelers and service providers. Review star ratings provide a quick summary of guest satisfaction by condensing complex service experiences into a single, quantifiable metric. For service providers, these ratings influence online visibility and booking demand, whereas for travelers, they reduce uncertainty and perceived risk by enabling quick comparisons and preference matching. Despite their usefulness, 

The associate editor coordinating the review of this manuscript and approving it for publication was Li He . 

a single star score summarizes a complex stay but does not explain which aspect-level strengths and weaknesses drove the evaluation. This limits the ability of managers to prioritize improvements and of customers to interpret what different rating levels typically imply in practice. Accordingly, there is a need for an interpretable, aspect-level perspective that links ratings to recurring combinations of experiences described in review text. 

Aspect-based sentiment analysis (ABSA) is a widely used technique to decompose unstructured review narratives into granular, multi-dimensional opinions by identifying aspects (e.g., food, service, cleanliness) and assigning sentiment polarity (positive, negative, or neutral).Although ABSA has been widely adopted for summarizing customer feedback and rating prediction, often through text-based machine 

2026 The Authors. This work is licensed under a Creative Commons Attribution 4.0 License. For more information, see https://creativecommons.org/licenses/by/4.0/ 

39496 

VOLUME 14, 2026 

A. C. Öztürk: Discovering Aspect–Sentiment Drivers of Hotel Review Ratings 



learning and ensemble models, two limitations remain prominent [1]. First, many studies focus on aggregated aspect importance (e.g., global weights or average sentiment) rather than capturing rating-specific multi-aspect patterns. Second, closed-box predictive models may achieve high accuracy but provide limited interpretability regarding which combinations of aspect–sentiment evaluations reliably distinguish rating levels. These limitations constrain the practical utility of review analytics, because managerial interventions typically require addressing co-occurring patterns of service issues rather than isolated aspects. 

To address these gaps, this study proposes an interpretable, rule-based framework to discover rating-specific aspect–sentiment driver patterns from review text. It is assumed that guest satisfaction is inherently multidimensional, such that ratings reflect the joint configuration of aspect-level evaluations expressed in review text. Therefore, beyond identifying aspects and their sentiments, the key methodological goal is to extract recurring multi-item patterns that are characteristic of different rating levels. To achieve this goal, High-Utility Itemset Mining (HUIM) is incorporated into the driver discovery process. Traditional frequent itemset mining and Association Rule Mining (ARM) primarily prioritize patterns by how often they occur. In review analytics, this can under-rank informative but infrequent aspect–sentiment combinations and over-rank generic frequent signals that are weakly discriminative. HUIM explicitly models the utility of items and itemsets, enabling the discovery of patterns that are not only present but also more discriminative for differentiating rating levels. In this setting, each item corresponds to an aspect–sentiment evaluation, and HUIM is applied in a rating-specific manner to uncover the most impactful, utility-bearing combinations that best characterize each star level. 

The proposed research is guided by the following research questions: 

- RQ1. Which co-occurring combinations of aspect– sentiment evaluations are characteristic of different rating levels in online hotel reviews? 

- RQ2. How do positive and negative aspect-level sentiments contribute asymmetrically to lower versus higher rating levels? 

- RQ3. How do interaction patterns between multiple aspects within the same review help distinguish adjacent rating levels? 

This study makes four main contributions. First, it introduces a transactional, rating-specific representation of aspect–sentiment evidence that supports interpretable driver discovery rather than global aspect weighting. Second, it integrates a HUIM-based procedure to prioritize discriminative multi-aspect patterns that distinguish rating levels. Third, it produces human-readable driver rules that support interpretability and managerial prioritization. Finally, it evaluates the driver discovery process against representative baselines using discovery-quality criteria and reports an 

auxiliary predictive validation on held-out reviews. Although the empirical evaluation is conducted on hotel reviews, the proposed HUIM-based framework is methodologically domain-agnostic, relying on fundamental itemset mining principles applicable to any textual review data containing aspect–sentiment information. While the methodology is transferable to other sectors such as e-commerce or restaurants, the hospitality domain was selected as a representative case study to demonstrate the framework’s capacity for deep, granular analysis of complex service interactions. 

The remainder of the paper is organized as follows: Section II reviews related work, Section III presents the methodology, Section IV reports the discovered drivers and evaluation results, and Section V concludes. 

### **II. RELATED WORK** 

### _A. EXTRACTING ASPECT AND SENTIMENT SIGNALS FROM REVIEWS_ 

Hotel customers generate a substantial volume of textual data by sharing their experiences on digital platforms such as TripAdvisor and Booking.com. This vast corpus of user-generated content has become a primary resource for understanding consumer behavior and shaping digital service strategies in the modern hospitality market. Previous studies have applied a range of natural language processing techniques to transform this unstructured content into actionable insights. In particular, aspect-based sentiment analysis (ABSA) has become a widely used approach for decomposing reviews into aspect-specific opinions and identifying the polarity expressed toward each aspect [2]. ABSA pipelines in the hospitality domain are synthesized in [3], where the shift toward transformer-based representations is emphasized and persistent challenges such as implicit aspect detection and practical deployment constraints are highlighted. ABSA is commonly formulated as a two-step framework [4]. The first step is aspect extraction for identifying the specific attributes discussed in a review, such as location, staff, and cleanliness, while the second step is sentiment classification for determining the polarity expressed toward each identified aspect, namely positive, negative, or neutral. For instance, Akhtar et al. apply ABSA to TripAdvisor hotel reviews to generate aspect-oriented sentiment summaries [5], while Sann and Lai use NLP-driven ABSA to identify and categorize service failures across the hotel guest cycle [6]. Furthermore, Ray et al. combine sentiment analysis with aspect categorization of hotel reviews in a recommendation setting [7]. 

Recent studies increasingly rely on embedding-based clustering that groups semantically similar review sentences into coherent aspect clusters. For instance, Ray et al. utilized word embedding-based clustering to identify specific hotel service dimensions from TripAdvisor feedback [7]. Liu and Zhao employed BERT-based embeddings to improve the granularity of aspect detection [8]. Similarly, in this study, aspects are derived by clustering sentence embeddings into 

39497 

VOLUME 14, 2026 

A. C. Öztürk: Discovering Aspect–Sentiment Drivers of Hotel Review Ratings 



fine-grained groups and then consolidating these groups into a smaller set of interpretable aspect categories used throughout the analysis. 

Sentiment labeling in ABSA is frequently performed at the sentence level to capture the mixed or even conflicting opinions often found within a single review. Sentence-level polarity assignment enables a cleaner alignment between an expressed opinion and the specific service attribute it refers to. As Su et al. highlight, identifying the polarity conveyed in a given sentence provides a natural granularity for building precise aspect-sentiment tuples from review narratives [9]. In recent years, this step has increasingly relied on fine-tuned pretrained transformers such as BERT and RoBERTa, which provide contextualized representations that are effective for text classification [10]. In the hospitality domain, transformer-based classifiers have been successfully applied to hotel review sentiment classification on largescale datasets [11]. In this study, a GPT-based sentence-level sentiment labeler is adopted as a text annotation tool, utilizing a fixed prompt template and deterministic settings to support reproducible labeling [12]. This direction aligns with recent LLM-based ABSA studies demonstrating that ChatGPTbased zero-shot labeling achieves strong agreement with human annotations in aspect-sentiment extraction tasks [13]. 

Once aspects and their sentiment polarities are identified, studies commonly aggregate these signals into compact, quantitative representations such as aspect-level polarity frequencies, averaged sentiment scores, or pooled aspect embeddings so that they can be used in statistical analysis and prediction tasks [14]. These structured aspectsentiment profiles support downstream applications, including hotel comparison and segmentation using large-scale review data [15], [16] and review rating prediction from text [17]. In recommendation settings, studies show that incorporating aspect-sentiment signals and reducing aspect sparsity through clustering can improve explainability and rating prediction performance in collaborative filtering-based recommenders [18], [19]. 

### _B. THE ROLE OF ASPECT-SENTIMENT SIGNALS IN SHAPING AND PREDICTING STAR RATINGS_ 

Online star ratings of hotel reviews function as a critical quantitative factor in the decision-making process and serve as a summarized form of electronic word-of-mouth. Unlike text-based reviews, these numerical ratings provide a fast first-pass filter, as travelers often apply a minimum rating threshold before engaging with the content of reviews [20]. Furthermore, Oliveira-Cardoso et al. confirm that TripAdvisor ratings are valid, reliable, and succinct indicators of guest satisfaction, and that these numerical scores can effectively predict satisfaction based on perceived service quality [21]. 

Although the overall star rating is a single score, it represents an aggregation of multiple aspect-specific sentiments whose relative importance may vary across traveler contexts. Previous studies show that aspect-level signals expressed 

in review text are significantly associated with overall hotel ratings. For instance, Yang et al. demonstrate that cleanliness-related evaluations strongly influence overall satisfaction [22]. Mokryn finds that the drivers of overall ratings vary by trip purpose. Specifically, for business travelers, the primary predictors are Wi-Fi quality and location, whereas for leisure travelers, ratings are more sensitive to room amenities and staff empathy [23]. Furthermore, Kolesárová et al. experimentally confirm that textual signals related to the physical environment and service quality carry a robust correlation with the final numerical score [24]. Kalnaovakul et al. additionally demonstrate that the impact of review sentiments on overall ratings is moderated by reviewer experience and hotel brand type [25]. 

To capture and operationalize these relationships, recent studies have developed rating prediction frameworks that bridge the gap between unstructured text and numerical scores. Kumar and Hanji introduced a predictive framework utilizing a fuzzy domain ontology algorithm and multinomial logistic regression [26]. While their analysis centered on travel destinations, their methodology is applicable to the hotel sector due to its emphasis on aspect-based extraction. Similarly, Kumar et al. predict hotel ratings using majority-voting ensembles trained on review-level textual features, including sentiment-based attributes [1]. Additionally, Peng et al. proposed a joint model that integrates fine-grained aspect information with matrix factorization to mitigate data sparsity and improve interpretability in rating prediction [27]. 

More recently, deep learning approaches have gained prominence. Puh and Bagić Babac demonstrate that bidirectional long short-term memory (BiLSTM) architectures are effective for jointly extracting sentiments and ratings from tourist reviews [28]. Ahmed and Ghabayen propose a two-phase deep learning framework mapping free-text reviews to star-level ratings, reporting that high star ratings consistently align with positive qualitative feedback [29]. Hutauruk and Sibaroni propose a hybrid RNN-LSTM model that captures sequential dependencies in guest narratives [30], and Yang et al. show that transformer-based models (e.g., BERT) outperform traditional networks in identifying complex sentiment logic [31]. In this context, distinct efforts to enhance interpretability have emerged. For instance, an explainable rating prediction framework is proposed in [32], utilizing intermediate semantic macro concepts to link textual evidence with predicted outcomes. 

Despite these advancements, existing approaches remain primarily prediction-oriented. Many methods, ranging from fuzzy logic to deep learning, treat aspects or single aspectsentiment pairs as independent features, limiting their ability to reveal synergistic effects among multiple service drivers. Furthermore, they typically do not yield compact, humanreadable patterns that explicitly show how recurring combinations of aspect-sentiment cues jointly push ratings upward or downward. Recent rule-based associative classification 

39498 

VOLUME 14, 2026 

A. C. Öztürk: Discovering Aspect–Sentiment Drivers of Hotel Review Ratings 



studies highlight a continued interest in extracting such interpretable rule sets for supervised decision-making [33]. To address this gap, the proposed study discovers interpretable high-utility itemset rules that explicitly capture influential co-occurring aspect-sentiment driver combinations for each rating level. Unlike concept-centric intermediate representations, this approach provides a direct, holistic understanding of how service attributes interact to shape the final numerical score. 

least five tokens were retained. Specifically, out of 88,390 total sentences, this filter preserved 80,988 and removed 7,402 fragments. At the review level, 11,303 out of 11,329 reviews retained at least one sentence, while only 26 reviews had all sentences removed. Although some very short sentences can be informative (e.g., ‘‘This hotel was dirty’’), the cutoff is conservative in practice discarding only 8.37% of sentences and fully affecting only 0.23% of reviews-while ensuring sufficient context for mining co-occurring aspectsentiment bundles rather than isolated keywords. 

### **III. METHODOLOGY** 

This study aims to identify the most prominent aspectsentiment drivers in hotel reviews by applying a HighUtility Itemset Mining (HUIM) based association rule mining framework. The workflow of the proposed study is illustrated in Figure 1 and consists of six main steps. In Step 1, English-language reviews posted between 2022 and 2024 for 14 five-star hotels located in Kuşadası, Turkey, were collected from TripAdvisor using Selenium in Python. In Step 2, the reviews were cleaned and split into sentences, transformer-based sentence embeddings were computed, and the sentences were clustered into fine-grained micro-aspects, which were subsequently merged into twelve interpretable macro-aspects such as _food_ , _staff_ , _room comfort_ , _cleanliness_ , and _location_ . In Step 3, a GPT-based sentiment classifier assigned a polarity label to each sentence-aspect pair as _positive_ , _negative_ , or _neutral_ . In Step 4, sentence-level aspect-sentiment labels were aggregated at the review-aspect level using a majority-net scheme. Neutral majority cases were discarded, and each review was represented as a set of distinct aspect-sentiment items (e.g., _Food_negative_ , _Staff_positive_ ), yielding a transactional database where each review corresponds to an item basket associated with its star rating.. In Step 5, a rating-specific HUIM procedure was applied to this transactional database to mine utility-based association rules. In Step 6, these mined rules were used to identify the characteristic aspect-sentiment driver patterns associated with each review rating level from 1 to 5 stars. 

### _A. DATA COLLECTION AND REVIEW PREPROCESSING_ 

A total of 11,275 English-language customer reviews were collected from TripAdvisor using Selenium in Python to construct the review dataset. The reviews correspond to 14 five-star hotels located in Kuşadası (Turkey) and include the review text, posting date, and overall star rating. Only reviews written in English and posted between January 1, 2022, and December 31, 2024, were retained. To improve reliability, review texts were preprocessed by converting all characters to lowercase and removing HTML artifacts, URLs, emojis, digits, punctuation, and other non-alphabetic symbols. Reviews were then segmented into sentences using spaCy [34]. Each sentence was tokenized, standard English stop words were removed, and the remaining tokens were lemmatized to their base forms. Finally, to exclude very short and uninformative fragments, only sentences containing at 

### _B. ASPECT DETECTION THROUGH SENTENCE EMBEDDINGS_ 

The aspect detection process is performed on review sentence embeddings rather than raw word overlaps. The review sentences are converted to their corresponding embedding using the all-mpnet-base-v2 model [35], and then to remove the differences in magnitude of each vector, L2-normalization was applied. A two-phase clustering approach was applied to detect aspects of each sentence. In this two-stage design, fine-grained micro-clusters were obtained using K- Means and then they were then aggregated into higher-level macro-clusters using agglomerative hierarchical clustering. This two stage clustering strategy is adopted from prior work [36]. In the first phase, K-Means clustering [37] with _k_ = 50 was applied to sentence embeddings with the distance metric 1 − _cosine_ similarity to find out microclusters. Since embeddings are L2-normalized, clustering on normalized vectors makes cosine-based similarity consistent with Euclidean distance used by K-Means. This large number of k was chosen to obtain fine-grained groups of semantically similar sentences such as different food issues or different types of room complaints. The resulting micro-clusters were then aggregated by using agglomerative hierarchical clustering [38] to obtain macro-clusters. The agglomerative hierarchical clustering was applied based on centroids of each micro-cluster where the centroid of a cluster was computed by averaging the sentence embeddings within a microcluster. This process resulted in 12 different macro-clusters. Each cluster is then manually assigned a thematic label by analyzing the terms having the highest TF-IDF scores within that cluster. 

Table 1 summarizes the resulting 12 macro-aspect clusters by reporting their assigned aspect names, the top TF-IDF terms used for labeling, and a brief aspect description. The table also reports the relative occurrence of each aspect in terms of sentence share and review share. The cluster distribution shows that _Room Comfort and Facilities_ , _Staff and Front-Desk Service_ , and _Food and Dining_ are the most dominant aspects, as they cover the largest proportions of sentences and appear in the majority of reviews. In contrast, aspects such as _Wi-Fi and Connectivity_ , _Sunbeds and Towels_ , and _Value and On-Site Amenities_ occur much less frequently which indicates more specific or less commonly mentioned experience dimensions. 

39499 

VOLUME 14, 2026 

A. C. Öztürk: Discovering Aspect–Sentiment Drivers of Hotel Review Ratings 





**FIGURE 1.** Workflow of the proposed framework. 

**TABLE 1.** Description of extracted aspects and their distribution across sentences and reviews. 



### _C. SENTIMENT ANALYSIS_ 

Following aspect labeling, sentiment analysis was performed using the GPT-4o mini model via the OpenAI API [39]. Unlike traditional supervised classifiers (e.g., SVM or logistic regression) which require extensive manual training data, this LLM-based strategy was selected for its balance of computational efficiency and zero-shot accuracy. Recent studies demonstrate that GPT-4 variants achieve competitive performance in aspect-based sentiment analysis, effectively handling the linguistic noise, colloquialisms, and pragmatic nuances (e.g., sarcasm) typical of user reviews [40]. 

Consequently, the mini variant was employed to ensure scalability across the full corpus without compromising annotation quality. 

The GPT model was instructed, through a system prompt, for acting as an expert hotel review annotator and assigning _positive_ , _negative_ , or _neutral_ sentiment labels to a given sentence. The prompt template used for aspect-level sentiment analysis with GPT-4.1 is shown in Table 2. The Role column shows whether the prompt content is the system instruction, the user request, or an input/output example. The Prompt Content column shows the corresponding message for the 

39500 

VOLUME 14, 2026 

A. C. Öztürk: Discovering Aspect–Sentiment Drivers of Hotel Review Ratings 



**TABLE 2.** Prompt template used for aspect-level sentiment analysis. 



model. The prompt for the _System_ defines the model’s role as an annotator and specifies the fields in the input file as _row_id_ , _aspect_ , and _sentence_ . It restricts the sentiment label set to _positive_ , _neutral_ , or _negative_ and describes the required _JSON_ output format. The _User_ prompt provides a high-level request to return one sentiment label for each item in the input array. The _Input Example_ and _Output Example_ rows illustrate a concrete _JSON_ instance of the items passed to the API and the expected _JSON_ array of results returned by the model. 

To improve efficiency while respecting context-length limits, the sentences were labeled in batches of 100 sentences per API request. For computational management and fault tolerance, intermediate outputs were written to disk after each block of 10,000 sentences. This block size is for checkpointing and does not correspond to a single model call. The model labelled a total of 53,048 (60.0%) sentences as _positive_ , 7,847 (8.9%) as _neutral_ , and 27,495 (31.1%) as _negative_ . For assessing the reliability of the GPT-based sentiment label annotation, a random sample of 1,000 review sentences was annotated manually. Next, the GPT4.1 mini predictions were compared against human labels using the accuracy and macro-averaged F1 score over the three sentiment classes. The results show that GPT-4.1 mini achieved an accuracy of 84.4% and a macro-F1 of 83.2%, indicating that the LLM-based annotations are sufficiently consistent for the subsequent analysis. Sentiment labeling used GPT-4.1 mini via the OpenAI API with the following parameters: _temperature = 0_ , _top_p = 1_ , _max_tokens = 10_ , and _seed = 42_ . Failed requests were retried up to 3 times. 

### _D. TRANSACTIONAL DATABASE REPRESENTATION FOR HIGH UTILITY BASED ASSOCIATION RULE MINING_ 

Let _I_ = { _i_ 1 _, i_ 2 _, . . . , im_ } be a finite set of different items. A transactional database _D_ = { _T_ 1 _, T_ 2 _, . . . , Tn_ } is a collection of transactions where each transaction _Ti_ is a subset of items ( _Ti_ ⊆ _I_ ) and every transaction is associated with a transaction identifier TID. Let _X_ ⊆ _I_ be an itemset. The association rule mining measures used in this study, namely _support_ , 

_confidence_ , and _lift_ , follow their standard definitions in [41] and [42]. The support of _X_ , denoted as sup( _X_ ), and it is defined as the number of transactions containing _X_ : 



An itemset is considered to be frequent if its support is greater than or equal to a user-specified minimum support threshold _min_  sup_ , i.e., sup( _X_ ) ≥ _min_  sup_ . 

An association rule is in the form _X_ ⇒ _Y_ , where _X_ ⊆ _I_ , _Y_ ⊆ _I_ , and _X_ ∩ _Y_ = ∅. The left-hand side of an association rule _X_ is called the antecedent, and the right-hand side of the association rule _Y_ is called the consequent. 

The confidence of a rule defines the reliability of an association rule, and it is defined as the conditional probability that a transaction contains _Y_ given that it contains _X_ : 



An association rule is considered strong if its confidence is greater than or equal to a user-specified minimum confidence threshold _min_  conf_ . 

The lift of a rule defines how much more often _X_ and _Y_ occur together than would be expected. The lift of a rule is defined as: 



A lift value greater than 1 indicates a positive dependence between _X_ and _Y_ , meaning they co-occur more frequently under statistical independence. Lift equal to 1 indicates no association (independence), while lift less than 1 indicates a negative association. 

In the proposed rating aware rule mining framework, the item set _I_ is defined as the set of different aspectsentiment pairs, such as Food_negative, Food_positive, or Room_negative. Given 12 aspects and 2 polarity labels, the cardinality of the item set is | _I_ | = 12 × 2 = 24. Neutral sentiment labels are excluded from the rule mining process, 

39501 

VOLUME 14, 2026 

A. C. Öztürk: Discovering Aspect–Sentiment Drivers of Hotel Review Ratings 



as they tend to generate generic, weakly informative rules. Each hotel review is converted into a transaction _Tj_ containing all aspect-sentiment pairs mentioned in that review and is associated with a 1-5 star review rating. The star rating of a review is the class label of a corresponding transaction _Tj_ . In this way, the transactional database _D_ captures which combinations of aspect-sentiment drivers co-occur within individual reviews and how they relate to different rating levels. 

**TABLE 3.** Sample transactional database. 



Table 3 shows a sample transactional database with | _D_ | = 4, where each transaction corresponds to the aspect-sentiment items contained in a single customer review together with its star rating. In this example, suppose _min_  sup_ = 1 and _min_  conf_ = 0 _._ 7. Let _X_ = { _Food_negative, Room_negative_ } and consider the association rule _X_ ⇒ _CLASS_ = 1. Since _X_ appears once in the database, sup( _X_ ) = 1. As the joint itemset _X_ ∪{ _CLASS_ = 1} also appears once, conf( _X_ ⇒ _CLASS_ = 1) = 1 _/_ 1 = 1. Because the prior probability of observing a 1-star review in this database is _P_ ( _CLASS_ = 1) = 1 _/_ 4 = 0 _._ 25, and thus lift( _X_ ⇒ _CLASS_ = 1) = conf( _X_ ⇒ _CLASS_ = 1) _/P_ ( _CLASS_ = 1) = 1 _/_ 0 _._ 25 = 4. A lift greater than 1 indicates positive dependence, and in this example it suggests that the co-occurrence of negative food and room experiences is strongly associated with the lowest rating class, 1-star. 

### _E. HUIM UTILITY DEFINITION AND RATING-AWARE MINING CONFIGURATION_ 

In the hotel review domain, previous studies have shown that review attributes contribute asymmetrically to customers’ overall ratings. Consequently, different aspects can have different effects on global evaluations [43], [44]. Motivated by this evidence, the proposed framework assumes that each aspect-sentiment pair has a different level of importance in characterizing rating outcomes. To capture this heterogeneity, weights are assigned to aspect-sentiment pairs rather than treating all items as equally informative. High-utility itemset mining (HUIM) is therefore adopted because it enables weighted evaluation of patterns and prioritizes combinations that are more influential for explaining specific rating levels. In the proposed rule mining framework, rule utility is defined to increase with confidence, lift, class conditional support, and antecedent length. Moreover, because 1-2 star reviews are substantially fewer than 5-star reviews, class-specific multipliers are applied to up-weight low rating rules and 

slightly down-weight the dominant 5-star class, preventing minority class drivers from being overshadowed. 

The utility score of a rule _X_ ⇒ CLASS _k_ is defined as follows: 



where _wk_ is a class specific weight that compensates for rating imbalance and takes larger values for minority classes. The term conf( _X_ ⇒ _k_ )<sup>_α_</sup> represents rule reliability, and _α >_ 0 controls how strongly confidence is emphasized. The factor lift( _X_ ⇒ _k_ ) − 1 measures improvement over the prior probability of class _k_ . The quantity sup _k_ ( _X_ ) denotes the class-conditional support count, defined as the number of transactions with rating _k_ that contain _X_ . The term log�1 + sup _k_ ( _X_ )� rewards rules that occur more frequently within class _k_ with diminishing returns, preventing highly frequent majority class patterns from dominating the utility. Finally, the factor �1 + _λ_ (| _X_ | − 1)� provides a mild bonus for longer antecedents, and _λ_ ≥ 0 controls the strength of this effect. To illustrate Eq. (4) numerically, consider the database in Table 3 and the rule _X_ = { _Food_negative, Room_negative_ } ⇒ _CLASS_ = 1, for which conf( _X_ ⇒ 1) = 1 _._ 0, sup1( _X_ ) = 1, lift( _X_ ⇒ 1) = 4 _._ 0, and | _X_ | = 2. Using the configuration adopted in experiments ( _w_ 1 = 1 _._ 40, _α_ = 1 _._ 5, _λ_ = 0 _._ 35), Eq. (4) gives; 



Candidate antecedents are restricted to a maximum length of three items (| _X_ | ≤ 3) to preserve interpretability of the discovered drivers and to control combinatorial growth in candidate generation. In pilot runs, allowing longer antecedents primarily produced overly specific rules with limited additional coverage gains. In the remainder of the study, candidate class-association rules that satisfy the minimum support and confidence constraints are first generated, and only rules with positive utility values are retained. 

Experiments were conducted using a stratified 80/20 traintest partition ( _TEST_SIZE_ = 0 _._ 20) with a fixed random seed ( _RANDOM_STATE_ = 42). Rules are mined on the training set under class-specific minimum thresholds on support, confidence, and lift, so that only patterns that are sufficiently frequent and strongly associated with a specific rating level are retained. These thresholds are set separately for each class to address strong class imbalance: lower support thresholds are used for low-rating classes (1-2 stars), whereas a higher support threshold is used for the dominant 5-star class to avoid generating many trivial rules. To avoid systematically under-selecting informative three-item interaction patterns, the minimum support requirement for | _X_ | = 3 antecedents is relaxed by one occurrence relative to the class base threshold, but not below two. 

39502 

VOLUME 14, 2026 

A. C. Öztürk: Discovering Aspect–Sentiment Drivers of Hotel Review Ratings 



The proposed HUIM-based driver discovery framework employs the utility formulation in Eq. (4) alongside class-specific minimum thresholds. Parameter values were determined via iterative empirical tuning on the training split, where conservative initial thresholds and imbalancecompensation weights were progressively adjusted to improve Macro-F1 under class imbalance while monitoring rule activation (coverage) and the number of retained rules. Here, _coverage_ is defined as the fraction of test reviews for which at least one mined rule antecedent is a subset of the review’s aspect-sentiment itemset (i.e., the rule fires at least once). In addition to maximizing Macro-F1, the final configuration was selected based on stability, where parameter settings were preferred if further small adjustments led to only marginal changes in Macro-F1 or coverage without causing the mined rule set to expand excessively or collapse to a sparse set. Lower thresholds were assigned to minority classes (1-2 stars) to facilitate pattern discovery despite limited transactions, whereas stricter thresholds were applied to the dominant 5-star class to suppress trivial highfrequency rules. 

Based on this procedure, the following class-specific thresholds are applied for _k_ =1 _, . . . ,_ 5: min sup _k_ ∈{3 _,_ 3 _,_ 5 _,_ 5 _,_ 8}, min conf _k_ ∈ {0 _._ 20 _,_ 0 _._ 18 _,_ 0 _._ 30 _,_ 0 _._ 35 _,_ 0 _._ 45}, and min lift _k_ ∈ {1 _._ 35 _,_ 1 _._ 30 _,_ 1 _._ 15 _,_ 1 _._ 15 _,_ 1 _._ 05}. In the utility definition, confidence is emphasized with _α_ = 1 _._ 5, and longer antecedents are promoted via a length bonus of _λ_ = 0 _._ 35. Cost-sensitive multipliers are set to _wk_ = {1 _._ 40 _,_ 1 _._ 95 _,_ 1 _._ 35 _,_ 1 _._ 25 _,_ 0 _._ 80} to mitigate imbalance. Finally, the vocabulary retains items observed at least twice in the training data ( _VOCAB_MIN_FREQ_ = 2). 

When no mined rule matches a given review, a singleton back-off model is used to provide a defined score for all classes. Specifically, back-off probabilities are estimated from training data using Laplace smoothing and combined with the rule-based score using a fixed mixture weight, whereas when rule matches exist the back-off acts as an auxiliary stabilizer rather than replacing the rule evidence. The isolated impact of the major framework components (class-specific thresholding, _λ_ , and _wk_ ) is evaluated via controlled ablations in Section IV-D. 

### _F. HUIM-BASED ASPECT-SENTIMENT DRIVER EXTRACTION_ 

In the proposed HUIM-based driver mining framework, the utility of an aspect-sentiment itemset for a given rating class is defined as a composite score that combines class-specific confidence, lift, class-conditional support, rule length, and cost-sensitive class multipliers. Confidence and lift capture the reliability and distinctiveness of a pattern for a given rating level, while a logarithmic class-conditional support term rewards patterns that occur sufficiently often to be interpretable and stable. A modest rule-length bonus favors multi-aspect patterns that jointly describe more complex rating drivers. Finally, class-specific multipliers up-weight low-star ratings and slightly down-weight the dominant 5-star 

**Algorithm 1** Rating-Specific High-Utility Rule Discovery 1: **Input:** _D_ train = {( _Tj, yj_ )}, _yj_ ∈{1 _, . . . ,_ 5}; thresholds { _min_supk , min_confk , min_liftk_ }; utility _U_ (·) (Eq. (4)) 2: **Output:** rating-specific high-utility rule sets { _Hk_ }<sup>5</sup> _k_ =1 3: _H_ ←∅ 4: **for** _k_ ← 1 to 5 **do** 5: _Dk_ ←{ _Tj_ | ( _Tj, yj_ ) ∈ _D_ train ∧ _yj_ = _k_ } 6: _Ck_ ← _FrequentItemsets_ ( _Dk , min_supk_ ) ▷ Enforces class-conditional support 7: _Hk_ ←∅ 8: **for all** _X_ ∈ _Ck_ **do** 9: Compute _conf_ ( _X_ ⇒ _k_ ) and _lift_ ( _X_ ⇒ _k_ ) on _D_ train 10: **if** _conf_ ( _X_ ⇒ _k_ ) ≥ _min_confk_ ∧ _lift_ ( _X_ ⇒ _k_ ) ≥ _min_liftk_ **then** 11: _u_ ← _U_ ( _X_ ⇒ _k_ ) ▷ Eq. (4) 12: **if** _u >_ 0 **then** 13: _Hk_ ← _Hk_ ∪{( _X_ ⇒ _k, u_ )} 14: **end if** 15: **end if** 16: **end for** 17: _H_ ← _H_ ∪{ _Hk_ } 18: **end for** 

19: **return** _H_ 

class, accounting for class imbalance and emphasizing the managerial importance of negative-review drivers. Using this definition, HUIM is applied to mine and rank high-utility class-association rules of the form _X_ ⇒ _CLASS_ = _k_ , where _X_ is a set of aspect-sentiment items and _k_ ∈{1 _,_ 2 _,_ 3 _,_ 4 _,_ 5}. Candidate rules that satisfy minimum thresholds on support and confidence are first generated, and utility values are then computed for the remaining rules; only rules with positive utility are retained. The highest-utility rules for each class are interpreted as characteristic aspect-sentiment driver configurations for the corresponding rating level, such as multi-aspect negative patterns for low ratings and multiaspect positive patterns for high ratings. 

Algorithm 1 summarizes the proposed rating-specific HUIM rule discovery procedure. Although a utility function is used, the proposed approach does not perform classical HUIM discovery under a minimum-utility constraint. Instead, utility is used only to rank class-association rules after classconditional frequent itemset generation and rule filtering. For each rating class _k_ , candidate antecedent itemsets are first generated from the class-filtered transactions _Dk_ by enforcing the minimum class-conditional support threshold _min_supk_ . Each candidate itemset _X_ is then evaluated as a class-association rule _X_ ⇒ _k_ by computing confidence and lift on the full training database and filtering rules that do not satisfy the class-specific thresholds _min_confk_ and _min_liftk_ . For the remaining rules, the utility score _U_ ( _X_ ⇒ _k_ ) is computed using Eq. (4), and only positive-utility rules are retained as rating-specific drivers. The resulting sets { _Hk_ } 

39503 

VOLUME 14, 2026 

A. C. Öztürk: Discovering Aspect–Sentiment Drivers of Hotel Review Ratings 



constitute interpretable driver patterns that characterize and differentiate rating levels. 

### **IV. RESULTS** 

### _A. OVERVIEW OF EXTRACTED ASPECT-SENTIMENT DRIVERS_ 

In this subsection, an overview of how rules are discovered by the HUIM-based association rule framework is provided. The rating distribution in the dataset is strongly imbalanced, with approximately 59% of reviews rated 5 stars, 19% rated 4 stars, 11% rated 3 stars, and only about 11% combined in the 1-2 star classes. For this reason, association rules are mined from the transactional review dataset using different predefined minimum thresholds on support, confidence, and lift for different class labels. These minimum thresholds are selected with three objectives: (i) ensuring every star rating level is represented by a non-trivial number of rules; (ii) avoiding an explosion of redundant or overly generic rules for the abundant 4-5 star classes; and (iii) obtaining a sufficient number of multi-aspect patterns for each rating class. The minimum support thresholds are set in a range between 3 and 8 occurrences per class, the minimum confidence thresholds are set between 0 _._ 18 and 0 _._ 45, and the minimum lift thresholds are assigned between 1 _._ 05 and 1 _._ 35. 

In a given review, a specific aspect may be highlighted in multiple sentences. To produce a single review level aspect sentiment, all sentences referring to the same aspect are aggregated via majority voting over their sentence-level sentiment labels. The aspect sentiment of a review is labelled as positive if the number of positive labels is greater than the negatives. Conversely, if negative labels outnumber positive ones, the aspect sentiment is labelled as negative. In cases where the counts of positive and negative labels are equal or the overall tone remains neutral, the aspect is discarded from the transactional database. The neutral sentiment labels are kept for descriptive statistics at the sentence level but elements with overall neutral sentiment are excluded from rule mining. The reason for this is that neutral sentiments do not consistently raise or lower perceived service quality so they behave like background noise in association rule analysis. Including them would generate low utility patterns that provide little managerial insight and are difficult to interpret. 

Applying the class-specific support, confidence, and lift thresholds described above to the transactional review database yielded a total of 2 _,_ 922 high-utility rules across the five rating levels. Of these, 2 _,_ 904 have an antecedent that matches at least one review in the test set. In terms of antecedent length, the final rule set consists of 45 singleitem, 526 two-item, and 2 _,_ 351 three-item rules. These counts correspond to approximately 1 _._ 5%, 18 _._ 0%, and 80 _._ 5% of all rules respectively, indicating that most discovered patterns involve interactions among three aspect-sentiment pairs. 

Table 4 summarizes the rating-wise distribution of review transactions and the coverage of the mined rules. Rating 

denotes the star rating class. Total gives the number of reviews in each class, while Train and Test report the class-wise counts in the rule-mining split and the held out evaluation split. HU Rules gives the number of retained high-utility rules whose consequent is the corresponding rating class. Test cov. reports the percentage of test reviews in that class for which at least one rule with the same consequent is triggered. The transactional dataset comprises 11 _,_ 275 reviews, of which 7 _,_ 892 are used for rule mining and 3 _,_ 383 are reserved for evaluation. On the held-out test set, at least one rule whose consequent equals the observed rating fires for 97 _._ 0% of all reviews. 

Coverage by rating class ranges from 91 _._ 6% for the 3-star class to 99 _._ 5% for the 2-star class. It is particularly high for the rare 1-star and 2-star classes, reaching 98 _._ 0% and 99 _._ 5%, respectively. Taken together, these results indicate that the mined rules achieve broad explanatory coverage while providing a compact yet expressive summary of how aspect-sentiment configurations are associated with different rating levels. 

**TABLE 4.** Rating-wise distribution of reviews, train-test split, and mined high-utility rules. 



Neutral aspect-sentiment items were also included in the HUIM transactional database as an additional experiment. This configuration substantially increased the number and length of the mined rules, producing 3 _,_ 458 antecedents with most rules having length three, but it did not improve overall predictive performance. Excluding neutral items yielded stronger rating prediction performance, with accuracy of 0 _._ 665 and macro-F1 of 0 _._ 462, compared with accuracy of 0 _._ 565 and macro-F1 of 0 _._ 380 when neutral sentiments were included. The neutral-inclusive variant slightly improved the F1-score for the 2-star class, but it reduced performance for the 1-star, 3-star, and 4-star classes and made the mined rule set less interpretable. Therefore, the main model considers only positive and negative sentiments. 

### _B. DISCOVERING ASPECT-SENTIMENT DRIVERS ACROSS RATING CLASSES_ 

This subsection investigates how specific aspect-sentiment expressions are associated with different star-rating levels in the review corpus. First, a majority-net sentiment is computed for each aspect at the review level by aggregating sentencelevel polarity labels. Only aspect outcomes with a clear majority polarity are retained, while mixed or tied outcomes are excluded. Each review is then represented as a transaction 

39504 

VOLUME 14, 2026 

A. C. Öztürk: Discovering Aspect–Sentiment Drivers of Hotel Review Ratings 



of aspect-sentiment items, and HUIM is applied under classspecific thresholds to mine rating-specific association rules. 

The aspect-level sentiment distributions across rating levels are summarized in Figure 2a and Figure 2b. In these figures, rows represent the aspect names and columns represent 1- to 5-star ratings of reviews. Figure 2a shows the fraction of reviews that express an overall positive sentiment for each aspect, whereas Figure 2b shows the fraction of reviews that express an overall negative sentiment for each aspect. As ratings shift from 1 to 5 stars, positive aspect outcomes generally increase and negative aspect outcomes generally decrease. Conversely, as ratings shift from 5 to 1 stars, positive outcomes decrease and negative outcomes increase. The strength of this relation varies across aspects and provides a descriptive context for rule based analysis. 

Rules are mined under HUIM thresholds and then ranked within each rating class for visualization. Ranking is based on the driver score, defined as support multiplied by lift, which prioritizes rules that are both frequent and distinctive for that class. Support captures how often an antecedent occurs within rating class _k_ , whereas lift quantifies how strongly the antecedent is associated with class _k_ relative to chance, as described by [44]. Accordingly, for a rule of the form antecedent ⇒ rating = _k_ , the driver score is computed as: 



Here _supportk_ denotes the number of reviews with rating _k_ in which the antecedent occurs, while _liftk_ is the lift of the rule with respect to _k_ . The HUIM procedure yields a total of 2 _,_ 922 high-utility rules that satisfy the class-specific support, confidence, and lift thresholds. Among these, 2 _,_ 904 rules have an antecedent that actually matches at least one review in the evaluation data and are therefore treated as activated rules. To identify which aspect-sentiment patterns most strongly influence each rating value, _driver_  scorek_ was computed for every activated rule and use this score was used for ranking and selecting the most influential rules within each rating. For each rating level, then up to five rules are selected with the highest driver scores, giving preference to multi-aspect antecedents. 

Figure 3 illustrates the top five high-utility rules for each rating class, ranked according to their driver scores. A clear polarity reversal is observed across the rating spectrum. Low ratings of 1- and 2-stars are primarily associated with co-occurring negative signals in core service dimensions, particularly _Room Comfort and Facilities_ and _Staff and FrontDesk Service_ , while negative _Food and Dining_ evaluations also appear prominently among the top drivers. For example, { _Room Comfort and Facilities_ (−), _Staff and Front-Desk Service_ (−) } is among the strongest drivers of dissatisfaction, reaching a driver score of 1 _,_ 664 in the 1-star class and 1 _,_ 222 in the 2-star class. 

The three-star category exhibits a mixed, transitional profile. While its top drivers still include negative signals regarding key service elements, such as { _Food and Dining_ (−), _Room Comfort and Facilities_ (−) } with a driver score of 

585, these patterns are in some cases accompanied by positive contextual strengths such as _Location_ (+) or _Beach and Sea_ (+). Overall, the three-star rules reflect trade-off experiences, where locational advantages are offset by service-related shortcomings, limiting ratings to the mid-range. 

High ratings of 4 and 5-stars show the opposite polarity to the 1- to 2-star classes and a clearer pattern than the mixed 3-star category. They are characterized by co-occurring positive strengths across the same core dimensions, rather than negative or trade-off combinations. For example, { _Room Comfort and Facilities_ (+), _Staff and Front-Desk Service_ (+)} attains a driver score of 2 _,_ 175 for 5-star reviews, the highest value observed in the study. 

In addition to these core strengths, 5-star satisfaction is also associated with value-added experiences, such as _Entertainment (Day and Night)_ , which emerge as high-impact drivers predominantly at the top end of the scale. Managerially, these results imply that preventing 1 to 2-star outcomes requires prioritizing improvements in _Staff and Front-Desk Service_ and _Room Comfort and Facilities_ , whereas securing 5-star ratings depends on sustaining excellence in these core areas and complementing them with delighter attributes. 

When aspects are treated independently, the analysis captures per-aspect sentiment shifts across rating classes. However, it cannot capture multi-aspect co-occurrence patterns within a rating class, where combinations of failures or strengths jointly shape the rating outcome. Accordingly, Figure 2 highlights marginal sentiment trends for individual aspects, whereas Figure 3 highlights the dominant multiaspect co-occurrence patterns extracted by HUIM across rating classes. 

For example, Figure 2 shows that _Room Comfort and Facilities_ and _Staff and Front-Desk Service_ shift from predominantly negative outcomes in 1- and 2-star review ratings and predominantly positive outcomes in 4- and 5-star reviews. However, this does not indicate whether these signals co-occur as a combined pattern within the same rating class. It can be seen in Figure 3 that 1- and 2-star outcomes are strongly linked to the joint negative pattern of _Room Comfort and Facilities_ and _Staff and Front-Desk Service_ . On the other hand, 4- and 5-star outcomes are characterized by their simultaneous positive evaluations. Focusing on multiaspect combinations can provide more nuanced insights. As a result, managerial interventions designed around these combined patterns are more likely to be effective than isolated improvements targeting a single aspect. 

### _C. COMPARATIVE EVALUATION OF THE DRIVER DISCOVERY_ 

The proposed utility-aware HUIM framework was benchmarked against three rule and pattern mining baselines, namely CPAR [45], CAEP [46], and MCTS-Diverse [47]. CPAR is a predictive association-rule classification algorithm, CAEP is an emerging-pattern based classification algorithm, and MCTS-Diverse is a Monte Carlo Tree Search 

39505 

VOLUME 14, 2026 

A. C. Öztürk: Discovering Aspect–Sentiment Drivers of Hotel Review Ratings 







**FIGURE 2.** Aspect-level sentiment distributions across rating classes: (a) positive sentiment fractions and (b) negative sentiment fractions. 

based pattern discovery and selection algorithm. In each method, star-rating drivers were discovered as class-specific aspect-sentiment itemsets that are strongly associated with each rating level. 

To ensure comparability across methods, the same candidate constraints and filtering protocol were applied. Drivers were evaluated for each of the five star-rating classes using metrics computed at Top- _K_ , and _K_ was set to 50. Across all methods, patterns were limited to itemsets with at most three items, and minimum support and minimum confidence thresholds were applied before ranking. The minimum support thresholds were set to 3 for classes 1 and 2, 5 for classes 3 and 4, and 8 for class 5. The minimum confidence thresholds were set to 0.15 for classes 1 and 2, 0.20 for class 3, 0.25 for class 4, and 0.35 for class 5. Candidate drivers were ranked using each method’s native objective. HUIM prioritizes reliability and utility alignment, CPAR emphasizes predictive rule strength, CAEP emphasizes class distinctiveness, and MCTS-Diverse balances high scores with reduced overlap. 

Mining quality was assessed using Coverage, Precision, and Macro-F1 at Top- _K_ . A test transaction was considered covered for its true star class when at least one of the Top- _K_ drivers of that class matched the transaction. Precision and recall were computed per class to obtain the class-wise F1-scores, and Macro-F1 was reported as the average of these class-wise F1-scores. In addition, Average Matched Utility at Top- _K_ was reported as the mean utility score of the highest-utility driver matching each transaction’s true star class. Utility was defined at the itemset level using the conditional mean rating estimated from the training split. Finally, within-set overlap was assessed using the average pairwise Jaccard similarity among the Top- _K_ drivers within each star class. Precision, Macro-F1, Average Matched Utility, and Jaccard similarity are reported in the range [0 _,_ 1], where higher values indicate better performance, while Coverage is reported as the percentage of covered test transactions. 

**TABLE 5.** Impact of itemset length complexity on the mining robustness and utility of the discovered drivers. 



Table 5 reports comparative performance across varying pattern length settings, where _MinLen_ denotes the minimum number of items required in a driver. In this study, _MinLen_ takes values 1, 2, or 3. All methods remain competitive when single-item drivers are permitted.However, clearer divergence emerges as the minimum required pattern length increases. At _MinLen_ = 2, the highest Macro-F1 and Average Matched Utility are achieved by HUIM. At _MinLen_ = 3, CPAR and CAEP exhibit degradation consistent with sparsity effects, and MCTS shows a marked drop that is consistent with the diversity-value trade-off under an expanded search space. In contrast, HUIM remains comparatively stable because selection is guided by utility alignment, and highutility multi-item drivers can still be retained even when their occurrences are relatively rare. 

Table 6 characterizes the coherence of discovered drivers across the five rating classes using the average pairwise Jaccard similarity. The results indicate that HUIM yields the most internally consistent driver sets overall, with a notable improvement for Class 3 where reviews typically include mixed or ambiguous signals. Conversely, lower coherence for MCTS is consistent with its stronger emphasis on diversity. Overall, these results suggest that explicitly optimizing 

39506 

VOLUME 14, 2026 

A. C. Öztürk: Discovering Aspect–Sentiment Drivers of Hotel Review Ratings 











**FIGURE 3.** size. 

**TABLE 6.** Class-wise evaluation of driver-set coherence measured by average pairwise Jaccard similarity at Top- _K_ ( _K_ **=** 50). 



for utility during driver selection improves the usefulness and structural quality of the extracted drivers. As _MinLen_ increases, baselines are more strongly affected by sparsity 

or diversity-value trade-offs, while HUIM maintains higher matched utility and internal consistency. 

### _D. PREDICTIVE VALIDATION OF DISCOVERED ASPECT-SENTIMENT DRIVERS_ 

Although the proposed HUIM framework was not designed for general-purpose review rating prediction, rating prediction was used as an auxiliary validation task to evaluate the consistency between the discovered aspect-sentiment drivers and the observed star ratings. The HUIM-based classifier was compared against four strong baselines, with all models evaluated on the same review set under an identical train-test split. Two classical text baselines and two additional baselines 

39507 

VOLUME 14, 2026 

A. C. Öztürk: Discovering Aspect–Sentiment Drivers of Hotel Review Ratings 



representing alternative review encodings were considered. Consistent with prior work [1], the classical baselines included TF-IDF with regularized logistic regression (TFIDF + LRCV) and Bag-of-Words with a random forest classifier (BoW + RF). In these models, the reviews were represented by TF-IDF or bag-of-words vectors and then classified by the corresponding learner. The remaining baselines employed logistic regression with cross-validated regularization (LRCV) on two different representations. _Bag of Items + LRCV_ used sparse indicator vectors of majoritynet aspect-sentiment items, whereas _BERT Embedding + LRCV_ used fixed-length embeddings extracted from a pretrained BERT encoder. In the HUIM-based classifier, each review was first represented as a transaction of majoritynet aspect-sentiment items. High-utility rules were then mined using class-specific thresholds, and the resulting rule evidence was combined with a singleton-based Naive Bayes backoff component under a cost-sensitive scheme. 

**TABLE 7.** Overall accuracy and Macro-F1 comparison across models. 



Table 7 reports overall Accuracy and Macro-F1 for all models. Since the label distribution is skewed toward high ratings, Macro-F1 is emphasized as it better reflects performance on minority classes. BERT Embedding + LRCV achieved the best overall results, with an accuracy of 0.698 and a Macro-F1 of 0.473. Although HUIM did not achieve the highest overall accuracy, it attained a MacroF1 of 0.462, which was the second-highest value among all methods and exceeded both TF-IDF + LRCV and Bag of Items + LRCV. This suggests a more balanced performance across rating classes under label imbalance, where overall accuracy can be dominated by the majority rating class. In contrast, BoW + Random Forest showed substantially lower performance, with an accuracy of 0.630 and a MacroF1 of 0.275. 

**TABLE 8.** Rating-wise accuracy comparison. 



As overall averages can mask performance on minority classes, Table 8 reports class-wise accuracy for each rating level from 1 to 5, revealing important differences in robustness and sensitivity. The 2-star class is particularly 

informative for dissatisfaction signals yet is difficult to identify due to limited support, making class-wise results essential for interpretation. HUIM achieves the highest accuracy on 2-star reviews at 52 _._ 8% while maintaining high accuracy on the dominant 5-star class at 89 _._ 4%. In contrast, the _Bag-of-Items + LRCV_ and _TF-IDF + LRCV_ baselines achieve very high 5-star accuracy at 94 _._ 8% and 93 _._ 5%, respectively, but exhibit weak recognition of 2-star reviews with accuracies below 15%. _BoW + Random Forest_ collapses on minority ratings and fails to correctly predict any 2-star reviews. _BERT Embedding + LRCV_ attains the highest 1-star accuracy at 60 _._ 3%, yet its 2-star accuracy remains low at 8 _._ 1%. In summary, these results indicate that HUIM provides a favorable trade-off by improving detection of 2-star reviews, where aspect-sentiment signals are more nuanced, while preserving strong performance on the majority class, supporting the rating-consistency of the mined drivers. 

**TABLE 9.** Impact of ablation settings on model performance and rule characteristics. 



### _E. ABLATION STUDY AND PARAMETER IMPACT_ 

The contribution of individual components in the proposed HUIM-based driver discovery framework is quantified through controlled ablations of the utility design and the rating-aware thresholding strategy defined in Section III-E (Eq. (4)). In each ablation, only one component is modified while the remainder of the mining pipeline is kept unchanged, so that performance differences can be attributed to the modified component. 

Five ablation variants are evaluated, where _k_ ∈{1 _, . . . ,_ 5} denotes the rating class: (i) _Uniform Support_ (min sup _k_ = _σ_ for all _k_ ), (ii) _Uniform Confidence_ (min conf _k_ = _δ_ for all _k_ ), (iii) _Uniform Lift_ (min lift _k_ = _τ_ for all _k_ ), (iv) _No Length Bonus_ ( _λ_ = 0), and (v) _Uniform Class Weights_ ( _wk_ = 1 for all _k_ ). For the uniform-threshold variants, global values are set to the rounded mean of the tuned class-specific thresholds reported in Section III-E, yielding _σ_ = 5, _δ_ = 0 _._ 30, and _τ_ = 1 _._ 20. The shaping terms in Eq. (4), namely the confidence exponent _α_ and the log(1 + sup _k_ ( _X_ )) scaling, are kept fixed across all variants, as they apply monotonic re-scalings rather than introducing additional framework components. 

Table 9 reports overall predictive performance (Accuracy and Macro-F1), explanatory reach (Coverage), and the number of retained rules. Coverage follows the definition in Section III-E and is computed on the test split as the fraction of reviews whose aspect-sentiment itemset matches at least one mined antecedent (i.e., at least one rule fires). Table 10 further reports class-wise F1-scores for all five rating 

39508 

VOLUME 14, 2026 

A. C. Öztürk: Discovering Aspect–Sentiment Drivers of Hotel Review Ratings 



classes to reveal class-specific sensitivity under imbalance. Homogenizing the support threshold mainly controls the rule set size, reducing the number of retained rules from 1,454 to 1,367 with negligible changes in Accuracy and Macro-F1, indicating that class-conditional support primarily regulates rule volume rather than predictive behavior. Homogenizing confidence ( _δ_ = 0 _._ 30) slightly improves Macro-F1 from 0.462 to 0.468) but decreases Accuracy from 0.665 to 0.656, suggesting a redistribution of errors across classes rather than a uniform gain. In contrast, homogenizing lift ( _τ_ = 1 _._ 20) substantially reduces Coverage from 0.981 to 0.856, demonstrating that class-specific lift thresholds are important for maintaining rule activation and explanatory breadth. Disabling the length bonus ( _λ_ = 0) yields a small but consistent Macro-F1 drop (0.462→0.457), indicating that mildly favoring longer antecedents contributes to balanced performance without affecting coverage. Finally, removing cost sensitivity ( _wk_ = 1) increases Accuracy (0.667) but decreases Macro-F1 (0.451), confirming that cost-sensitive weighting is necessary to mitigate imbalance and reduce majority-class dominance. 

**TABLE 10.** Impact of ablation settings on class-wise F1 performance. 



Class-wise F1-scores for each star rating class under each ablation variant are shown in Table 10. The Uniform Support produces only small changes across the 2-star and 3-star classes, while the 1-star and 5-star classes remain the same as the full model. The Uniform Confidence improves the performance for the 3-star class from 0.368 to 0.409 and for the 4-star class from 0.301 to 0.354. However, it reduces performance for the 2-star class from 0.400 to 0.361 and slightly reduces the 1-star and 5-star classes from 0.377 to 0.368 and from 0.862 to 0.849, respectively. The Uniform Lift keeps the 1-star, 2-star, and 3-star performances unchanged and slightly increases the 4-star class from 0.301 to 0.311, while the 5-star class slightly decreases from 0.862 to 0.858. However, as shown in Table 9, the Uniform Lift reduces coverage from 0.981 to 0.856, indicating that class-specific lift thresholds are important for maintaining rule activation. = Removing the length bonus ( _λ_ 0) slightly reduces the 1-star F1-score from 0.377 to 0.369, the 2-star F1score from 0.400 to 0.391, and the 4-star F1-score from 0.301 to 0.294, while the 5-star class remains unchanged and the 3-star class shows only a small change (0.368 to 0.370). Although under Uniform Class Weights, the F1-score for the 1-star class increases from 0.377 to 0.470, the 2- star class drops from 0.400 to 0.239. This indicates that cost-sensitive weighting is important for mitigating class imbalance and preventing accuracy-driven bias that harms 

low-frequency classes, especially 2-star ratings.Overall, the ablations indicate that the tuned configuration provides the most balanced trade-off between predictive robustness under class imbalance and broad rule activation. 

### **V. DISCUSSION OF RESULTS** 

The discovered driver sets indicate that star ratings are associated with co-occurring customer experiences rather than isolated, single-aspect effects. This moves beyond the tautological claim that negative reviews correspond to low ratings by showing that each star class is characterized by recurring configurations of aspect-sentiment evidence (compound failures, compensatory trade-offs, and delighter add-ons). The results contribute an interpretable, utilityaware account of rating formation by expressing these classspecific configurations as compact rules, and the comparative mining evidence indicates that utility/coherence-oriented selection supports robust discovery of multi-item drivers as pattern complexity increases. Low star ratings are dominated by compound failures in core service delivery. Both the 1-star and 2-star classes are strongly associated with compound negative drivers spanning core service dimensions, most notably co-occurring negatives in Room Comfort and Facilities, Staff and Front-Desk Service, and Food and Dining. Ratings in the 3-star mid-range reflect compensatory tradeoffs characterized by mixed signals. Specifically, negative Food and Dining co-occurs with positive Location and Access, and positive Beach and Sea co-occurs with negative Staff, producing mixed narratives that are harder to model coherently than the high or low ratings. High ratings are characterized by cohesive positives across core aspects. In the 4-star class, the strongest drivers are core-positive bundles such as Food and Dining with Room comfort and Room comfort with Staff, indicating strong but largely core-focused satisfaction. Additionally, delighters such as Entertainment (Day and Night) emerge primarily at 5 stars, suggesting that exceptional ratings combine compounded core excellence with unique experiential enhancers. 

Predictive validation indicates that the discovered drivers are operationally informative because HUIM achieves competitive overall Accuracy and Macro-F1 while retaining the interpretability of explicit rules. For hotel managers, the framework can be applied by collecting newly posted reviews with their ratings, running aspect–sentiment labeling, and mining high-utility rules to identify the most influential co-occurring drivers of ratings. The output is a small set of interpretable drivers that explain rating shifts and support targeted managerial actions beyond simply tracking average ratings. From a practical standpoint, early-warning monitoring can be implemented by tracking the activation of high-impact negative bundles in newly posted reviews. Furthermore, intervention prioritization can be guided by bundle structure to target 3-star cases by resolving persistent core-service negatives. Finally, investments in delighter attributes are likely to be most effective once core service reliability is stabilized. Valuable extensions of this study 

39509 

VOLUME 14, 2026 

A. C. Öztürk: Discovering Aspect–Sentiment Drivers of Hotel Review Ratings 



include evaluating generalizability across destinations and platforms, as well as incorporating temporal analysis to capture drift in driver bundles. 

### **ACKNOWLEDGMENT** 

The author used OpenAI ChatGPT (GPT-5.2) to assist with proofreading and language editing of the manuscript. All edits were reviewed and approved by him. No AI system was used to generate the study’s figures or experimental results. 

### **VI. CONCLUSION** 

This study identifies which recurring combinations of guest experiences drive the overall evaluation expressed in online hotel reviews. To provide an interpretable, aspect-level account of rating formation, a sentence-level ABSA pipeline is combined with a rating-specific High-Utility Itemset Mining framework. Reviews are converted into transactions of aspect-sentiment items, and class-association rules are mined and ranked using a utility definition that integrates confidence, lift, class-conditional support, rule length, and cost-sensitive class multipliers. The resulting rule sets yield human-interpretable driver patterns that characterize each rating level and make explicit how multiple aspects interact within the same review. 

The discovered drivers indicate that low ratings are typically associated with concurrent negatives spanning more than one service dimension, whereas higher ratings more often reflect reinforcing positives across core aspects, with top ratings additionally linked to value-added experiences. Mid-range ratings exhibit mixed trade-offs in which negative signals in some service dimensions can coexist with contextual strengths. From a theoretical perspective, the findings underscore that service dimensions do not operate in isolation, as aspect failures can compound to depress ratings, while reaching the highest satisfaction levels is more consistent with positive synergies across multiple dimensions. 

To assess not only interpretability but also practical signal quality, the proposed utility-based framework is benchmarked against established rating prediction baselines on held-out reviews. Overall, the framework achieves competitive performance with an Accuracy of 0.665 and Macro-F1 of 0.462, approaching the strongest baseline (BERT Embedding + LRCV), which yielded an Accuracy of 0.698 and Macro-F1 of 0.473. Importantly, the class-wise results show that the framework is particularly effective at identifying some difficult minority ratings, notably the 2-star class, while performance is less uniform for adjacent mid-tohigh ratings such as 4-star. 

Overall, the proposed approach contributes a transparent alternative to closed-box rating prediction by extracting actionable and explainable aspect-sentiment configurations that clarify how customers translate detailed experiences into overall star ratings. For practitioners, the identified patterns suggest a practical intervention logic that prioritizes the elimination of recurring toxic multi-aspect negative bundles linked to low ratings, while treating value-added features as amplifiers that are most effective once core service issues are stabilized. Future work can extend the framework to additional destinations and hotel categories, test crossplatform generalization, and incorporate temporal dynamics. 

### **REFERENCES** 

- [1] M. Kumar, C. Kumar, N. Kumar, and S. Kavitha, ‘‘Efficient hotel rating prediction from reviews using ensemble learning technique,’’ _Wireless Pers. Commun._ , vol. 137, no. 2, pp. 1161–1187, Jul. 2024. 

- [2] J. Z. Maitama, N. Idris, A. Abdi, L. Shuib, and R. Fauzi, ‘‘A systematic review on implicit and explicit aspect extraction in sentiment analysis,’’ _IEEE Access_ , vol. 8, pp. 194166–194191, 2020. 

- [3] I. C. Sahin and C. Eyupoglu, ‘‘Aspect-based sentiment analysis for hospitality industry applications: A systematic literature review,’’ _Appl. Comput. Syst._ , vol. 30, no. 1, pp. 53–67, Jan. 2025, doi: 10.2478/acss-20250007. 

- [4] M. Hu and B. Liu, ‘‘Mining and summarizing customer reviews,’’ in _Proc. 10th ACM SIGKDD Int. Conf. Knowl. discovery data mining_ , Aug. 2004, pp. 168–177. 

- [5] N. Akhtar, N. Zubair, A. Kumar, and T. Ahmad, ‘‘Aspect based sentiment oriented summarization of hotel reviews,’’ _Proc. Comput. Sci._ , vol. 115, pp. 563–571, Nov. 2017. 

- [6] R. Sann and P.-C. Lai, ‘‘Understanding homophily of service failure within the hotel guest cycle: Applying NLP-aspect-based sentiment analysis to the hospitality industry,’’ _Int. J. Hospitality Manage._ , vol. 91, Oct. 2020, Art. no. 102678. 

- [7] B. Ray, A. Garain, and R. Sarkar, ‘‘An ensemble-based hotel recommender system using sentiment analysis and aspect categorization of hotel reviews,’’ _Appl. Soft Comput._ , vol. 98, Jan. 2021, Art. no. 106935. 

- [8] N. Liu and J. Zhao, ‘‘A BERT-based aspect-level sentiment analysis algorithm for cross-domain text,’’ _Comput. Intell. Neurosci._ , vol. 2022, no. 1, Jun. 2022, Art. no. 8726621. 

- [9] J. Su, Q. Chen, Y. Wang, L. Zhang, W. Pan, and Z. Li, ‘‘Sentence-level sentiment analysis based on supervised gradual machine learning,’’ _Sci. Rep._ , vol. 13, no. 1, Sep. 2023, Art. no. 14500. 

- [10] J. Devlin, M.-W. Chang, K. Lee, and K. Toutanova, ‘‘BERT: Pre-training of deep bidirectional transformers for language understanding,’’ in _Proc. Conf. North Amer. Chapter Assoc. Comput. Linguistics, Hum. Lang. Technol. (NAACL-HLT)_ , Jun. 2019, pp. 4171–4186. 

- [11] Y. Wen, Y. Liang, and X. Zhu, ‘‘Sentiment analysis of hotel online reviews using the BERT model and ERNIE model—Data from China,’’ _PLoS ONE_ , vol. 18, no. 3, Mar. 2023, Art. no. e0275382. 

- [12] M. Mathebula, A. Modupe, and V. Marivate, ‘‘ChatGPT as a text annotation tool to evaluate sentiment analysis on South African financial institutions,’’ _IEEE Access_ , vol. 12, pp. 144017–144043, 2024, doi: 10.1109/ACCESS.2024.3464374. 

- [13] M. Água, N. António, P. Carrasco, and C. Rassal, ‘‘Large language models powered aspect-based sentiment analysis for enhanced customer insights,’’ _Tourism Manage. Stud._ , vol. 21, no. 1, pp. 1–19, Jan. 2025, doi: 10.18089/tms.20250101. 

- [14] K. Schouten and F. Frasincar, ‘‘Survey on aspect-level sentiment analysis,’’ _IEEE Trans. Knowl. Data Eng._ , vol. 28, no. 3, pp. 813–830, Mar. 2016. 

- [15] L. Cagliero, M. La Quatra, and D. Apiletti, ‘‘From hotel reviews to city similarities: A unified latent-space model,’’ _Electronics_ , vol. 9, no. 1, p. 197, Jan. 2020. 

- [16] Z. Shu, R. A. C. González, J. P. García-Miguel, and M. SánchezMontañés, ‘‘Clustering using ordered weighted averaging operator and 2-tuple linguistic model for hotel segmentation: The case of TripAdvisor,’’ _Expert Syst. Appl._ , vol. 213, Mar. 2023, Art. no. 118922. 

- [17] L. Qu, G. Ifrim, and G. Weikum, ‘‘The bag-of-opinions method for review rating prediction from sparse text patterns,’’ in _Proc. 23rd Int. Conf. Comput. Linguistics (COLING)_ , Aug. 2010, pp. 913–921. 

- [18] P. Bai, Y. Xia, and Y. Xia, ‘‘Fusing knowledge and aspect sentiment for explainable recommendation,’’ _IEEE Access_ , vol. 8, pp. 137150–137160, 2020. 

- [19] S. M. Al-Ghuribi, S. A. M. Noah, M. A. Mohammed, S. N. Qasem, and B. A. H. Murshed, ‘‘To cluster or not to cluster: The impact of clustering on the performance of aspect-based collaborative filtering,’’ _IEEE Access_ , vol. 11, pp. 41979–41994, 2023. 

39510 

VOLUME 14, 2026 

A. C. Öztürk: Discovering Aspect–Sentiment Drivers of Hotel Review Ratings 



- [20] S. Chan, M. Amin, S. Rasool, and O. R. Syed, ‘‘From click to confirmation. The effect of hotel website quality and online reviews in fostering booking intentions,’’ _Int. J. Quality Service Sci._ , vol. 17, no. 2, pp. 232–254, 2025. 

- [21] Q. J. D. Oliveira-Cardoso, J. A. Martínez-González, and C. D. Álvarez-Albelo, ‘‘Hotel guest satisfaction: A predictive and discriminant study using TripAdvisor ratings,’’ _Administ. Sci._ , vol. 15, no. 7, p. 264, Jul. 2025. 

- [22] Y. Yang, M. S. Lin, and V. P. Magnini, ‘‘Do guests care more about hotel cleanliness during COVID-19? Understanding factors associated with cleanliness importance of hotel guests,’’ _Int. J. Contemp. Hospitality Manage._ , vol. 36, no. 1, pp. 239–258, Jan. 2024. 

- [23] O. Mokryn, ‘‘Consumer sentiment and hotel aspect preferences across trip modes and purposes,’’ _J. Theor. Appl. Electron. Commerce Res._ , vol. 19, no. 4, pp. 3017–3034, Nov. 2024. 

- [24] S. Kolesárová, A. Šenková, E. Kormaníková, and K. Šambronská, ‘‘Customer reviews of accommodation as an important factor in choosing and booking accommodation: Analysis of conditions in V4 countries,’’ _Administ. Sci._ , vol. 14, no. 12, p. 308, Nov. 2024. 

- [25] K. Kalnaovakul, K. Balasubramanian, and S. H.-W. Chuah, ‘‘Service quality, customer sentiment and online ratings of beach hotels: An analysis of moderating factors,’’ _J. Hospitality Tourism Insights_ , vol. 8, no. 3, pp. 988–1009, Feb. 2025. 

- [26] N. Kumar and B. R. Hanji, ‘‘Aspect-based sentiment score and star rating prediction for travel destination using multinomial logistic regression with fuzzy domain ontology algorithm,’’ _Expert Syst. Appl._ , vol. 240, Apr. 2023, Art. no. 122493. 

- [27] Q. Peng, L. You, H. Feng, W. Du, K. Zheng, F. Zhu, and X. Xu, ‘‘Jointly modeling aspect information and ratings for review rating prediction,’’ _Electron._ , vol. 11, no. 21, p. 3532, 2022. 

- [28] K. Puh and M. B. Babac, ‘‘Predicting sentiment and rating of tourist reviews using machine learning,’’ _J. Hospitality Tourism Insights_ , vol. 6, no. 3, pp. 1188–1204, Jun. 2023. 

- [29] B. H. Ahmed and A. S. Ghabayen, ‘‘Review rating prediction framework using deep learning,’’ _J. Ambient Intell. Humanized Comput._ , vol. 13, no. 7, pp. 3423–3432, Jul. 2022. 

- [30] B. Hutauruk and Y. Sibaroni, ‘‘Multi-aspect sentiment analysis for hotel reviews with hybrid RNN-long short-term memory (LSTM) method,’’ in _Proc. Int. Conf. Data Sci. Appl. (ICoDSA)_ , Jul. 2025, pp. 387–392. 

- [31] S. Yang, J. Xing, Z. Liu, and Y. Sun, ‘‘Short-text sentiment classification model based on BERT and dual-stream transformer gated attention mechanism,’’ _Electronics_ , vol. 14, no. 19, p. 3904, Sep. 2025. 

- [32] H. Zhou, S. Zhou, H. Chen, N. Liu, F. Yang, and X. Huang, ‘‘Enhancing explainable rating prediction through annotated macro concepts,’’ in _Proc. 62nd Annu. Meeting Assoc. Comput. Linguistics_ , 2024, pp. 11736–11748, doi: 10.18653/v1/2024.acl-long.631. 

- [33] X. Geng, Z. Yang, L. Jiao, Z.-J. Zhou, and Z. Ma, ‘‘Association rulebased classification: A comprehensive review of methodologies and applications,’’ _Expert Syst. Appl._ , vol. 280, Jun. 2025, Art. no. 127454, doi: 10.1016/j.eswa.2025.127454. 

- [34] M. Honnibal, I. Montani, S. Van Landeghem, and A. Boyd, ‘‘SpaCy: Industrial-strength natural language processing in Python,’’ Zenodo, Geneva, Switzerland, Tech. Rep., 2020, doi: 10.5281/zenodo. 1212303. 

- [35] Sentence-Transformers. _All-MPNet-Base-V2_ . Accessed: Jan. 26, 2026. [Online]. Available: https://huggingface.co/sentence-transformers/allmpnet-base-v2 

- [36] W. Ma, F. Jia, C. Liang, Q. Sun, and J. Wu, ‘‘A deep learning and large group consensus based cruise satisfaction evaluation model with online reviews,’’ _Inf. Sci._ , vol. 676, Aug. 2024, Art. no. 120801. 

- [37] S. Lloyd, ‘‘Least squares quantization in PCM,’’ _IEEE Trans. Inf. Theory_ , vol. IT-28, no. 2, pp. 129–137, Mar. 1982. 

- [38] J. H. Ward, ‘‘Hierarchical grouping to optimize an objective function,’’ _J. Amer. Stat. Assoc._ , vol. 58, no. 301, pp. 236–244, Mar. 1963. 

- [39] J. Achiam et al., ‘‘GPT-4 technical report,’’ 2023, _arXiv:2303.08774_ . 

- [40] W. Zhang, Y. Deng, B. Liu, S. Pan, and L. Bing, ‘‘Sentiment analysis in the era of large language models: A reality check,’’ in _Proc. Findings Assoc. Comput. Linguistics, NAACL_ , Mexico City, Mexico, Jun. 2024, pp. 3881–3906, doi: 10.18653/v1/2024.findings-naacl.246. 

- [41] J. Han, M. Kamber, and J. Pei, _Data Mining: Concepts and Techniques_ , 3rd ed., San Mateo, CA, USA: Morgan Kaufmann, 2012. 

- [42] R. Agrawal, T. Imieliński, and A. Swami, ‘‘Mining association rules between sets of items in large databases,’’ in _Proc. ACM SIGMOD Int. Conf. Manage. Data_ , Washington, DC, USA, May 1993, pp. 207–216, doi: 10.1145/170035.170072. 

- [43] D. T. B. Nguyen and V. T. K. Nguyen, ‘‘The impact of electronic wordof-mouth on the purchase intention of tourists on online hotel booking applications,’’ _Int. J. Asian Bus. Inf. Manage._ , vol. 15, no. 1, pp. 1–19, Apr. 2024. 

- [44] A. Messias, G. Rosa, P. Couto, V. Rodrigues, L. M. Silva, and J. Marques, ‘‘A new hotel classification model combining guest reviews with official hotel classification systems: Bridging expert and consumer ratings,’’ _Tourism Hospitality Res._ , Sep. 2025, Art. no. 14673584251379305, doi: 10.1177/14673584251379305. 

- [45] X. Yin and J. Han, ‘‘CPAR: Classification based on predictive association rules,’’ in _Proc. SIAM Int. Conf. Data Mining_ , May 2003, pp. 331–335. 

- [46] G. Dong, X. Zhang, L. Wong, and J. Li, ‘‘CAEP: Classification by aggregating emerging patterns,’’ in _Proc. Int. Conf. Discovery Sci._ , Oct. 1999, pp. 30–42. 

- [47] G. Bosc, J.-F. Boulicaut, C. Raïssi, and M. Kaytoue, ‘‘Anytime discovery of a diverse set of patterns with Monte Carlo tree search,’’ _Data Mining Knowl. Discovery_ , vol. 32, no. 3, pp. 604–650, May 2018. 

AHMET CUMHUR ÖZTÜRK received the Ph.D. degree in computer engineering from İzmir Institute of Technology, İzmir, Türkiye, in 2018. He is currently an Assistant Professor with Söke Vocational School, Department of Database, Network Design and Management, Aydın Adnan Menderes University. His research interests include data mining, large language models, text analysis, graph mining, and tourism analytics. 



39511 

VOLUME 14, 2026 

