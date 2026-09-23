# Fault of Our Stars: Behavioral Drivers of Rating–Sentiment Incongruence 

Ramanaish Abaiyan, Ruththiragayan Sutharsan, Kusal Amantha, Anusan Krishnathas, Asma Rauff, Kovindarajah Sriyathurshan, Patalee Narasinghe, Nirasha Munasinghe, Nisansa de Silva, Sandareka Wickramanayake _Department of Computer Science and Engineering_ , _University of Moratuwa_ , Moratuwa, Sri Lanka 

{abaiyanr.23, ruththiragayans.23, kusala.23, anusank.23, asmar.23, 

sriyathurshank.23, patalee.21, nirasha.25, NisansaDdS, sandarekaw}@cse.mrt.ac.lk 

**_Abstract_ —When people share experiences online, they often express thoughts in two ways: a star rating and a written review. In sentiment analysis, ratings are widely used as convenient weak labels for textual sentiment, yet whether the two actually agree is rarely questioned. This study investigates sentiment–rating incongruence, where the sentiment expressed in review text differs from the sentiment implied by the assigned star rating, in Sri Lankan tourism attraction reviews. A dataset of 16,156 reviews from 2010 to 2023 is analyzed using a transformer-based sentiment pipeline that derives textual sentiment independently of assigned ratings. Incongruence occurs in 18.6% of reviews and falls into six directional patterns, with Conservative Rater and Obligatory 5-Star behaviors accounting for the majority of mismatches. Prevalence also varies across venue types, with museums showing the highest rates. Statistical tests, logistic regression, Random Forest, and SHAP analysis identify venue type, reviewer expertise, review length, and temporal factors as contributors to rating–text divergence. Overall, this study demonstrates that star ratings are not interchangeable with textual sentiment and should be validated before being treated as ground-truth labels in NLP.** **_Index Terms_ —Sentiment Analysis, Natural Language Processing, BERT, Weak Label Reliability, Review Analytics,** 

## I. INTRODUCTION 

Online tourism reviews are an important source of usergenerated content for understanding visitor experiences. Most review platforms allow users to express their experience through both a star rating and a written review. In sentiment analysis and review mining, star ratings are often treated as convenient weak labels for textual sentiment [1, 2]. However, this assumption is not always reliable. A high rating does not necessarily mean that the review text is fully positive, and a moderate rating may still contain strongly positive language. For instance, a review reading "Beautiful gardens, but overpriced and overcrowded" accompanied by a 5-star rating illustrates this tension: the text conveys mixed-to-negative sentiment, while the numerical score signals unambiguous satisfaction. This creates an NLP problem: ratings may introduce noisy or context-biased labels when used as ground truth for sentiment analysis. 

The growth of platforms such as TripAdvisor has expanded tourism review data [3]. Many studies use these reviews to analyze destination image, tourist satisfaction, and consumer behavior. However, the relationship between rating-derived and text-derived sentiment remains insufficiently examined. In many sentiment analysis pipelines, star ratings are used as 

proxy labels without validating whether the written review expresses the same polarity. From an NLP perspective, this becomes a weak-supervision problem, where models trained or evaluated using ratings may learn distorted patterns rather than the actual sentiment expressed in language. 

Previous studies suggest that rating–text inconsistency is a recurring issue in online reviews [4, 5]. However, much of the tourism sentiment analysis literature still relies on ratings as sentiment labels, particularly in hotel and restaurant contexts [2, 6]. Although aspect-based sentiment analysis and topic modeling have improved the extraction of fine-grained information from review text [7, 8], the broader question of whether ratings reliably represent textual sentiment has received less attention. This gap is particularly important in underrepresented tourism contexts, where reviews are shaped by culture, attraction types, and reviewer experience. 

Recent transformer-based language models provide an opportunity to study sentiment–rating incongruence more effectively. Models such as BERT [9, 10] and RoBERTa capture contextual meaning more effectively than traditional lexicon-based approaches [11, 12]. In this study, transformerbased sentiment inference is used to derive textual sentiment independently from assigned ratings, allowing review text to be analyzed as a separate linguistic signal. 

Using 16,156 Sri Lankan tourism attraction reviews collected between 2010 and 2023 [13], this study investigates how often rating-derived sentiment and NLP-derived textual sentiment diverge, what directional forms these mismatches take, and which contextual and reviewer-level factors are associated with them. Star ratings are grouped into negative, neutral, and positive classes, while textual sentiment is inferred using a transformerbased sentiment pipeline selected through comparative model evaluation. The resulting mismatches are organized into six directional incongruence patterns, moving beyond a simple matched/mismatched classification. 

After deriving textual sentiment through transformer-based NLP inference, statistical and machine learning models are used as secondary explanatory tools to examine factors associated with rating–text divergence.This study makes four contributions. First, unlike prior work that treats rating–text mismatch as a binary correction problem, it introduces six directional incongruence patterns that capture how sentiment and ratings 

diverge, not just whether they do. Second, while transformerbased sentiment inference has been applied to tourism reviews before, this study is among the first to apply it to Sri Lankan tourism attraction data, a setting with limited prior coverage compared to hotel- and restaurant-focused studies. Third, rather than focusing on a single venue type or platform, this study examines incongruence across 11 attraction types over a 13year span, identifying venue type, reviewer expertise, and temporal trends as structural correlates of mismatch. Finally, it reframes rating–text divergence as a weak-label reliability problem in NLP, rather than primarily a tourism-analytics or review-correction proble, directly questioning the common practice of using ratings as ground-truth sentiment labels in downstream NLP pipelines. 

The findings indicate that sentiment–rating incongruence is a meaningful, context-dependent signal and that star ratings should not be treated as ground-truth sentiment without validation. For tourism review analytics, they show that ratings and written reviews capture different aspects of visitor experience, supporting the need for context-aware sentiment analysis approaches. Data and code are publicly available. 

## II. RELATED WORK 

The foundational survey by Pang and Lee [1] established sentiment analysis as a major research area and reinforced the common assumption that star ratings broadly reflect the sentiment expressed in review text. Despite recognized limitations, this convention remains widely used in tourism research as a practical weak-labeling strategy. Alaei et al. [2] note that ratings are often treated as weak labels without explicit validation, and that the literature has been heavily concentrated on hotels and restaurants. This imbalance is further highlighted by Ameur et al. [6], who report limited venue diversity and restricted geographic coverage in existing studies, especially for emerging tourism destinations. 

Methodological advances have substantially improved sentiment analysis in tourism. Wen et al. [11] demonstrate the effectiveness of transformer-based models such as BERT [9] and ERNIE [10], while Puh and Babac [12] show that jointly analyzing sentiment and ratings can provide more detailed insight. Multilingual approaches and aspect-based methods further improve interpretability by linking sentiment to specific components of the tourism experience [7, 8]. More recently, zero-shot approaches have expanded the feasibility of analyzing under-studied datasets with limited labeled data [14]. 

This inconsistency shows up in regional literature as well. Abeysinghe and Walgampaya [15] document rating–text incompatibility in hotel reviews in Anuradhapura, while Abeysinghe and Bandara [16] extend this finding across five Sri Lankan cities and propose a self-learning approach to resolve it. However, both depend on lexicon-based methods and define the problem primarily as one requiring correction rather than explanation. In contrast, this study uses transformer-based sentiment analysis and interprets incongruence as a contextdependent NLP weak-label reliability issue. 

In low-resource settings where a language does not have an adequate amount of tagged text sentiment data [17], there have been attempts to derive the text sentiment using star ratings [18, 19] or Facebook reactions [20, 21]. However, empirical findings on the relationship between ratings and review text remain mixed. Bigne et al. [4] report general alignment between the two, but also identify variation across contexts. George and Ramos [3] show that ratings may exceed text-based sentiment in destination-related reviews, while Kwon et al. [5] demonstrate that rating–text inconsistency varies by context and influences perceived review usefulness. These findings suggest that ratings and text do not always capture the same dimension of experience. 

Reviewer characteristics also appear to matter. Chua and Banerjee [22] show that reviewer expertise influences the relationship between ratings and textual content, while related work links sentiment polarity and review depth to perceived usefulness [6, 22]. Taken together, these studies indicate that ratings and text may encode different aspects of user experience and that inconsistency may be partly shaped by reviewer-level behavior. 

Overall, sentiment–rating incongruence remains insufficiently understood, particularly in tourism attraction contexts and emerging destinations. Although recent methods enable largescale and fine-grained analysis [7, 8, 11, 12, 14], there is still limited evidence on the structure of directional mismatch patterns and their drivers in multi-venue, longitudinal datasets. 

## III. METHODOLOGY 

Fig. 1 summarizes the four-phase methodology adopted in this study. 

## _A. Dataset and Preprocessing_ 

The study used the “Tourism and Travel Reviews: Sri Lankan Destinations” dataset from Mendeley Data [13], which contains 16,156 English reviews from 2010 to 2023 across 11 attraction types in Sri Lanka. Date fields were used to create travel year and review delay, with negative delay values set to zero. Raw location text was processed using rule-based parsing and manual mapping to identify province and district. _Review_Length_ was calculated as the character count of the review text. Star ratings were grouped into three classes: 

- Negative (1–2 _⋆_ ) 

- Neutral (3 _⋆_ ) 

- Positive (4–5 _⋆_ ) 

This grouping follows common practice in sentiment analysis [1, 2] and makes the rating scale directly comparable with the three-class sentiment output. Table I lists the source columns retained for analysis. 

## _B. Sentiment Model Selection_ 

Model candidates were selected to span a representative range of adaptation strategies: a community fine-tuned checkpoint (gosorio/robertaSentimentFT) representing an off-theshelf fine-tuned option, the pretrained cardiffnlp/twitter-robertabase-sentiment model representing a strong general-purpose 



<!-- Start of picture text -->
Sentiment Model<br>Clean data and engineer features PreprocessingDataset and Evaluate models on 1,000 manuallylabeled reviews; train & test; Selection Sentiment Prediction Predict textual sentiment for allreviews using selected model Rating–SentimentComparison<br>choose best model<br>Variable<br>Construction Results &<br>Create reviewer tiers and Statistical Analysis Interpretation<br>derived features<br><!-- End of picture text -->

Fig. 1. Overview of the four-phase methodology. 

### TABLE I 

SOURCE COLUMNS USED IN ANALYSIS 

TABLE II 

SENTIMENT MODEL PERFORMANCE (TEST SET, _n_ = 300) 

|**Feature**|**Description**|
|---|---|
|Location|Used to derive province and district|
|Location_Type|Type of attraction (museum, beach etc.)|
|User_Contributions<br>Travel_Date<br>Published_Date|Total reviews posted by the reviewer<br>Date of visit; used to derive travel year<br>Date of review posting; used to derive<br>review delay|
|Rating<br>Title|Star rating used to create Rating_Class<br>Review title; combined with text for<br>sentiment inference|
|Text|Review body; used for sentiment and<br>review length|



social-media sentiment baseline, and two in-house fine-tuned variants (Cardiff RoBERTa and RoBERTa-base) to test whether further domain-specific fine-tuning on the manually labeled subset improved performance. 

To derive textual sentiment independently from ratings, four transformer-based models were tested on a manually labeled set of 1,000 reviews. The dataset was split into 700 training and 300 testing instances, where the training portion was used to fine-tune selected models and the test set was used for comparative evaluation. Review titles and texts were combined as input, and model performance was assessed using Macro F1, accuracy, and weighted F1. Macro F1 was included because sentiment classes may be imbalanced. As shown in Table II, the pretrained cardiffnlp/twitter-roberta-base-sentiment model performed best overall and was selected to label the full dataset [9, 10]. This model achieved a strong balance between classification performance and generalization, outperforming fine-tuned variants while avoiding potential overfitting given the limited size of the labeled dataset. This approach measured textual sentiment independently from star ratings, reducing circularity and enabling mismatch detection between two signals: rating-derived sentiment and NLP-derived textual sentiment. 

|**Model**|**Acc.**|**Mac. F1**|**Wt. F1**|**Decision**|
|---|---|---|---|---|
|gosorio/robertaSentimentFT|0.730|0.281|0.616|Rejected|
|cardiffnlp/twitter-roberta (pretrained)|0.830|0.692|0.805|**Selected**|
|Fine-tuned Cardiff RoBERTa|0.733|0.677|0.758|Lower overall fit|
|Fine-tuned RoBERTa-base|0.777|0.698|0.780|Higher Mac. F1 only|



## _C. Variable Construction_ 

After sentiment labeling, raw title and text were removed from further analysis. _Incongruent_ was defined as a mismatch between _Sentiment_ and _Rating_Class_ , while _Pattern_ recorded the six mismatch types. _Reviewer_Tier_ grouped reviewers as follows: Novice (0–5), Casual (6–20), Active (21–100), Expert (101+). 

Reviewer tiers were defined by analyzing the distribution of contributions. The data show strong positive skew (median = 54, max = 9010): most reviewers contribute 1–5 reviews, while few exceed 100. Based on this distribution, thresholds were set at 0–5, 6–20, 21–100, and 101+ to capture distinct engagement levels. Each tier corresponds to measurable differences in behavior. Reviewers with 0–5 reviews exhibit minimal platform familiarity, whereas the 6–20 range reflects casual engagement. The 21–100 tier identifies active users with sustained participation, and 101+ represents highly engaged expert reviewers. This tiering is further supported by rating behavior: the Conservative Rater pattern increases from 27 _._ 4% among novice reviewers to 40 _._ 4% among experts, indicating experience-dependent rating practices. These tiers therefore capture both contribution intensity and observable differences in rating–text alignment [22]. 

The constructed analytical variables used in this study comprise both target-defining and explanatory features. _Sentiment_ is represented as a three-class label derived from model output, while _Rating_Class_ is a three-class label obtained by grouping star ratings (1–5); together, these variables define sentiment–rating incongruence, from which the binary variable _Incongruent_ (0/1) is derived as the target outcome. _Pattern_ is 

a six-category variable formed from the interaction between _Sentiment_ and _Rating_Class_ , capturing distinct mismatch typologies, and _Reviewer_Tier_ is a four-level ordinal variable based on grouped contribution levels, used as a predictor. Continuous predictors include _log_review_length_ , computed as the logarithm of review length in characters using log(1 + _x_ ), and _log_review_delay_ , defined as the logarithm of the time gap between visit and posting using log(1+ _x_ ). Temporal effects are modeled using _Travel_Year_c_ , a centered travel year variable, and its squared term _Travel_Year_c_<sup>_2_</sup> , which captures potential nonlinear time trends. Together, these variables capture key textual, behavioral, and temporal factors relevant to the analysis. 

TABLE III 

MODELING AND INTERPRETATION FRAMEWORK 

|**Model**|**Purpose**|**Metric**|**Key Detail**|
|---|---|---|---|
|1A: Logistic|Linear baseline|AUC-ROC|Stratified 80/20 split;|
|Reg.|performance||balanced classes; 5-fold<br>CV|
|1B: Logit|Identifies independent|95% CI|Unweighted inference|
|(statsmodels)|drivers||model fit on full design<br>matrix|
|2: Random|Captures complex|AUC-ROC|GridSearchCV on|
|Forest|relationships||training set; same<br>held-out test set|
|SHAP (post|Explains model|Mean _|ϕ|_|TreeExplainer on the|
|hoc)|predictions||best Random Forest|



## _D. Statistical Testing and Predictive Modeling_ 

After deriving textual sentiment through transformer-based NLP inference, statistical and machine learning models were used as secondary explanatory tools to examine factors associated with rating–text mismatch. _Incongruent_ was used as the binary outcome variable, while variables used to define it were excluded from the predictors to avoid data leakage. The final predictor set included venue type, province, reviewer tier, review length, review delay, and travel year terms, with low multicollinearity (max VIF = 3 _._ 663). 

Table III summarizes the modeling and interpretation framework used in this phase. Chi-square and Mann–Whitney U tests were used for bivariate analysis, with Benjamini–Hochberg correction applied for multiple testing. Logistic regression and logit models were used to examine linear effects and adjusted odds ratios, while Random Forest was used to assess nonlinear relationships. SHAP was used only as a post hoc interpretation layer for the Random Forest model, supporting the explanation of NLP-derived incongruence rather than replacing the main sentiment analysis framework [12]. Model performance was evaluated using AUC-ROC. 

## IV. RESULTS 

## _A. Prevalence and Six-Pattern Typology_ 

Each incongruence type reflects a directional mismatch between rating and sentiment polarity. The pattern names, as shown in Fig 2, are original to this study, derived from the behavioral characteristic each mismatch most plausibly reflects. 

Among the reviews analyzed, 3,005 were identified as incongruent, giving an overall prevalence of 18.6%, or roughly 



<!-- Start of picture text -->
Rating given as Stars<br>Positive Neutral Negative<br>Conservative Punitive<br>Rater Rater<br>38.4% 3.7%<br>Obligatory Harsh<br>5-Star Deflator<br>28.3% 5.3%<br>Polite Frustrated<br>Inflator Neutral<br>7.3% 16.9%<br>Positive<br>Neutral<br>Sentiment Expressed in Text<br>Negative<br><!-- End of picture text -->

Fig. 2. Distribution of the six directional incongruence patterns. 

one in five reviews. Fig. 2 further shows that incongruence follows a six-pattern typology. The two most common patterns, Conservative Rater (38.4%) and Obligatory 5-Star (28.3%), together account for 66.7% of all incongruent reviews. This indicates that rating–text mismatch is directionally structured rather than random. In addition, Frustrated Neutral and Polite Inflator account for a further 24.2% of incongruent cases, showing that negative sentiment is often paired with nonnegative ratings. This directional structure suggests that ratingderived labels introduce systematic rather than random noise into sentiment analysis tasks. The concentration of mismatches in a few recurring patterns also makes the typology useful for interpreting how numerical ratings and written sentiment diverge in review-mining datasets. 

## _B. Variation Across Venue Types_ 

Incongruence rates were compared across 11 attraction categories to assess contextual variation. The Chi-square test showed a statistically significant association between venue type and incongruence, with a small but meaningful effect size ( _χ_<sup>2</sup> (10) = 125 _._ 85, _p <_ 0 _._ 001; Cramer’s V = 0.088). As shown in Fig. 3, National Parks had the lowest incongruence rate (12.8%), whereas Museums had the highest (26.3%). Overall, variation across venue types indicates that rating–text mismatch is not evenly distributed, but differs by review context. 

## _C. Predictors of Incongruence_ 

Bivariate screening with Benjamini–Hochberg correction was used to identify predictors associated with incongruence. As shown in Table IV, reviewer tier, province, travel year, and review length remained significant after correction, while = review delay was not significant ( _q_ 0 _._ 7503). Expert reviewers were 1.97 times more likely than novices to produce incongruent reviews [22]. In addition, incongruent reviews were longer at the median than congruent reviews (296 vs. 279 characters). These findings indicate that both reviewer 



<!-- Start of picture text -->
Museums 26.3%<br>Bodies of Water 23.7%<br>Zoological Gardens 21.6%<br>Religious Sites 19.8%<br>Beaches 19.0%<br>Waterfalls 18.0%<br>Gardens 17.4%<br>Farms 16.6%<br>Nature & Wildlife Areas 16.4%<br>Historic Sites 15.6%<br>National Parks 12.8%<br>0 5 10 15 20 25 30<br>Incongruence Rate (%)<br>Venue Type<br><!-- End of picture text -->

Fig. 3. Incongruence rate by venue type. 

characteristics and review content are associated with sentiment– rating mismatch, although multivariable modeling is needed to test their independent effects. 

Fig. 4 further illustrates the reviewer expertise effect for selected mismatch patterns, showing that Conservative Rater becomes more common among expert reviewers, while Harsh Deflator becomes less common. 

TABLE IV 

BIVARIATE PREDICTOR SCREENING WITH BH-FDR CORRECTION 

|Predictor|Test Statistic|Raw _p_|_q_-value|Retained|
|---|---|---|---|---|
|Reviewer Tier|_χ_<sup>2</sup>(3) = 85_._99|1_._59_×_<br>10<sup>_−_18</sup>|7_._94_×_<br>10<sup>_−_18</sup>|Yes|
|Province|_χ_<sup>2</sup>(7) = 49_._10|2_._17_×_<br>10<sup>_−_8</sup>|3_._62_×_<br>10<sup>_−_8</sup>|Yes|
|Travel Year|Mann–Whitney|7_._73_×_<br>10<sup>_−_11</sup>|1_._93_×_<br>10<sup>_−_10</sup>|Yes|
|Review Length|Mann–Whitney|0.0011|0.0014|Yes|
|Review Delay|Mann–Whitney|0.7503|0.7503|No|



## _D. Model-Based Analysis and Interpretation_ 

1) Model 1A – Logistic Regression: A class-balanced logistic regression model was used as a linear baseline. It achieved a mean cross-validated AUC of 0 _._ 5890 _±_ 0 _._ 0093 and a test AUC of 0.5840, indicating modest but stable predictive performance. This suggests that incongruence is only partly explained by the observed variables. 

2) Model 1B – Explanatory Logit: Used to identify independent predictors of incongruence. Based on 95% confidence intervals, 19 predictors were statistically significant. Venue type, reviewer expertise, review length, and travel year showed important effects, while review delay had only a weak negative association. Overall, the model shows that incongruence is shaped by structural, behavioral, and temporal factors. 

3) Model 2 – Random Forest (Nonlinear Structure Test): Applied to capture nonlinear relationships and interactions. It achieved a test AUC of 0.6095, which was slightly higher than logistic regression. This indicates that nonlinear effects are present, although their contribution is modest. 

4) SHAP Analysis: SHAP was used as a post hoc interpretation layer for the Random Forest model to identify influential features behind NLP-derived incongruence. The results were broadly consistent with the logit model, highlighting review length, reviewer expertise, travel year, review delay, and venue type as influential factors. SHAP therefore supports interpretation of nonlinear patterns rather than replacing the main sentiment analysis framework. 

Temporal effects indicate a modest but consistent decline in sentiment–rating incongruence over time. The linear travel year term shows a significant negative association (Travel_Year_c: OR = 0.946, CI < 1), suggesting that more recent reviews are less likely to be incongruent. In contrast, the quadratic term (Travel_Year_c²: OR = 0.995) is not statistically significant, providing no evidence of nonlinear temporal effects and indicating an approximately linear trend. SHAP analysis further supports this finding, identifying Travel_Year_c as an influential predictor (mean |SHAP| = 0.0219) and confirming the overall direction of the effect. This indicates increasing alignment between textual sentiment and ratings over time. 

## V. DISCUSSION 

## _A. Structured Incongruence_ 

The incongruence rate of 18.6% shows that rating–text mismatch is systematic rather than random. Ratings capture overall judgments, while review text captures more specific details of the visitor experience. For sentiment analysis, a numerical score may compress a complex experience into a single label, while the written review can express mixed or context-dependent sentiment. 

The six-pattern structure further shows that incongruence is directional rather than accidental. _Conservative Rater_ and _Obligatory 5-Star_ patterns dominate the mismatched cases, indicating that reviewers do not simply make random rating errors. For NLP pipelines, this means that star ratings do not function equally across contexts as weak sentiment labels. Using them without validation can introduce systematic label noise into sentiment analysis models. Ratings and textual sentiment therefore capture different dimensions of experience, and treating them as interchangeable signals creates modeling risk [4]. This supports the use of review text as an independent sentiment signal when building or evaluating review-mining systems. It also suggests that rating-based labels should be checked for domain-specific bias before being used for supervised sentiment classification. 

## _B. Conservative Rating Behavior_ 

The Conservative Rater pattern further reinforces structural incongruence. Positive textual sentiment paired with moderate ratings accounts for 38.4% of incongruent reviews, showing that reviewers often temper numerical scores relative to their written sentiment. This pattern rises from 27.4% among novice reviewers to 40.4% among experts, suggesting that rating behavior becomes more calibrated with experience. Experienced reviewers may reserve high ratings for exceptional cases while still expressing positive textual sentiment. For 

NLP, this creates structured label noise when ratings are used as ground-truth sentiment labels, making reviewer expertise important for interpreting rating–text relationships. 

## _C. Location Type as a Structural Moderator of Label Reliability_ 

Location type affects rating–text reliability. Museums are over twice as likely to be incongruent compared with national parks (Adjusted OR = 2.386), with similar patterns for beaches, inland waterbodies, zoological gardens, and waterfalls. This suggests that some attraction types are harder to evaluate using a single numerical score. Museums and cultural sites often involve layered experiences, where visitors may describe positive exhibits, heritage value, or emotional significance while also mentioning issues such as crowding, pricing, accessibility, or facilities. 

These findings indicate that star-rating reliability is contextdependent rather than uniform across all review types. Ratingderived labels may therefore introduce systematic bias when treated as equally reliable sentiment labels across different tourism contexts. For NLP, this supports the need for contextaware sentiment modeling that validates whether rating-derived sentiment and textual sentiment are aligned before using ratings as ground-truth labels. In practical NLP applications, this means that attraction categories may require different levels of label validation before ratings are reused as sentiment labels. 

## _D. Complementary Roles of Linear and Nonlinear Models_ 

The results show that linear and nonlinear models offer complementary insights into sentiment–rating incongruence rather than competing explanations. Logistic regression (AUC = 0 _._ 584) provides a stable and interpretable baseline, identifying 19 significant predictors, while the Random Forest achieves a modest improvement (AUC = 0 _._ 6095), confirming the presence of nonlinear and interaction effects. However, the limited performance gain suggests that these nonlinearities are not dominant. The overall predictive range (AUC _≈_ 0 _._ 58– 0 _._ 61) indicates that incongruence is structured but only partially observable, with substantial variation driven by latent behavioral and contextual factors. Importantly, this moderate predictive performance should not be interpreted as a weakness; rather, it reflects the inherent complexity and subjectivity of human judgment in review behavior, where not all influencing factors are directly measurable. SHAP analysis reinforces this interpretation by showing that variables such as reviewer expertise, review length, and venue type contribute in nonlinear and context-dependent ways, underscoring the need for richer features to further capture the phenomenon. 

A further limitation concerns the reliability and suitability of the underlying sentiment model. Because the selected model (cardiffnlp/twitter-roberta-base-sentiment) is used in a pretrained, off-the-shelf form rather than fine-tuned on tourismdomain text, its predictions are shaped by its original Twitterstyle training distribution; this raises a validity concern, since any systematic bias in how the model interprets sentiment may directly affect whether a given rating-text pair is classified as incongruent, independent of actual reviewer behavior. The 

selected model was originally trained on short-form, Twitterstyle text, whereas tourism reviews are typically longer, more descriptive, and often express mixed or aspect-level sentiment within a single review; this domain mismatch may cause the model to misclassify nuanced or compound sentiment expressions, potentially inflating or deflating the measured incongruence rate. Compounding this concern, model evaluation itself relied on a manually labeled subset of only 1,000 reviews (700 training, 300 test), with model selection performed directly on the test set rather than a separate validation set. Given that the final claims are drawn over the full corpus of 16,156 reviews, this relatively small and unvalidated evaluation basis means that the selected model’s generalization cannot be fully verified. 

Furthermore, the reported incongruence patterns rely on a single sentiment model and a fixed modeling framework (logistic regression, Random Forest, and SHAP); robustness against alternative baselines (e.g., VADER, TextBlob, TF-IDFbased classifiers, or domain-specific review sentiment models) and alternative predictive models (e.g., XGBoost, SVM) was not assessed. Future work should incorporate a larger manually annotated sample with a dedicated validation split, explore domain adaptation or fine-tuning on review-specific corpora, and benchmark against these alternative baselines and modeling approaches to establish whether the observed patterns are robust or specific to the chosen pipeline. 

Additionally, because incongruence is defined purely as a mismatch between rating and model-predicted sentiment, some flagged cases may reflect sentiment model error rather than genuine reviewer behavior. No manual validation of the incongruent subset was performed in this study; a manual audit of a sample of incongruent reviews would help confirm that the identified behavioral patterns reflect actual reviewer tendencies rather than residual classification noise. 

## _E. Review Delay and Reviewer Expertise Effects_ 

Review delay plays limited role in incongruence, showing no significance in bivariate analysis and only a weak negative association (OR = 0.960). In contrast, reviewer expertise is more influential, with experts exhibiting more conservative and fewer harsh rating behaviors, indicating that incongruence is driven more by reviewer behavior than timing. 



<!-- Start of picture text -->
45<br>40.4%<br>40 Novice<br>35 Expert<br>30 27.4%<br>25<br>20<br>15 10.8%<br>10<br>4.2%<br>5<br>0<br>Conservative Rater Harsh Deflator<br>Mismatch Pattern<br>Percentage<br><!-- End of picture text -->

Fig. 4. Selected incongruence patterns by reviewer expertise, showing higher Conservative Rater prevalence and lower Harsh Deflator prevalence among expert reviewers. 

## VI. CONCLUSION 

Sentiment–Rating incongruence in tourism reviews is systematic rather than random. Using transformer-based sentiment inference, this study showed that 18.6% of reviews contain rating–text mismatch forming six directional patterns. The findings show that reviewer expertise, review length, venue type, and temporal factors influence rating–text divergence. More importantly, star ratings and textual sentiment are not interchangeable signals [4]. This distinction is especially important for datasets where ratings are used automatically as training labels. 

For NLP research, the main implication is that star ratings should not be treated as ground-truth sentiment labels without validation. Rating-derived sentiment labels may introduce systematic label noise when the written review expresses a different sentiment polarity from the assigned score. This study therefore supports the need for context-aware sentiment analysis methods that evaluate weak-label reliability before model training or evaluation. This puts the premise and validity of some prior low-resource sentiment analysis work [18, 19] into question. 

## REFERENCES 

analysis with zero-shot learning for hospitality service enhancement,” _Information_ , vol. 15, no. 8, p. 499, Aug. 2024. 

   - [15] H. P. P. M. Abeysinghe and C. K. Walgampaya, “Sentiment analysis in user reviews: A study of incompatibility in hotel reviews in city of anuradhapura, sri lanka,” in _Proceedings of iPURSE_ , vol. 23, Peradeniya, Sri Lanka, Nov. 2021. 

   - [16] P. Abeysinghe and T. Bandara, “A novel self-learning approach to overcome incompatibility on tripadvisor reviews,” _Data Science and Management_ , vol. 5, pp. 1–10, 2022. 

   - [17] N. de Silva, “Survey on Publicly Available Sinhala Natural Language Processing Tools and Research,” _arXiv preprint arXiv:1906.02358v26_ , 2026. 

   - [18] V. Jayawickrama, G. Weeraprameshwara, N. de Silva, and Y. Wijeratne, “Seeking sinhala sentiment: Predicting facebook reactions of sinhala posts,” in _International Conference on Advances in ICT for Emerging Regions_ , 2021, pp. 177–182. 

   - [19] ——, “Facebook for sentiment analysis: Baseline models to predict facebook reactions of sinhala posts,” _The International Journal on Advances in ICT for Emerging Regions_ , vol. 15, no. 2, 2022. 

   - [20] G. Weeraprameshwara, V. Jayawickrama, N. de Silva, and Y. Wijeratne, “Sinhala Sentence Embedding: A Two-Tiered Structure for Low-Resource Languages,” in _Proceedings of the 36th Pacific Asia Conference on Language, Information and Computation_ , 2022, pp. 325–336. 

   - [21] ——, “Sentiment Analysis with Deep Learning Models: A Comparative Study on a Decade of Sinhala Language Facebook Data,” in _2022 The 3rd International Conference on Artificial Intelligence in Electronics Engineering_ . Association for Computing Machinery, 2022, pp. 16–22. 

   - [22] A. Y. K. Chua and S. Banerjee, “Understanding review helpfulness as a function of reviewer reputation, review rating, and review depth,” _Journal of the Association for Information Science and Technology_ , vol. 66, no. 2, pp. 354–362, 2015. 

- [1] B. Pang and L. Lee, “Opinion mining and sentiment analysis,” _Foundations and Trends in Information Retrieval_ , vol. 2, no. 1–2, pp. 1–135, 2008. 

- [2] A. Alaei, S. Becken, and B. Stantic, “Sentiment analysis in tourism: Capitalising on big data,” _Journal of Travel Research_ , vol. 58, no. 2, pp. 175–191, 2019. 

- [3] O. A. George and C. M. Q. Ramos, “Sentiment analysis applied to tourism: exploring tourist-generated content in the case of a wellness tourism destination,” _International Journal of Spa and Wellness_ , vol. 7, no. 2, pp. 139–161, 2024. 

- [4] E. Bigne, C. Ruiz, C. Perez-Cabanero, and A. Cuenca, “Are customer star ratings and sentiments aligned? a deep learning study of the customer service experience in tourism destinations,” _Service Business_ , vol. 17, pp. 281–314, 2023. 

- [5] B. Kwon, J. Lee, J. Min, C. Kwak, and H. B. S. Choi, “Beyond the stars: The impact of rating-text inconsistency on perceived review usefulness,” _Asia Pacific Journal of Information Systems_ , vol. 35, no. 1, pp. 49–72, 2025. 

- [6] A. Ameur, S. Hamdi, and S. B. Yahia, “Sentiment analysis for hotel reviews: A systematic literature review,” _ACM Computing Surveys_ , vol. 56, no. 2, p. Article 51, Sep. 2023. 

- [7] M. Chu, Y. Chen, L. Yang, and J. Wang, “Language interpretation in travel guidance platform: Text mining and sentiment analysis of tripadvisor reviews,” _Frontiers in Psychology_ , Oct. 2022. 

- [8] T. Ali, B. Omar, and K. Soulaimane, “Analyzing tourism reviews using an lda topic-based sentiment analysis approach,” _MethodsX_ , vol. 9, p. 101894, Nov. 2022. 

- [9] J. Devlin, M. W. Chang, K. Lee, and K. Toutanova, “Bert: Pre-training of deep bidirectional transformers for language understanding,” in _NAACL_ , Minneapolis, MN, USA, Jun. 2019, pp. 4171–4186. 

- [10] Y. Sun, S. Wang, Y. Li, S. Feng, X. Chen, H. Zhang, X. Tian, D. Zhu, H. Tian, and H. Wu, “Ernie: Enhanced representation through knowledge integration,” _arXiv preprint arXiv:1904.09223_ , 2019. 

- [11] Y. Wen, Y. Liang, and X. Zhu, “Sentiment analysis of hotel online reviews using the bert model and ernie model—data from china,” _PLOS ONE_ , vol. 18, no. 3, p. e0275382, Mar. 2023. 

- [12] K. Puh and M. B. Babac, “Predicting sentiment and rating of tourist reviews using machine learning,” _Journal of Hospitality and Tourism Insights_ , vol. 6, no. 3, pp. 1188–1204, 2023. 

- [13] T. Sewwandi, “Tourism and travel reviews: Sri lankan destinations,” Mendeley Data, V1, 2023. 

- [14] I. Nawawi, K. F. Ilmawan, M. F. Maarif, and M. Syafrudin, “Exploring tourist experience through online reviews using aspect-based sentiment 

