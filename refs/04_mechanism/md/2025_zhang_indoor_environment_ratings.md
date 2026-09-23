Building and Environment 280 (2025) 113135 



Contents lists available at ScienceDirect 

# Building and Environment 

journal homepage: www.elsevier.com/locate/buildenv 



The impact of indoor environmental quality on tourist accommodation ratings using guest reviews 



Fan Zhang<sup>a,*</sup> , Karthick Seshadri<sup>b</sup> , Shichao Liu<sup>c</sup> , Matthaios Santamouris<sup>d</sup> 

a _School of Engineering and Built Environment, Griffith University, Southport, QLD, Australia_ 

b _Department of Computer Science and Engineering, National Institute of Technology Andhra Pradesh, Tadepalligudem, India_ 

c _Department of Civil, Environmental, and Architectural Engineering, Worcester Polytechnic Institute, MA, USA_ d _High Performance Architecture, School of Built Environment, University of New South Wales, Sydney, NSW, Australia_ 

### A R T I C L E I N F O 

A B S T R A C T 

_Keywords:_ Guest satisfaction is pivotal for the hospitality industry, yet the role of Indoor Environmental Quality (IEQ) in Indoor environmental quality shaping guest ratings remains inadequately explored. This study addresses this gap by leveraging web-mining, Social media natural language processing and the Three-Factor Theory to analyse guest reviews of Australian hotels and Natural language processing serviced apartments listed on Booking.com. Findings indicate that most IEQ factors—thermal comfort, indoor air Three-factor theory COVID-19 quality, luminous environment, acoustics, space, facilities, cleanliness, and layoutWhile deficiencies in these areas drive dissatisfaction, their adequacy alone does not significantly enhance —function as Basic Factors. satisfaction. Notably, exterior view serves as an Excitement Factor in budget accommodations (three stars or below) but transitions to a Basic Factor in luxury settings. Among all IEQ factors, cleanliness, indoor air quality, and acoustics had the strongest negative impacts when underperforming, whereas satisfactory exterior views, cleanliness, and available space positively influenced guest ratings. The COVID-19 pandemic intensified these effects, heightening guest sensitivity to IEQ deficiencies (e.g., poor air quality) while elevating expectations for high-performing attributes like exterior views and available space. Overall, IEQ factors accounted for 32.8 % of customer ratings in budget hotels and 23.9 % in luxury accommodations. The findings underscore the necessity of ensuring satisfactory performance across all IEQ factors, particularly cleanliness and indoor air quality, while strategically enhancing exterior views and spatial configuration to optimize guest satisfaction. These insights provide hospitality managers and policymakers with data-driven guidance for enhancing guest satisfaction and operational resilience in post-pandemic hospitality settings. 

## **1. Introduction** 

The Australian tourism industry makes a substantial contribution to the nation’s economy. In the 2023–24 financial year, tourism contributed $78.1 billion to Australia’s gross domestic product, representing 2.9 % of the national economy [1]. The industry also supported 691,500 jobs, or approximately 4.4 % of total employment in Australia [1]. Within this sector, hotels and serviced apartments dominate the accommodation landscape, catering to diverse traveller needs. Hotels typically offer fully staffed services and amenities such as restaurants, daily housekeeping, and recreational facilities, while serviced apartments—which include kitchens or kitchenettes and separate living areas—are designed for extended stays and offer more residential-style comfort at a lower nightly cost [2]. Customer satisfaction in tourist 

accommodations plays a critical role in the success of the hospitality businesses. Positive guest experiences contribute to higher loyalty, stronger brand reputation, and increased bookings. Conversely, dissatisfied travellers often share critical feedback via online platforms, which can undermine a property’s reputation and deter future customers [3,4]. 

A key but often overlooked driver of guest satisfaction is indoor environmental quality (IEQ), the physical and environmental conditions within a building that directly affect occupants’ health, comfort, and productivity [5]. It comprises various factors, including thermal comfort, indoor air quality (IAQ), luminous environment, acoustics, available space, facilities, and cleanliness, all of which collectively shape occupant experiences in built environments [6–8]. Although the significance of IEQ is widely acknowledged as an essential factor in residential, office, and healthcare settings [9–11], its role in hospitality 

* Corresponding author. _E-mail address:_ fan.zhang@griffith.edu.au (F. Zhang). 

https://doi.org/10.1016/j.buildenv.2025.113135 Received 22 February 2025; Received in revised form 3 May 2025; Accepted 5 May 2025 Available online 6 May 2025 

0360-1323/© 2025 The Author(s). Published by Elsevier Ltd. This is an open access article under the CC BY license ( http://creativecommons.org/licenses/by/4.0/ ). 

_Building and Environment 280 (2025) 113135_ 

_F. Zhang et al._ 

environments—particularly in shaping guest ratings—has received limited attention. Most existing hospitality research has focused on traditional service attributes such as service quality, location, and pricing [3,12], often overlooking the contribution of physical environmental conditions to the overall guest experience. This represents a broader research gap, as few studies have systematically examined how specific IEQ factors influence guest perceptions and ratings in hotels and serviced apartments. As the hospitality industry increasingly relies on data-driven approaches and user-generated reviews to guide service and design strategies, understanding the impact of IEQ on guest satisfaction is both timely and essential. Addressing this gap would offer valuable insights for accommodation providers, enabling them to optimize environmental quality, enhance guest satisfaction, and strengthen long-term competitive advantage. 

## _1.1. Conventional and web-mining methods to assess IEQ_ 

IEQ is traditionally assessed through an objective measurement of indoor environment parameters, subjective assessment of occupant satisfaction, or a combination of both [13]. One widely used subjective method for evaluating IEQ is Post-Occupancy Evaluation (POE), which systematically examines a building’s performance after it has been occupied. POE typically uses validated and standardised questionnaires to capture occupants’ experiences and perceptions. This approach has been extensively utilized to assess IEQ satisfaction in commercial buildings around the world, collecting feedback from occupants on various IEQ factors, along with their overall satisfaction [14,15]. These surveys can be paired with physical measurements or used independently to evaluate IEQ conditions (e.g., [16–19]). 

While POE remains a highly efficient and direct method for gaining occupant feedback—especially when compared to more experimental approaches—its effectiveness is closely tied to the design of the survey instrument itself. A growing body of research points out that many POE studies fail to include all necessary IEQ variables or use overly generalized indicators that may not comprehensively or effectively assess IEQ [20,21]. For instance, POE surveys often overlook spatial availability or cleanliness in favour of traditional factors like thermal comfort, visual comfort, acoustic comfort, and IAQ, whereas web-mining studies reveal these as critical to guest satisfaction [22–24]. Another important consideration is temporal bias: studies have identified a phenomenon known as the “honeymoon-hangover effect” [25], wherein occupants initially provide inflated satisfaction ratings shortly after moving into a building, and then satisfaction decreases with the length of time they have been there. In hospitality buildings, the ‘honeymoon-hangover effect’ may be compressed due to short stays, where initial impressions disproportionately influence ratings. These limitations highlight the need to carefully interpret POE findings, particularly in early-stage evaluations or when survey scope is narrow. 

In hospitality contexts, the challenges of implementing POE are further amplified due to the transient nature of guests, short stays, and limited post-visit contact. For example, Qi et al. [26] attempted to conduct a POE-based IEQ assessment in five-star hotels in China. Despite engaging multiple hotels, only a small number agreed to distribute questionnaires to departing guests. Among the guests that are invited, many declined to participate or did not complete the survey. This case highlights the logistical and operational barriers that can make POE methods impractical in short-term accommodation settings, particularly at scale. 

In recent years, web-mining and natural language processing (NLP) techniques have become increasingly popular for extracting insights from online reviews and analysing user-generated contents across various social media platforms and review websites. NLP, a branch of artificial intelligence (AI), enables computers to process, interpret, and analyse human language [27], while web-mining uses data mining methods to sift through massive amounts of online data and find hidden patterns that might not be obvious at first glance [28]. This procedure 

generally involves the automatic aggregation of data from several sources, including web pages, social media, and web logs. Web mining techniques are frequently utilised to evaluate consumer inputs, including reviews, to determine levels of customer satisfaction [29]. 

The hospitality sector has already leveraged these advanced methodologies to analyse customer feedback about the general hotel attributes, such as staff attitude, service, and location [3,30,31]. However, limited studies have investigated IEQ satisfaction in hospitality settings using web-mining and NLP. Given the increasing availability of large-scale guest review datasets, these techniques present a valuable opportunity to explore the role of IEQ in shaping guest ratings with greater depth and granularity. Although online reviews are self-reported and may reflect subjective viewpoints, they provide unsolicited and spontaneous guest feedback, which can offer authentic and context-rich insights into user experiences that may not be easily obtained through structured survey instruments. They also enable the analysis of diverse, longitudinal guest feedback across a broad geographic and categorical spectrum. 

The application of web-mining for IEQ assessment is still a relatively new approach within built environment community; yet some pioneering studies have already demonstrated its effectiveness in extracting meaningful insights from large-scale user-generated data. For instance, Parkinson et al. [32] investigated thermal comfort inequalities in US office buildings by analysing 16,791 tweets posted by office workers between 2010 and 2019. Ma et al. [33] collected 1.2 million Booking. com reviews and evaluated 71,665 IEQ-related comments from U.S. hotels using the sentiment analysis, finding that IAQ emerges as the most significant complaint across all climate zones, followed by visual, acoustic, and thermal discomfort. Similarly, Villeneuve & O’Brien [34] scrapped 1.35 million Airbnb reviews from six Canadian cities to examine the IEQ issues in guest accommodations using sentiment analysis. Results found that acoustics and thermal comfort complaints were the most common IEQ issues, with more cold-related complaints in winter and noise-related issues in summer. Qi et al. [26] analysed over 160,000 online reviews in China’s five-star hotels from Ctrip.com, demonstrating that 4 % of reviews contained IEQ-related complaints, with air conditioning, noise, and humidity being the most frequently mentioned issues. These studies illustrate the potential of web-mining and NLP techniques in generating data-driven insights from large, diverse datasets, offering a more scalable and representative alternative to traditional POE-based approaches. However, most prior research utilizing web-mining and NLP for IEQ assessment in hospitality settings has examined only four primary IEQ factors—thermal comfort, indoor air quality, luminous environment, and acoustics [26,33–35]. Furthermore, these studies have not examined the relative contributions of different IEQ factors to the overall accommodation ratings. Addressing this gap is critical for developing a comprehensive understanding of how various IEQ factors influence guest experiences, enabling more targeted and effective improvements in hospitality environments. 

_1.2. Asymmetric effects on customer satisfaction and the COVID-19 dynamics_ 

The Three-Factor Theory originated from the Kano Model [36]. In 1984, Professor Kano and his colleagues proposed the Kano model of attractive quality, which postulated that the individual quality attributes of a product have an asymmetric effect on overall customer satisfaction and that different attributes have varying effects. In 2008, Füller and Matzler [37] proposed the “Three-Factor Theory of Customer Satisfaction” as a modification of Kano’s theory, suggesting that customers have different levels of satisfaction with products or services based on three factors: Basic Factors, Performance Factors, and Excitement Factors. 

- Basic Factors: also known as dissatisfiers, refer to the minimum requirements that customers expect from a product or service. The 

2 

_Building and Environment 280 (2025) 113135_ 

_F. Zhang et al._ 

- absence of these factors elicits dissatisfaction; however, their presence does not guarantee satisfaction. 

- • Performance Factors: satisfaction is proportionally influenced by performance factors whereby high performance elicits satisfaction and low performance results in dissatisfaction. The effects of these attributes on overall satisfaction are linear and symmetrical. 

- • Excitement Factors: also known as satisfiers, are the extra features or characteristics that customers don’t expect, but when present, result in a significant increase in satisfaction. However, their absence does not necessarily result in dissatisfaction. 

In the hospitality sector, many studies have utilized the Three-Factor Theory to explore the uneven influence that various product and service features have on overall customer satisfaction. For example, Albayrak and Caber [38] identified that Basic Factors include entertainment, child-friendly amenities, cleanliness, food and beverage quality, staff service, pool facilities, and room d´ecor, which play a key role in satisfying hotel guests. Aspects like beach access and the technical features of hotel rooms act as Performance Factors. Additionally, Park et al. [39] examined wellness attributes in luxury hotels and found that those related to rest had the most significant impact on both satisfaction and dissatisfaction, with nutritional, social, and environmental aspects also contributing notably. Despite these insights, few studies in hospitality settings have investigated how IEQ factors influence guests’ overall ratings of the premises. The closest study may be Villeneuve & O’Brien [34], in which they compared the sentiment scores of IEQ-related comments and all comments for six Canadian cities using the independent sample _t_ -test, and found that IEQ-related comments had significantly lower sentiment scores than the general comments, indicating strong negative impact of poor IEQ on guest satisfaction. However, to the authors’ best knowledge, few existing studies has examined the impact of specific IEQ factors on guest satisfaction and tourist accommodation ratings. 

Previous studies indicate that situational factors, such as pandemics, can amplify the asymmetric effects of product and service attributes on customer satisfaction [40]. In the wake of COVID-19, cleanliness has emerged as the most critical dimension of service quality in hospitality settings, with consumers expecting rigorous sanitary measures to mitigate perceived health risks [41–44]. While IAQ is commonly viewed as a critical component of environmental quality, studies indicate that in transient settings like hotels, guests often form perceptions of air quality based on visible cleanliness and sensory cues like odour or freshness, especially when objective measurements are unavailable [45–47]. These sensory cues act as intuitive indicators of a clean and healthy environment [48,49], and likely contribute to the prominence of cleanliness in post-pandemic hospitality evaluations. As such, managing cleanliness and odour not only enhance visible hygiene and perceived air quality but may also indirectly reinforce perceptions of air safety, which became especially salient during COVID-19 [43]. 

Kim et al. [50] applied the Three-Factor Theory to assess how the pandemic impacted asymmetric effects in hotel service quality and found that COVID-19 intensified the influence of certain attributes on overall satisfaction. Similarly, Xu et al. [51] demonstrated that the pandemic reshaped the classification of Basic, Performance, and Excitement Factors in hospitality settings. However, these studies focused primarily on general hotel attributes and did not examine whether COVID-19 moderated the effects of IEQ factors on guest ratings. This gap highlights the need for further investigation into how shifting guest expectations during and after the pandemic have altered the perceived importance of IEQ in transient accommodations. 

## _1.3. Influence of individual IEQ factors on overall satisfaction and dissatisfaction_ 

Recent reviews [13,52] indicate that IEQ satisfaction impacts overall satisfaction in a complex, nonlinear manner, with individual IEQ factors 

exerting asymmetric and disproportionate effects. For instance, Tang et al. [53] found that the lowest-rated IEQ factor most strongly affects overall satisfaction, regardless of how well other factors perform. Similarly, Cao et al. [54] showed that poor thermal and acoustic conditions can significantly reduce satisfaction ratings, even if other IEQ aspects perform well. Despite these insights, many earlier studies assumed a linear relationship, overlooking the complex nonlinear associations between IEQ factors and the overall satisfaction. 

Research in IEQ confirms that factors driving dissatisfaction often differ from those contributing to satisfaction, and occupants respond differently to negative and positive environmental stimuli [9,17,55]. Kent et al. [55] analysed responses from over 36,000 office occupants and found that the primary sources of dissatisfaction were lack of visual privacy, sound privacy, noise control, and personal space. In contrast, satisfied occupants tended to report consistently high ratings across multiple IEQ factors. The study also revealed that satisfied occupants were generally more tolerant of minor shortcomings if other aspects of the workspace performed well, while dissatisfied occupants—especially those lacking privacy and space—were significantly less forgiving, even when other IEQ factors were satisfactory [55]. These findings align with the Three-Factor Theory (also known as the Kano model), which posits that certain attributes—referred to as “Basic Factors”—can lead to substantial dissatisfaction when absent, but do not notably increase satisfaction when present. 

Kim and de Dear [17] introduced the Three-Factor Theory to the built environment studies, assessing how nine IEQ dimensions from the Building Occupancy Survey System Australia (BOSSA) [56] influence workplace satisfaction. These dimensions included _spatial comfort, individual space, IAQ, thermal comfort, noise distraction & privacy, visual comfort, personal control, connection to outdoor environment, and building image & maintenance_ . Satisfaction with IEQ factors was measured by a 7-point Likert scale. To apply the Three-Factor Theory, occupant responses for each IEQ factor were divided into three performance groups: Satisfied (+2, +3), Neutral (− 1, 0, +1), and Dissatisfied (− 2, − 3). Multiple regression analysis with dummy variables assessed the impact of IEQ satisfaction on overall satisfaction, identifying three factor types: 

- Basic Factors (e.g. temperature, noise level, amount of space, visual privacy, workspace cleanliness) negatively impacted satisfaction when deficient but had limited positive effects when adequate. 

- Performance (Proportional) Factors (e.g. air quality, visual comfort, and building cleanliness and maintenance) had a direct linear relationship with satisfaction. 

- No Excitement (Bonus) Factors were identified. 

While these findings are well established in office and classroom settings, the nonlinear dynamics of satisfaction and dissatisfaction remain underexplored in hospitality contexts, where guest experiences are shorter in duration and often shaped by heightened expectations of comfort and hygiene. The applicability of the Three-Factor Theory to hotels and serviced apartments is still uncertain, as few studies have systematically classified IEQ factors based on their asymmetric effects in these transient environments. This gap presents an opportunity to deepen our understanding of how specific IEQ factors contribute differently to guest satisfaction and dissatisfaction, and how these effects manifest in online review behaviour. 

## _1.4. Research objectives and original contributions_ 

This study presents a novel integration of web-mining, deep learning-based sentiment analysis, and the Three-Factor Theory of customer satisfaction, combined with multilevel mixed-effects models, to analyse large-scale, unstructured online guest reviews for understanding the impacts of IEQ on guest ratings of tourist accommodations. The objectives are to quantify the impact of IEQ factors on customer ratings, examine the asymmetric effects through the Three-Factor 

3 

_Building and Environment 280 (2025) 113135_ 

_F. Zhang et al.                                                                                                                                                                                                                                   Building and Environment_ 

Theory, and explore how the COVID-19 pandemic has influenced this relationship. 

Unlike previous studies that applied the Three-Factor Theory to general hotel attributes or to IEQ in non-hospitality settings using survey-based methods, this study is among the first to systematically classify IEQ factors as Basic, Performance, or Excitement Factors in the context of hospitality. By leveraging NLP, this research moves beyond traditional POE methods, offering a scalable, data-driven approach that captures real-world guest perceptions with greater accuracy. 

Additionally, the study provides new insights into the effects of COVID-19 on IEQ-related satisfaction, revealing shifts in guest expectations and heightened sensitivity to certain IEQ attributes. These findings offer practical guidance for hoteliers, policymakers, and building professionals seeking to improve guest experience and resilience in post-pandemic accommodation settings. While focused on Australia, the results have broader relevance to countries with similar socio-economic conditions, as supported by comparable studies from Canada [34] and the United States [33]. 

This research builds upon our prior work [23,57], which developed the underlying guest review dataset. While that earlier study focused on general sentiment trends related to IEQ satisfaction, the present study extends the analysis by applying the Three-Factor Theory and multilevel mixed-effects models to examine the asymmetric effects of specific IEQ factors on guest ratings and to quantify the moderating impact of the COVID-19 pandemic. 

## **2. Methods** 

This study employed a multi-stage analytical approach to evaluate how IEQ influences guest ratings in hospitality accommodations, integrating web-mining, NLP, and multilevel statistical modelling. The process began with the extraction and preprocessing of 543,213 online guest reviews from Booking.com, followed by sentiment classification using a deep learning model trained on domain-specific lexicons. Reviews were categorized into sentiment groups (satisfied, neutral, dissatisfied) for nine IEQ factors. These sentiment categories were linked to numerical guest ratings (1–10 scale) and contextual metadata such as city, star rating, travel period (pre/during COVID), and traveller origin (domestic/international). 

To account for the nested structure of the data—where reviews are grouped within hotels and cities—multilevel mixed-effects regression 

models were applied. This modelling approach quantifies the unique impact of each IEQ factor on guest ratings while controlling for potential confounding variables, such as traveller origin and travel period. For instance, it adjusts for systematic differences in guest expectations between national and international travellers, or between pre- and postpandemic travellers. The Three-Factor Theory provided the theoretical framework for classifying IEQ factors into _Basic, Performance_ , and _Excitement_ categories. Fig. 1 summarizes the workflow, integrating webmining, sentiment analysis, Three-Factor Theory and Multilevel mixedeffects models. Below, we first summarize the dataset’s structure, preprocessing steps, and sentiment analysis procedures, and then detail the application of the Three-Factor Theory and multilevel mixed-effects modelling to analyse asymmetric relationships between IEQ factors and guest ratings. 

## _2.1. Dataset overview_ 

The dataset comprises 1,470,709 guest reviews scraped from Booking.com (May 2019–May 2022) for hotels and serviced apartments across ten Australian cities (e.g., Sydney, Melbourne, Brisbane, and Gold Coast). Reviews were filtered to exclude very short comments fewer than five words, resulting in 759,877 usable entries. As described in Zhang et al. [23], sentences were parsed and classified into nine IEQ factors— _thermal environment, IAQ, luminous environment, acoustics, available space, facilities, exterior view, cleanliness and maintenance,_ and _layout & design_ using a semi-supervised NLP model trained on domain-specific lexicons (Fig. 2). _Luminous environment_ refers specifically to the quality and distribution of light within a space, encompassing brightness, glare, and the intensity of natural or artificial lighting. In contrast, _exterior view_ is treated as a distinct IEQ factor, reflecting visual access to outdoor environments and the perceived quality of the view, which can have independent psychological effects on guest experience. _Available space_ pertains to guests’ perceptions of spatial volume (e.g., “spacious,” “cramped,” “enough room”), reflecting quantitative assessments of room size. _Layout & design_ focuses on the functional organization and aesthetic arrangement of interior elements. Review sentences that did not address any IEQ factors were excluded from further analysis. 

A deep learning model, specifically a Bidirectional Long Short-Term Memory (BI-LSTM) model, was trained to analyse the context of each IEQ-related review sentence and determine whether it expressed a 



**Fig. 1.** Research methods flowchart. 

4 

_Building and Environment 280 (2025) 113135_ 

_F. Zhang et al._ 



**Fig. 2.** Seed words for categorising reviews into nine IEQ factors, adapted from [23]. 

positive (satisfied), neutral, or negative (dissatisfied) sentiment toward each identified IEQ factor. The BI-LSTM architecture was selected for its ability to capture both short- and long-range dependencies in forward and backward directions, enabling more context-aware and semantically rich sentiment analysis than traditional or unidirectional models. In the IEQ literature, alternative sentiment analysis approaches have included Naïve Bayes classifiers [58], DistilBERT-based transformer models [33], and rule-based or manual keyword extraction methods [26,35]. While Naïve Bayes and rule-based methods are easier to implement, they often lack the capacity to model nuanced language. Transformer models like DistilBERT offer strong general performance but demand extensive computational resources and domain-specific fine-tuning. The BI-LSTM model used in this study offers a balanced solution—achieving high sentiment classification accuracy (92 %–96 %) while maintaining scalability and domain adaptability across multiple IEQ dimensions. Details regarding the model architecture, training algorithm, optimization objectives, and hyperparameter settings can be found in [23]. 

In our previous study [23], sentiment polarities—satisfied, neutral, and dissatisfied—were mapped onto a 9-point numerical scale, where a score of 5 represented neutrality, values above 5 indicated satisfaction, and values below 5 indicated dissatisfaction. These scores captured the intensity of sentiment expressed toward each IEQ factor. However, the present study focuses solely on the categorical sentiment polarities, in line with the requirements of the Three-Factor Theory, which operates on discrete categories rather than continuous scales. 

While other studies such as Ma et al. [33] and Guo et al. [58] also used three sentiment categories—positive, neutral, and negative—our approach differs in how the neutral polarity is defined. Instead of classifying low-intensity or ambiguous statements as neutral, we assign neutral polarity to IEQ factors that are not explicitly mentioned in a review sentence. This choice reflects the structure of Booking.com reviews, where guests are prompted to comment on both positive and negative experiences, without an option to leave sentiment-neutral feedback. As such, unmentioned aspects cannot be assumed to carry 

either positive or negative sentiment. Given that most guest reviews mention multiple IEQ factors [34,35], it is essential to distinguish between expressed sentiment and absence of mention. For instance, if a review praises the view quality but does not reference acoustics, only the view quality is assigned a satisfied polarity whereas all other unmentioned IEQ factors are marked as neutral. This ensures that sentiment classification is grounded in actual guest feedback rather than assumptions. Each review sentence is analysed by the BI-LSTM model, which assigns a distinct sentiment polarity (satisfied or dissatisfied) to each mentioned IEQ factor. A single sentence may yield multiple sentiment labels. Representative examples of each sentiment category are provided in Table 1. 

The final dataset comprised a total of 543,213 IEQ-related reviews from 1,397 hotels and serviced apartments located in ten cities across Australia. Each guest evaluated their accommodation experience using a 1–10 rating scale, as provided by the Booking.com platform. Approximately 75 % of the accommodations were concentrated in four metropolitan areas, namely Gold Coast (22.2 %), Sydney (20.6 %), Melbourne (16.7 %), and Brisbane (14.2 %). Most travellers (90.4 %) were from Australia, while only 9.6 % were from overseas. Also, 34.5 % of the trips occurred prior to the outbreak of COVID-19 in April 2020, while 65.5 % of the trips occurred during the COVID-19 period (April 2020 to May 2022, when the travel data were collected). Fig. 3 illustrates the distribution and overall rating scores of the hotels and apartments examined in the current study across various star ratings. The data imply a positive correlation between the star ratings of tourist lodgings and the average guest ratings. Fig. 4 illustrates the results of the sentiment analysis, showing the distribution of the three sentiment polarities (satisfied, neutral, and dissatisfied) across each IEQ factor. Among the reviewed comments, _facilities_ and _cleanliness & maintenance_ emerged as the most frequently discussed IEQ factors, as indicated by their lower proportions of neutral sentiment. The analysis revealed that dissatisfaction was primarily driven by issues related to _facilities_ , which accounted for 32.0 % of negative responses, followed by _cleanliness and maintenance_ at 18.2 %. Other factors contributing to guest dissatisfaction included _acoustics_ 

5 

_Building and Environment 280 (2025) 113135_ 

_F. Zhang et al._ 

**Table 1** 

Examples of sentiment classification for IEQ factors. 

|IEQ Factor|Satisfied (Positive Sentiment)|Neutral (No Mention)|Dissatisfied (Negative Sentiment)|
|---|---|---|---|
|**Thermal**|“Heaters in most rooms made it a comfortable temperature|No mention of|“Quilt too hot for weather and difficult to get room to|
|**Environment**|throughout cottage and was nice to come back to after we did a<br>ghost tour”|thermal aspect|i<br>comfortable temperature to suit”|
|**IAQ**|“Decent, good ventilation, seamless check in and check out”|No mention of air<br>quality|“So it was quite stuffy in the room”|
|**Luminous**|“Bright room”|No reference to|“Our room is a bit too dark”|
|**Environment**||luminous conditions|i|
|**Acoustics**|“The room was a great size and very quiet”|No mention of<br>acoustic aspect|“There was quite a bit of outside noise, sirens, traffic noise, etc.<br>even though we were 21 storeys up”|
|**Available Space**|“Lovely spacious room with kitchen”|No reference to room<br>size or space|<br>“for $450 a night a VERY small room (they called it "suite"....just<br>enough space for a bed, a big leather chair, and that was it…)”|
|**Facilities**|“My children loved the pool and outdoor play area”<br>i|<br>No mention of<br>facilities or amenities|<br>“The beds were a little hard”|
|**Exterior View**|“Room had a nice view and good fit out”|No mention of view|“View was blocked by adjacent building”|
|**Cleanliness& **|i<br>“I love that it was clean and the staff were super friendly”|No comment on|“Honestly, I had to really look and the only thing I could fault was<br>l|
|**Maintenance**||cleanliness|the rug on the floor in the living room, it was stained and looked<br>dirty.”|
|**Layout& Design**|“good layout, well presented and clean”|No mention of room<br>layout or design|“Room has an awkward layout”|





**Fig. 3.** Hotel/apartment distribution and performance by star rating. 



**Fig. 4.** Percentage of “satisfied,” “neutral,” and “dissatisfied” sentiment polarities across nine IEQ factors from the sentiment analysis, adapted from [23]. 

6 

_Building and Environment 280 (2025) 113135_ 

_F. Zhang et al._ 

(7.8 %), _available space_ (6.4 %), _indoor air quality_ (4.3 %), _exterior view_ (2.9 %), _luminous environment_ (2.2 %), _thermal environment_ (2.1 %), and _layout and design_ (0.2 %). 

## _2.2. Application of the three-factor theory_ 

To examine asymmetric effects of IEQ on guest ratings, this study applies the Three-Factor Theory [36]. Fig. 5 presents the conceptual framework, which explains the asymmetric relationship between an attribute’s performance and its effect on customer satisfaction. This model classifies attributes into Basic, Performance, and Excitement Factors by analysing how satisfaction levels change across different performance groups and comparing absolute differences in average satisfaction scores between these groups. An attribute is classified as a Basic Factor if the drop in satisfaction from mid-performance to low-performance is greater than the increase in satisfaction from mid- to high-performance (bottom curve in Fig. 5). This indicates that poor performance causes significant dissatisfaction, while improvements beyond an acceptable threshold yield minimal gains in satisfaction. Conversely, an Excitement Factor emerges when the increase in satisfaction from mid- to high-performance exceeds the decline from mid- to low-performance (top curve in Fig. 5), meaning that high performance substantially enhances satisfaction, but low performance does not necessarily lead to dissatisfaction. Lastly, Performance Factors exhibit a proportional relationship between performance levels and satisfaction (middle line in Fig. 5), where improvements consistently enhance satisfaction, and declines result in equivalent dissatisfaction. 

Regression models with dummy coding are frequently used in empirical research to operationalize the Three-Factor Theory [3,17,37]. Notably, the performance groups in these regression models are represented by three-level categorical independent variables: high, medium, and low. If the original independent variable is continuous or have more than three levels, it must first be transformed into a 3-level categorical variable using a logical grouping method (e.g., percentile cut-offs, sentiment analysis, or domain-specific thresholds), such as the one used in [17]. This ensures that the resulting regression coefficients reflect the satisfaction differences among the three distinct performance groups. Classification of the Three Factors was determined using the 150 % threshold criterion established in Kim and de Dear [17], where a factor was classified as a Basic Factor if its negative impact was at least 1.5 times greater than its positive impact, and as an Excitement Factor if the reverse was true. The IEQ factor was classified as a Performance Factor if neither of the conditions were met. 



**Fig. 5.** The three-factor theory (adapted from Matzler et al. [59]). 

This study employed the method depicted in Fig. 5 to investigate the individual IEQ influences on guest ratings. Fig. 5’s "Performance Axis" represents the satisfaction level of tourists with a particular IEQ factor, as determined by the sentiment analysis. The "Satisfaction Axis" corresponds to the overall customer satisfaction with the hospitality building, based on their numerical ratings of the premises. Subsequently, the study categorised IEQ performance into three levels based on sentiment polarity values for each IEQ factor: "high" (satisfied), "medium" (neutral), and "low" (dissatisfied). To represent these performance levels statistically, dummy coding was applied, a common method for categorising groups using binary variables. In accordance with existing literature, two dummy variables were created, and a 0 and 1 binary coding scheme was applied. We chose the medium IEQ performance group as the reference group because we were interested in determining whether the high IEQ performance group led to greater overall satisfaction than the mid-performance group, and whether the low IEQ performance group had lower satisfaction than the mid-performance group. The reference group had a dummy coding of (0, 0). A dummy variable (coded 1, 0) was assigned to the high-performance group, while another dummy variable (coded 0, 1) was assigned to the lowperformance group. This procedure was repeated for nine IEQ factors. 

## _2.3. Multilevel mixed-effects model_ 

This study evaluated both simple linear regression models with dummy variables and multilevel mixed-effects regression models incorporating dummy variables. The goodness-of-fit parameters were compared to identify the most suitable modelling approach. The fundamental distinction is that the former generally incorporates fixed parameter values that are derived from the sample (fixed effects), whereas the latter account for random effects, allowing intercepts and slopes to vary across hierarchical structures such as cities or hotels [60, 61]. Multilevel mixed-effects models are particularly well-suited for datasets with nested or hierarchical structures, as they model the combined influence of fixed and random effects. Fixed effects explain the population-level trends, while random effects account for context-specific variability [61]. Given the hierarchical nature of this study’s dataset, which includes customer ratings nested within hotels and cities, multilevel mixed-effects models were deemed more appropriate. The model performance metrics showed that the multilevel mixed-effects model produced a better goodness-of-fit compared to simple regression, supporting its selection for data analysis. 

The multilevel mixed-effects model used dummy coding to operationalize the Three-Factor Theory. The dependent variable was the guest rating of the premise ranging between 1 and 10 (also referred to as the overall satisfaction), and the independent variables were nine IEQ factors coded into high-, medium-, and low-performance groups. According to the findings of Li et al. [3], IEQ impacts on overall satisfaction was associated with factors such as the star ratings of the premises, locations, travellers’ origins (whether they were national or international travellers), and the year of travel. In our prior study utilising the identical dataset, it was discovered that guest ratings exhibited a statistically significant decline after the onset of the COVID pandemic (Apr 2020 in Australia) in comparison to pre-pandemic levels [23]. Hence, to accurately model the asymmetric effects of IEQ factors, the multilevel mixed-effects model accounted for the differences between cities, nationality, and time of travel in relation to COVID-19 by adding three covariates in the model. 

Given that the guest accommodations categorised as "two star" and "three star" facilities accounted for only 1.5 % and 13.7 % of the total entries in the database (Fig. 3), respectively, these two categories were combined for the purpose of conducting statistical analysis. The dataset was partitioned into three subsets based on the three categories of star ratings, specifically, three stars and below, four stars, and five stars. 

Both a two-level and a three-level hierarchical structure (customerhotel and customer-hotel-city) were tested while developing multilevel 

7 

_Building and Environment 280 (2025) 113135_ 

_F. Zhang et al._ 

mixed-effects models. In this study, a two-level structure was used since the goodness-of-fit measures and covariance parameters showed that a three-level structure did not enhance the model’s fit over a two-level structure. When developing multilevel mixed-effects models for three categories of star ratings, random slopes for all independent variables were evaluated; if they did not enhance the models’ goodness-of-fit, they were removed from the model. Eq. (1) represents the multilevel mixedeffects model being tested. In the subsequent analysis, we only report and interpret the fixed effect coefficients. Eq. (1) yields two fixed-effect coefficients for each of the nine IEQ items: one coefficient bx pertained to the high-performance group, examining the effect when the sentiment polarity of the IEQ item was satisfied, while the other coefficient bx’ pertained to the low-performance group, assessing the impact when the sentiment polarity of the IEQ item was dissatisfied. 



## where 

- _Yij_ : Guest rating for customer _i_ at lodging _j_ . 

- _HPx,ij_ and _LPx,ij_ : Dummy variables for high/low IEQ performance. 

- _b0_ and _u_ 0 _j_ : Fixed and random intercepts. 

- _bx_ and _b_<sup>ʹ</sup> _x_<sup>: Fixed effects for high/low performance groups.</sup> 

- _uxj_ and _uxj_<sup>ʹ</sup> : Random slopes. 

- Covariates: city, nationality, and time of travel. 

- Error terms: Ɛ _ij._ 

In the reference group, both dummy variables HP and LP were coded as 0, thus the model estimated the average guest ratings when IEQ satisfaction was deemed as neutral across all nine IEQ factors. This estimation was conducted for a reference city, nationality, and time of travel. In the HP group, the dummy variable HP was coded as 1, and LP was coded as 0, and the regression coefficients bx indicated the difference between the average ratings of the HP and the reference group for nine IEQ factors, respectively. Similarly, in the LP group, the dummy variable LP was coded as 1 and the HP as 0, then bx’ indicated the differences between the average ratings of the LP and the reference group. Unstandardized regression coefficients are reported, reflecting changes in overall satisfaction scores (1–10 scale) for binary predictors (satisfied/dissatisfied groups). This approach allows for direct comparison of coefficients across IEQ factors, with negative coefficients indicating the impact of dissatisfaction and positive coefficients indicating the impact of satisfaction. 

While our previous study [23] used non-parametric testing—specifically the Mann-Whitney U test—to compare average guest ratings before and during the COVID-19 pandemic, the current study adopts a more targeted approach by examining how the influence of individual IEQ factors on guest ratings changed across the two periods. To achieve this, interaction terms between IEQ sentiment groups (i.e., satisfied, neutral, and dissatisfied) and the time of travel (pre- or during COVID) were added to the multilevel mixed-effects models. Coefficients for these interactions quantified changes in the magnitude of IEQ effects during pandemic, enabling us to assess whether certain IEQ factors gained or lost importance in influencing guest satisfaction during the pandemic. 

## _2.4. Model performance metrics and diagnostic checks_ 

The coefficient of determination, denoted as R<sup>2</sup> , provides a measure of the goodness-of-fit of a model, which cannot be derived from the Akaike Information Criterion (AIC) commonly employed in multilevel mixed-effects models. The incorporation of the statistical metric “variance explained” (R<sup>2</sup> ) as a relevant summary indicator in mixed-effects models has not been frequently observed in prior studies. In this 

project, the pseudo-R<sup>2</sup> measures were computed using the methodology proposed by Nakagawa and Schieizeth [62] to illustrate the explanatory power of the developed model. The decision to utilise a multilevel mixed-effects model instead of a simple regression model was also based on the comparatively higher pseudo-R<sup>2</sup> value of the former. Unlike traditional linear regression, there are no universally accepted thresholds for interpreting R² values in multilevel models. All statistical analyses were conducted in SPSS Version 29.0. Statistical significance was set at _p <_ 0.05. 

To evaluate the robustness of the multilevel mixed-effects models, we conducted diagnostic checks aligned with Schielzeth et al. [63], who emphasize four criteria: (a) low multicollinearity, (b) approximately normal residuals, (c) homoscedasticity, and (d) independence of random effects from residuals. Variance inflation factors (VIFs) for all predictors across all models (for 3-star or below, 4-star, and 5-star properties) ranged from 1.01 to 1.20, well below the threshold of 5, indicating no multicollinearity among the independent variables. Residual normality was assessed via Q–Q plots and histograms, revealing slight positive skewness across all three sub-samples of star ratings but no extreme deviations. Homoscedasticity was confirmed through residual-versus-fitted plots, which showed constant variance across predictor levels. Random effects were inspected for normality and variance homogeneity, with no significant issues detected. While residuals were not perfectly normal, Schielzeth et al. [63] assert that fixed-effect estimates in large, balanced datasets (like _n_ = 543,213 in this study) remain robust to moderate non-normality. Thus, despite minor skewness, our models meet all robustness criteria per Schielzeth et al.’s framework, ensuring reliable interpretation of IEQ effects on guest ratings. 

## **3. Results** 

## _3.1. Effects of traveller origins and time of travel_ 

In the multilevel mixed-effects model, the reference groups were domestic travellers and those who travelled before COVID. Therefore, the regression coefficients for traveller origins represented the difference in the score ratings between international and domestic travellers. Similarly, the regression coefficients for time of travel illustrate the difference between the "travelling during COVID" group and the "travelling before COVID" group. Table 2 presents the regression coefficients for these two binary variables, broken down by star ratings. International travellers rated their accommodations 0.06 point lower (on a 10point scale) than their domestic counterparts for budget properties (3 stars or lower), and 0.04 point lower for 4-star accommodations. However, this disparity disappeared for five-star properties. The pandemic had a consistent impact on guest rating scores of all tiers of tourist accommodations—average guest ratings during COVID-19 declined by 0.60 point for budget properties, 0.53 point for 4-star hotels/apartments, and 0.66 point for luxury accommodations compared to pre- 

**Table 2** 

Regression coefficients for traveller origins and time of travel in the multilevel mixed-effects model for tourist accommodations with various star ratings. 

|Star Rating|Variable|Regression Coefficient|
|---|---|---|
|3 Star or Below|International travellers|−0.06*|
||Travelling during COVID|−0.60***|
|4 Star|International travellers|−0.04*|
||Travelling during COVID|−0.53***|
|5 Star|International travellers|n.s.|
||Travelling during COVID|−0.66***|



(***: _p <_ 0.001; *: _p <_ 0.05; n.s.: not significant. Notes: Baseline Groups = “Travelling before COVID” and “Domestic travellers”. Travels undertaken from May 2019 to March 2020 were classified as travels occurring before the COVID period, while travels undertaken from Apr 2020 and May 2022 were classified as travels during the COVID period.). 

8 

_Building and Environment 280 (2025) 113135_ 

_F. Zhang et al.                                                                                                                                                                                                                                   Building and Environment_ 

pandemic levels. This result aligned with our previous findings [23]. 

## _3.2. Asymmetric effects of IEQ factors on overall satisfaction_ 

Fig. 6 presents the regression coefficients representing the impact of various IEQ factors on guest ratings across accommodations with different star ratings (3 star or below, 4 stars, and 5 stars). The analysis is based on three multilevel mixed-effects models, each controlling for cities, traveller origin, and time of travel. The baseline group includes domestic travellers before the COVID-19 pandemic. 

Positive coefficients (mostly shown in shades of red) indicate that satisfaction with an IEQ factor is associated with an increase in the overall rating, while negative coefficients (mostly in shades of blue) indicate that dissatisfaction corresponds to a decrease in rating. For example, in budget accommodations (3 star or below), satisfaction with IAQ (HP group) increases guest ratings by 0.17 point on a 10-point scale, whereas dissatisfaction (LP group) results in a rating decrease of 0.99. This asymmetry is common across most IEQ dimensions, where dissatisfaction tends to have a stronger impact on lowering ratings than satisfaction has on raising them—as reflected in generally longer blue bars compared to red. However, not all regression coefficients have achieved statistical significance. For example, the layout and design did not achieve statistical significance in the model for 3-star or below properties, with a positive coefficient (0.04, a blue bar) for the LP group, and a negative coefficient (− 0.07, a red bar) for the HP group. 

According to this analysis, key IEQ factors with the strongest negative impacts from the LP group across all star categories include cleanliness & maintenance, IAQ, and acoustics. Meanwhile, factors such as exterior view, cleanliness & maintenance, and available space show the most significant positive influence on ratings from the HP group. These findings support the Three-Factor Theory of satisfaction, showing that negative experiences (low-performance IEQ) tend to weigh more heavily on guest perceptions than positive ones. 

When the regression coefficients for the LP group achieved statistical significance but the regression coefficients for the HP group did not, the corresponding IEQ factor can be identified as a Basic Factor without applying the 150 % threshold criterion. This is because overall satisfaction in the LP group was significantly lower than that in the midperformance group, but there was no significant difference between the mid-performance and high-performance groups. This characteristic corresponds to the definition of a Basic Factor; failure to meet the needs induces dissatisfaction, whereas meeting the needs does not guarantee 

satisfaction. In other instances, ratios between the magnitude of regression coefficients for the LP and HP groups were computed to assess the classification of an IEQ factor using the 150 % threshold criterion. The findings indicated that, except for the exterior view, all other IEQ factors were classified as Basic Factors across tourist accommodations with different star ratings. The exterior view served as an Excitement Factor in lower-end hotels and serviced apartments (three stars and below), and a Basic Factor in four- to five-star tourist lodgings. Table 3 lists the classification of nine IEQ factors across star ratings. 

## _3.3. Dynamics of IEQ impacts due to COVID-19_ 

To examine how the COVID-19 pandemic has influenced the relationship between IEQ and guest ratings, we analysed the interaction effects between IEQ factors and the time of travel. Table 4 presents the statistically significant interaction terms, with the mid-performance ("neutral sentiment") group and pre-pandemic travellers serving as baseline categories. The coefficients in Table 4 are derived from a dataset of 543,213 IEQ-related reviews, with 187,341 (34 %) collected pre-COVID (May 2019–March 2020) and 355,872 (66 %) collected during COVID (April 2020–May 2022). The regression coefficients indicate how IEQ factor effects changed during the pandemic, relative to the pre-COVID baseline. For instance, in budget accommodations, the multilevel mixed-effects model revealed a − 0.35 difference in the regression coefficient for low-performing IAQ during versus before COVID (Table 4). This suggests that during COVID, poor IAQ had an additional 0.35 point negative impact on guest ratings (on a 10-point 

**Table 3** 

Classification of IEQ factors in tourist accommodation with different star ratings. 

|IEQ Factor|Ratio (magnitude of|LP/HP)||
|---|---|---|---|
||3 Star or Below|4 Star|5 Star|
|Thermal Environment|N/A (Basic)|4.03 (Basic)|N/A (Basic)|
|Indoor Air Quality|N/A (Basic)|N/A (Basic)|N/A (Basic)|
|Luminous environment|N/A (Basic)|3.64 (Basic)|N/A (Basic)|
|Acoustics|2.65 (Basic)|3.35 (Basic)|3.85 (Basic)|
|Available Space|1.99 (Basic)|2.35 (Basic)|4.54 (Basic)|
|Facilities|N/A (Basic)|12.06 (Basic)|7.93 (Basic)|
|Exterior View|0.56 (Excitement)|1.92 (Basic)|2.61 (Basic)|
|Cleanliness&Maintenance|3.18 (Basic)|3.79 (Basic)|4.33 (Basic)|
|Layout&Design|N/A|2.06 (Basic)|N/A (Basic)|





**Fig. 6.** Positive or negative impact of nine IEQ factors on rating scores of hotels and apartments with various star ratings (Baseline Groups = “Travelling before COVID” and “Domestic travellers”). 

9 

_F. Zhang et al._ 

_Building and Environment 280 (2025) 113135_ 

**Table 4** 

Significant interaction effects between time of travel and IEQ dummy sets. 

|Star Rating|Interaction Term|Regression Coefficient (during COVID<br>relative to before COVID)|p-value for<br>Interaction Term|Coefficient (Before<br>COVID)|Coefficient (During<br>COVID)|
|---|---|---|---|---|---|
|3 Star or<br>Below|Travelling during COVID*Dissatisfied<br>IAQ<br>i|−0.35|_p<_0.001|−0.99|−1.34|
||Travelling during COVID*Dissatisfied<br>acoustics<br>i|−0.17|0.006|−0.55|−0.72|
||Travelling during COVID*Dissatisfied<br>facility<br>i|−0.14|0.002|−0.64|−0.77|
||Travelling during COVID*Dissatisfied<br>cleanliness<br>i|−0.26|_p<_0.001|−1.26|−1.53|
||Travelling during COVID*Satisfied<br>cleanliness<br>i|0.14|0.007|0.40|0.53|
|4 Star|Travelling during COVID*Dissatisfied<br>IAQ<br>i|−0.16|_p<_0.001|−0.87|−1.03|
||Travelling during COVID*Dissatisfied<br>acoustics<br>i|−0.18|_p<_0.001|−0.60|−0.78|
||Travelling during COVID*Satisfied<br>space<br>i|0.10|_p<_0.001|0.19|0.29|
||Travelling during COVID*Dissatisfied<br>facility<br>i|−0.08|_p<_0.001|−0.57|−0.65|
||Travelling during COVID*Satisfied<br>view<br>i|0.16|_p<_0.001|0.26|0.43|
||Travelling during COVID*Dissatisfied<br>cleanliness<br>i|−0.22|_p<_0.001|−1.14|−1.36|
||Travelling during COVID*Satisfied<br>cleanliness<br>i|0.08|_p<_0.001|0.30|0.38|
|5 Star|Travelling during COVID*Dissatisfied<br>IAQ<br>i|−0.12|0.014|−0.83|−0.95|
||Travelling during COVID*Dissatisfied<br>acoustics<br>i|−0.21|_p<_0.001|−0.56|−0.76|
||Travelling during COVID*Satisfied<br>space<br>i|0.12|_p<_0.001|0.10|0.21|
||Travelling during COVID*Dissatisfied<br>facility<br>i|−0.07|_p<_0.001|−0.54|−0.61|
||Travelling during COVID*Satisfied<br>facility<br>i|0.05|0.011|0.07|0.12|
||Travelling during COVID*Dissatisfied<br>view<br>i|−0.10|0.046|−0.59|−0.68|
||Travelling during COVID*Satisfied<br>view<br>i|0.17|_p<_0.001|0.22|0.40|
||Travelling during COVID*Dissatisfied<br>cleanliness<br>i|−0.22|_p<_0.001|−1.13|−1.35|
||Travelling during COVID*Satisfied<br>cleanliness|0.12|_p<_0.001|0.26|0.38|



(Notes: Baseline Groups = “Travelling before COVID” and “Domestic travellers”.). 

scale) compared to the pre-COVID period. Given the pre-pandemic coefficient for dissatisfied IAQ is − 0.99 (Fig. 6), the regression coefficient during COVID-19 can be calculated as − 0.99 - 0.35 = − 1.34. Overall, findings indicate that thermal comfort, luminous environment, and layout and design were minimally affected by the pandemic, whereas IAQ, acoustics, facilities, and cleanliness and maintenance had stronger negative effects on guest ratings during COVID-19. Conversely, highperforming IEQ factors, particularly cleanliness and maintenance, available space, and exterior views in four- and five-star accommodations, had stronger positive effects on ratings during the pandemic than before. These results highlight how guest expectations evolved in response to health and safety concerns during COVID-19. The findings also suggest that COVID-19 significantly altered the asymmetric relationship of certain IEQ factors. To assess whether the pandemic reclassified any IEQ factors under the Three-Factor framework, we adjusted the baseline group to "traveling during COVID" and re-ran the multilevel mixed-effects model. As shown in Table 5, the classifications remained largely consistent, except for exterior views in four-star hotels and apartments, which shifted from a Basic Factor before the pandemic to a Performance Factor during the pandemic. This shift suggests that during COVID-19, dissatisfaction with poor views was comparable in magnitude to the satisfaction derived from superior views. 

Findings in Tables 3 and 5 confirm that the Three-Factor Theory 

effectively explains the impact of IEQ on guest ratings in tourist accommodations. Most IEQ factors functioned as Basic Factors, meaning their absence led to dissatisfaction but their presence did not substantially enhance ratings. However, the exterior view exhibited greater variability, acting as an Excitement Factor in budget accommodations, a Basic Factor in luxury guest homes, and shifting from a Basic to a Performance Factor in four-star hotels during COVID-19. These distinctions reflect elevated guest expectations in higher-end accommodations, where pricing influences perceived value. 

## _3.4. IEQ contribution to the overall satisfaction_ 

According to Nakagawa and Schieizeth [62], the variance explained by the fixed factors is considered by the marginal R<sup>2</sup> , whereas the variance explained by both the fixed and random factors is considered by the conditional R<sup>2</sup> . Fig. 7 illustrated the marginal R<sup>2</sup> and conditional R<sup>2</sup> measures for three multilevel mixed-effects models. In hotels and serviced apartments with three stars or lower, the combined fixed and random impacts of IEQ factors were found to account for 32.8 % of the variations observed in guests’ rating scores of these establishments. It is noteworthy that the explained variance attributed to IEQ factors exhibited the highest proportion in lower-end accommodations but showed a gradual decline in middle-level (27.6 %) and higher-end guest residences (23.9 %). 

10 

_Building and Environment 280 (2025) 113135_ 

**Table 5** 

Regression coefficients for IEQ dummy sets in the multilevel mixed-effects model for travels undertaken during the pandemic while controlling for cities and traveller origins. 

|Star Rating|IEQ factors|Low IEQ Performance|High IEQ Performance|Ratio (magnitude of LP/HP)|Identification of Three Factors|
|---|---|---|---|---|---|
|3 Star or Below|Thermal Environment|−0.32***|0.05n.s.|—|Basic|
||Indoor Air Quality|−1.34***|0.38n.s.|—|Basic|
||Luminous environment|−0.23***|0.13n.s.|—|Basic|
||Acoustics|−0.72***|0.31***|2.30|Basic|
||Available Space|−0.49***|0.25***|1.99|Basic|
||Facilities|−0.77***|0.07n.s.|—|Basic|
||Exterior View|−0.28***|0.50***|0.56|Excitement|
||Cleanliness&Maintenance|−1.53***|0.53***|2.86|Basic|
||Layout&Design|0.04n.s.|−0.07n.s.|—|—|
|4 Star|Thermal Environment|−0.42***|0.11*|4.03|Basic|
||Indoor Air Quality|−1.03***|0.11n.s.|—|Basic|
||Luminous environment|−0.33***|0.09*|3.64|Basic|
||Acoustics|−0.78***|0.25***|3.15|Basic|
||Available Space|−0.45***|0.29***|1.55|Basic|
||Facilities|−0.65***|0.05***|12.40|Basic|
||Exterior View|−0.56***|0.43***|1.32|Performance|
||Cleanliness&Maintenance|−1.36***|0.38***|3.55|Basic|
||Layout&Design|−0.43***|0.21***|2.06|Basic|
|5 Star|Thermal Environment|−0.43***|0.05n.s.|—|Basic|
||Indoor Air Quality|−0.95***|0.21*|4.61|Basic|
||Luminous environment|−0.19***|0.06n.s.|—|Basic|
||Acoustics|−0.76***|0.20***|3.91|Basic|
||Available Space|−0.40***|0.21***|1.90|Basic|
||Facilities|−0.61***|0.12***|5.02|Basic|
||Exterior View|−0.68***|0.40***|1.72|Basic|
||Cleanliness&Maintenance|−1.35***|0.38***|3.57|Basic|
||Layout&Design|−0.33***|0.09n.s.|—|Basic|



(***: _p <_ 0.001; **: _p <_ 0.01; *: _p <_ 0.05; n.s.: not significant; Notes: Baseline Groups = “Travelling during COVID” and “Domestic travellers”.). 



**Fig. 7.** Multilevel mixed-effects model explanatory power by star ratings. 

## **4. Discussions** 

## _4.1. Comparison with previous studies_ 

The findings of this study reinforce the critical role of IEQ in shaping guest satisfaction, supporting research emphasizing environmental determinants of customer experience in hospitality settings [3,35]. While traditional hospitality literature has extensively examined service quality, pricing, and location as drivers of satisfaction [3,38], this study provides empirical evidence that physical environmental factors are equally influential. This aligns with environmental psychology theories, particularly Mehrabian and Russell [64]’s Stimulus-Organism-Response (SOR) model, which posits that built environment stimuli can trigger affective responses, ultimately shaping behavioural intentions such as guest satisfaction and likelihood of return visits. The strong influence of cleanliness and air quality corroborates prior studies linking IEQ to 

perceived well-being in hotels, where inadequate thermal conditions or poor ventilation significantly reduced guest comfort [26,35,65]. 

The results of this study are generally consistent with the findings of Li et al. [3], where an examination was carried out on five hotel attributes, namely “cleanliness”, “location”, “room”, “service”, and “value”. The findings revealed that these attributes were all Basic Factors for mid-range and high-end hotels. However, some attributes became Performance or Excitement Factors for budget hotels. Given that “cleanliness” and “room” attributes are largely overlapping with IEQ, their results corroborate with the current study that IEQ factors serve as the basic factors of customer satisfaction except for quality of views. 

The application of the Three-Factor Theory extends prior hospitality research focused on service quality by demonstrating asymmetric effects of IEQ attributes. For instance, cleanliness and maintenance consistently functioned as Basic Factors, echoing findings that hygiene is a nonnegotiable expectation for guests [66]. Conversely, exterior views 

11 

_Building and Environment 280 (2025) 113135_ 

_F. Zhang et al.                                                                                                                                                                                                                                   Building and Environment_ 

acted as Excitement Factors in budget hotels, paralleling research on how novelty-seeking behaviour drives satisfaction in tourism contexts [67]. These insights bridge gaps between built environment research and consumer behaviour studies, offering a holistic framework for understanding IEQ’s role in transient accommodations. 

The COVID-19 moderation analysis provide new insights into how the pandemic reshaped guest expectations for IEQ, contributing to the growing body of research on crisis-driven shifts in hospitality consumer behaviour [51,68,69]. Aligning with findings of Kim et al. [50], our results indicate that the pandemic heightened guest sensitivity to poor IEQ conditions—such as deficiencies in air quality and cleanliness—while amplifying the positive impact of high-performance IEQ features, such as good quality views and spatial adequacy. These findings corroborate with Gopalakrishna et al. [41]’s study, which has reported cleanliness and spatial adequacy as critical safety-related priorities during the pandemic. Furthermore, the habit formation theory [70] reveal that crisis-induced behavioural changes can become persistent over time. As a result, IEQ features that were previously considered premium amenities—such as air purification systems, touchless controls, and high-standard hygiene protocols—may now be perceived as baseline safety expectations by guests. 

## _4.2. Implications for building design and management_ 

The present study provided strong empirical evidence that demonstrates the substantial influence of IEQ on shaping guest satisfaction, offering practical guidance for hotel managers, policymakers, and building professionals to optimize environmental conditions in hospitality buildings. Since most IEQ factors are Basic Factors, hotel operators must ensure satisfactory performance in all IEQ aspects to avoid receiving a low rating. Specifically, poor air quality, insufficient cleaning and poor acoustics performance impose the strongest negative impact on guest satisfaction, suggesting that hotels should invest in advanced air filtration systems, adopt stricter cleaning procedures, and use eco-friendly, low-emission materials in hotel rooms to prevent dissatisfaction. The acoustics properties of the rooms are often overlooked, however, turned out to be a significant dissatisfier. Improvements can be made by installing soundproofing materials or use acoustic panels in the guest rooms to reduce noise, particularly in metropolitan areas or those with heavy traffic flow. In addition, it is imperative for the hospitality management team to persistently monitor and assess guests’ evaluations in the post-pandemic period, as the dynamics of the asymmetric relationship may undergo changes over time [50]. 

For policymakers, this study highlights the need to establish IEQ performance benchmarks for hospitality buildings. In Australia, the National Australian Built Environment Rating System (NABERS) serves as the industry standard for assessing and benchmarking the environmental performance of various building types, including offices, apartments, hotels, shopping centres, data centres, warehouses, and cold storage facilities. However, while NABERS includes a dedicated Indoor Environment (IE) rating scheme for office buildings, which evaluates IAQ, luminous environment, thermal comfort, and acoustics through a combination of POE surveys and onsite measurements, no equivalent rating scheme exists for hospitality buildings. In light of the crucial role that IEQ factors play in achieving guest satisfaction and business success, policy makers and regulatory agencies should consider making the NABERS IE rating scheme available to hospitality buildings with the assessed IEQ factors adapted to the hospitality contexts. Additionally, this study, along with our prior research, demonstrates the potential of having large-scale guest reviews, web-mining techniques, and NLP as cost-effective alternatives to traditional POE surveys. Integrating these data-driven approaches into NABERS IE assessments could enhance scalability, efficiency, and real-world applicability. 

For architects and service engineers, this study provides a critical foundation for establishing rational priorities in IEQ optimization. Rather than relying solely on subjective experience and professional 

judgment, which can vary significantly between disciplines [71], building professionals should use empirical evidence to inform design and retrofit decisions. This holds particular significance in situations where there are constraints on the resources that are accessible. In this manner, the allocation of scarce resources can be directed towards the IEQ factors that hold the greatest significance in achieving guest satisfaction. 

## _4.3. Limitations of the study_ 

This study utilized web-mining and NLP methods for data collection and processing, but these approaches have inherent limitations. The primary constraint is classification accuracy of IEQ factors. Despite efforts to filter out irrelevant keyword matches, some misclassified phrases remained, potentially affecting analysis precision. Future research could improve classification accuracy by adopting advanced NLP techniques to better contextualize textual data. 

This study focused exclusively on IEQ’s impact on guest ratings, though prior research indicates that non-IEQ attributes—such as location, pricing, staff attitude, food quality, and brand reputation—also significantly influence satisfaction. Additionally, demographic factors such as age, gender, education, and health conditions were not considered, though they may moderate guest perceptions. Future studies could incorporate these variables to refine estimates of IEQ’s effects. 

Furthermore, this study relied solely on publicly available social media data, without on-site measurements or survey-based validation. Integrating web-mined data with field studies in smaller-scale research could offer a more comprehensive understanding of IEQ’s complex relationship with guest ratings. 

## **5. Conclusion** 

This study applied web mining, NLP, the Three-Factor Theory, and multilevel mixed-effects models to examine the relationship between IEQ satisfaction and guest ratings of Australian tourist accommodations, as well as the impact of COVID-19 on this relationship. The findings indicate that IEQ significantly influences guest ratings, accounting for 32.8 % in lower-tier accommodations and 23.9 % in luxury hotels and serviced apartments. 

Most IEQ factors, including thermal comfort, indoor air quality, luminous environment, acoustics, space, facilities, cleanliness, and layout, were identified as Basic Factors, meaning guests expect these elements to function adequately. Notably, exterior views served as Excitement Factors in budget accommodations, elevating satisfaction when present, but transitioned to Basic Factors in luxury settings, reflecting heightened guest expectations. Cleanliness, IAQ, and acoustics emerged as the most influential drivers of low ratings across all hotel tiers, while satisfactory exterior views, cleanliness, and available space positively impacted ratings. The COVID-19 pandemic amplified guest sensitivity to IEQ shortcomings, particularly poor IAQ and inadequate cleanliness, while elevating expectations for high-performing attributes like exterior views and spaciousness. 

Methodologically, this study pioneers the integration of web-mining, NLP, and the Three-Factor Theory to assess IEQ impacts on guest ratings at scale, offering a replicable framework for analysing unstructured customer reviews. Practically, the findings highlight the critical role of all IEQ factors in achieving guest satisfaction, especially the need to prioritize air quality, hygiene protocols, and soundproofing while leveraging exterior views and spatial design as competitive differentiators. For policymakers, the results advocate for IEQ performance benchmarks to be integrated into building rating schemes tailored for hospitality environments. 

## **Use of AI-assisted tools** 

ChatGPT (OpenAI, USA) was used for typo correction, grammar and 

12 

_Building and Environment 280 (2025) 113135_ 

_F. Zhang et al._ 

coherence checks, and language refinement in this manuscript. It did not alter the scientific content, structure, or originality of the work. The authors independently formulated all technical descriptions, data interpretations, and conclusions. 

## **CRediT authorship contribution statement** 

**Fan Zhang:** Writing – original draft, Visualization, Software, Project administration, Methodology, Formal analysis, Data curation, Conceptualization. **Karthick Seshadri:** Writing – review & editing, Software, Methodology, Data curation. **Shichao Liu:** Writing – review & editing, Methodology, Investigation. **Matthaios Santamouris:** Writing – review & editing, Investigation. 

## **Declaration of competing interest** 

The authors declare the following financial interests/personal relationships which may be considered as potential competing interests: 

Dr Fan Zhang reports a relationship with Australian Research Council that includes: funding grants. If there are other authors, they declare that they have no known competing financial interests or personal relationships that could have appeared to influence the work reported in this paper. 

## **Data availability** 

The authors do not have permission to share data. 

## **References** 

- [1] Australian Bureau of Statistics, Tourism satellite account, tour. Satell. Acc. (2024). https://www.abs.gov.au/statistics/economy/national-accounts/tourism-satellit e-account/latest-release. (accessed April 4, 2025). 

- [2] IBIS World, Serviced apartments in Australia - market research report, (2022). https://www.ibisworld.com/default.aspx (accessed April 10, 2023). 

- [3] H. Li, Y. Liu, C.W. Tan, F. Hu, Comprehending customer satisfaction with hotels: data analysis of consumer-generated reviews, Int. J. Contemp. Hosp. Manag. 32 (2020) 1713–1735, https://doi.org/10.1108/IJCHM-06-2019-0581. 

- [4] M. Beck, Step 2: The Customer—building a Detailed Understanding of the Buyer and Customer BT - Transforming Sales Strategies: Conquering Markets Step by Step, Springer Fachmedien Wiesbaden, Wiesbaden, 2025, pp. 53–115, https://doi. org/10.1007/978-3-658-46809-5_3. M. Beck (Ed.). 

- [5] M. Awada, B. Becerik-Gerber, G. Lucas, S. Roll, Associations among home indoor environmental quality factors and worker health while working from home during COVID-19 Pandemic, ASME J. Eng. Sustain. Build. Cities (2021) 1–19, https://doi. org/10.1115/1.4052822. 

- [6] W. Chan, S.C. Lee, Y. Chen, B. Mak, K. Wong, C.S. Chan, C. Zheng, X. Guo, Indoor air quality in new hotels’ guest rooms of the major world factory region, Int. J. Hosp. Manag. 28 (2009) 26–32, https://doi.org/10.1016/j.ijhm.2008.03.004. 

- [7] M. Suh, H. Moon, H. Han, S. Ham, Invisible and intangible, but undeniable: role of ambient conditions in building hotel guests’ Loyalty, J. Hosp. Mark. Manag 24 (2015) 727–753, https://doi.org/10.1080/19368623.2014.945223. 

- [8] C. Candido, J. Zhang, J. Kim, R. De Dear, L. Thomas, P. Strapasson, C. Joko, Impact of workspace layout on occupant satisfaction, perceived health and productivity, in: F. Nicol, S. Roaf, L. Brotas, M.A. Humphreys (Eds.), proc. - 9th int. Wind. Conf. 2016 Mak. Comf. Relev., NCEUB 2016, Indoor Environmental Quality Lab, Faculty of Architecture, Design and Planning, University of Sydney, Australia, 2016: pp. 1214–1225.2025 https://www.scopus.com/inward/record.uri?eid=2-s2. 

   - 0-85055842884&partnerID=40&md5=e3311898d1d1456b4da149b1d2c298b6. 

- [9] S. Roumi, F. Zhang, R.A. Stewart, M. Santamouris, Indoor environment quality effects on occupant satisfaction and energy consumption: empirical evidence from subtropical offices, Energy Build. 303 (2024) 113784, https://doi.org/10.1016/j. enbuild.2023.113784. 

- [10] C. Wang, F. Zhang, J. Wang, J.K. Doyle, P.A. Hancock, C.M. Mak, S. Liu, How indoor environmental quality affects occupants ’ cognitive functions : a systematic review, Build. Environ. 193 (2021) 107647, https://doi.org/10.1016/j. buildenv.2021.107647. 

- [11] S. Marzban, C. Candido, B. Avazpour, M. Mackey, F. Zhang, L. Engelen, D. Tjondronegoro, The potential of high-performance workplaces for boosting worker productivity, health, and creativity: a comparison between WELL and nonWELL certified environments, Build. Environ. 243 (2023) 110708, https://doi.org/ 10.1016/j.buildenv.2023.110708. 

- [12] C. Lu, C. Berchoux, M.W. Marek, B. Chen, Service quality and customer satisfaction: qualitative research implications for luxury hotels, Int. J. Cult. Tour. Hosp. Res. 9 (2015) 168–182, https://doi.org/10.1108/IJCTHR-10-2014-0087. 

- [13] S. Roumi, F. Zhang, R.A. Stewart, M. Santamouris, Commercial building indoor environmental quality models: a critical review, Energy Build. 263 (2022) 112033, https://doi.org/10.1016/j.enbuild.2022.112033. 

- [14] C. Candido, O. Gocer, S. Marzban, K. Gocer, L. Thomas, F. Zhang, Z. Gou, M. Mackey, L. Engelen, D. Tjondronegoro, Occupants’ satisfaction and perceived productivity in open-plan offices designed to support activity-based working: findings from different industry sectors, J. Corp. Real Estate 23 (2021) 106–129, https://doi.org/10.1108/JCRE-06-2020-0027. 

- [15] S. Roumi, R.A. Stewart, F. Zhang, M. Santamouris, Unravelling the relationship between energy and indoor environmental quality in Australian office buildings, Sol. Energy 227 (2021) 190–202, https://doi.org/10.1016/j.solener.2021.08.064. 

- [16] T. Cheung, S. Schiavon, L.T. Graham, K.W. Tham, Occupant satisfaction with the indoor environment in seven commercial buildings in Singapore, Build. Environ. 188 (2021) 107443, https://doi.org/10.1016/j.buildenv.2020.107443. 

- [17] J. Kim, R. de Dear, Nonlinear relationships between individual IEQ factors and overall workspace satisfaction, Build. Environ. 49 (2012) 33–40, https://doi.org/ 10.1016/j.buildenv.2011.09.022. 

- [18] S. Nkini, E. Nuyts, G. Kassenga, O. Swai, G. Verbeeck, Evaluation of occupants’ satisfaction in green and non-green office buildings in Dar es Salaam-Tanzania, Build. Environ. 219 (2022) 109169, https://doi.org/10.1016/j. buildenv.2022.109169. 

- [19] I. Tekce, E. Ergen, D. Artan, Structural equation model of occupant satisfaction for evaluating the performance of office buildings, Arab. J. Sci. Eng. 45 (2020) 8759–8784, https://doi.org/10.1007/s13369-020-04804-z. 

- [20] J. Park, V. Loftness, A. Aziz, Post-occupancy evaluation and IEQ measurements from 64 office buildings: critical factors and thresholds for user satisfaction on thermal quality, Buildings 8 (2018), https://doi.org/10.3390/buildings8110156. 

- [21] H. Tang, Y. Ding, B. Singer, Post-occupancy evaluation of indoor environmental quality in ten nonresidential buildings in Chongqing, China, J. Build. Eng. 32 (2020) 101649, https://doi.org/10.1016/j.jobe.2020.101649. 

- [22] S. Bae, C. Martin, A. Asojo, Indoor environmental quality factors that matter to workplace occupants: an 11-year-benchmark study, Build. Res. Inf. 49 (2020) 445–459, https://doi.org/10.1080/09613218.2020.1794777. 

- [23] F. Zhang, K. Seshadri, V.P.D. Pattupogula, C. Badrinath, S. Liu, Visitors’ satisfaction towards indoor environmental quality in Australian hotels and serviced apartments, Build. Environ. 244 (2023) 110819, https://doi.org/10.1016/j. buildenv.2023.110819. 

- [24] L.T. Graham, T. Parkinson, S. Schiavon, Lessons learned from 20 years of CBE ’ s occupant surveys, Build. Cities 2 (2021) 166–184, https://doi.org/10.5334/bc.76. 

- [25] J. Xiong, T. Parkinson, J. Kim, R. De Dear, Honeymoon-hangover effect: occupant workspace satisfaction decreases over time, Indoor Environ. (2024), https://doi. org/10.1016/j.indenv.2024.100005. 

- [26] M. Qi, X. Li, E. Zhu, Y. Shi, Evaluation of perceived indoor environmental quality of five-star hotels in China: an application of online review analysis, Build. Environ. 111 (2017) 1–9, https://doi.org/10.1016/j.buildenv.2016.09.027. 

- [27] G.G. Chowdhury, Natural language processing, Annu. Rev. Inf. Sci. Technol. 37 (2003) 51–89, https://doi.org/10.1002/aris.1440370103. 

- [28] J. Han, M. Kamber, J. Pei, Data mining trends and research frontiers, in: J. Han, M. Kamber, J. Pei (Eds.), Data Mining, 3rd ed., Morgan Kaufmann, Boston, 2012, pp. 585–631, https://doi.org/10.1016/B978-0-12-381479-1.00013-7. . Concepts Tech. Vol. Morgan Kaufmann Ser. Data Manag. Syst. 

- [29] M. Alzate, M. Arce-Urriza, J. Cebollada, Mining the text of online consumer reviews to analyze brand image and brand positioning, J. Retail. Consum. Serv. 67 (2022) 102989, https://doi.org/10.1016/j.jretconser.2022.102989. 

- [30] S. Jang, T. Liu, J.H. Kang, H. Yang, Understanding important hotel attributes from the consumer perspective over time, Australas Mark. J. 26 (2018) 23–30, https:// doi.org/10.1016/j.ausmj.2018.02.001. 

- [31] B. Kim, S. Kim, C.Y. Heo, Analysis of satisfiers and dissatisfiers in online hotel reviews on social media, Int. J. Contemp. Hosp. Manag. 28 (2016) 1915–1936, https://doi.org/10.1108/IJCHM-04-2015-0177. 

- [32] T. Parkinson, S. Schiavon, R. de Dear, G. Brager, Overcooling of offices reveals gender inequity in thermal comfort, Sci. Rep. 11 (2021) 23684, https://doi.org/ 10.1038/s41598-021-03121-1. 

- [33] N. Ma, Q. Zhang, F. Murai, W.W. Braham, H.W. Samuelson, Learning building occupants’ indoor environmental quality complaints and dissatisfaction from textmining booking.Com reviews in the United States, Build. Environ. 237 (2023) 110319, https://doi.org/10.1016/j.buildenv.2023.110319. 

- [34] H. Villeneuve, W. O’Brien, Listen to the guests: text-mining Airbnb reviews to explore indoor environmental quality, Build. Environ. 169 (2020) 106555, https:// doi.org/10.1016/j.buildenv.2019.106555. 

- [35] Z. Shen, X. Yang, C. Liu, J. Li, Assessment of indoor environmental quality in budget hotels using text-mining method: case study of top five brands in China, Sustainability 13 (2021), https://doi.org/10.3390/su13084490. 

- [36] N. Kano, N. Seraku, F. Takahashi, S. Tsuji, Attractive quality and must-be quality, J. Jpn. Soc. Qual. Control 14 (1984) 39–48 (in Japanese). 

- [37] J. Füller, K. Matzler, Customer delight and market segmentation: an application of the three-factor theory of customer satisfaction on life style groups, Tour. Manag. 29 (2008) 116–126, https://doi.org/10.1016/j.tourman.2007.03.021. 

- [38] T. Albayrak, M. Caber, Prioritisation of the hotel attributes according to their influence on satisfaction: a comparison of two techniques, Tour. Manag. 46 (2015) 43–50, https://doi.org/10.1016/j.tourman.2014.06.009. 

- [39] H. Park, M. Lee, K.J. Back, Exploring the roles of hotel wellness attributes in customer satisfaction and dissatisfaction: application of Kano model through mixed methods, Int. J. Contemp. Hosp. Manag. 33 (2021) 263–285, https://doi.org/ 10.1108/IJCHM-05-2020-0442. 

13 

_Building and Environment 280 (2025) 113135_ 

_F. Zhang et al._ 

- [40] K. Matzler, B. Renzl, Assessing asymmetric effects in the formation of employee satisfaction, Tour. Manag. 28 (2007) 1093–1103, https://doi.org/10.1016/j. tourman.2006.07.009. 

- [41] S. Gopalakrishna, K. Haldorai, W. Seok, W. Gon, COVID-19 and hospitality 5.0: redefining hospitality operations, Int. J. Hosp. Manag. 94 (2021) 102869, https:// doi.org/10.1016/j.ijhm.2021.102869. 

- [42] A. Bonfanti, V. Vigolo, G. Yfantidou, The impact of the Covid-19 pandemic on customer experience design: the hotel managers’ perspective, Int. J. Hosp. Manag. 94 (2021) 102871, https://doi.org/10.1016/j.ijhm.2021.102871. 

- [43] V. Magnini, A. Zehrer, Subconscious influences on perceived cleanliness in hospitality settings, Int. J. Hosp. Manag. 94 (2020) 102761, https://doi.org/ 10.1016/j.ijhm.2020.102761. 

- [44] Y. Jiang, J. Wen, Effects of COVID-19 on hotel marketing and management: a perspective article, Int. J. Contemp. Hosp. Manag. 32 (2020) 2563–2573, https:// doi.org/10.1108/IJCHM-03-2020-0237. 

- [45] S. Zanni, M. Mura, M. Longo, G. Motta, D. Caiulo, Indoor air quality monitoring and management in hospitality: an overarching framework, Int. J. Contemp. Hosp. Manag. 35 (2023) 397–418, https://doi.org/10.1108/IJCHM-12-2021-1549. 

- [46] L. Xu, Y. Hu, W. Liang, Subjective and objective sensory assessments of indoor air quality in college dormitories in Nanjing, Build. Environ. (2022), https://doi.org/ 10.1016/j.buildenv.2022.108802. 

- [47] Y. Yang, M. Lin, V. Magnini, Do guests care more about hotel cleanliness during COVID-19? Understanding factors associated with cleanliness importance of hotel guests, Int. J. Contemp. Hosp. Manag. (2023), https://doi.org/10.1108/ijchm-082022-0956. 

- [48] G. Torriani, S. Torresin, I. Lara-Ibeas, R. Albatici, F. Babich, Perceived air quality (PAQ) assessment methods in office buildings: a systematic review towards an indoor smellscape approach, Build. Environ. (2024), https://doi.org/10.1016/j. buildenv.2024.111645. 

- [49] P. Lewkowska, T. Dymerski, J. Gębicki, J. Namie´snik, The use of sensory analysis techniques to assess the quality of indoor air, Crit. Rev. Anal. Chem. 47 (2017) 37–50, https://doi.org/10.1080/10408347.2016.1176888. 

- [50] J.M. Kim, J. Liu, K.K. Park, The dynamics in asymmetric effects of multi-attributes on customer satisfaction: evidence from COVID-19, Int. J. Contemp. Hosp. Manag. 35 (2023) 3497–3517, https://doi.org/10.1108/IJCHM-02-2022-0170. 

- [51] J. Xu, X. Wang, J. Zhang, S.S. Huang, X. Lu, Explaining customer satisfaction via hotel reviews: a comparison between pre- and post-COVID-19 reviews, J. Hosp. Tour. Manag. 53 (2022) 208–213, https://doi.org/10.1016/j.jhtm.2022.11.003. 

- [52] Y. Zhao, D. Li, Multi-domain indoor environmental quality in buildings: a review of their interaction and combined effects on occupant satisfaction, Build. Environ. 228 (2023) 109844, https://doi.org/10.1016/j.buildenv.2022.109844. 

- [53] H. Tang, Y. Ding, B. Singer, Interactions and comprehensive effect of indoor environmental quality factors on occupant satisfaction, Build. Environ. 167 (2020) 106462, https://doi.org/10.1016/j.buildenv.2019.106462. 

- [54] B. Cao, Q. Ouyang, Y. Zhu, L. Huang, H. Hu, G. Deng, Development of a multivariate regression model for overall satisfaction in public buildings based on field studies in Beijing and Shanghai, Build. Environ. 47 (2012) 394–399, https:// doi.org/10.1016/j.buildenv.2011.06.022. 

- [55] M. Kent, T. Parkinson, J. Kim, S. Schiavon, A data-driven analysis of occupant workspace dissatisfaction, Build. Environ. 205 (2021) 108270, https://doi.org/ 10.1016/j.buildenv.2021.108270. 

- [56] C. Candido, J. Kim, R. De Dear, L. Thomas, BOSSA: a multidimensional postoccupancy evaluation tool, Build. Res. Inf. 44 (2016) 214–228, https://doi.org/ 10.1080/09613218.2015.1072298. 

- [57] F. Zhang, K. Seshadri, S. Liu, Impact of indoor environmental quality satisfaction on guests’ rating of Australian tourist accommodation, in: M. Dewsbury, D. Tanton (Eds.), Proceedings of the 56th International Conference of the Architectural Science Association Science Association, Launceston, Australia, 2023, pp. 358–372. https://www.scopus.com/inward/record.uri?eid=2-s2.0-85211131708&partn 

   - erID=40&md5=6bfc47dd000c6d9ca234f31748a086ef. 

- [58] X. Guo, K. Lee, Z. Wang, S. Liu, Occupants’ satisfaction with LEED- and non-LEEDcertified apartments using social media data, Build. Environ. 206 (2021) 108288, https://doi.org/10.1016/j.buildenv.2021.108288. 

- [59] K. Matzler, F. Bailom, H.H. Hinterhuber, B. Renzl, J. Pichler, The asymmetric relationship between attribute-level performance and overall customer satisfaction: a reconsideration of the importance–performance analysis, Ind. Mark. Manag. 33 (2004) 271–277, https://doi.org/10.1016/S0019-8501(03)00055-5. 

- [60] F. Zhang, R. de Dear, Impacts of demographic, contextual and interaction effects on thermal sensation—Evidence from a global database, Build. Environ. 162 (2019) 106286, https://doi.org/10.1016/j.buildenv.2019.106286. 

- [61] A. Field, Discovering Statistics Using IBM SPSS Statistics, 4th ed., SAGE Publications, 2013. https://books.google.com.au/books?id=AlNdBAAAQBAJ. 

- [62] S. Nakagawa, H. Schielzeth, A general and simple method for obtaining R2 from generalized linear mixed-effects models, Methods Ecol. Evol. 4 (2013) 133–142, https://doi.org/10.1111/j.2041-210x.2012.00261.x. 

- [63] H. Schielzeth, N.J. Dingemanse, S. Nakagawa, D.F. Westneat, H. Allegue, C. Teplitsky, D. R´eale, N.A. Dochtermann, L.Z. Garamszegi, Y.G. Araya-Ajoy, Robustness of linear mixed-effects models to violations of distributional assumptions, Methods Ecol. Evol. 11 (2020) 1141–1152, https://doi.org/10.1111/ 2041-210X.13434. 

- [64] A. Mehrabian, J.A. Russell, An Approach to Environmental Psychology, The MIT Press, Cambridge, MA, US, 1974. 

- [65] H.S. Abdulaali, I.M.S. Usman, S. Alqawzai, Relationship between indoor environmental quality and guests’ comfort and satisfaction at green hotels: a comprehensive review, Open Eng. 14 (2024), https://doi.org/10.1515/eng-20240042. 

- [66] T. Lockyer, Hotel cleanliness—How do guests view it? Let us get specific. A New Zealand study, Int. J. Hosp. Manag 22 (2003) 297–305, https://doi.org/10.1016/ S0278-4319(03)00024-0. 

- [67] Q.N. Nguyen, H. Nguyen, T. Le, Relationships among novelty seeking, satisfaction, return intention, and willingness to recommend of foreign tourists in Vietnam, Manag. Sci. Lett. 10 (2020) 2249–2258, https://doi.org/10.5267/J. MSL.2020.3.011. 

- [68] C.K. Peres, E.P. Paladini, Quality attributes of hotel services in Brazil and the impacts of COVID-19 on users’ Perception, Sustainability (2022) 14, https://doi. org/10.3390/su14063454. 

- [69] O.A. El-Said, S. Elhoushy, M. Smith, M. Youssif, Crisis-driven innovation in hospitality: how do international hotel chains innovate to recover from a global crisis? Int. J. Hosp. Manag. 120 (2024) 103758 https://doi.org/10.1016/j. ijhm.2024.103758. 

- [70] B. Verplanken, W. Wood, Interventions to break and create consumer habits, J. Public Policy Mark. 25 (2006) 90–103, https://doi.org/10.1509/jppm.25.1.90. 

- [71] S. Roumi, F. Zhang, R.A. Stewart, M. Santamouris, Weighting of indoor environment quality parameters for occupant satisfaction and energy efficiency, Build. Environ. 228 (2023) 109898, https://doi.org/10.1016/j. buildenv.2022.109898. 

14 

