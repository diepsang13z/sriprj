**_Applied Stochastic Models in Business and Industry_** 



**RESEARCH ARTICLE OPEN ACCESS** 

# **How Well Do Ratings Reflect Sentiment? Evidence From a Large Italian Review Corpus** 

Nicolò Biasetton<sup>1</sup> | Riccardo Ricciardi<sup>2</sup> | Luigi Salmaso<sup>1</sup> | Paola Zuccolotto<sup>2</sup> 

> 1Department of Management Engineering, University of Padova, Vicenza, Italy | 2Department of Economics and Management, University of Brescia, Brescia, Italy 

**Correspondence:** Nicolò Biasetton (nicolo.biasetton@unipd.it) 

**Received:** 29 September 2025 | **Revised:** 17 March 2026 | **Accepted:** 24 March 2026 

**Keywords:** ordinal regression | sentiment analysis | star ratings | transformer 

## **ABSTRACT** 

Understanding whether numerical ratings reliably reflect the _sentiment_ expressed in user-generated product reviews is critical for accurate interpretation of online feedback. Although star ratings provide immediate, quantifiable signals to consumers and businesses, they may not fully convey the nuanced sentiment contained in text. Thus, we investigate the relationship between review ratings and underlying sentiment using a large corpus of Italian online product reviews. Since review corpora typically lack explicit sentiment labels, we develop a predictive framework for sentiment. We use a BERT-based encoder (specifically, AlBERTo), fine-tuned on our large, domain-specific corpus, and a multi-task CORAL ordinal regression trained on a sample with multiple human annotations. Finally, we utilize Correspondence Analysis to compare user ratings with the predicted sentiment scores. Our sentiment model shows strong performance on the validation set when evaluated on a five-point ordinal scale, achieving MAE below 0.62 and RMSE below 0.82. The comparison between ratings and sentiment predictions shows that ratings and textual sentiment are generally aligned at extreme and neutral points, but notable discrepancies exist for mid-scale evaluations, where ratings often fail to capture underlying textual nuances. 

## **1 | Introduction** 

Online product reviews have become an indispensable resource—especially in e-commerce platforms—for consumers evaluating products and services before making purchase decisions. These reviews typically consist of two components: a rating score or a star rating, usually on a scale of 1 to 5 stars, and a textual review. Numerical ratings or star ratings offer a concise, easily digestible summary of consumer sentiment, frequently serving as a primary signal for perceived product quality and significantly influencing purchasing decisions [1–3]. They are 

commonly regarded as a direct indicator of _sentiment orientation_ or _polarity_ [4, 5]. 

However, the efficacy of these rating scores in truly representing the complex and subjective nature of user perception and opinion is a critical area of inquiry. Traditional rating systems, while convenient, frequently fall short in capturing the nuanced and subjective experiences of users. This creates a fundamental challenge where ratings, despite their widespread reliance, inherently struggle to encapsulate the full spectrum of user sentiment actually conveyed into the textual review. This limitation 

> This is an open access article under the terms of the Creative Commons Attribution License, which permits use, distribution and reproduction in any medium, provided the original work is properly cited. 

> © 2026 The Author(s). _Applied Stochastic Models in Business and Industry_ published by John Wiley & Sons Ltd. 

1 of 14 

_Applied Stochastic Models in Business and Industry_ , 2026; 42:e70090 https://doi.org/10.1002/asmb.70090 

suggests that relying exclusively on a numerical rating can lead to an incomplete or even misleading understanding of consumer sentiment [6]. 

Users may express dissatisfaction in text but still assign a high rating, or vice versa, resulting in directional inconsistencies between score and sentiment [7]. Additionally, the degree of sentiment intensity in the text may not align with the star rating score, reflecting degree inconsistency [1]. These mismatches suggest that ratings, while useful at a glance, can represent incomplete indicators of true user sentiment. 

In contrast, textual reviews offer rich, contextual narratives that highlight specific product strengths, weaknesses, and user expectations. They help other consumers assess product fit and reduce uncertainty in the purchase of a product. However, extracting insights from text at scale requires computational tools—leading to the growing use of _Sentiment Analysis_ (SA). 

Despite their close relationship, ratings and sentiment are still too often studied separately. The goal of the present work is to evaluate whether the user-provided rating attached to a review can be considered a reliable indicator of the sentiment expressed in its textual content. Addressing this question benefits multiple stakeholders: consumers, by clarifying the informational value of ratings; firms, by improving how review signals are interpreted in decision-making; and platforms, by guiding the design of more representative feedback systems. Our contribution is to provide a rigorous, statistically grounded comparison of rating and sentiment using a large corpus of Italian product reviews. By combining (i) a new transformer-based encoder to extract feature from text, (ii) an ordinal regression modeling on a human-annotated corpus, and (iii) a Correspondence Analysis, we directly assess the reliability of ratings as proxies for sentiment. The paper is structured the following way: Section 2 report some insights from the State of the Art concerning ratings limitations and the use of sentiment analysis as a tool to complement ratings, Section 3 present the methodological framework we adopted to assess the relationship between rating and sentiment while Section 4 represent an application of such framework on Made in Italy review and rating data. Finally, Section 5 reports final consideration and conclusions of the present study. 

## **2 | Related Works** 

**Limitations of the star rating scale.** Star ratings are the most common mechanism for summarizing user evaluations, but several well-documented factors influence how they are distributed and interpreted. For instance, ratings typically exhibit a J-shaped distribution, with extreme opinions dominating and moderate ones underrepresented [8]. This phenomenon can be explained by self-selection biases [9, 10]: 

- _acquisition bias_ : consumers with positive expectations are more likely to purchase and leave a review; 

- _underreporting bias_ : those with very positive or very negative experiences are more motivated to provide feedback than users with average ones. 

Although these tendencies skew the observed distribution, research also shows that when all customers are prompted to review, the resulting shape approaches a normal distribution, suggesting that ratings still carry meaningful information about product quality when biases are properly accounted for. 

Psychological and contextual factors may also affect rating behavior. Studies have documented the presence of cognitive dissonance, where users inflate ratings to justify their purchases [5]; confirmation bias, where consumers interpret reviews in ways consistent with prior beliefs [11]; and social influence, whereby visible ratings shape subsequent ones [12]. Moreover, the presence of manipulated reviews can undermine trust in the system [5]. 

From a behavioral economics perspective, these effects can be interpreted through well-established theoretical mechanisms. Cognitive dissonance theory [13] predicts that, especially for high-involvement or expensive purchases, consumers may inflate post-purchase ratings to rationalize their decisions and reduce psychological discomfort. This process can generate a systematic upward bias in numerical ratings relative to the sentiment expressed in accompanying text, where reviewers may feel less constrained and more willing to articulate ambivalent or critical evaluations. 

While these dynamics complicate interpretation, they also motivate more refined analyses that combine ratings with textual signals. 

Social influence can further give rise to herding behavior and informational cascades, whereby early or salient ratings disproportionately affect later evaluations independently of individual experiences [12]. From a game-theoretic perspective, reviewers may also behave strategically, adjusting their ratings to conform to visible averages or to counterbalance what they perceive as overly positive or negative existing scores. Such strategic behavior introduces additional, systematic deviations between observed ratings and underlying sentiment. 

Cultural differences provide further nuance. Wan and Nakayama [5] showed that U.S. reviews typically align linearly with sentiment, whereas Chinese reviews often follow a J-shaped curve and Japanese reviewers tend to avoid the most extreme scores. Such patterns do not invalidate ratings but highlight the importance of contextualizing them when comparing across regions and platforms. In fact, they reflect deeper cultural dimensions such as individualism versus collectivism, emotional expressiveness norms, and communication styles [14]. In the context of our study, which focuses on Italian product reviews, it is important to acknowledge potential cultural specificity. Mediterranean cultures, including Italy, are generally characterized by high emotional expressiveness and direct communication styles [15], which may influence both the textual richness of reviews and the calibration of numerical ratings. While this cultural context may limit direct generalization to other cultural settings, it also provides an important complement to existing studies that have predominantly focused on Anglo-Saxon and East Asian contexts. Future research should explore whether the rating-sentiment relationships we identify hold across diverse cultural contexts, potentially leveraging multilingual transformer 

2 of 14 

_Applied Stochastic Models in Business and Industry_ , 2026 

models and cross-cultural annotation protocols to enable systematic comparison. 

Finally, numerical ratings offer less granularity than textual reviews. They summarize overall impressions but cannot always capture multidimensional or attribute-specific evaluations [1]. At the same time, their simplicity is precisely what makes them accessible and widely used by consumers and platforms. 

Taken together, these insights from consumer behavior and behavioral economics provide a strong theoretical motivation for our empirical investigation. If psychological, social, and strategic factors can systematically distort rating behavior, then textual sentiment—extracted through computational methods that operate independently of these biasing mechanisms—may offer a more faithful representation of consumer evaluation. Our methodological framework directly addresses this gap by comparing observed ratings with independently derived sentiment measures. 

**Sentiment analysis.** To enrich rating information, SA has emerged as a computational approach for extracting sentiment orientation from text. SA can classify polarity (positive, neutral, negative) [6] or even measure sentiment intensity on a continuous scale [16]. Approaches range from lexicon-based methods to advanced deep learning and _Large Language Models_ (LLMs) with state-of-the-art performance [17]. 

A large body of work confirms that ratings and textual sentiment are usually strongly correlated [4, 18, 19], though not perfectly aligned. In some cases, text reveals nuances not directly visible in the rating alone. For example, a five-star review may include critical remarks about specific product aspects [1]. Studies on durable goods have even observed non-linear patterns, such as an inverted U-shaped relationship between satisfaction and sentiment, where reviews closer to neutrality signal higher usefulness [3]. Similarly, neutral or moderately expressed reviews are often perceived as more credible and helpful than highly emotional ones. 

Such findings demonstrate that text and ratings provide complementary perspectives. On platforms like TripAdvisor, for example, users sometimes assign positive scores even when including negative statements in their text; in these cases, SA is able to detect the subtleties more accurately [20]. To integrate both signals, hybrid approaches have been proposed, such as the Polarity Aggregation Model (PAM) [20] and SentiDraw [21], which combine ratings with text-based sentiment information to achieve more faithful representations of user opinion. 

**Gaps and practical implications.** Despite these advances, several research gaps remain. Many models treat ratings and text separately, rather than holistically integrating them [3, 8]. A first step toward integration has been proposed by Barzizza et al. [22], who combine both sources for customer clustering, though their scope is limited. Moreover, a comprehensive comparison of SA techniques across domains is still lacking [21, 23], and factors such as review length, domain specificity, and linguistic complexity remain underexplored [2]. The relationship between sentiment polarity and perceived review helpfulness also remains inconclusive, with evidence supporting linear, U-shaped, and inverted 

U-shaped patterns. Moreover, testing these kind of relationships is particularly challenging and requires advanced and sophisticated methodological approaches [24–27]. 

Another methodological issue arises because SA models often use ratings as training labels. If rating biases are not addressed, they can propagate into sentiment models, potentially misrepresenting user opinion. Human-annotated sentiment provides a valuable benchmark to assess and correct these effects. 

In this context, the present work provides a direct and statistically rigorous assessment of the alignment between ratings and sentiment. By leveraging a large corpus of Italian product reviews, enriched with human-annotated sentiment labels, we are able to assess whether ratings can indeed be considered reliable indicators of the sentiment expressed in text. More broadly, our findings not only clarify the extent to which ratings reflect sentiment but also support their use as equidistant, interpretable measures in analytical and managerial applications—thereby offering actionable insights for research and practice in the domain of consumer behavior and e-commerce. 

## **3 | Methods** 

The objective of this work is to assess whether the user-provided _rating_ attached to product reviews is a reliable indicator of the _sentiment_ expressed in the text. This objective corresponds to the statistical comparison between a rating variable _𝑅_ and the sentiment variable _𝑌_ within a review corpus. Let 



be the corpus of _𝑁_ reviews, where _𝑥𝑛_ denotes the textual content of the _𝑛_ th review, _𝑟𝑛_ ∈{r _𝑖_ }<sup>_𝐼_</sup> _𝑖_ =1<sup>denotes its associated rating, and</sup><sup>_𝑦𝑛_</sup> is a continuous latent variable indicating its associated sentiment. 

However, we consider the most common practical scenario, in which only the rating variable is observed, while the sentiment variable is unobserved. To recover the missing sentiment information, we propose the following procedure: (i) train a domain-adaptive language encoder to produce dense review embeddings, (ii) create a ground-truth annotated sample, (iii) train an ordinal sentiment predictor-based on an ordinal regression model-on the annotated sample using the embeddings as features. 

To enable a direct comparison between the observed rating _𝑅_ and the unobserved continuous sentiment _𝑌_ , we discretize _𝑌_ into _𝐼_ ordered sentiment categories by means of the variable _𝑆_ . Concretely, let 



denote the categorical sentiment associated with review _𝑛_ . The categories are exhaustive and ordered, covering the entire support of the latent sentiment variable from a most negative category to a most positive category (e.g., from “very negative” to “very positive”). By construction the discrete sentiment _𝑠𝑛_ is ordered. Thus, in our experiments, each review will be associated with an estimated sentiment value, that is, _̂ 𝑠𝑛_ , which will 

3 of 14 

_Applied Stochastic Models in Business and Industry_ , 2026 



**FIGURE 1** | Summary of the proposed methodology. 

be compared to _𝑟𝑛_ ∈{r _𝑖_ }<sup>_𝐼_</sup> _𝑖_ =1<sup>. The discretization of the continuous</sup> sentiment variable _𝑌_ into _𝐼_ ordered categories serves a fundamental purpose in our analytical framework. Since our primary objective is to compare textual sentiment with user-provided ratings—which are inherently discrete and ordinal (1 to 5 stars)—we require both variables to be measured on comparable scales. By discretizing predicted sentiment into ordered categories _𝑠𝑖_<sup>_𝐼_</sup> _𝑖_ =1<sup>that mirror the rating scale</sup><sup>_𝑟𝑖𝐼_</sup> _𝑖_ =1<sup>, we establish a com-</sup> mon measurement framework that enables direct statistical comparison through Correspondence Analysis. This approach preserves the ordinal structure of both variables while allowing us to assess alignment and identify discrepancies across the entire spectrum of consumer evaluations, from very negative to very positive opinions. 

In the following, we first introduce the methodology for estimating sentiment, and subsequently describe the procedure for comparing the resulting sentiment predictions with the rating variable. In addition, the entire process is illustrated in Figure 1. 

## **3.1 | Sentiment Prediction Model** 

The sentiment prediction model consists of three interconnected components: (i) domain-adaptive feature extraction with a transformer encoder, (ii) annotation and assessment of annotator agreement, and (iii) a multi-task ordinal regression head based on the CORAL formulation. We begin by introducing the transformer-based feature extractor (AlBERTo), which provides document-level embeddings of reviews as the model backbone. We then describe the annotated sample and the analysis of annotator agreement, and finally present the ordinal regression head that leverages these features and annotations for sentiment prediction. 

### **3.1.1 | Feature Extraction** 

Extracting features from text requires the choice of an embedding function 



which maps a textual input _𝑥𝑛_ into a semantic vector representation **_𝒙_** _𝑛_ of dimension _𝐸_ . 

To set _𝑓_ , we adopt the now standard practice of leveraging _trasformers_ -based pre-trained language models [28], subsequently fine-tuned on our specific domain to capture domainspecific nuances while retaining general semantic knowledge. During the _pre-training_ phase, a transformer model is trained on a massive corpus of text, to learn general language patterns from the data. Then the model’s knowledge can be adapted (or _fine-tuned_ ) for specific downstream tasks on a task-specific text corpus and domain.<sup>1</sup> 

The practice of fine-tuning pre-trained transformer models has become standard in natural language processing for both theoretical and practical reasons. Theoretically, models like BERT acquire rich, generalizable linguistic representations during pre-training on massive text corpora. However, different domains exhibit distinct vocabularies, semantic patterns, and linguistic structures. Product reviews, specifically, contain domain-specific terminology, expressions of satisfaction or dissatisfaction, and evaluative language that differ substantially from general text. Fine-tuning enables the model to adapt its general representations to capture these domain-specific nuances while retaining broad linguistic knowledge, avoiding the computational cost and extensive data requirements of training from scratch [29, 30]. Practically, fine-tuning has consistently demonstrated superior performance across various NLP tasks, with studies showing significant improvements in accuracy for domain-specific applications [31–33]. In our context, fine-tuning AlBERTo on the review corpus allows the model to better recognize the specific ways Italian consumers express sentiment in product evaluations. 

_Bidirectional Encoder Representations from Transformers_ (BERT) is one of the most influential transformer-based language models, proposed by a research team at Google AI [29]. 

It has been applied and fine-tuned across a wide range of tasks and application domains [30, 31, 33, 34]. Furthermore, several BERT-like architectures have been proposed, for example, RoBERTa [35], DistilBERT [36], ALBERT [37], and SciBERT [38]. 

Since our corpus consists of product reviews written in Italian, we selected the AlBERTo model [39], originally pre-trained on TWITA, a large-scale collection of Italian tweets. 

The model comprises approximately 184 million parameters [39], and is specifically optimized for the Italian language, thus making it a suitable choice for our task. 

The pre-training of AlBERTo is based on the _Masked Language Modeling_ (MLM) objective, a widely used self-supervised approach. Under this objective, a fraction of the input tokens are randomly masked, and the model learns to predict the masked tokens given the surrounding context. Each input token is represented as the sum of three embedding components: 

1. **Token embedding** , which learns a representation for each element of the vocabulary (i.e., each token); 

2. **Sentence embedding** , which provides sentence-level information by indicating the sentence to which each token belongs; 

4 of 14 

_Applied Stochastic Models in Business and Industry_ , 2026 

3. **Positional embedding** , which encodes the relative position of each token within the sequence. 

The resulting embedding vector is fed into a stack of transformer encoders [28], which apply multi-head self-attention and feed-forward transformations to produce contextualized representations. The output is a set of contextual embeddings, one for each token. From these, one can derive both token-level semantic representations as well as a document-level representation. 

In our study, we further continue training AlBERTo on the corpus  reviews using the same MLM objective. This additional training step allows the model to adapt its internal representations to the distributional properties of our product reviews while retaining the general linguistic knowledge acquired during the original pre-training phase. The resulting document-level embeddings of reviews serve as the backbone of the sentiment prediction model, forming its feature matrix. The underlying transformer encoder (AlBERTo) is kept frozen during training, so that only the parameters of the ordinal classification head are learned. 

We have provided the model cards for both the pre-trained and fine-tuned models in the Supporting Information, including training details and statistics about training data. Additionally, the source code for fine-tuning AlBERTo has been made available. 

### **3.1.2 | Annotation and Annotator Agreement** 

We extract a sample  from  and collect _𝑇_ annotations for each _𝑑_ ∈ . Each annotation corresponds to an ordinal label: 



With the aim of evaluating the agreement between annotators, we adopted the _entropy index for ordinal distributions_ as defined by Leti and Cerbara [40]. This index provides a measure of dispersion that accounts for the ordinal nature of the sentiment scale on which annotators classified reviews. 

**Counts and relative frequencies.** Let _𝑇𝑑,𝑖_ denote the number of annotators (out of _𝑇_ ) who assigned category s _𝑖_ to review _𝑑_ , for _𝑖_ = 1 _, . . . , 𝐼_ . By construction 



The relative frequency of category s _𝑖_ for review _𝑑_ is 



**Heterogenity index for ordinal categorical variables** The cumulative proportion up to category s _𝑖_ for review _𝑑_ (with _𝑖_ = 1 _, . . . , 𝐼_ ) is defined as 



Using these cumulative proportions, Heterogenity index for ordinal categorical variables index for review _𝑑_ is given by 



The dispersion index _𝐻𝑑_ quantifies how spread out the ratings are across the ordinal scale. A value of _𝐻𝑑_ = 0 indicates perfect agreement among annotators, where all ratings fall within a single category. Higher values of _𝐻𝑑_ reflect increasing disagreement, with ratings distributed across more distant categories. Because it is based on cumulative proportions, this index is sensitive to the ordinal structure of the scale—it penalizes not just disagreement, but how far apart the ratings are. Thus, it is especially well-suited for analyzing inter-rater variability on ordered categorical scales. 

**Multiple Correspondence Analysis.** While _𝐻_ provides a scalar measure of annotator disagreement that is sensitive to the ordinal structure of the rating scale, it does not convey how disagreement patterns are structured across categories or across annotators. For this reason, we complemented the entropy-based analysis with _Multiple Correspondence Analysis_ (MCA). 

MCA is a dimensionality reduction technique specifically designed for categorical data, which projects categories and observations into a common low-dimensional geometric space. In this space, proximity reflects similarity of categorical profiles: categories or annotators that tend to co-occur in their assignments are positioned close together, while those showing systematically divergent choices are located further apart. This geometric representation allows us to go beyond a unidimensional index of dispersion and to visualize the structure of agreement and disagreement in a more interpretable way. In our setting, MCA provides a direct and intuitive means to explore whether the three human annotators who independently labeled the sentiment of reviews are sufficiently aligned in their judgments. If annotators are largely consistent, their positions in the MCA space will cluster tightly around the same regions of the first dimensions; conversely, if systematic differences exist, the method will reveal them as separations or distinct groupings along the axes. Thus, MCA not only complements the entropy-based measure by adding a visual dimension, but also helps to detect potential biases or systematic patterns of disagreement among annotators that a scalar index cannot capture. 

To interpret MCA results, it is necessary to decide how many dimensions (axes) to retain from the analysis. Each dimension corresponds to a singular value (or eigenvalue) and captures a proportion of the total variance—also referred to as _inertia_ —present in the data. The number of meaningful dimensions is typically determined using a scree plot, which displays the eigenvalues in decreasing order. A common criterion is to retain the first _𝛿_ dimensions such that they collectively explain a sufficiently large proportion of the total inertia (e.g., 70%–80%). Alternatively, the “elbow” point in the scree plot—where additional dimensions contribute only marginally—can be used to define the cutoff. Retaining a small number of dimensions allows us to summarize the complex structure of annotator agreement in a reduced space while preserving most of the variability in the data, making patterns of consensus or divergence easier to interpret. 

5 of 14 

_Applied Stochastic Models in Business and Industry_ , 2026 

### **3.1.3 | Multi-Task CORAL Ordinal Regression** 

Our prediction model takes a review text as input and returns an ordinal sentiment label. The feature matrix is derived from the embeddings of the annotated sample, while the ground-truth supervision is given by the _𝑇_ annotations available for each review. The model architecture consists of a transformer-based encoder, which is fine-tuned and subsequently frozen, and an ordinal classification head stacked on top. 

Neural networks are endowed with ordinal regression capabilities by decomposing the ordinal prediction problem into a set of binary classification subproblems. To ensure rank consistency among these binary classifiers, we adopt the _COnsistent RAnk Logits_ (CORAL) framework [41]. Furthermore, we employ a multi-task CORAL formulation, where each annotator _𝑡_ defines a separate task. Joint training across annotators allows the model to capture shared structure [42]. 

**Rank consistency and label extension.** Given a label _𝑆_ ∈ {s _𝑖_ }<sup>_𝐼_</sup> _𝑖_ =1<sup>withorderedrankss</sup><sup>_𝐼>_s</sup><sup>_𝐼_−1</sup><sup>_>_· · ·</sup><sup>_>_s1,weadoptthe</sup> CORAL framework, which enforces the required rank consistency in the cumulative probabilities, namely: _𝑃𝑟_ ( _𝑆>_ s1) ≥ _𝑃𝑟_ ( _𝑆>_ s2) ≥ _. . . 𝑃𝑟_ ( _𝑆>_ s _𝐼_ −1). 

In our specific case, this framework extends the label _𝑆𝑑_<sup>(</sup><sup>_𝑡_)into</sup> _𝐼_ − 1 cumulative binary indicators: 



Modeling the ordinal problem as _𝐼_ − 1 cumulative binary subproblems leads to cumulative probabilities 



**Model head and outputs.** For task (annotator) _𝑡_ , the CORAL head of our neural network takes as input: 



The CORAL head computes logits 



where **_𝑾_**<sup>(</sup><sup>_𝑡_)</sup> ∈ ℝ<sup>(</sup><sup>_𝐼_−1)×</sup><sup>_𝐾_</sup> and **_𝒃_**<sup>(</sup><sup>_𝑡_)</sup> ∈ ℝ<sup>_𝐼_−1</sup> are task-specific linear parameters, and, particularly, **_𝒃_**<sup>(</sup><sup>_𝑡_)</sup> is a vector of distinct bias for _𝐼_ − 1 binary problems. 

Applying the sigmoid activation function elementwise yields estimated cumulative probabilities: 



**Multi-task loss function.** Given an annotated example _𝑑_ ∈  with ground-truth label _𝑠𝑑_<sup>(</sup><sup>_𝑡_)</sup> and thus _𝐼_ − 1 cumulative 

binary indicators _𝑠_<sup>(</sup> _𝑑_<sup>_𝑡_)</sup><sup>_,𝑖_,thelossfortask</sup><sup>_𝑡_isthesumofbinary</sup> cross-entropy losses across the _𝐼_ − 1 cumulative subproblems: 



The global training objective sums the losses across annotators: 



A simple unweighted sum of losses is a reasonable choice in multi-task settings when there is no need to give different emphasis to any particular task. In our case, this corresponds to the absence of systematic annotator-specific bias in the annotation process, for which empirical evidence is provided in Section 3.1.2. 

**Predictions and evaluation metrics.** Let  _⊂_  be a held-out validation set. For each validation example _𝑣_ ∈  we compute a task-specific predicted label: 



During training, we iterate over the entire training set multiple times, where each complete pass through the dataset is referred to as an _epoch_ . At the end of each epoch, we evaluate the model on the set , computing the total loss across all tasks, as in Equation (10). The model achieving the lowest validation loss over all epochs is selected as the _best model_ . This procedure allows us to monitor learning progress and prevent overfitting by comparing training and validation losses across epochs. 

Thus, we compute the task-specific _Mean Absolute Error_ (MAE) and _Root Mean Square Error_ (RMSE) as evaluation metrics on the validation set: 



**Aggregation rule.** We derive a single consensus sentiment prediction across annotators to be used in the comparison between rating and sentiment. Given an odd number _𝑇_ of annotators, we adopt the following majority rule: 



In other terms, the rule assigns the majority label if one exists, and falls back to the median sentiment category when no absolute majority is present. 

The model card for this multi-task regression model is provided in the Supporting Information, detailing training procedures, dataset statistics, and performance metrics. The source code for both training and inference has also been made available. 

6 of 14 

_Applied Stochastic Models in Business and Industry_ , 2026 

## **3.2 | Rating Vs Sentiment: A Comparison Through Correspondence Analysis** 

To formally compare the rating variable _𝑅_ and the (predicted) sentiment variable _̂ 𝑌_ we employ Correspondence Analysis (CA). CA is a multivariate statistical technique that allows the representation of categorical data in a low-dimensional latent space [43]. Given a contingency table of frequencies, CA decomposes the chi-square distances between rows and columns into orthogonal dimensions, each associated with an eigenvalue _𝜆𝑘_ that measures the proportion of inertia (variance) explained by that dimension. Being _𝐾_ the number of dimensions, the sum of all eigenvalues equals the total inertia, and the normalized eigenvalues can be interpreted as the relative importance of each latent axis, with ∑ _𝐾𝑘_ =1<sup>_𝜆𝑘_= 1.</sup> 

**CA space.** In our context, the row profiles correspond to _sentiment categories_ (predicted from the textual analysis of reviews), while the column profiles correspond to _rating scores_ (provided explicitly by users). By projecting both onto the same factorial space, we can measure the divergence between sentiment and rating for each level _𝑖_ ∈{1 _, . . . ,_ 5}. 



Higher values of Δ _𝑖_ indicate a greater aggregated difference between rating and sentiment for level _𝑖_ . 

Thus, we consider the relative contribution of each dimension _𝑘_ to the aggregated difference for category _𝑖_ : 



This decomposition expresses the percentage share of the weighted squared difference on axis _𝑘_ with respect to a categorywise difference. It allows us to assess which latent dimensions drive the distance between sentiment and rating for each category. For instance, if _𝐶𝑖𝑘_ is large, dimension _𝑘_ is the main source of disagreement at category _𝑖_ . 

An overview of the entire methodology is further illustrated in Figure 1. 

Let **_𝑺_** _,_ **_𝑹_** ∈ ℝ<sup>_𝐼_×</sup><sup>_𝐾_</sup> with: 



They are the coordinate matrices of sentiment and rating, respectively, with _𝐼_ categories (rows) and _𝐾_ dimensions (columns). The _𝑖_ -th row of **_𝑺_** and **_𝑹_** corresponds to the coordinates of category _𝑖_ in the CA space. 

**Elementwise differences.** For each category _𝑖_ ∈{1 _, . . . , 𝐼_ } and dimension _𝑘_ ∈{1 _, . . . , 𝐾_ }, we define the squared difference between sentiment and rating coordinates as 

## **4 | Application** 

## **4.1 | Data** 

This research is part of the 8.03 Project of the _Made in Italy – Circular and Sustainable_ Extended Partnership<sup>2,3</sup> , whose general objective is to develop a model for consumer preferences towards Made in Italy products, with particular attention to sustainability attributes. The analysis in this paper fits within this context, as it is crucial to verify the reliability of ratings as an indicator of sentiment to study those preferences, and otherwise to produce a model that predicts a reliable one. 

As described in the previous section, our methodology considers a review corpus  , of which a sample  has been annotated with sentiment labels. 



This quantity represents the elementwise (squared) difference between sentiment and rating along dimension _𝑘_ for the _𝑖_ th category. Large values of _𝛿𝑖𝑘_<sup>2indicate that, for category</sup><sup>_𝑖_, sentiment</sup> and rating occupy distant positions on the latent axis _𝑘_ , whereas small values suggest a close alignment. 

Because not all dimensions are equally informative, we weight the elementwise differences by the eigenvalue _𝜆𝑘_ associated with each CA dimension: 



The eigenvalues reflect the proportion of inertia explained by each dimension in the correspondence analysis. By weighting, we ensure that differences along highly informative axes are emphasized, while those on marginal axes are downweighted. 

**Aggregated differences.** We computed the _categorywise_ difference between sentiment and rating for category _𝑖_ by means of the weighted Euclidean distance: 

To collect  , we used a web scraping procedure from the publicly accessible major e-commerce website. In particular we focused on the “Made in Italy” section available in the website. This category comprises a curated selection of products manufactured in Italy and includes multiple subcategories. For this research, we focused on two main sub-sections within the “Made in Italy” catalog: _Home Essentials_ and _Fashion Wear_ . 

The procedure firstly resulted in 424,816 scraped reviews. We selected only non void data with textual reviews written in Italian obtaining a final dataset that consists of 312,928 individual customer’s reviews, each associated with a product listed within one of the aforementioned categories. The variables extracted for each review are listed in Table 1. 

Note from Table 1 that the rating variable is an ordinal variable taking categories {r _𝑖_ }<sup>5</sup> _𝑖_ =1<sup>, corresponding to values from 1 to 5.</sup> 

To compare the rating variable and the categorical sentiment variable, in our setting, _𝐼_ = 5, and the ranks {s _𝑖_ }<sup>5</sup> _𝑖_ =1<sup>correspond to the</sup> 

7 of 14 

_Applied Stochastic Models in Business and Industry_ , 2026 

**TABLE 1** | Reviews’ collected variables. 

|**Variable**|**Description**|
|---|---|
|Website Section|The e-commerce sub-category to<br>which the product belong (either<br>_Home Essentials_or_Fashion Wear_).|
|Product name|The full product name listed on the<br>website.|
|Price|The price of the product at the time of<br>data collection.|
|Date time review|Timestamp of the review posting.|
|Review rating|Star rating provided by the customer<br>for the review (from 1 to 5 stars).|
|Review title|Title of the customer’s review.|
|Review text|Full text body of the review.|



sentiment labels _very negative_ , _negative_ , _neutral_ , _positive_ , and _very positive_ sentiment, respectively. 

Among the total reviews, 70.84% (221,725 reviews) originated from the _Home Essentials_ section, while the remaining 29.16% (91,203 reviews) were collected from _Fashion Wear_ . This distribution reflects the varying review volumes across categories within the “Made in Italy” selection. 

While the data were publicly accessible, we took measures to ensure ethical compliance. No personal identifiers (e.g., reviewer names or user IDs) were scraped or stored. Only anonymized and aggregate-level content was used in the analysis. The data collection was performed solely for academic research purposes, and no attempts were made to interact with or influence the original reviews or the website. 

To explore potential patterns in review sentiment related to key review and product attributes, we implemented an unsupervised clustering approach. Prior to clustering, the following continuous variables were scaled using a standard normalization procedure (z-score normalization): 

- **Review length scaled** : Computed as the number of characters in the **Review text** field (once adequately pre-processed, with remotion of Italian stopwords, punctuation, special characters and whitespaces). 

- **Price scaled** : Normalized product price. 

- **Rating scaled** : The customer’s star rating -considered for simplicity a numerical variable-for the review, normalized. 

These three features, together with the **Website Section** and Year of publication of the review (extracted from the **Date time review** variable) were selected as segmentation variables for a clustering procedure. The goal of such clustering was to sample reviews for the consequent human annotation step including as much variability as possible of the customer perception. Therefore, aiming at a stratified sampling, we partition the data using the previously described segmentation variables, under the theoretical assumption that length of reviews, different prices of the product, and varying customer ratings, the section to which the 

product belongs and the time at which the review has been posted can explain much of the variability possibly present in the sentiment. Using these dimensions, we performed k-means clustering [44] and identified, using silhouette validation index [45, 46], and optimal of seven distinct clusters. 

To conduct sentiment labeling, a representative stratified sample of 1000 reviews was drawn from the dataset using stratified sampling with clusters data: each cluster contributed to the final sample proportionally to its size in the full dataset, ensuring that all identified segments of the review corpus were adequately represented in the annotated subset and that under- or over-represented clusters did not bias the annotation outcomes. 

The sampled reviews were manually annotated by three independent annotators (thus, _𝑇_ = 3), all of whom held at least a bachelor’s degree in a scientific or economic discipline. Annotators were instructed in multiple training session to classify the sentiment expressed in each review based on its textual content. An annotation guideline was provided to ensure consistency in labeling across reviewers. Annotators were asked to label sentiment on a five-point ordinal scale {s _𝑖_ }<sup>5</sup> _𝑖_ =1<sup>, correspond-</sup> ing respectively to the categories _very negative_ , _negative_ , _neutral_ , _positive_ , and _very positive_ . The choice of the number of annotators represents a practical balance between annotation quality and resource efficiency. Methodologically, _𝑇_ = 3 is the minimum number that enables implementation of a meaningful majority voting rule (Equation 13) while allowing assessment of inter-annotator agreement through appropriate statistical measures. Three annotators permit detection of systematic biases and provide sufficient information for the multi-task learning framework to capture consensus patterns. While additional annotators could potentially increase robustness, the observed high inter-annotator reliability suggests that three annotators are sufficient for establishing ground-truth sentiment labels in our study, particularly given the multi-task framework that leverages information from all annotators simultaneously. It is worth noting that the annotators were given indication to consider the ordinal scale of sentiment from 1 to 5 as an interval scale. This indication of equidistance implies that the five ordinal categories are treated as equally spaced points on a latent continuum of sentiment intensity. In other words, the difference between two adjacent labels (e.g., from negative to neutral) is considered equivalent in magnitude to the difference between any other pair of adjacent labels (e.g., from positive to very positive) thus implying the same amount of change in satisfaction for passing from category 1 to 2 as for passing from category 3 to 4. This interpretation allows the ordinal scale to be modeled as an interval scale. 

Once obtained the results of these annotations, to assess labeling reliability and inter-annotator coherence and agreement we adopted the approach proposed at Section 3. 

To quantify the level of agreement among annotators on an ordinal rating scale, we employed the Heterogeneity index _𝐻_ , as described in Equation (5). 

Figure 2 displays the empirical distribution of the agreement index _𝐻_ , computed across all annotated reviews. The values of _𝐻_ are discretized according to their theoretical support for three raters on a 5-level ordinal sentiment scale. The plot reveals that 

8 of 14 

_Applied Stochastic Models in Business and Industry_ , 2026 



**FIGURE 2** | Empirical distribution of Heterogeneity index for ordinal categorical variables _𝐻_ for reviews annotated by three raters on a 5-point sentiment scale. 

most reviews fall into the lower portion of the dispersion range. The most common value is _𝐻_ = 0 _._ 222, which corresponds to the situation where two annotators agree and the third selects an adjacent category. A substantial number of cases also show perfect agreement ( _𝐻_ = 0) indicating unanimous labeling. Only a small proportion of reviews exhibit higher disagreement ( _𝐻_ = 0 _._ 444), and the maximum of _𝐻_ = 0 _._ 667 is more than rare, occurring only for one review out of 1000. This empirical distribution suggests that inter-annotator agreement is generally high. In the vast majority of cases, annotators either chose the same rating or closely adjacent ones. Such consistency implies that the labeling task was well-defined and that annotators shared a common understanding of the scale semantics. 

The structure of inter-annotator agreement was furthermore evaluated using the Multiple Correspondence Analysis (MCA) that enables a compact, low-dimensional visualization of inter-variable associations. The scree plot (Figure 3) shows the percentage of explained variance (inertia) by each MCA dimension. The first two dimensions together account for approximately 40.8% of the total variance (22.7% and 18.1%, respectively), suggesting that a substantial amount of the association structure can be interpreted in a two-dimensional space. The sharp decline in explained variance after the fifth dimension lead us to the selection of 5 dimensions for interpretative purposes, in line with the “elbow” criterion. 

The MCA variable map (Figure 4) displays the positions of all score categories (_1, _2, _3, _4 and _5 in the plot) across the three annotators (respectively S1, S2, S3) in the reduced two-dimensional space. Categories corresponding to the same rating level tend to cluster closely, indicating coherent usage of the scale across annotators. For instance, the mid-scale category “3” shows consistent agreement, with S1_3, S2_3, and S3_3 located within the same general region of the plot. Across all rating levels, annotators S1 and S3 are generally more tightly grouped, suggesting a higher degree of similarity in their labeling patterns. Annotator S2, while still aligned, tends to be slightly offset from the other two, particularly for ratings 2 through 5—an 



**FIGURE 3** | Scree plot of eigenvalues from Multiple Correspondence Analysis applied to human annotated sentiment. 



**FIGURE 4** | MCA variable factor map of inter-annotator agreement. 

indication of minor systematic variation in his judgment criteria. Importantly, even with these small deviations, the overall configuration supports a high level of agreement among all three annotators. The spatial coherence across corresponding categories confirms that the rating behavior is consistent and reliable, with only mild annotator-specific tendencies rather than major disagreements. 

Taken together, the results from entropy of ordinal distribution and MCA confirm quite high agreement among annotators. This point is crucial for the multi-task (multi-annotator) approach in the subsequent sentiment modeling phase: the observed agreement supports modeling the overall loss function as an unweighted sum, as in Equation (10), without the need to compensate for systematic annotator-specific bias in the annotation process. 

## **4.2 | Analysis** 

### **4.2.1 | Performance of Sentiment Prediction** 

As described in Sections 3.1.1 and 3.1.3, we employed our fine-tuned AlBERTo encoder to extract a feature matrix from the 

9 of 14 

_Applied Stochastic Models in Business and Industry_ , 2026 

**TABLE 2** | Performance metrics on the validation set for the best models of multi-task CORAL sentiment regression, comparing pre-trained and fine-tuned AlBERTo encoders; best models selected over 100 training epochs. 

|**Metric**|**Task**|**Pre-trained**<br>**AlBERTo**|**Fine-tuned**<br>**AlBERTo**|**%**<br>**Difference**|
|---|---|---|---|---|
|**_MAE_**|_𝑡_=1|0.613|0.466|−23.992|
||_𝑡_=2|0.510|0.466|−8.650|
||_𝑡_=3|0.569|0.490|−13.788|
|**_RMSE_**|_𝑡_=1|0.963|0.814|−15.481|
||_𝑡_=2|0.834|0.731|−12.382|
||_𝑡_=3|0.939|0.780|−17.002|



annotated reviews. We then used these features to train a sentiment prediction model using a multi-task (i.e., multi-annotator) CORAL ordinal regression framework. Performance metrics are shown in Table 2. To show the advantage of fine-tuning, the table reports the performance of the ordinal CORAL multi-task regression, over 100 epochs of training, when using (i) the original pre-trained AlBERTo encoder and (ii) the same encoder after MLM fine-tuning on our review corpus. All other components and training and validation conditions were held constant—that is, same tokenizer, identical training and validations sets, identical CORAL head architecture, frozen encoder during downstream CORAL training. The table also reports the percentage difference in MAE and RMSE obtained with fine-tuning compared to the original pre-trained model. 

The fine-tuned encoder yields consistent reductions in error across all annotator-specific tasks, in the vast majority of cases exceeding 12%. The largest reduction in MAE is observed for task _𝑡_ = 1 (≈ 24%), while the largest reduction in RMSE occurs for task _𝑡_ = 3 (≈ 17%). These results indicate that our fine-tuning step produces embeddings that are more informative for our specific domain of Italian product reviews in the downstream ordinal regression. 

Our multi-task CORAL regression model, based on the finetuned AlBERTo encoder, shows a good performance. MAE provides an interpretable, average error in rating points: for the fine-tuned AlBERTo, the MAE values (0.466, 0.466, 0.490 for tasks 1,2,3, respectively) indicate that the model’s prediction deviates on average by less than half a rating point from the annotator label. RMSE penalizes larger errors more heavily: its values (0.814, 0.731, 0.780 for tasks 1,2,3, respectively) further indicate that larger deviations from the annotator labels are relatively rare, confirming that the model provides robust ordinal sentiment estimates with limited extreme errors. 

### **4.2.2 | Correspondence Analysis of Sentiment and Rating** 

To investigate the relationship between textual sentiment and user-provided rating scores, we first used our CORAL sentiment model to predict the sentiment variable on the corpus  ⧵ . Given _𝑇_ = 3 annotators, the majority rule, defined in Equation 

**TABLE 3** | Contingency table. 

||||**Ratin**|**g**||
|---|---|---|---|---|---|
|**Sentiment**|**1**|**2**|**3**|**4**|**5**|
|1|7187|1938|1356|415|311|
|2|9416|3772|3643|1562|1255|
|3|6019|4289|7261|6307|6417|
|4|1913|2171|7605|28059|84,248|
|5|117|70|648|10422|115,506|



(13) to derive a single consensus sentiment prediction across annotators, becomes: 



Then, we applied CA to the contingency table summarizing frequencies of (predicted) sentiment–rating pairs (Table 3). 

To formally assess the association between these two variables before proceeding with CA, we performed a Pearson’s Chi-square test of independence. The test revealed a highly significant relationship, characterized by a chi-square statistic of 213,398 with an associated _p_ -value of less than 2 _._ 2 × 10<sup>−16</sup> and 16 degrees of freedom. This significant association provides the statistical grounds for the subsequent analysis of inertia and the interpretation of the CA biplot. 

CA allows the representation of categorical data in a lowdimensional space, decomposing the chi-square distances between row (sentiment) and column (rating) profiles into orthogonal latent dimensions. Each dimension captures a proportion of the total variance, measured by its eigenvalue, with higher eigenvalues corresponding to more informative axes. The scree plot of eigenvalues (Figure 5) indicates that the first dimension accounts for the majority of the inertia, while subsequent dimensions contribute progressively smaller amounts. Specifically, Dimension 1 explains over 86% of the variance, while Dimension 2 accounts for a modest 11%, and Dimension 3 and Dimension 4 are negligible. This suggests that the two primary dimensions captures the dominant pattern of agreement or divergence between sentiment and rating, whereas higher-order dimensions reflect finer, less influential distinctions. The biplot at Figure 6 represent the placing of ratings and sentiment from 1 to 5 in the 2 dimensional CA space considering the most important dimensions in terms of explained variance. In this representation, rating categories (R1 through R5, corresponding to 1-star through 5-star ratings) and sentiment categories (S1 through S5, corresponding to very negative through very positive sentiment) are projected into a common geometric space. The horizontal axis (Dimension 1) captures the primary gradient from negative to positive evaluation and accounts for 86.9% of the total variance, representing the main axis along which both ratings and sentiment vary. The vertical axis (Dimension 2) accounts for 11.0% of variance and distinguishes neutral evaluations from extreme ones. In this space, categories that are positioned close 

10 of 14 

_Applied Stochastic Models in Business and Industry_ , 2026 



**FIGURE 5** | Scree plot of eigenvalues from Correspondence Analysis (CA) applied to the comparison of Sentiment and Rating. 



**FIGURE 6** | Biplot of first 2 dimensions of Correspondence Analysis (CA) applied to the comparison of Sentiment and Rating. 

together indicate similar patterns in the rating-sentiment relationship: if ratings perfectly reflected sentiment, then R1 would coincide with S1, R2 with S2, and so forth. The observed distances between corresponding rating and sentiment categories (e.g., the space between R2 and S2, or between R4 and S4) visually represent the degree of misalignment between what users rate and what they express in text. Notably, extreme categories (R1/S1 and R5/S5) cluster more closely, indicating good alignment at the extremes, while mid-range categories (R2–R4 and S2–S4) show greater separation, reflecting the systematic divergences documented in our quantitative analysis. 

By using the coordinate matrices of sentiment and rating from Equation (14), we measured the divergence between sentiment and rating. 

Table 4 presents the elementwise and categorywise differences between sentiment and rating, which are: _𝛿𝑖𝑘_<sup>2,therawelement-</sup> wise difference, _̃ 𝛿_ 2 _𝑖𝑘_<sup>, the squared elementwise difference weighted</sup> by the corresponding eigenvalue, _𝐶𝑖𝑘_ , the percentage of the total aggregated difference for that category attributable to each 

**TABLE 4** | Elementwise and aggregated differences between sentiment and rating. 

|**_𝒊_**|**_𝒌_**|**_𝜹_**<sup>**2**</sup><br>**_𝒊𝒌_**|**_𝜹_**<br>**2**<br>**_𝒊𝒌_**|**_𝑪𝒊𝒌_**|**𝚫****_𝒊_**|
|---|---|---|---|---|---|
|1|1|2_._21×10<sup>−2</sup>|1_._91×10<sup>−2</sup>|8_._03×10<sup>1</sup>|0.154|
||2|3_._87×10<sup>−2</sup>|4_._46×10<sup>−3</sup>|1_._87×10<sup>1</sup>||
||3|1_._27×10<sup>−2</sup>|2_._33×10<sup>−4</sup>|9_._77×10<sup>−1</sup>||
||4|8_._24×10<sup>−4</sup>|2_._16×10<sup>−7</sup>|9_._06×10<sup>−4</sup>||
|2|1|7_._04×10<sup>−2</sup>|6_._10×10<sup>−2</sup>|8_._03×10<sup>1</sup>|0.276|
||2|1_._25×10<sup>−1</sup>|1_._44×10<sup>−2</sup>|1_._90×10<sup>1</sup>||
||3|3_._20×10<sup>−2</sup>|5_._84×10<sup>−4</sup>|7_._69×10<sup>−1</sup>||
||4|2_._07×10<sup>−4</sup>|5_._41×10<sup>−8</sup>|7_._10×10<sup>−5</sup>||
|3|1|2_._08×10<sup>−3</sup>|1_._80×10<sup>−3</sup>|6_._56×10<sup>1</sup>|0.052|
||2|8_._10×10<sup>−3</sup>|9_._34×10<sup>−4</sup>|3_._41×10<sup>1</sup>||
||3|4_._16×10<sup>−4</sup>|7_._59×10<sup>−6</sup>|2_._77×10<sup>−1</sup>||
||4|1_._57×10<sup>−4</sup>|4_._12×10<sup>−8</sup>|1_._51×10<sup>−3</sup>||
|4|1|3_._43×10<sup>−2</sup>|2_._97×10<sup>−2</sup>|8_._10×10<sup>1</sup>|0.192|
||2|5_._94×10<sup>−2</sup>|6_._85×10<sup>−3</sup>|1_._87×10<sup>1</sup>||
||3|7_._79×10<sup>−3</sup>|1_._42×10<sup>−4</sup>|3_._88×10<sup>−1</sup>||
||4|8_._97×10<sup>−6</sup>|2_._35×10<sup>−9</sup>|6_._00×10<sup>−6</sup>||
|5|1|5_._15×10<sup>−3</sup>|4_._46×10<sup>−3</sup>|7_._47×10<sup>1</sup>|0.077|
||2|1_._28×10<sup>−2</sup>|1_._48×10<sup>−3</sup>|2_._47×10<sup>1</sup>||
||3|2_._12×10<sup>−3</sup>|3_._87×10<sup>−5</sup>|6_._48×10<sup>−1</sup>||
||4|9_._49×10<sup>−7</sup>|2_._49×10<sup>−10</sup>|4_._00×10<sup>−6</sup>||



dimension, and Δ _𝑖_ , the categorywise difference between sentiment and rating, as detailed in Equations in Section 3.2. 

From the values of _𝐶𝑖𝑘_ , we can observe that across nearly all sentiment categories, Dimension 1 contributes the largest share of divergence, typically around 75%–81%: this indicates that the first latent dimension in CA captures the main misalignment between sentiment and rating. For example, sentiment 2 (category 2) shows 80.3% of its divergence explained by Dimension 1, highlighting that the largest source of disagreement occurs along this primary axis. We observe as well that Dimension 2 contributes moderately, ranging from 18% for extreme sentiments (1, 2, 4) to 34% for sentiment 3. This suggests that the second dimension is especially relevant for neutral or mid-range sentiment, capturing subtler patterns of misalignment that are not explained by the main axis. Weighted squared differences for Dimension 3 and 4 are very small ( _<_ 1% in all cases) showing that higher-order dimensions contribute minimally to the divergence and can be considered negligible for interpretation. 

This provides a nuanced understanding of the sentiment–rating relationship: extreme sentiments (1 and 5) exhibit strong alignment with the ratings along the primary dimension, while mid-range sentiments (2–4) show both larger overall divergence and more pronounced contributions from the secondary dimension. In essence, the misalignment between sentiment and rating is largely unidimensional, driven by Dimension 1, with Dimension 2 capturing category-specific subtleties, and higher-order dimensions being effectively irrelevant. These results complement the CA biplot in Figure 6, where the primary axis clearly separates misaligned categories, and the secondary axis highlights finer distinctions for neutral sentiment. 

11 of 14 

_Applied Stochastic Models in Business and Industry_ , 2026 

Table 4 also shows the values of Δ _𝑖_ , with _𝑖_ = 1 _, . . . ,_ 5, that is, the difference between sentiment category _𝑖_ and rating category _𝑖_ , aggregated across the 4 dimensions—as in Equation (17). 

It shows the following: 

- Sentiment 2 exhibits the largest divergence (Δ2 = 0 _._ 276), indicating that mid-negative reviews are often rated inconsistently, with significant spread across rating scores. This is consistent with the contingency table, where sentiment 2 spans all ratings, showing a mixture of user evaluations. 

- Sentiment 4 shows moderate divergence (Δ4 = 0 _._ 192), suggesting that while high sentiment mostly aligns with high ratings, some reviews are rated lower than their textual sentiment implies. 

- Sentiment 1 and 5 show intermediate but smaller divergence (Δ1 = 0 _._ 154 and Δ5 = 0 _._ 773), reflecting generally good alignment at the extremes, with sentiment 5 showing particularly strong agreement with high ratings. 

- Sentiment 3 exhibits minimal divergence (Δ3 = 0 _._ 052) highlighting that neutral sentiment aligns closely with user ratings. 

This pattern reveals that misalignment is most pronounced for mid-range sentiment categories, where rating is less representative of the textual sentiment provided. 

## **5 | Conclusions** 

The analysis of the relationship between textual sentiment and user-provided ratings through Correspondence Analysis reveals several important patterns. Overall, sentiment and ratings are closely aligned at the extremes, with very positive and very negative sentiments corresponding well to high and low ratings, respectively. Mid-range sentiments, however, show greater divergence, indicating that ratings are less reliable indicators of textual sentiment in these categories. Notably, neutral sentiment is well captured by the rating system: reviews expressing neutrality in text tend to correspond to mid-level ratings, such as three stars, suggesting that when a user assigns a three-star rating, they are effectively expressing a neutral evaluation of the product. 

The decomposition of differences along latent dimensions shows that most of the misalignment is captured by a single dominant axis, which represents the primary pattern of disagreement between sentiment and rating. A secondary dimension accounts for smaller, category-specific effects, particularly for mid-range sentiments, capturing subtle discrepancies that are not explained by the main axis. Higher-order dimensions are negligible, indicating that the main structure of divergences can be interpreted using just the first two dimensions. 

In other terms, ratings provide a broadly accurate representation of textual sentiment at the extremes and for neutral opinions. Extreme ratings reliably indicate positive or negative sentiment, while three-star ratings effectively reflect neutrality. Misalignment is most pronounced for mid-range positive or negative sentiments, suggesting that ratings alone may not fully capture 

nuanced opinions. The primary latent dimension explains the bulk of sentiment–rating divergence, while a secondary dimension highlights subtler patterns, reinforcing the importance of considering textual sentiment analysis alongside numerical ratings for a comprehensive understanding of user evaluations. 

It is also worth noting that annotators were explicitly instructed to treat the five sentiment classes as equidistant, and the high level of agreement observed confirms that this assumption was consistently understood and applied during the annotation process. The combination of this consistent annotation behavior with the results of our rating–sentiment comparison provides empirical support for considering the five sentiment categories as approximately equidistant for the population represented in our sample. While our findings cannot claim universal validity across all contexts, they nonetheless represent a strong indication that, within the studied domain, rating scores and sentiment categories may be reasonably modeled under an equidistance assumption. In this sense, our results offer at least a preliminary clue in favor of the equidistance of rating categories, supporting their use as an ordinal but evenly spaced scale in subsequent analyses of consumer evaluations. As a direction for future work, a rigorous sensitivity analysis of this assumption would require re-annotating the dataset without explicitly instructing annotators to treat sentiment categories as equally spaced, thus allowing natural psychological distances between sentiment levels to emerge. Such an extension would involve comparing the current equidistant specification with alternatives based on empirically derived category spacing and would necessitate a substantial new annotation effort. Future research could further assess the robustness of the equidistance property across diverse contexts by leveraging psychometric scaling techniques, alternative annotation protocols, or ordinal modeling frameworks that explicitly estimate category thresholds from data. These approaches would provide deeper insights into the psychological structure underlying sentiment evaluation in consumer reviews. 

## **5.1 | Managerial and Practical Implications** 

Our findings have direct implications for both methodological practice and applied sentiment analysis in consumer research. From a methodological perspective, the proposed transformerbased sentiment prediction framework demonstrates that reliable sentiment measures can be extracted from textual reviews even when explicit sentiment annotations are unavailable. By relying on a limited human-annotated sample and an ordinal multi-task learning strategy, the model achieves strong predictive performance, making it suitable for large-scale applications where manual labeling is impractical or prohibitively costly. Beyond model performance, the results clarify when numerical ratings can be treated as reliable proxies for sentiment. The strong alignment observed at the extremes (1-star and 5-star) and at the neutral midpoint (3-star) suggests that these ratings can be used with relatively high confidence as sentiment labels. In contrast, the systematic misalignment detected for mid-range ratings (2-star and 4-star) indicates that these categories introduce substantial noise if used uncritically. In practical applications, this implies that rating-based supervision should be applied selectively, for example by down-weighting mid-range ratings, explicitly modeling their uncertainty, or replacing them with sentiment 

12 of 14 

_Applied Stochastic Models in Business and Industry_ , 2026 

inferred directly from text. From an applied analytics and managerial standpoint, these findings highlight the limits of relying solely on aggregated rating statistics. Textual sentiment analysis provides complementary information that captures nuanced or mixed evaluations that ratings alone fail to reflect. Integrating sentiment measures with ratings supports more accurate diagnosis of product strengths and weaknesses and leads to more robust evidence for decision-making. 

Beyond overall sentiment classification, more granular approaches such as Value-Aspect-Based Sentiment Analysis (VABSA-see [47]) can further enhance managerial insight by distributing sentiment across specific product attributes and consumer values. Integrating our sentiment model within the VABSA framework enables the identification of which attributes or value dimensions systematically drive satisfaction or dissatisfaction, thereby supporting targeted interventions in product design, marketing communication, and customer experience management. Finally, for practitioners developing sentiment analysis pipelines based on user-generated content, our results provide empirical guidance on when star ratings can be trusted as sentiment labels and when they should be treated with caution. Adopting a differentiated use of rating information improves both the robustness and interpretability of sentiment models and, consequently, the quality of downstream analyses built on consumer review data. 

#### **Author Contributions** 

Conceptualization [Nicolò Biasetton, Riccardo Ricciardi]; Methodology [Nicolò Biasetton, Riccardo Ricciardi, Paola Zuccolotto]; Data curation and Software [Nicolò Biasetton, Riccardo Ricciardi, Paola Zuccolotto]; Formal analysis and Investigation [Nicolò Biasetton, Riccardo Ricciardi, Paola Zuccolotto]; Writing – original draft preparation [Nicolò Biasetton, Riccardo Ricciardi]; Writing – review and editing: [Nicolò Biasetton, Riccardo Ricciardi, Luigi Salmaso, Paola Zuccolotto]; All authors read and approved the final manuscript. 

#### **Acknowledgments** 

This study was carried out within the MICS (Made in Italy – Circular and Sustainable) Extended Partnership and the European Union Next-GenerationEU (PIANO NAZIONALE DI RIPRESA E RESILIENZA (PNRR) – MISSIONE 4 COMPONENTE 2, INVESTIMENTO 1.3 – D.D. 1551.11-10-2022, PE00000004 CUP D73C22001250001). This manuscript reflects only the authors’ views and opinions, neither the European Union nor the European Commission can be considered responsible for them. 

#### **Funding** 

The work was supported by Ministry of Education, India. 

#### **Conflicts of Interest** 

The authors declare no conflicts of interest. 

#### **Endnotes** 

- 1The Hugging Face community is one of the main source of pre-trained language models: https://huggingface.co/models. 

2https://www.mics.tech/. 

3https://www.mics.tech/projects/8-03-end-to-end-procedures-for-strateg ic-data-driven-management-and-development-of-sustainable-productservices-that-anticipate-customer-needs/. 

#### **References** 

1. S. Al-Natour and O. Turetken, “A Comparative Assessment of Sentiment Analysis and Star Ratings for Consumer Reviews,” _International Journal of Information Management_ 54 (2020): 102132. 

2. H. Hong, D. Xu, G. A. Wang, and W. Fan, “Understanding the Determinants of Online Review Helpfulness: A Meta-Analytic Investigation,” _Decision Support Systems_ 102 (2017): 1–11. 

3. J. Li, Y. Zhang, J. Li, and J. Du, “The Role of Sentiment Tendency in Affecting Review Helpfulness for Durable Products: Nonlinearity and Complementarity,” _Information Systems Frontiers_ 25, no. 4 (2023): 1459–1477. 

4. B. Kwon, J. Lee, J. Min, C. Kwak, and H. S. Choi, “Beyond the Stars: The Impact of Rating-Text Inconsistency on Perceived Review Usefulness,” _Asia Pacific Journal of Information Systems_ 35, no. 1 (2025): 49–72. 

5. Y. Wan and M. Nakayama, “A Sentiment Analysis of Star-Rating: A Cross-Cultural Perspective,” in _Proceedings of the 55th Hawaii International Conference on System Sciences_ , cC BY-NC-ND 4.0, 2022. 

6. Z. Singla, S. Randhawa, and S. Jain, “Statistical and Sentiment Analysis of Consumer Product Reviews,” in _2017 8th International Conference on Computing, Communication and Networking Technologies (ICCCNT)_ , pp. 1–6, 2017. 

7. O. Akinlaja and M. Mosia, “Using Deep Learning and Sentiment Analysis to Identify Mismatches Between Online Courses’ Reviews and Ratings,” in _2021 3rd International Multidisciplinary Information Technology and Engineering Conference (IMITEC), November 2021_ , pp. 1–6. 

8. N. Aghakhani, O. Oh, D. Gregg, and H. Jain, “How Review Quality and Source Credibility Interacts to Affect Review Usefulness: An Expansion of the Elaboration Likelihood Model,” _Information Systems Frontiers_ 25, no. 4 (2023): 1513–1531. 

9. N. Hu, P. A. Pavlou, and J. Zhang, “On Self-Selection Biases in Online Product Reviews,” _MIS Quarterly_ 41, no. 2 (2017): 449–475. 

10. N. Hu, P. A. Pavlou, and J. J. Zhang, “Why Do Online Product Reviews Have A j-Shaped Distribution? Overcoming Biases in Online Word-Of-Mouth Communication,” _Communications of the ACM_ 52, no. 10 (2009): 144–147. 

11. S. S. Wang, A. Aribarg, and R. Van der Lans, “Learning From Consumer Reviews: The Role of Selection and Evaluation Biases,” in _45th INFORMS Society for Marketing Science (ISMS) Marketing Science Conference_ , Miami, Florida, USA, 2023. 

12. G. Askalidis, S. J. Kim, and E. C. Malthouse, “Understanding and Overcoming Biases in Online Review Systems,” _Decision Support Systems_ 97 (2017): 23–30. 

13. L. Festiger, _A Theory of Cognitive Dissonance_ (Row, Peterson, 1957). 

#### **Data Availability Statement** 

The data that support the findings of this study are part of the _Made in Italy Circular and Sustainable_ (MICS) Extended Partnership. Access to these data is subject to restrictions, as they were made available under specific agreements within the MICS research framework and are not publicly available. However, the data may be available from the authors upon reasonable request and with the permission of the MICS Partnership https://www.mics.tech/. 

14. G. Hofstede, _Cultures’ Consequences: International Differences in Work-Related Values_ , vol. 5 (Sage, 1984). 

15. E. T. Hall, _Beyond Culture_ (Anchor, 1976). 

16. P. S. Ghatora, S. E. Hosseini, S. Pervez, M. J. Iqbal, and N. Shaukat, “Sentiment Analysis of Product Reviews Using Machine Learning and Pre-Trained Llm,” _Big Data and Cognitive Computing_ 8, no. 12 (2024): 199, https://doi.org/10.3390/bdcc8120199. 

13 of 14 

_Applied Stochastic Models in Business and Industry_ , 2026 

17. B. Liu, _Sentiment Analysis and Opinion Mining_ (Springer Nature, 2022). 

18. E. Abedin, A. Mendoza, and S. Karunasekera, “Exploring the Moderating Role of Readers’ Perspective in Evaluations of Online Consumer Reviews,” _Journal of Theoretical and Applied Electronic Commerce Research_ 16, no. 7 (2021): 3406–3424. 

19. N. Aghakhani, O. Oh, D. G. Gregg, and J. Karimi, “Online Review Consistency Matters: An Elaboration Likelihood Model Perspective,” _Information Systems Frontiers_ 23, no. 5 (2021): 1287–1301. 

20. A. Valdivia, E. Hrabova, I. Chaturvedi, et al., “Inconsistencies on TripAdvisor Reviews: A Unified Index Between Users and Sentiment Analysis Methods,” _Neurocomputing_ 353 (2019): 3–16. 

21. S. Sharma and G. Dutta, “SentiDraw: Using Star Ratings of Reviews to Develop Domain Specific Sentiment Lexicon for Polarity Determination,” _Information Processing & Management_ 58, no. 1 (2021): 102412, https://doi.org/10.1016/j.ipm.2020.102412. 

22. E. Barzizza, N. Biasetton, M. Disegna, and L. Salmaso, “Combining Textual and Rating Data From Online Reviews to Cluster Consumers,” _Communications in Statistics-Case Studies, Data Analysis and Applications_ 11, no. 2 (2025): 204–231. 

23. P. Lak and O. Turetken, “Star Ratings Versus Sentiment Analysis – A Comparison of Explicit and Implicit Measures of Opinions,” in _2014 47th Hawaii International Conference on System Sciences, January 2014_ , pp. 796–805, ISSN: 1530-1605. 

24. D. Basso and L. Salmaso, “A Permutation Test for Umbrella Alternatives,” _Statistics and Computing_ 21, no. 1 (2011): 45–54. 

25. S. Bonnini, M. Borghesi, and M. Giacalone, “Advances on Multisample Permutation Tests for “v-Shaped” and “u-Shaped” Alternatives With Application to Circular Economy,” _Annals of Operations Research_ 342, no. 3 (2024): 1655–1670. 

26. S. Bonnini, M. Borghesi, and M. Giacalone, “Nonparametric Analysis of Firm Size and Innovation Intensity in Circular Economy Adoption: S. Bonnini Et al,” _Quality & Quantity_ 59, no. Suppl 2 (2025): 1345–1367. 

27. F. Pesarin and L. Salmaso, _Permutation Tests for Complex Data: Theory, Applications and Software_ (John Wiley & Sons, 2010). 

28. A. Vaswani, N. Shazeer, N. Parmar, et al., “Attention Is All You Need,” _Advances in Neural Information Processing Systems_ 30 (2017): aXiv:1706.03762. 

37. Z. Lan, M. Chen, S. Goodman, K. Gimpel, P. Sharma, and R. Soricut, “ALBERT: A Lite BERT for Self-Supervised Learning of Language Representations,” arXiv Preprint arXiv:1909.11942, 2019. 

38. I. Beltagy, K. Lo, and A. Cohan, “SciBERT: A Pretrained Language Model for Scientific Text,” arXiv Preprint arXiv:1903.10676, 2019. 

39. M. Polignano, V. Basile, P. Basile, M. de Gemmis, and G. Semeraro, “Alberto: Modeling Italian Social Media Language With Bert,” _IJCoL. Italian Journal of Computational Linguistics_ 5, no. 5–2 (2019): 11–31. 

40. G. Leti and L. Cerbara, _Elementi di Statistica Descrittiva_ (Il mulino, 2009). 

41. W. Cao, V. Mirjalili, and S. Raschka, “Rank Consistent Ordinal Regression for Neural Networks With Application to Age Estimation,” _Pattern Recognition Letters_ 140 (2020): 325–331. 

42. A. M. Davani, M. Díaz, and V. Prabhakaran, “Dealing With Disagreements: Looking Beyond the Majority Vote in Subjective Annotations,” _Transactions of the Association for Computational Linguistics_ 10 (2022): 92–110. 

43. M. Greenacre, _Correspondence Analysis in Practice_ (Chapman and hall/crc, 2017). 

44. J. MacQueen, “Some Methods for Classification and Analysis of Multivariate Observations,” in _Proceedings of the Fifth Berkeley Symposium on Mathematical Statistics and Probability_ . Vol. 1. Oakland, CA, USA, pp. 281–297, 1967. 

45. L. Kaufman and P. Rousseeuw, _Finding Groups in Data: An Introduction to Cluster Analysis_ (John Wiley & Sons, 2005). 

46. P. J. Rousseeuw, “Silhouettes: A Graphical Aid to the Interpretation and Validation of Cluster Analysis,” _Journal of Computational and Applied Mathematics_ 20 (1987): 53–65. 

47. N. Biasetton, R. Ricciardi, and N. Arghistani, “The VABSA Framework: A Value- and Attribute-Based Sentiment Analysis of Consumer Perceptions,” in _IES 2025 Book of Short Papers – Innovation & Society: Statistics and Data Science for Evaluation and Quality_ , 2025. 

#### **Supporting Information** 

Additional supporting information can be found online in the Supporting Information section. **Data S1:** Supporting Information. 

29. J. Devlin, M. W. Chang, K. Lee, and K. Toutanova, “BERT: Pre-Training of Deep Bidirectional Transformers for Language Understanding,” in _Proceedings of naacL-HLT_ . Vol. 1, p. 2, 2019. 

30. C. Sun, X. Qiu, Y. Xu, and X. Huang, “How to Fine-Tune Bert for Text Classification?,” in _Chinese Computational Linguistics: 18th China National Conference, CCL 2019, Kunming, China, October 18–20, 2019, Proceedings 18_ . Springer, pp. 194–206, 2019. 

31. J. S. Lee and J. Hsiang, “Patent Classification by Fine-Tuning BERT Language Model,” _World Patent Information_ 61 (2020): 101965. 

32. R. Ricciardi and M. Manisera, “A Multilingual Bert-Based Classification of Reviews for Enhanced Visitors’ Experience Analysis,” _Scientific Reports_ 15, no. 1 (2025): 31429. 

33. X. Zhang, Y. Zhang, Q. Zhang, et al., “Extracting Comprehensive Clinical Information for Breast Cancer Using Deep Learning Methods,” _International Journal of Medical Informatics_ 132 (2019): 103985. 

34. Y. Liu and M. Lapata, “Text Summarization With Pretrained Encoders,” arXiv Preprint arXiv:1908.08345, 2019. 

35. Y. Liu, M. Ott, N. Goyal, et al., “RoBERTa: A Robustly Optimized BERT Pretraining Approach,” arXiv Preprint arXiv:1907.11692, 2019. 

36. V. Sanh, L. Debut, J. Chaumond, and T. Wolf, “DistilBERT, a Distilled Version of BERT: Smaller, Faster, Cheaper and Lighter,” arXiv Preprint arXiv:1910.01108, 2019. 

14 of 14 

_Applied Stochastic Models in Business and Industry_ , 2026 

