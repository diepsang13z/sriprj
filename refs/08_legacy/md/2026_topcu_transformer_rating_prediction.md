

**SAKARYA UNIVERSITY JOURNAL OF COMPUTER AND INFORMATION SCIENCES** <u>http://saucis.sakarya.edu.tr/</u> e-ISSN: 2636-8129 Vol. 9, No. Special Issue, 451-464, 2026 <u>DOI: 10.35377/saucis...1748175</u> Publisher : Sakarya University 



**RESEARCH ARTICLE** 

Improving Hotel Review Rating Prediction with Transformer Models **Ayhan Topçu**<sup>**1**</sup> **, Mert Arda Asar**<sup>**1,***</sup> **, Günce Keziban Orman**<sup>**1**</sup> 



1Galatasaray University, Computer Engineering Department, Ortaköy, İstanbul, Türkiye 

Corresponding author: Mert Arda Asar, **ABSTRACT** maasar@gsu.edu.tr Online review platforms have become crucial decision-making tools in the hospitality industry, where automated sentiment analysis and rating prediction offer valuable insights for both businesses and consumers. This study investigates the performance of transformer-based language models for predicting hotel review ratings and examines the impact of oversampling techniques on model accuracy. We introduce a novel dataset of 68,785 English hotel reviews from TripAdvisor (2014-2023) in Turkey. Four transformer models, i.e., BERT, DistilBERT, RoBERTa, and DeBERTa, were systematically compared using multiple perspectives. Results show DeBERTa achieves the highest performance among all evaluated models. Random oversampling (ROS) significantly improved classification performance, with F1-scores increasing from 62% to 81% and accuracy from 76% to over 82% across all models. The oversampling approach effectively addressed class imbalance while preserving semantic information, enabling better distinction between rating categories. Through quantitative and qualitative analysis, including the embedding of visualization and SHAP-based interpretability studies, we demonstrate that Article History: transformer models effectively capture sentiment patterns. However, they remain sensitive to mixed sentiments Received:23.07.2025 and linguistic subtleties. This work contributes a novel dataset, a systematic comparison of four transformer Revised: 24.10.2025 models, and empirical evidence of oversampling effectiveness in sentiment analysis. Accepted: 28.11.2025 Published Online: 01.06.2026 **Keywords:** Sentiment analysis, Transformer models, Rating prediction, Oversampling 

# **1. Introduction** 

Online review platforms have become essential to decision-making processes across various industries in today’s digital world. The hospitality sector, particularly hotel booking platforms, relies heavily on user-generated content [1]. Hotel reviews provide valuable insights into customer experience and significantly influence booking decisions [2]. However, manually analyzing large volumes of user reviews is time-consuming and impractical for real-time applications. Automated sentiment analysis and rating prediction from user reviews have emerged as essential tools for both businesses and consumers to process and understand customer feedback efficiently [3]. These reviews not only influence the perceptions of potential customers but also provide valuable feedback for service providers to improve their offers. However, the vast scale and unstructured nature of these texts present significant challenges for manual interpretation and timely analysis. Automated review analysis techniques allow businesses to systematically extract meaningful patterns from customer feedback and integrate them into their operational strategies [4]. 

Despite the growing interest in this area, several fundamental challenges remain unresolved that complicate the accurate prediction of ratings from textual reviews. First, the inherent subjectivity of user-generated reviews often contains mixed sentiments, ambiguous expressions, or contextual nuances that make straightforward interpretation difficult [5]. Second, the distribution of review ratings is typically imbalanced, with a dominance of high or low scores, leading to biased learning and suboptimal performance in predictive models [6]. Third, the semantic richness and linguistic diversity of user reviews further complicate this task, requiring analytical methods that are both scalable and context sensitive [7]. Finally, ensuring model interpretability and fairness across rating levels remains a concern, particularly when such systems are used in high-stakes decision-making environments. 

Addressing these challenges is essential not only for improving prediction accuracy but also for ensuring that automated systems produce fair and reliable outputs across all rating levels. Beyond the technical implications, more reliable review prediction tools can help highlight systemic service issues and amplify underrepresented perspectives. They also reduce the risk of misleading representations on public platforms. In this regard, improving automated rating prediction is not only a matter of technical performance but also a step toward building more equitable digital services. As the volume 



**Cite as:** A. Topçu, M. A. Asar, and G. K. Orman, “Improving hotel review rating prediction with transformer models”, _Sakarya University Journal of Computer and Information Sciences,_ vol. 9, no. Special Issue, pp. 451-464, 2026. <u>doi: 10.35377/saucis...1748175</u> 

This work is licensed under Creative Commons Attribution-NonCommercial 4.0 International License. 

Ayhan Topçu et al. 

_Sakarya University Journal of Computer and Information Sciences_ 9 (Special Issue) 2026, 451-464 

of online content continues to grow, advancing techniques for understanding and leveraging user reviews will remain a critical area of research, with implications for recommender systems, customer satisfaction monitoring, and business intelligence. 

Review rating prediction and sentiment classification have been extensively studied in the context of hospitality and tourism, where online reviews play a key role in driving consumer decisions. Several studies have explored machine learning and natural language processing methods to predict numerical ratings from user review text. Although some studies utilize traditional machine learning models, such as support vector machines (SVM) [8,9] or tree-based algorithms [10], transformer-based language models have become increasingly popular due to their ability to handle and understand complex sequential structures. Instead of training a transformer model from scratch, adapting previously trained models to our objective task, known as fine-tuning, is the most popular approach [11]. In this way, we not only limit ourselves to our own data, but we also use information from other datasets [12]. In the literature, various pre-trained language models are available for fine-tuning to specific tasks [13]. Yudinda et al. [14] compared the review rating prediction performance of two popular transformer-based language models. They fine-tuned BERT [15] and RoBERTa [16] to classify hotel reviews in Indonesia. Their results showed that BERT outperforms RoBERTa while classifying the unstructured textual data. Yuan [17] also fine-tuned various transformer-based language models and compared their performance in predicting hotel review ratings. They evaluated popular language models, such as BERT, RoBERTa, and DistilBERT [18], as well as traditional approaches, including decision trees, random forests, and logistic regression. They showed that DistilBERT outperformed the other predictive models. Asyaky et al. [19] compared the text classification performance of transformerbased models on social media data. Their findings also suggest that BERT-based models are highly suitable for classifying unstructured text data over traditional methods. Despite the given studies, due to the high computational resources required to fine-tune transformer-based models, using them as a feature extractor without any tuning operation is also a popular alternative approach. Chen et al.[20] combined BERT and XGBoost to improve the review classification performance. They extract review feature vectors using BERT and use XGBoost to classify them. Similarly, Dogra et al. [21] utilized DistilBERT as the textual feature extractor and compared the prediction performance of various models, including logistic regression, decision trees, and random forests. They achieved the highest performance with a combination of DistilBERT and a random forest. 

In addition to processing textual data and learning its proper representation, handling imbalanced data is another significant challenge in NLP applications. The outcome will likely exhibit biased performance when predicting on novel data if the analysis is conducted with imbalanced classes [22]. Sampling techniques represent a widely adopted methodological approach for addressing class distribution imbalances in datasets [23]. They are typically categorized into two main categories: oversampling and undersampling strategies. Oversampling methods aim to increase the representation of minority classes by generating additional samples, while undersampling methods aim to balance class distributions by removing samples from majority classes. Oversampling methods are often preferred over undersampling in text classification because they ensure minority classes are sufficiently represented without discarding valuable data from the majority class [24]. Undersampling methods may lead to a loss of information, particularly when the majority class contains critical nuances that are essential for accuracy [25]. Synthetic Minority Oversampling Technique (SMOTE) [26] is one of the most popular oversampling methods, which generates synthetic samples for the minority class by interpolating between existing minority class samples [27]. However, its application to textual datasets presents several disadvantages. These include issues related to noise propagation, over-generalization, lack of diversity in generated samples, and increased class overlap [28]. On the other hand, sample duplication, also known as random oversampling (ROS), is a more straightforward method that increases the size of the minority classes by duplicating the existing samples [29]. Since textual data relies on both sequential and semantic information, preserving this information is also a crucial aspect [30]. Since synthetic data generation methods, such as SMOTE, struggle to preserve semantic information, ROS is a preferred method for textual data [31]. Sani et al. [32] enhanced the essay scoring task by applying ROS to their imbalanced data. They utilized BERT as the essay classifier and demonstrated the effect of oversampling on text classification success. Rathpisey et al. [33] compared the efficiency of different oversampling techniques on hate speech classification. They applied four popular oversampling methods and observed that all of them enhanced the classification accuracy. Among these oversampling methods, the most successful result was obtained from ROS. 

Despite these advancements, most studies focus solely on accuracy-based evaluations. They overlook model interpretation, fairness, and robustness under real-world conditions. Limited work has examined how oversampling impacts the internal representations of transformer models from multiple perspectives. This gap is particularly evident in hotel review datasets, where class imbalance persists as a significant issue. Furthermore, existing research predominantly analyzes aggregated global datasets. Turkish hotels, representing a major tourism destination with distinct characteristics, remain underexplored in transformer-based sentiment analysis. To address these gaps, this study investigates both quantitative and qualitative effects of oversampling on review rating prediction. We utilize a unique dataset of English reviews from Turkish hotels, collected over 10 years. Our geographically focused corpus enables region-specific analysis while maintaining linguistic consistency. 

This study contributes to the field of hotel review analysis by (i) introducing a novel dataset of 68,785 Turkish hotel reviews collected from TripAdvisor spanning from 2014 to 2023, which represents a unique and comprehensive resource 

452 

Ayhan Topçu et al. 

_Sakarya University Journal of Computer and Information Sciences_ 9 (Special Issue) 2026, 451-464 

for sentiment analysis research, (ii) providing a systematic comparison of four prominent transformer-based language models (BERT, DistilBERT, RoBERTa, and DeBERTa) on this imbalanced dataset, (iii) demonstrating the significant impact of random oversampling techniques on classification performance across all evaluated models, (iv) conducting comprehensive analysis using multiple evaluation metrics including classification measures and clustering-based assessments. 

In the rest of the article, we first introduce our methodology in Section 2. We then present the details of the experiments and results in Section 3. Afterwards, we discuss the experimental results and conclude the article in Section 4. 

# **2. Methodology** 

This study examines the effect of random oversampling on transformer-based language models for predicting hotel review ratings under conditions of class imbalance. We employ a systematic two-pathway approach to isolate and quantify the effect of oversampling on model performance. Our methodology comprises five primary stages: (1) data collection and exploratory analysis from TripAdvisor, (2) random oversampling to balance minority rating classes, (3) text preprocessing through tokenization and train-test splitting, (4) parallel fine-tuning of four state-of-the-art transformer models (BERT, DistilBERT, RoBERTa, and DeBERTa), and (5) comprehensive evaluation using both quantitative metrics (accuracy, F1score, ROC-AUC) and qualitative analysis (SHAP, PCA visualization, silhouette scores). Figure 1 presents the complete workflow, illustrating both the oversampled (blue arrows) and non-oversampled (orange arrows) processing pathways that enable direct comparison of the oversampling effect. 



**Figure 1.** Overall workflow of the proposed study. Following data collection and exploratory analysis from TripAdvisor, the dataset branches into two parallel scenarios: (blue arrows) a path with random oversampling to balance minority classes, and (orange arrows) a path without oversampling. Both paths proceed through tokenization (maximum 128 tokens). Preprocessed data are then used to fine-tune four transformer-based language models in parallel. Predictions from each model are subsequently evaluated through quantitative metrics and qualitative analysis to systematically compare the impact of oversampling on model performance across all rating classes. 

# **2.1. Data Collection and Exploratory Analysis** 

We collected hotel review data from TripAdvisor for this study. Our dataset comprises reviews for Turkish hotels from 2014 to the end of 2023, including ratings, titles, and full-text data. Rating values cover integer values between 1, a.k.a the most unpleasant experience, and 5, a.k.a the most pleasant experience. During the data collection phase, we included only the reviews originally written in English. In total, we have 68,785 unique reviews. Table 1 shows the example format of our dataset. 

**Table 1.** Example Format of Hotel Review Dataset 

|**Rating **|**Title**|**Text**|**Date**|
|---|---|---|---|
|5|Good hotel next to the mall|Good location next to the mall and not far from the airport…|Aug 2023|
|3|New hotel with something missing|We had a nice suite with a city view. But many things didn't work…|Aug 2023|
|1|Bad Service, non-cooperative staff|Upon arrival, the FO staff did not process the booking that was…|Aug 2022|



Before the training in predictive modeling, we analyzed some key features of our dataset. First, we examined the distribution of the given ratings. Our dataset exhibits a clearly imbalanced rating distribution, as shown in Figure 2-a. There are significantly more high-rated reviews (4 and 5 stars) than low-rated reviews (3 stars and below). 62% of all reviews are rated 5 stars. This is an important observation to take into account during the evaluation phase. Second, we analyzed the length of the reviews in terms of word count. Figure 2-b presents the distribution of review lengths measured in word counts. The histogram indicates that the majority of reviews are relatively short, with a noticeable peak of around 40-50 words. The median is 58 words, and the mean is 74 words. A secondary peak is observed at approximately 145 words, suggesting that reviewers often conform to certain length patterns, which reveals some common user behaviors. 

453 

Ayhan Topçu et al. 

_Sakarya University Journal of Computer and Information Sciences_ 9 (Special Issue) 2026, 451-464 



**Figure 2.** The Left Figure (a) demonstrates the rating distribution of the Dataset. The Second Figure (b) presents the review length distribution. 

After examining the overall distribution of review lengths, we further analyzed how review length varies between positive and negative reviews. This distinction offers insight into whether user sentiment influences the quantity of written feedback. As illustrated in Figure 3, we separated the reviews into two groups: _negative reviews_ , which are the reviews whose ratings are equal to or lower than  3 stars and are shown in red, and positive reviews, which are the reviews whose ratings are equal to or higher than  4 stars and are shown in green. The figure reveals that positive reviews are not only more frequent but also tend to be slightly shorter, with a concentration around the 40–50 word range. In contrast, negative reviews tend to be longer and show a left-skewed distribution. This suggests that users may write more detailed feedback when expressing dissatisfaction, while positive comments tend to be more concise. Despite this, both distributions exhibit peaks at similar lengths (approximately 150), indicating a common length pattern regardless of sentiment. 



**Figure 3.** Distribution of review lengths by rating groups. Green bars represent positive reviews (≥ 4), while red bars indicate negative reviews (≤ 3) 

s our third analysis, to gain a deeper understanding of the semantic content of the reviews, we visualized the most frequently used words as word clouds for both positive and negative reviews. Figure 4a presents the most common words in positive reviews. The most prominent terms include “great,” “good,” “friendly,” “staff,” “clean,” and “walking distance,” which suggest that satisfied customers frequently praised the staff, cleanliness, and location of the hotels. In contrast, Figure 4-b illustrates the word cloud for negative reviews. The dominant words in this group, such as “room,” “breakfast,” “dirty,” “small,” and “staff,” indicate recurring issues and points of dissatisfaction. Notably, while some words, such as “room” and “staff,” appear in both clouds, their surrounding context likely differs, reflecting either praise or criticism depending on the sentiment. 



**Figure 4.** Word clouds for positive and negative reviews. Left subfigure (a) displays the most frequent words in positive reviews (ratings ≥ 4), shown in green. Right subfigure (b) shows the word cloud for negative reviews (ratings ≤ 3), visualized in red. Word size indicates the frequency of occurrence 

454 

Ayhan Topçu et al. 

_Sakarya University Journal of Computer and Information Sciences_ 9 (Special Issue) 2026, 451-464 

# **2.2. Transformer-based Language Models** 

Compared to traditional natural language processing methods, transformer-based models demonstrate significantly greater capability in understanding and processing long texts. One of the primary advantages of these models lies in their ability to capture contextual relationships between words over extended sequences, which is often a challenge for conventional approaches such as bag-of-words or n-gram models. Furthermore, transformer architecture does not require extensive preprocessing steps such as stopword removal or stemming/lemmatization. This eliminates the potential for error propagation introduced by these preprocessing techniques, which are often heuristic and can inadvertently discard semantically important information. In contrast, models that depend heavily on such preprocessing steps typically require more careful tuning and are more susceptible to performance fluctuations due to variations in the quality of preprocessing. For all these reasons, our study focuses on evaluating and comparing the following transformer-based language models: 

BERT [15] is one of the pioneering transformer-based models introduced by Devlin et al. in 2018, which significantly advanced the state-of-the-art in a variety of NLP tasks. Unlike traditional left-to-right or right-to-left language models, BERT employs a bidirectional training approach, jointly conditioning on both left and right contexts in all layers. This allows the model to develop a deeper understanding of language context and semantics. In the context of our study, BERT serves as a strong baseline due to its robust contextual encoding capabilities, which are particularly beneficial for tasks involving longer or more complex textual inputs. 

DistilBERT [18] is a smaller, faster, and more efficient variant of BERT, introduced by Sanh et al. in 2019 through the technique of knowledge distillation. It retains much of BERT’s language understanding capability while significantly reducing the number of parameters and computational requirements. 

RoBERTa [16] is an enhanced variant of BERT, introduced by Liu et al. in 2019, which modifies key aspects of BERT’s pretraining strategy to improve performance across a broad range of natural language understanding tasks. While RoBERTa maintains the same underlying transformer encoder architecture as BERT, it diverges significantly in terms of training methodology. 

DeBERTa [34], introduced by He et al. in 2021, is a transformer-based language model that builds upon and improves the BERT architecture by introducing two key innovations: _disentangled attention_ and _enhanced positional encoding_ . These modifications enable DeBERTa to model language more accurately, particularly in contexts that require a fine-grained understanding of token interactions. 

# **2.3. Tokenization** 

The process of dividing texts into smaller units is called tokenization, and the component that performs this process is referred to as a tokenizer [35]. In this paper, we use the default pretrained tokenizers associated with each transformer model to ensure compatibility with their respective vocabularies and training configurations. Specifically, BERT and DistilBERT use the WordPiece tokenizer [36], while RoBERTa and DeBERTa rely on a Byte-Pair Encoding (BPE) tokenizer [37]. These tokenizers convert text into subword units, enabling the models to handle rare or unseen words effectively. They also automatically add special tokens and apply truncation or padding to standardize input lengths across samples. 

Each tokenization process requires a pre-determined maximum token size. If the input text exceeds this limit, the tokenizer truncates the excess tokens from the end to fit within the allowed length. This constraint ensures uniform input dimensions for batch processing and model compatibility, but may lead to the loss of potentially informative content in longer texts. On the other hand, shorter texts are padded with special tokens to match the required length. A high token size is related to computational inefficiency and increased resource consumption [38]. The need to handle large token sizes often results in increased memory usage and longer training times. It is essential to select an optimal token size that captures key information without truncating the text excessively, while also ensuring efficient memory usage. 

# **2.4. Oversampling of the Imbalanced Dataset** 

We selected random oversampling over synthetic generation methods, such as SMOTE. The main reason for our choice is that hotel reviews contain highly contextual sentiment expressions where the relationships between words and their sequence are crucial for rating prediction. Synthetic interpolation methods risk generating semantically inconsistent samples that could confuse transformer models during training. Random oversampling helps models learn from real user reviews while fixing the class imbalance problem. Specifically, we duplicated the samples from the minority classes in our dataset. Since a large part of our dataset consists of positive reviews, we have increased the number of negative reviews. We oversampled the user reviews, which have ratings between 1 and 3, and set their final counts as 12,000 for each. Figure 5 presents the final obtained distributions of our ratings (Fig. a) and review lengths (Fig. b). The balance between negative and positive review distributions improved compared to the original dataset, which is shown in Figure 1. We maintained the number of reviews for both 4- and 5-star samples at 13,298 and 42,809, respectively. 

455 

Ayhan Topçu et al. 

_Sakarya University Journal of Computer and Information Sciences_ 9 (Special Issue) 2026, 451-464 



**Figure 5.** Rating (Figure a) and review length (Figure b) distributions of the oversampled dataset 

# **2.5. Dimension Reduction** 

Transformer-based language models generate high-dimensional embedding vectors for each review, capturing rich semantic and contextual information. While these embeddings are effective for downstream classification tasks, their high dimensionality makes direct interpretation and structural analysis difficult. To address this, we incorporated a dimensionality reduction step to understand better and visualize how well the learned representations capture class-specific information in a more interpretable space. To this end, we employed Principal Component Analysis (PCA). This widely used linear dimensionality reduction technique projects high-dimensional data onto a lower-dimensional subspace while preserving the directions of maximum variance. PCA identifies orthogonal axes, referred to as principal components, that capture the most informative directions in the data. By projecting the embeddings onto the first two principal components, we obtained a two-dimensional latent space that facilitates visualization and enables further evaluation of structural properties such as class separation. 

To quantify how well the reduced representations reflect meaningful clustering aligned with rating classes, we used the _Silhouette Score_ . The silhouette score _s_ ( _i_ ) for a sample _i_ is computed as: 



where is the average distance between sample iii and all other points in the same class, and is the average distance between sample iii and the nearest neighboring class. 

The silhouette score ranges from -1 to 1, where a value close to 1 indicates that the sample is well-clustered, while values near 0 suggest overlapping clusters, and negative values imply potential misclassification. 

By combining PCA with silhouette analysis, we systematically assessed the extent to which the models learn distinguishable latent structures for each rating category, independent of classification accuracy. This step not only aids in interpreting the internal representations but also supports a more holistic evaluation of model performance. 

# **2.6. Evaluation Metrics** 

In this study, we focus on a multi-class classification problem. Evaluating model performance in such settings, particularly when class distributions are highly imbalanced, as is the case with our dataset, requires careful selection of metrics. Relying on a single performance metric is often insufficient, as it may fail to capture important aspects of the model’s behaviour across all classes. Therefore, we employ three complementary evaluation metrics, each offering a different perspective on model performance. 

Specifically, we report Accuracy and F1-score, both derived from the confusion matrix (see Table 2), to capture overall correctness and the balance between precision and recall. Additionally, we include the ROC-AUC score, which evaluates the model’s ability to distinguish between positive and negative instances. Although originally defined for binary classification, ROC-AUC can be extended to the multi-class setting using one-vs-rest or one-vs-one strategies. Lastly, we incorporate the Silhouette Score, a clustering-based metric that quantifies how well-separated the predicted classes are in the embedding space. This allows us to evaluate not only classification correctness but also the structural separability of the model’s learned representations. 

456 

Ayhan Topçu et al. 

_Sakarya University Journal of Computer and Information Sciences_ 9 (Special Issue) 2026, 451-464 

**Table 2.** Confusion Matrix Format Including Precision and Recall Equations 

|||**Predicte**<br>0|**d Class**<br>1|
|---|---|---|---|
||0|True Negatives (TN)|False Positives (FP)|
||1|False Negatives (FN)|True Positives (TP)|
|**Actual Class**||||



Each metric is briefly explained below: 

**Accuracy** measures the proportion of correctly predicted instances among all samples. While commonly used, accuracy can be misleading in imbalanced datasets, as it may be dominated by the majority classes. It is calculated using the following equation: 



**F1-score** is the harmonic mean of precision and recall, two fundamental metrics that evaluate the quality of positive predictions. While precision measures the proportion of predicted positive instances that are actually correct, recall measures the proportion of actual positive instances that the model correctly identifies. The F1-score balances these two and is especially valuable when there is a trade-off between them, as is often the case in imbalanced classification tasks. In multi-class settings, the F1-score must be computed separately for each class, treating each class as the “positive” class in a one-vs-rest manner. These per-class F1-scores are then aggregated using an averaging strategy. In our study, we employ macro averaging, which assigns equal weight to each class, regardless of its frequency of occurrence in the dataset. This is particularly important in imbalanced scenarios, where the majority classes might otherwise dominate the overall performance metric. The macro F1 score is calculated as follows: 



Where is the F1 score for class , and  macro F1 is the average of all F1 scores for each class as given below: 



Where K denotes the total number of classes in the classification task. 

**Area Under the Curve (ROC-AUC)** score quantifies the model’s ability to distinguish between classes. The ROC curve plots the true positive rate (also known as recall) against the false positive rate across various classification thresholds. The AUC represents the probability that the classifier ranks a randomly chosen positive instance higher than a randomly chosen negative one. An AUC score of 1.0 indicates perfect discrimination, while a score of 0.5 suggests no discriminative ability, equivalent to random guessing. In multi-class classification settings, we compute the AUC in a one-vs-rest manner for each class and aggregate the results using macro-averaging, ensuring equal contribution from each class regardless of its frequency in the dataset. This approach provides a fair assessment of the model’s performance, particularly in cases of class imbalance. 

# **3. Experiments and Results** 

This section presents the experimental setup, training procedures, and comprehensive evaluation of our proposed approach. We first describe the experimental configuration and model training details, followed by a quantitative analysis of classification performance on both original and oversampled datasets. Finally, we provide a qualitative analysis to gain a deeper understanding of the model’s behavior and prediction patterns. 

# **3.1. Experimental Setup and Model Training** 

All experiments were conducted on a system equipped with an NVIDIA RTX 3060 Ti GPU. We split the dataset into train and test sets following an 80-20 ratio. We set the batch size to 16, the optimizer to AdamW, and the learning rate to 5e-5 for each fine-tuning operation. There are 55,028 unique samples in the training set and 13,757 unique samples in 

457 

Ayhan Topçu et al. 

_Sakarya University Journal of Computer and Information Sciences_ 9 (Special Issue) 2026, 451-464 

the test set. We perform this splitting operation while preserving the class distribution in the original dataset.  We set the maximum token size of models as 128, which allows us to cover 95% of the reviews. The longer reviews are trimmed to fit the determined token size. We stopped training at the end of the two epochs for each language model. We calculated the training time for each language model to facilitate an efficiency comparison. We selected BERT as the baseline model since all other models evaluated in this study are variations or enhancements of the original BERT architecture. Figure 6 presents the fine-tuning times of our selected language models on the original dataset. DistilBERT runs almost twice as fast, while DeBERTa completes training one-third slower. RoBERTa has the same training time as BERT. We observed the same pattern when we trained the same models on the oversampled dataset. 



**Figure 6.** Models’ training time comparison in seconds on the original dataset 

# **3.2. Quantitative Analysis** 

We give the accuracy, F1, and ROC-AUC scores in Table 3. DeBERTa achieves the highest scores across all metrics, while RoBERTa comes in second. The performance difference between DeBERTa and RoBERTa is relatively minor, suggesting that both models offer robust contextual understanding for this classification task. However, when training efficiency is also considered, the trade-off between performance and computational cost becomes more apparent. While DeBERTa yields the best predictive performance, it also has the longest training time. In contrast, RoBERTa, despite delivering nearly equivalent performance, completes training significantly faster than DeBERTa. This observation highlights RoBERTa as a potentially more practical choice in scenarios where computational efficiency is a concern. DistilBERT, designed for efficiency, achieves slightly lower classification performance, but there is still not much significant difference. Although it underperforms compared to the other models, its lightweight architecture makes it suitable for deployment in resourceconstrained environments without sacrificing too much performance. 

**Table 3.** Accuracy, F1, and ROC-AUC scores on the original test sets. Bold scores are the best scores, while underlined scores are the second-best. 

|**Model**|**Accuracy**|**F1-Macro**|**ROC-AUC**|
|---|---|---|---|
|DistilBERT|0.7609|0.6043|0.9783|
|BERT|0.7619|0.6042|0.9799|
|RoBERTa|0.7674|0.6114|0.9805|
|DeBERTa|0.7695|0.6234|0.9814|



We present the detailed classification performance of each language model for individual classes in Figure 7 using confusion matrices. Among the evaluated models, DeBERTa demonstrates better distinction between adjacent classes, especially in mid-scale ratings (e.g., distinguishing between 3-star and 4-star reviews), which aligns with its higher macro F1 score. RoBERTa also shows consistent performance but exhibits slightly more misclassification between neighboring classes than DeBERTa. In contrast, DistilBERT, although efficient, exhibits a noticeable tendency to overpredict the dominant class (5-star), resulting in reduced sensitivity to minority classes. These results suggest that although all models are capable of learning from imbalanced data to some extent, higher-capacity models, such as DeBERTa, are better equipped to capture imbalanced distributions. 

458 

Ayhan Topçu et al. 

_Sakarya University Journal of Computer and Information Sciences_ 9 (Special Issue) 2026, 451-464 



**Figure 7.** Confusion matrices showing the classification performance for each class on the original dataset 

Beyond the common classification metrics, Figure 8 presents a visualization of the learned embeddings for each test sample. We reduced the embedding dimensions to 2 using PCA and calculated their corresponding Silhouette scores. These scores evaluate the structural separability of the classes in the embedding space. Although some classes are more distinguishable than others, we observed that there are lots of overlaps between samples from different classes. These results also suggest that we need to augment our dataset to allow models to learn distinguishable features among different classes. 



**Figure 8.** Visualization of learned embeddings in 2D latent space for the original dataset. Each color represents a different rating class (1-5 stars). Silhouette scores indicate cluster separation quality. 

To assess the impact of oversampling on classification performance, we evaluated the predictions using the previously explained approaches. First, we presented the accuracy, F1-Macro, and ROC-AUC scores of the evaluated language models in Table 4. Although the best-performing model remained unchanged from Table 3, we observed noticeable improvements in model performance. Especially the F1 values, which indicate the model’s ability to balance precision and recall across all classes, showed significant improvements after applying oversampling techniques. The maximum F1 score obtained increased from 62% to 81%, representing a 29% performance improvement. The accuracy scores also showed consistent improvements, with all models achieving over 82% accuracy on the oversampled dataset, compared to approximately 76% on the original imbalanced dataset, resulting in a 7% performance increase. Similarly, ROC-AUC scores increased across all models, indicating enhanced discriminative ability between different rating categories. These substantial improvements can be attributed to several key factors. First, the balanced training data allows transformer models to develop more robust attention mechanisms across all rating categories. In the original imbalanced dataset, the models’ self-attention layers were predominantly exposed to positive review patterns (4-5 stars), resulting in biased internal representations that favored the majority class features. After oversampling, the models can learn distinct linguistic 

459 

Ayhan Topçu et al. 

_Sakarya University Journal of Computer and Information Sciences_ 9 (Special Issue) 2026, 451-464 

patterns for each rating level. Then, the improved F1-macro scores (from 62% to 81%) indicate that oversampling particularly enhanced the models’ ability to recognize the boundaries of the minority class. This is crucial for hotel review analysis, where distinguishing between “disappointing” (2-star) and “adequate” (3-star) experiences requires a nuanced understanding of sentiment gradations that can only be learned with sufficient exposure to each class. 

**Table 4.** Accuracy, F1, and ROC-AUC scores on the oversampled sets. Bold scores are the best scores, while underlined scores are the second-best. 

|**Model**|**Accuracy**|**F1-Macro**|**ROC-AUC**|
|---|---|---|---|
|DistilBERT|0.8390|0.8106|0.9924|
|BERT|0.8219|0.7836|0.9904|
|RoBERTa|0.8307|0.7943|0.9908|
|DeBERTa|0.8438|0.8141|0.9928|



To visually validate our findings, we represent the actual and predicted values as a heatmap in Figure 9. The confusion matrices reveal that oversampling significantly improves the models’ ability to classify minority classes compared to the original imbalanced dataset. All models demonstrate strong performance on the diagonal elements, indicating accurate predictions across all rating categories. Notably, DeBERTa shows the most balanced performance with minimal offdiagonal confusion, particularly excelling in distinguishing between adjacent rating classes. RoBERTa also exhibits robust classification performance with slightly higher confusion between neighboring classes. For all models, although there is still some confusion between the neighbor classes, they clearly distinguish between positive and negative reviews better than the previous experiment, which we fine-tuned on a non-oversampled dataset. 



**Figure 9.** Confusion matrices showing the classification performance for each class on the oversampled dataset 

To further evaluate the structural separability of the learned representations, Figure 10 presents a visualization of the learned embeddings in a 2D latent space using PCA, along with their corresponding Silhouette scores for the oversampled dataset. DistilBERT achieves the highest Silhouette score of 0.433 (previous was 0.286), followed by DeBERTa (0.427 from 0.282), BERT (0.416 from 0.281), and RoBERTa (0.397 from 0.269). Given that a higher score indicates better learning of class distinctions, each model learned the semantic differences between classes and separated them better thanks to the oversampling approach. 

460 

Ayhan Topçu et al. 

_Sakarya University Journal of Computer and Information Sciences_ 9 (Special Issue) 2026, 451-464 



**Figure 10.** Visualization of learned embeddings in 2D latent space for the oversampled dataset. Each color represents a different rating class (1-5 stars). Silhouette scores indicate cluster separation quality. 

# **3.3. Qualitative Analysis** 

To supplement the numerical evaluation of model performance, we conducted a qualitative analysis to gain a deeper understanding of the behavioral patterns and limitations of the trained models. Specifically, we investigated how the models interpret review content, what kinds of linguistic cues influence their predictions, and in which cases prediction errors are most likely to occur. This analysis provides a more intuitive understanding of model decisions, especially in edge cases where the predicted and actual ratings diverge. 

We began by selecting a sample of test reviews and comparing the predicted ratings to the ground truth. For each example, we manually examined the linguistic tone, sentiment cues, and specific keywords that might influence the model’s classification. In most consistent predictions, there was a strong alignment between textual sentiment and the star rating. Highly positive reviews, characterized by words like “amazing,” “spotless,” or “great service,” were predicted as 5-star reviews with high confidence. Likewise, reviews containing terms such as _“filthy,” “rude,”_ or _“unacceptable”_ were correctly classified as 1- or 2-star. However, misclassifications often occurred in ambiguous reviews—those that contained both positive and negative sentiment or used indirect language. For instance, one review stated: _“The location was convenient, and the room was clean, but the breakfast was a disappointment.”_ The actual rating was 3 stars, while some models predicted 2 or 4 stars, reflecting the difficulty in balancing mixed sentiment. These examples highlight that the models sometimes weigh positive and negative phrases differently depending on their position in the sentence and contextual strength. 

To deepen our understanding, we employed SHAP analysis to identify the most influential tokens that contribute to the model’s decisions. For example, in the review _“The hotel room was clean and spacious, but the staff was extremely rude and unhelpful,”_ the model focused heavily on the negative terms _“rude”_ and _“unhelpful,”_ which led it to predict a low rating despite the initially positive tone. This attention alignment confirms that the model captures key sentiment transitions indicated by contrastive connectors, such as “ _but.”_ 

We also examined cases of rating-text inconsistency, which are instances where the textual content suggested a different sentiment polarity than the assigned rating. In one example, a review filled with superlatives such as “ _exceeded expectations,_ ” “ _perfect experience,_ ” and “ _highly recommend_ ” was associated with a 2-star rating, a mismatch likely due to user error or sarcasm. Conversely, another review, which contained multiple complaints, ended with an unexpectedly high rating of 5 stars. These outliers underscore the value of model predictions as a secondary verification tool for identifying potentially anomalous reviews on user-generated content platforms. 

The qualitative improvements after oversampling are particularly evident in boundary cases. For instance, reviews with mixed sentiment, such as “The room was clean, but service was disappointing,” were more accurately classified as 3-star after oversampling. In contrast, the original imbalanced models tended to either over-penalize (predicting 1-2 stars) or under-penalize (predicting 4-5 stars) such nuanced expressions. This suggests that balanced training enables models to learn more sophisticated sentiment calibration, recognizing that moderate ratings often correspond to reviews containing both positive and negative elements. 

Overall, our qualitative analysis underscores the effectiveness of transformer models in capturing sentiment and aligning it with star ratings. Nonetheless, they remain sensitive to sentiment ambiguity and linguistic subtleties. 

461 

Ayhan Topçu et al. 

_Sakarya University Journal of Computer and Information Sciences_ 9 (Special Issue) 2026, 451-464 

# **4. Discussion and Conclusion** 

This study presents a comprehensive evaluation of transformer-based language models for predicting hotel review ratings under class imbalance conditions. By fine-tuning four prominent models (BERT, DistilBERT, RoBERTa, and DeBERTa) on a large-scale Turkish hotel review dataset, we demonstrate that oversampling strategies such as Random Oversampling (ROS) significantly enhance classification performance, particularly in terms of macro-averaged F1 and ROC-AUC scores. Among the evaluated models, DeBERTa achieved the highest overall performance, which can be attributed to its disentangled attention mechanism that separately encodes content and positional information, enabling better capture of nuanced sentiment-aspect relationships critical for distinguishing adjacent rating classes. Specifically, DeBERTa more effectively models the dependencies between sentiment-bearing tokens (e.g., “disappointing,” “excellent”) and aspect mentions (e.g., “breakfast,” “location”), which frequently appear at varying distances within review texts. This architectural advantage becomes particularly evident in our confusion matrices, where DeBERTa demonstrated superior performance in disambiguating mid-range ratings that often contain mixed sentiments distributed across multiple aspects. However, RoBERTa offered a compelling balance between efficiency and accuracy, making it a strong candidate for practical applications. 

Beyond numerical metrics, qualitative findings revealed that transformer models can effectively capture sentiment cues and shifts in context. However, misclassifications still occurred in ambiguous reviews or in cases where ratings conflicted with textual sentiment. These inconsistencies may stem from user error, sarcasm, fraud, or single-factor ratings, suggesting that models could serve as tools for anomaly detection by platform moderators. Additionally, visualizations of the learned latent representations showed improved cluster separability after oversampling, confirming that class balance influences not only prediction accuracy but also the underlying embedding space. 

In addition to our findings, several important limitations must be acknowledged: our reliance on English-only reviews from TripAdvisor limits the generalizability of our results across languages, cultures, and platforms. Sentiment expression varies significantly across linguistic and cultural contexts, and these findings should be validated across multiple languages. Ethical considerations are also critical. Automated rating prediction could be misused for ranking manipulation or review fraud. This requires transparent safeguards and fairness audits to prevent disproportionate impacts on certain demographics or establishments. 

In conclusion, this work highlights the necessity of handling class imbalance in review classification tasks and validates the utility of oversampling in transformer-based approaches. The proposed framework and findings can support future developments in automated review analysis systems, especially in hospitality platforms where textual feedback plays a crucial role in user decision-making. Future studies should prioritize multilingual validation to assess the transferability of models across diverse linguistic and cultural contexts. Robust frameworks for detecting rating-text conflicts could help identify potential fraud or user error. Finally, examining fairness and bias in deployment is essential to ensure equitable treatment across different demographic groups and establishment types. 

# **Article Information Form** 

**Authors Contributions:** Ayhan Topçu contributed to this article by conducting the experiments. Günce Keziban Orman and Mert Arda Asar were responsible for conducting the literature review and writing the article. 

**Conflict of Interest Notice:** The authors declare that there is no conflict of interest regarding the publication of this paper. 

**Ethical Approval:** This article contains no data or other information from studies or experiments involving human or animal subjects. 

**Availability of Data and Material:** Not applicable / or link 

**Plagiarism Statement:** This article has been scanned by iThenticate ™. 

# **References** 

- [1]  O. Ciftci, K. Berezina, M. Cavusoglu, and C. Cobanoglu, “Winning the battle: The importance of price and online reviews for hotel selection,” _Adv. Hospitality Tourism Res._ , vol. 8, no. 1, pp. 177–202, Jun. 2020, doi: 10.30519/ ahtr.528150. 

- [2]  M. Suwal, P. Neupane, and G. D. Pant, “Online review on hotel booking decision: Consumer view,” _Int. J. Atharva_ , vol. 3, no. 1, pp. 133–150, Mar. 2025, doi: 10.3126/ija.v3i1.76724. 

- [3]  P. S. Ghatora, S. E. Hosseini, S. Pervez, M. J. Iqbal, and N. Shaukat, “Sentiment analysis of product reviews using machine learning and pre-trained LLM,” _Big Data Cogn. Comput._ , vol. 8, no. 12, Art. no. 199, Dec. 2024, doi: 10.3390/bdcc8120199. 

- [4]  N. Malik and M. Bilal, “Natural language processing for analyzing online customer reviews: A survey, taxo- 

462 

Ayhan Topçu et al. 

_Sakarya University Journal of Computer and Information Sciences_ 9 (Special Issue) 2026, 451-464 

nomy, and open research challenges,” _PeerJ Comput. Sci._ , vol. 10, Art. no. e2203, Aug. 2024, doi: 10.20944/preprints202312.2210.v1. 

- [5]  J. Hartmann, M. Heitmann, C. Siebert, and C. Schamp, “More than a feeling: Accuracy and application of sentiment analysis,” _Int. J. Res. Marketing_ , vol. 40, no. 1, pp. 75–87, Mar. 2023, doi: 10.1016/j.ijresmar.2022.05.005. 

- [6]  R. Obiedat _et al_ ., “Sentiment analysis of customers’ reviews using a hybrid evolutionary SVM-based approach in an imbalanced data distribution,” _IEEE Access_ , vol. 10, pp. 22260–22273, Mar. 2022, doi: 10.1109/ACCESS.2022.3149482. 

- [7]  W. Zhou, Y. Wang, Y. Qu, and L. Li, “Automating app review classification based on extended semantic,” in _Proc. 9th Int. Conf. Dependable Syst. Appl. (DSA)_ , Aug. 2022, pp. 106–115, doi: 10.1109/DSA56465.2022.00022. 

- [8]  Y. C. A. P. Reddy, S. P. P. Sagar, R. P. Kalyan, and N. S. Charan, “Classification of hotel reviews using machine learning techniques,” in _Proc. 8th Int. Conf. Smart Struct. Syst. (ICSSS)_ , Apr. 2022, pp. 1–5, doi: 10.1109/ ICSSS54381.2022.9782215. 

- [9]  A. R. Simarmata and M. Zakariyah, “Sentiment analysis of hotel reviews using support vector machine,” _Indonesian J. Comput. Sci._ , vol. 12, no. 5, pp. 2603–2614, Nov. 2023, doi: 10.33022/ijcs.v12i5.3405. 

- [10] S. Yordanova and D. Kabakchieva, “Sentiment classification of hotel reviews in social media with decision tree learning,” _Int. J. Comput. Appl._ , vol. 158, no. 5, pp. 1–7, Jan. 2017, doi: 10.5120/ijca2017912806. 

- [11] S. Pratap, A. R. Aranha, D. Kumar, G. Malhotra, A. P. N. Iyer, and S. S. S., “The fine art of fine-tuning: A structured review of advanced LLM fine-tuning techniques,” _Natural Lang. Process. J._ , vol. 11, Art. no. 100144, Jun. 2025, doi: 10.1016/j.nlp.2025.100144. 

- [12] Y. Gui, X. Yan, P. Yin, H. Yang, and J. Cheng, “SPT: Fine-tuning transformer-based language models efficiently with sparsification,” _arXiv preprint arXiv:2312.10365_ , Dec. 2023. 

- [13] H. Wang, J. Li, H. Wu, E. Hovy, and Y. Sun, “Pre-trained language models and their applications,” _Engineering_ , vol. 25, pp. 51–65, Jun. 2023, doi: 10.1016/j.eng.2022.04.024. 

- [14] Y. G. Pramudya and A. Alamsyah, “Hotel reviews classification and review-based recommendation model construction using BERT and RoBERTa,” in _Proc. 6th Int. Conf. Inf. Commun. Technol. (ICOIACT)_ , Nov. 2023, pp. 437–442, doi: 10.1109/ICOIACT59844.2023.10455890. 

- [15] J. Devlin, M.-W. Chang, K. Lee, and K. Toutanova, “BERT: Pre-training of deep bidirectional transformers for language understanding,” in _Proc. Conf. North Amer. Chapter Assoc. Comput. Linguistics: Human Lang. Technol. (NAACL-HLT)_ , Jun. 2019, pp. 4171–4186. 

- [16] Y. Liu _et al_ ., “RoBERTa: A robustly optimized BERT pretraining approach,” _arXiv preprint arXiv:1907.11692_ , Jul. 2019. 

- [17] Y. Yuan, “DistilBERT hotel rating prediction model based on an ensemble learning framework,” in _Proc. 3rd Int. Conf. Electron. Inf. Technol. (EIT)_ , Sep. 2024, pp. 763–769, doi: 10.1109/EIT63098.2024.10762068. 

- [18] V. Sanh, L. Debut, J. Chaumond, and T. Wolf, “DistilBERT, a distilled version of BERT: Smaller, faster, cheaper and lighter,” _arXiv preprint arXiv:1910.01108_ , Oct. 2019. 

- [19] M. S. Asyaky, M. Al-Husaini, and H. H. Lukmana, “Sentiment analysis on short social media texts using DistilBERT,” _J. Comput. Netw. Archit. High Perform. Comput._ , vol. 7, no. 2, pp. 524–533, May 2025, doi: 10.47709/ cnahpc.v7i2.5836. 

- [20] M. Chen, H. Xu, Y. Wu, and J. Wu, “Sentiment analysis of hotel reviews based on BERT and XGBoost,” in _Proc. 3rd Int. Conf. Comput. Technol. (ICCTech)_ , Feb. 2024, pp. 11–15, doi: 10.1109/ICCTech61708.2024.00011. 

- [21] V. Dogra, S. Verma, A. Singh, Kavita, M. N. Talib, and M. Humayun, “Banking news-events representation and classification with a novel hybrid model using DistilBERT and rule-based features,” _Turkish J. Comput. Math. Educ._ , vol. 12, no. 10, pp. 3039–3054, Apr. 2021. 

463 

Ayhan Topçu et al. 

_Sakarya University Journal of Computer and Information Sciences_ 9 (Special Issue) 2026, 451-464 

- [22] A. P. Ratnasari and R. Nur’aini, “Performance of random oversampling, random undersampling, and SMOTE-NC methods in handling imbalanced class in classification models,” _Int. J. Sci. Res. Manag._ , vol. 12, no. 04, pp. 494–501, Apr. 2024, doi: 10.18535/ijsrm/v12i04.m03. 

- [23] R. Mohammed, J. Rawashdeh, and M. Abdullah, “Machine learning with oversampling and undersampling techniques: Overview study and experimental results,” in _Proc. 11th Int. Conf. Inf. Commun. Syst. (ICICS)_ , Apr. 2020, pp. 243–248, doi: 10.1109/ICICS49469.2020.239556. 

- [24] M. M. Ahsan, M. S. Ali, and Z. Siddique, “Enhancing and improving the performance of imbalanced class data using novel GBO and SSG: A comparative analysis,” _Neural Netw._ , vol. 173, Art. no. 106157, May 2024, doi: 10.1016/j. neunet.2024.106157. 

- [25] S. García and F. Herrera, “Evolutionary undersampling for classification with imbalanced datasets: Proposals and taxonomy,” _Evol. Comput._ , vol. 17, no. 3, pp. 275–306, Sep. 2009, doi: 10.1162/evco.2009.17.3.275. 

- [26] N. V. Chawla, K. W. Bowyer, L. O. Hall, and W. P. Kegelmeyer, “SMOTE: Synthetic minority over-sampling technique,” _J. Artif. Intell. Res._ , vol. 16, pp. 321–357, Jun. 2002, doi: 10.1613/jair.953. 

- [27] M. Mujahid _et al_ ., “Data oversampling and imbalanced datasets: An investigation of performance for machine learning and feature engineering,” _J. Big Data_ , vol. 11, Art. no. 87, Jun. 2024, doi: 10.1186/s40537-024-00943-4. 

- [28] M. Goyal and Q. H. Mahmoud, “A systematic review of synthetic data generation techniques using generative AI,” _Electronics_ , vol. 13, no. 17, Art. no. 3509, Sep. 2024, doi: 10.3390/electronics13173509. 

- [29] A. P. Ratnasari and R. Nur’aini, “Performance of random oversampling, random undersampling, and SMOTE-NC methods in handling imbalanced class in classification models,” _Int. J. Sci. Res. Manag._ , vol. 12, no. 04, pp. 494–501, Apr. 2024, doi: 10.18535/ijsrm/v12i04.m03. 

- [30] Z. Zhang, Z. Li, J. Zhu, Z. Guo, B. Shi, and B. Hu, “Enhancing user sequence representation with cross-view collaborative learning for depression detection on Sina Weibo,” _Knowl.-Based Syst._ , vol. 293, Art. no. 111650, Jun. 2024, doi: 10.1016/j.knosys.2024.111650. 

- [31] A. A. Khan, O. Chaudhari, and R. Chandra, “A review of ensemble learning and data augmentation models for class imbalanced problems: Combination, implementation and evaluation,” _Expert Syst. Appl._ , vol. 244, Art. no. 122778, Jun. 2024, doi: 10.1016/j.eswa.2023.122778. 

- [32] D. A. Sani, “A random oversampling and BERT-based model approach for handling imbalanced data in essay answer correction,” _J. Infotel_ , vol. 16, no. 4, pp. 729–739, Dec. 2024, doi: 10.20895/infotel.v16i4.1224. 

- [33] H. Rathpisey and T. B. Adji, “Handling imbalance issue in hate speech classification using sampling-based methods,” in _Proc. 5th Int. Conf. Sci. Inf. Technol. (ICSITech)_ , Oct. 2019, pp. 193–198, doi: 10.1109/ICSITech46713.2019.8987500. 

- [34] C. W. Schmidt _et al_ ., “Tokenization is more than compression,” in _Proc. Conf. Empirical Methods Natural Lang. Process. (EMNLP)_ , Nov. 2024, pp. 678–702. 

- [35] X. Song, A. Salcianu, Y. Song, D. Dopson, and D. Zhou, “Fast WordPiece tokenization,” in _Proc. Conf. Empirical Methods Natural Lang. Process. (EMNLP)_ , Nov. 2021, pp. 2089–2103. 

- [36] L. Kozma and J. Voderholzer, “Theoretical analysis of Byte-Pair Encoding,” _arXiv preprint arXiv:2411.08671_ , Nov. 2024. 

- [37] W. Zhang, W. Wei, W. Wang, L. Jin, and Z. Cao, “Reducing BERT computation by padding removal and curriculum learning,” in _Proc. IEEE Int. Symp. Perform. Anal. Syst. Softw. (ISPASS)_ , Mar. 2021, pp. 90–92, doi: 10.1109/ ISPASS51385.2021.00025. 

464 

