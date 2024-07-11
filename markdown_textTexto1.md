

# Detecting LLM-Generated Text in Computing Education: A Comparative Study for ChatGPT Cases

Michael Sheinman Orenstrakh

Oscar Karnalim
Although Artificial Intelligence (AI) can foster education [(9)], it might be misused to breach academic integrity. Paraphrasing tools [(40)] and code obfuscation tools [(2)] for example, are misused to cover up evidence for plagiarism (a breach of academic integrity about copying one's work and reusing it without proper acknowledgment [(14)]).

Misuse of AI chatbots with large language models (LLM) [(6)] such as ChatGPT1 is another trending threat for breaching academic integrity. Students can complete exams or assessments with limited effort, resulting in questionable performance; it is unclear whether the learning objectives are actually met. The misuse can be considered as contract cheating (i.e., getting help in exchange for mutual incentives [(27)]) since AI chatbots provide responses in exchange for additional user data. However, considering AI responses are generated based on other people's textual data without proper acknowledgment, we believe it is more justifiable to consider the misuse as plagiarism.

Footnote 1: https://openai.com/blog/chatgpt

While checking student work for plagiarism, instructors are often aided by automated detectors. A number of detectors have been developed to detect whether a work is a result of LLM. Two of them are GPT-2 Output Detector [(50)] and Giant Language model Test Room (GLTR) [(16)]. Nevertheless, due to the recency of misuse of AI chatbots, Computing educators might have limited information about publicly available detection detectors. Further, it is challenging to choose the most suitable detector for their teaching environment. To the best of our knowledge, there are no empirical studies comparing the detectors in terms of effectiveness.

In response to the aforementioned gaps, we investigate LLM-generated text detectors and formulate the following research question (RQ): "How effective are LLM-generated text detectors?"

It is clear that there is a need in the community to understand if the currently available detectors are able to detect LLM-generated content [(37; 45; 52)] and what there reliability is.

As an additional contribution, we also report our experience in using the LLM-generated text detectors. It might be useful for readers interested in employing those detectors in their classrooms.

## 2. Related Work

This section discusses common breaches of academic integrity in computing education and misuse of AI to breach academic integrity.

### Common Breaches of Academic Integrity

Academic integrity encourages students to act honestly, trustworthy, respectfully, and responsibly in learning2. Lancaster [(25)] lists five common breaches of academic integrity in computing education: plagiarism, collusion, contract cheating, exam cheating, and research fraud. It is important to inform students about instructors' expectations about academic integrity in their courses [(49)] and penalize those who breach academic integrity.

Footnote 2: https://lo.unisa.edu.au/course/view.php?id=6751&amp.section=6

Plagiarism happens when ideas, words, or even code is reused without proper acknowledgment and permission to the original author(s) [(14)]. It is commonly identified with the help of automated detectors [(3)] such as Turnitin3, Lichen [(38)], MOS4, and JPlag [(39)]. Any submissions with high similarity will be investigated and if they are indeed a result of misconduct, the students will be penalized [(20)].

Footnote 3: https://www.turnitin.com/

Nevertheless, identifying plagiarism is not always straightforward; some perpetrators disguise their act with automated paraphrasing [(23; 40)], essay spinning [(26)] or code obfuscation [(2)]. The automated detectors should be resilient to common disguising practices in addition to being effective and efficient. GPlag [(29)] and BPlag [(8)] for examples, focus on content semantic while measuring similarity among submissions. Tahaei and Noelle (2016) and Yan et al. (2017) developed detectors that detect substantial changes among consecutive saves. Ljubovic and Pajic (2017) developed a detector that is automatically integrated to a programming workspace to record any code edits.

Collusion is also about reusing ideas, words, or code without proper acknowledgment. However, the original author(s) is aware about the matter and somewhat allows it (Tahaei and Noelle, 2016). Typically, this occurs when two or more students work closely beyond reasonable levels of collaboration (Sen et al., 2017). Collusion can be identified in the same manner as plagiarism with the help of automated detectors. Similar submissions are reported by the detectors and then manually investigated by the instructors; students whose submissions are indeed a result of misconduct will be penalized.

Contract cheating occurs when third parties are paid to complete student assessments (Sen et al., 2017). The third parties can be professional companies or even their colleagues. Contract cheating is quite challenging to identify as the third parties tend to know how to evade detection. It is only identifiable when the writing style and the quality of the submission is substantially different to those of the student's prior submissions. To expedite the identification process, instructors can either use the help of authorship identification detectors (Kumar et al., 2017) such as Turnitin Authorship Investigate5(Tururthy et al., 2017) or check contract cheating sites (Sen et al., 2017).

Footnote 5: https://help.turnitin.com/MicroContent/authorship-investigate.htm

Exam cheating happens when some students have unfair advantages in the exams (Sen et al., 2017). The advantages can vary from concealed notes during exams, leaked exam questions, to impersonation (i.e., an individual switch places with a student to take the exam). Exam cheating can be identified via careful investigation on the whole process of the exams. Sometimes, such identification can be aided with online proctoring systems (Turthy et al., 2017) (e.g., Proctorio6 and ProctorExam7) or local monitoring tools (e.g., NetSupport8).

Footnote 6: https://protorio.com/

Footnote 7: https://protortexam.com/

Footnote 8: https://www.netsupportschool.com/

Footnote 9: https://grants.nih.gov/policy/research_integrity/definitions.htm

Research fraud means reporting research results without verifiable evidence (Sen et al., 2017). It can be data fabrication (i.e., generating artificial data to benefit the students) or data falsification (i.e., updating the data so that it aligns with the students' desired findings). Both are parts of research misconduct9 and they can happen in research-related assessments. Research fraud can be identified via careful investigation on the whole process of research. Due to its complex nature, such misbehaviour is manually identified on most cases. However, instructors can get some help from source metadata (Sen et al., 2017) and automated image manipulation detection (Beng et al., 2017).

Footnote 9: https://protortexam.com/

### Misuse of AI

AI substantially affects education (Beng et al., 2017). It improves student learning experience via the help of intelligent tutoring systems (Sen et al., 2017) and personalized learning materials (Sen et al., 2017). AI expedites the process of providing feedback (Beng et al., 2017), identifying breaches of academic integrity (Sen et al., 2017), maintaining student retention (Beng et al., 2017), learning programming (Sen et al., 2017), creating programming exercises (Sen et al., 2017), and recording attendance (Beng et al., 2017).

Advances in AI might also be misused for breaching academic integrity. Paraphrasing tools (Sen et al., 2017) which are intended to help students learn paraphrasing are misused to cover up plagiarism. Code generators like GitHub Copilot (Sen et al., 2017) which are intended to help programmers in developing software are misused to complete programming tasks that should be solved independently. Code obfuscation tools (Beng et al., 2017) which are intended to secure code in production are misused to disguise similarities in copied code submissions.

 AI chatbots [34], especially those with Large Language Model (LLM) [6] are intended to help people searching information, but they are misused to unethically complete exams10 and assessments11. LLM is derived from Language Model (LM), a statistical model at which each sequence of words are assigned with a probability [11]. Per query or question, the response is generated by concatenating sequences of words that have high probability with the query or the question.

Footnote 10: https://edition.cnn.com/2023/01/26/tech/chatgpt-passes-exarms/index.html

Footnote 11: https://theconversation.com/chatgpt-students-could-use-ai-to-cheat-but-its-a-chance-to-rethink-assessment-altogether-198019

ChatGPT is a popular example of LLM. The tool is developed by OpenAI, a non-profit American research laboratory on top of GPT-3, a LLM with deep learning to generate human-like text. The tool relies on reinforcement and supervised learning to further tune the model.

A number of automated detectors have been developed to help instructors identifying AI misuses for breaching academic integrity. In the context of plagiarism and collusion, automated detectors nullify common alterations that can be done without understanding the content [24; 43] and remove contents that are not evident for raising suspicion [48]. In dealing with misuses of AI chatbots, a few automated detectors are developed under the same way as the chatbots via pretrained model, but dedicated to detect AI-generated texts. GPT-2 Output Detector [50] and GLTR [16] are two of the examples.

## 3. Methodology

This section discusses how the research question stated in the introduction would be addressed and our preliminary work to discover publicly available LLM-generated text detectors.

We collected historical assignment data dating back to 2016 from two publicly funded research-focused institutions, one in North America and one in South America. The data collected was from upper-year undergraduate computer science and engineering students.

We analyzed a total of 164 submissions (124 were submitted by humans, 30 were generated using ChatGPT, and 10 were generated by ChatGPT and altered using the Quillbot paraphrasing tool) and compared them against eight LLM-generated text detectors. This results in a total of \(1,312\) prediction results.

Of the 164 submissions, 134 were written in English (20 of which were generated by a LLM, and another 10 which were LLM-generated and paraphrased) and 20 were written in Spanish (10 of which were AI-generated). The submissions were collected between 2016 and 2018 (prior to the release of ChatGPT), and were made in "databases", "networking", and a "final thesis project" course. These courses were specifically selected as they are upper-year computer science major courses that touch on a mix of systems and theory (databases and networking), as well as technical writing in computer science with a programming/development component (final thesis project). The students in these courses were primarily in a computer science major. It should also be noted that Spanish was selected as an alternative language to analyse because it is one of the world's most popular languages, and some of the authors have experience writing and evaluating technical material in this language.

The assessments analyzed in this study (see Table 1) are taken from three undergrad courses. The first course is a databases course offered to third-year computer science students in their first or second semester. It is a mix of database theory and practical systems application. There are 101 paper submissions from this course which involved a final assessment where students wrote a report analyzing two industry players and their use of databases and data centers, this was written in English.

 The second course is a networking course offered to third-year computer science students in their second semester. It is a mix of theoretical concepts and practical system application. There are 13 paper submissions from this course which involved an exam question where students explain how they would implement the NOVEL-SMTP and NEO-SMTP email protocols using only UDP, this was written in English.

The third course is a final thesis project course offered to fourth-year computer science students throughout their final year of study (across both semesters). It is meant to bridge theory and practice to develop something that can be used/implemented in the real world. There are 10 paper submissions from this course which involved improving computing systems and engineering processes in their local community, this was written in Spanish.

Due to the character limitations, data below 1,000 characters was excluded and data above 2,500 characters was truncated to the last complete sentence. This ensures the input data fits within the range of all detectors. As many LLM-generated text detection platforms have a 2,500 character maximum, to ensure fairness across platform, we used 2,500 characters as our upper-bound.

LLM-generated texts were created with the help of ChatGPT12, a popular LLM. The handouts were parsed to prompts by removing irrelevant information (course code, deadlines, submission instruction) so the prompts only contain the core requirements of the task. These prompts were then fed into ChatGPT to generate a solution to the assignment.

Footnote 12: https://openai.com/blog/chatgpt

It should be noted, the authors mined through over 2, 000 submissions in programming, data structures and algorithms, and compilers courses, however, the submission data varied too much for the content to easily be extracted and analyzed for detectors. Often due to a lack of context after removing any code. The selected submissions were purely writing-based and did not involve coding components, they did in some cases discuss theoretical concepts in computer science.

Finally, all of the detectors were tested in April 2023.

### Discovering Publicly Available LLM-generated Text Detectors

Publicly available LLM-generated text detectors were discovered from January to February 2023 from social media (i.e., Twitter, Facebook, and blogs), online news, and previous literature on LLM-generated text detection (GPT-2, GLTR). Public interest in LLM-generated text detectors followed the release of GPTZero which went viral on January, 2023. After GPTZero, many other companies launched their own LLM-generated text detectors.

A number of LLM-generated text detectors were discovered but we limited this study to LLM-generated text detectors that appear to offer proprietary solutions to LLM-generated text detection. We found that some LLM-generated text detectors are likely to be replicas of open source work (GPT-2) and hence we excluded such detectors from the study.

\begin{table}
\begin{tabular}{|p{142.3pt}|p{142.3pt}|} \hline
**Course** & **Question** \\ \hline Databases & Write a report analyzing two industry players and their use of databases and data centers. Discuss the efficiency, scalability, and social impact. \\ \hline Networking & Implement the NOVEL-SMTP and NEO-SMTP email protocols using only UDP at the transport layer. \\ \hline Thesis Project & Continuous Improvement and Operational Excellence in Manufacturing and Industrial Processes. \\ \hline \end{tabular}
\end{table}
Table 1. Questions analyzed from submissions We identified eight such publicly available LLM-generated text detectors, as shown in Table 2. Two of them (GPT-2 Output Detector and GLTR) are featured with technical reports [16; 50].

**GPT-2 Output Detector**[50] is a LLM-generated text detector based on the RoBERTa large pretrained model [30]. RoBERTa is a transformers model trained on a large corpus of raw English data. The GPT-2 Output Detector starts with the pre-trained ROBERTA-large model and trains a classifier for web data and the GPT-2 output dataset. The GPT-2 Detector returns the probability that an input text is real on GPT-2 text with accuracy of 88% at 124 million parameters and 74% at 1.5 billion parameters [50]. The detector is limited to the first 510 tokens, although there are extensions that extend this limit [36].

**GLTR**[16] is a detector that applies statistical methods to detect GPT-2 text. The model is based on three simple tests: the probability of the word, the absolute rank of a word, and the entropy of the predicted distribution. This detector shows an interface where each word is highlighted along with a top-k class for that word.

The GLTR detector does not provide quantifiable overall probability that a text is AI-generated. To make a fair comparison between GLTR and other detectors, we define a detector on top of GLTR to make probability predictions using the normal distribution. We compute an average \(\mu\) and a standard deviation \(\sigma\) over a sample dataset of 20 human and 20 ChatGPT submissions. The results were \(\mu=35.33\), and \(s=15.68\). We then used those results to normalize a prediction by computing the standard score of a data point \(x\) using \(\frac{x-\mu}{s}\). This score is sent as input to the sigmoid function to obtain a probability prediction.

**GPTZero** was the first detector [54] to claim to detect ChatGPT data. The original version of the detector used two measures: perplexity and burstiness. Perplexity refers to a measurement of how well GPT-2 can predict the next word in the text. This appears similar to the way the GLTR detector works [16]. The second measure is burstiness: the distribution of sentences. The idea is that humans tend to write with bursts of creativity and are more likely to have a mix of short and long sentence. The current version of GPTZero gives four classes of results. Table 3 shows how different classes are interpreted as probability. GPTZero claims an 88% accuracy for human text and 72% accuracy for AI text for this detector [53].

\begin{table}
\begin{tabular}{l l l} \hline \hline Name & Link & Model Info \\ \hline GPT-2 Output Detector & https://openai-openai- & Complete \\ GLTR & http://gltr.io/dist/index.html & Complete \\ CopyLeaks & https://copyleaks.com/ & None \\  & features/ai-content-detector & \\ GPTZero & https://gptzero.me/ & Partial \\ AI Text Classi- & https://platform.openai.com/ & Partial \\ fier & ai-text-classifier & \\ Originality & https://originality.ai/ & None \\ GPTKit & https://gptkit.ai/ & Partial \\ CheckForAI & https://checkforai.com/ & Partial \\ \hline \hline \end{tabular}
\end{table}
Table 2: Discovered publicly available LLM-generated text detectors; model info refers to how detailed the information of the used LLM (complete, partial, and none) 

**AI Text Classifier** is OpenAI's 2023 model fine tuned to distinguish between human-written and AI-generated text [35]. The model is trained on text generated from 34 models from 5 different organization. The model provides 5 different categories for the results based on the internal probabilities the model provides. Table 4 shows how different classes are interpreted as probability. The interpretations are based on the final category, not the internal model. Usage of this classifier requires at least 1,000 characters.

**GPTKit** uses an ensemble of 6 other models, including DistilBERT [46], GLTR, Perplexity, PPL, RoBERTa [30], and RoBERTa (base). The predictions of these models are used to form an overall probability that a text is LLM-generated. However, the exact weight used for each of the detectors is unclear. The detector claims an accuracy of 93% based on testing on a dataset of 100K+ responses [15].

**CheckForAI** claims to combine the GPT-2 Output Detector along with custom models to help limit false readings [22]. The detector also supports account sign up, history storage, and file uploads. The detector provides four classes to compute the probability of text, as shown in Table 5. This detector is currently limited to 2,500 characters.

**CopyLeaks** offers products for plagiarism and AI content detection targeted broadly for individuals, educators, and enterprises. The detector highlights paragraphs written by a human and by AI. CopyLeaks also claims detection across multiple languages, including Spanish (tested in this paper). CopyLeaks claims an accuracy of 99.12% [10]. The detector is currently available publicly [10].

\begin{table}
\begin{tabular}{l l l} \hline \hline Category & Internal Probability & Interpretation \\ \hline Very unlikely & \textless{}0.1 & 0\% \\ Unlikely & 0.1 - 0.45 & 20\% \\ Unclear & 0.45 - 0.9 & 50\% \\ Possibly & 0.9 - 0.98 & 75\% \\ Likely & \textgreater{}0.98 & 100\% \\ \hline \hline \end{tabular}
\end{table}
Table 4: AI Text Classifier interpretation.

\begin{table}
\begin{tabular}{l l} \hline \hline Category & AI Probability \\ \hline Entirely written by human & 0\% \\ Likely entirely human, but some sentences have low perplexity & 20\% \\ May contain parts written by AI & 60\% \\ Entirely written by AI & 100\% \\ \hline \hline \end{tabular}
\end{table}
Table 3: GPTZero accuracy interpretation.

\begin{table}
\begin{tabular}{l l} \hline \hline Category & AI Probability \\ \hline Low Risk & 0\% \\ Medium Risk & 60\% \\ High Risk & 80\% \\ Very High Risk & 100\% \\ \hline \hline \end{tabular}
\end{table}
Table 5: CheckForAI accuracy interpretation.



**Originality.AI** is a detector targeted for content publishers. The detector is available through a commercial sign-up page (Krishnan et al., 2018) with a minimum fee $20. We received research access for analysis of the detector. The detector comes with API access and a number of additional features for content creators. A self-proclaimed study by Originality on ChatGPT suggests that the detector has an accuracy of 98.65% (Krishnan et al., 2018).

We did not impose a systematic approach (Krishnan et al., 2018) to discover publicly available LLM-generated text detectors. Most of the detectors are recent and cannot be easily found on the internet or academic papers. A systematic approach might cover fewer results.

### Addressing the RQ: Effectiveness of LLM-generated text detectors

A detector is only worthy of use if it is reasonably effective. We addressed the RQ by comparing detectors listed in Table 2 under three metrics: accuracy, false positives, and resilience. Instructors prefer to use detectors that are reasonably accurate, reporting a minimal number of false positives, and are resilient to disguises.

Accuracy refers to how effective the detectors are in identifying LLM-generated texts. We present all accuracy results using two measures of accuracy, as we have found that using only one measure may mislead about some aspect of the results.

The first method (averages) takes the average prediction each detector across a dataset. As discussed in the discovery section, each detector either provides a probability that a text is LLM-generated or a category that represents such a probability. We apply our category to AI conversion tables to obtain a probability for each detector. These probabilities are averaged for the final results.

The second method (thresholds) is calculated as the proportion of correctly-classified LLM-generated texts. These are measured as the number of texts that correctly receive above or below a 50% score out of the total number of texts. This measure is strict, so a prediction of 50% is always considered to be incorrect.

False positives are original submissions that are suspected by LLM-generated text detectors. Fewer false positives are preferred. For this metric, we collected student submissions before the release of ChatGPT (2019) and measured their degree of originality with the detectors. Any suspected submissions (originality degree less than 50%) were expected to be false positives.

Resilience refers to how good LLM-generated text detectors are in removing disguises. Some students might disguise their LLM-generated texts to avoid getting caught. QuillBot (QuillBot, 2019) is a paraphrasing tool capable of paraphrasing text. The tool uses Artificial Intelligence to reword writing. We paraphrased 10 ChatGPT submissions through QuillBot and measured the results.

It is worth noting that measuring effectiveness of LLM-generated text detectors is time consuming and labour intensive. Further, some detectors are not supported with API integration; the authors needed to manually copy and paste each test case.

### Summarizing our experience using the LLM-generated text detectors

We also report our experience in using the LLM-generated text detectors. Several aspects are considered: intuitiveness, clarity of documentation, extendability, variety of inputs, quality of reports, number of supported LLM-generated languages, and pricing.



## 4. Results

This section discusses our findings from addressing the research question and our experience using LLM-generated text detectors.

### Addressing the RQ: Effectiveness of LLM-generated Text Detector

Table 6 shows accuracy of each detector across human and ChatGPT data using the threshold method. The data shows CopyLeaks to be the most accurate LLM-generated text detector, with an accuracy of 97.06%. CopyLeaks is followed by

\begin{table}
\begin{tabular}{l l l} \hline \hline Detectors & Human Data & ChatGPT Data \\ \hline CopyLeaks & 99.12\% & 95.00\% \\ GPT2 Detector & 98.25\% & 95.00\% \\ CheckForAI & 98.25\% & 95.00\% \\ GLTR & 82.46\% & 95.00\% \\ GPTKit & 100.00\% & 75.00\% \\ OriginalityAI & 93.86\% & 70.00\% \\ AI Text Classifier & 94.74\% & 60.00\% \\ GPTZero & 54.39\% & 45.00\% \\ \hline \hline \end{tabular}
\end{table}
Table 6. Overall accuracy of LLM-generated text detectors measured using thresholds. Sorted from best to worst.

\begin{table}
\begin{tabular}{l l l} \hline \hline Detectors & Human & ChatGPT \\  & Data & Data \\ \hline CopyLeaks & 99.06\% & 94.14\% \\ CheckForAI & 99.12\% & 94.00\% \\ GPT2 Detector & 97.88\% & 94.70\% \\ GPTKit & 95.13\% & 69.05\% \\ AI Text Classifier & 96.49\% & 67.50\% \\ OriginalityAI & 86.48\% & 66.77\% \\ GLTR & 64.19\% & 67.48\% \\ GPTZero & 73.95\% & 55.00\% \\ \hline \hline \end{tabular}
\end{table}
Table 7. Accuracy of LLM-generated text detectors measured using weighted averages. Sorted from best to worst.

\begin{table}
\begin{tabular}{l l} \hline \hline Detectors & False Positives \\ \hline GPTKit & 0 \\ CopyLeaks & 1 \\ GPT2 Detector & 2 \\ CheckForAI & 2 \\ AI Text Classifier & 6 \\ OriginalityAI & 7 \\ GLTR & 20 \\ GPTZero & 52 \\ \hline \hline \end{tabular}
\end{table}
Table 8. False positive readings on LLM-generated text detectors. Sorted from best to worst.

the GPT-2 Output Detector/CheckForAI (96.62%), GLTR (88.73%), GPTKit (87.50%), OpenAI's Detector (77.37%), and GPTZero (49.69%).

Table 7 shows the results using averages instead of thresholds. The results show CopyLeaks to provide the best probabilities (99.53%), followed by CheckForAI (96.56%), the GPT-2 Output Detector (96.29%), GPTKit (82.09%), OpenAI's Detector (82%), OriginalityAI (76.63%), GLTR (65.84%), GPTZero (64.47%).

\begin{table}
\begin{tabular}{l l l} \hline \hline Detectors & Before & After \\  & Quillbot & Quillbot \\ \hline GLTR & 76.00\% & 62.57\% \\ GPTZero & 88.00\% & 62.00\% \\ AI Text Classifier & 67.50\% & 55.00\% \\ GPT2 Detector & 99.99\% & 54.95\% \\ CheckForAI & 100\% & 44.00\% \\ OriginalityAI & 90.24\% & 40.00\% \\ CopyLeaks & 100.00\% & 39.31\% \\ GPTKit & 82.60\% & 35.50\% \\ \hline \hline \end{tabular}
\end{table}
Table 10: Resilience against Quillbot (weighted). Sorted from highest to lowest weight.

\begin{table}
\begin{tabular}{l l l} \hline \hline Detectors & Human & ChatGPT \\  & Data & Data \\ \hline AI Text Classifier & 22.50\% & 100.00\% \\ OriginalityAI & 99.40\% & 19.89\% \\ GLTR & 89.98\% & 20.70\% \\ CopyLeaks & 1.31\% & 100.00\% \\ GPT2 Detector & 99.98\% & 0.02\% \\ CheckForAI & 100\% & 0.00\% \\ GPTZero & 95.00\% & 0.00\% \\ GPTKit & 57.60\% & 36.50\% \\ \hline \hline \end{tabular}
\end{table}
Table 11: Accuracy of LLM-generated text detectors measured using weighted averages (using submissions in Spanish). Sorted from best to worst.

\begin{table}
\begin{tabular}{l l l} \hline \hline Detectors & Before & After \\  & Quillbot & Quillbot \\ \hline GLTR & 100.00\% & 100.00\% \\ GPT2 Detector & 100.00\% & 60.00\% \\ CopyLeaks & 100.00\% & 50.00\% \\ CheckForAI & 100.00\% & 40.00\% \\ OriginalityAI & 100.00\% & 40.00\% \\ GPTKit & 90.00\% & 30.00\% \\ AI Text Classifier & 60.00\% & 20.00\% \\ GPTZero & 70.00\% & 20.00\% \\ \hline \hline \end{tabular}
\end{table}
Table 9: Resilience against Quillbot (accuracy). Sorted from highest to lowest accuracy.

 The data in Tables 6 and 7 are both normally distributed, verified using the Shapiro-Wilk and Kolmogorov-Smirnov tests. Thus, no correction needed to be applied. Overall, from the t-tests (Table 6: \(t=1.67\) and \(p=0.116\), Table 7: \(t=1.154\), \(p=0.268\), both with 14 degrees of freedom) we did not find significant differences in the accuracy of LLM-generated text detectors between human and ChatGPT data.

Table 8 shows the false positive results on the human data from the databases and network assignments. GPTKit is the only detector that managed to achieve no false positives across the entire set of human submissions. This is followed by CopyLeaks (1), the GPT-2 Output Detector/CheckForAI (2), OpenAI's detector (6), OriginalityAI (7), GLTR (20), and finally GPTZero (52).

A further investigation of GPTKit, which appears to be the the best detector for avoiding false positives, shows that this detector is still prone to false positives. While none of our original test samples appeared more than 50% fake, we found that some submissions score up to 37% fake from GPTKit. In some cases, removing the last paragraph(s) from these submissions led to a false positive. Figures 1 and 2 show such a case. We note that in this case the output of GPTKit also shows that the detector merged separate paragraphs into a single one. This unexpected merge may contribute to the problem.

Table 9 shows results of 10 ChatGPT papers before and after the Quillbot paraphraser. The results are measured using overall accuracy. The GLTR detector was the most resilient, with none of the predictions changing. It is worth noting that the overall weighted result of GLTR also decreased by 10%, although the change did not effect the accuracy. In contrast, the rest of the detector saw a significant drop following the transformation of Quillbot.

\begin{table}
\begin{tabular}{l l l} \hline \hline Detectors & Human Data & ChatGPT Data \\ \hline OriginalityAI & 100.00\% & 20.00\% \\ GPT2 Detector & 100.00\% & 0.00\% \\ AI Text Classifier & 0.00\% & 100.00\% \\ GreyLeaks & 0.00\% & 100.00\% \\ CheckForAI & 100.00\% & 0.00\% \\ GLTR & 100.00\% & 0.00\% \\ GPTKit & 80.00\% & 20.00\% \\ GPTZero & 90.00\% & 0.00\% \\ \hline \hline \end{tabular}
\end{table}
Table 12: Overall accuracy of LLM-generated text detectors measured using thresholds (using submissions in Spanish). Sorted from best to worst.

Figure 1: Report introduction with 37% AI Probability on GPTKit.

 Figures 3 and 4 show an example of a ChatGPT data point that went from 98% before Quillbot to 5% after Quillbot on Originality.

Manuscript submitted to ACM

Figure 4: ChatGPT report plugged to Originality AI after Quillbot .

Figure 3: ChatGPT report plugged to Originality AI before Quillbot .

Figure 2: Truncated introduction with 54% AI Probability on GPTKit.

 Tables 11 and 12 show results from the capstone course data, written using Spanish. We found that CopyLeaks and the AI Text Classifier tend always output fake predictions on AI data. In contrast, the GPT-2 Output Detector, GPTZero, CheckForAI, GLTR, GPTKit, and Originality tend to output human predictions.

The data in Tables 11 and 12 are both normally distributed, verified using the Shapiro-Wilk and Kolmogorov-Smirnov tests. Thus, no correction needed to be applied. Overall, from the t-tests (Table 11: \(t=1.766\) and \(p=0.099\), Table 12: \(t=1.862\), \(p=0.084\), both with 14 degrees of freedom) we did not find significant differences in the accuracy of LLM-generated text detectors between human (Spanish text) and ChatGPT (Spanish text) data.

The GLTR detector shows an interesting mild success with Spanish data. The average top-k score on human data was 104, while the average top-\(k\) score on ChatGPT data was 85. When we changed the implementation of GLTR to set a mean of a 94.5 top-k score, GLTR managed to achieve the highest accuracy of 65% on Spanish text.

### Our experience using the LLM-generated text detectors

Generally, many LLM-generated text detectors are intuitive to use. Similar with many online similarity detectors for identifying text plagiarism [(3)]. They have a web-based interface where a user can paste the text they want to check its originality. GPTZero and CheckForAI allow their users to upload a document instead.

While there are a number of LLM-generated text detectors, only two of them have their technical reports publicly available (GPT-2 Output Detector [(50)] and GLTR [(16)]). This is possibly due to at least two reasons. First, technical reports might be misused by some individuals to trick the detectors. Second, some detectors are commercial.

Most LLM-generated text detectors do not facilitate API integration. GPTZero, GPTKit, OriginalityAI, CopyLeaks provide such a feature with a fee. Without API integration, it is challenging to integrate the detectors to existing teaching environments, especially learning management system. LLM-generated text detectors are unlikely to be independently used as the task is labor intensive.

As many of the detectors are commercial, their code is not publicly available. This might complicate instructors to further develop the detectors to fit their particular needs. The only open source detectors are the GPT-2 Output Detection and GLTR.

The detectors are also limited in the input formats they support. Most of them only allow raw text pasted in a form, making them difficult to automate. The PDF parsers that we attempted to use often parsed in an incorrect order and had a tendency to include unwanted characters. We had to write custom scripts to parse the text in a format that translates all information to text.

Detection results are challenging to interpret. Detectors attempt to combat this problem by highlighting content that is more likely to be AI-generated. Table 13 shows the highlighting support each detector provides. Highlighting is provided on either a paragraph, sentence, or a word basis.

While highlighting does seem to mitigate some barriers, we found that the highlighting feature can still be misleading. This was particularly evident in GPTZero, which highlighted 52 human submissions as either possibly or entirely AI-generated. Figure 5 shows a sample human report where some sentences were highlighted as more likely to be written by AI. It is unclear what makes the highlighted text more likely be written by AI than the other sentences.

In terms of output quality, it seems like the detectors are limited in their ability to export results. Nevertheless, some detectors were more effective than others. We provided screenshots of GPTKit, GPTZero, and Originality in this report since they provided more detailed results and it was easier to screenshot the results along with the text in contrast to the other detectors. It was more challenging to show full results of other detectors as they did not allow side-by-side results.

 

## 6. Conclusion

\begin{table}
\begin{tabular}{l l} \hline \hline Detector & Highlighting support \\ \hline GPT2 Detector & None \\ AI Text Classifier & None \\ CopyLeaks & Paragraphs \\ CheckForAI & Sentences \\ GPTZero & Sentences \\ GLTR & Words \\ GPTKit & Paragraphs \\ OriginalityAI & Sentences \\ \hline \hline \end{tabular}
\end{table}
Table 13. Highlighting support per detector.

Figure 5. A false positive using GPTZero.

Most LLM-generated text detectors only support English as the language of LLM-generated text. While one can still send text in other languages, the results do not appear meaningful as we previously showed.

As many LLM-generated text detectors are commercial and they are relatively new, there appear to mostly individual pricing options. GPTZero CopyLeaks, for instance, have business pricing. GPTZero currently has a subscription plan for business users for $19.99USD per month.

These detectors might be far less useful for instructors living in countries with weak currency; the pricing options are only available in USD.

## 5. Discussion

The current state of LLM-generated text detectors suggests that they are not yet ready to be trusted blindly for academic integrity purposes or as reliable plagiarism detectors such as Turnitin, MOSS, or JPlag. Our study demonstrates that detectors under-perform compared to the GPT-2 Output Detector and GLTR, which are older and freely available detectors from 2019.

At first glance, it appears that LLM-generated text detectors are fairly accurate with human data being correctly detected \(\sim 89.59\%\)13 while the average accuracy for ChatGPT-generated data is substantially lower; \(\sim 77.42\%\)14. Upon deeper inspection, it is apparent that the number of potential false positives can lead to a wide array of issues, especially if being trusted for plagiarism detection at educational institutions.

Footnote 13: this percentage is the average accuracy for human data using Tables 6 and 7.

Delving further, when a paraphraser (in this case, QuillBot) is utilized the average accuracy is slightly reduced for human data \(\sim 89.02\%\)15 but this substantially reduces the accuracy of ChatGPT-generated data \(\sim 49.17\%\)16. This means that in more than half of all cases, ChatGPT-generated data cannot correctly be identified by these detectors. Though, some detectors perform better than others (e.g., GLTR), it is still a serious concern for users of these detectors.

Footnote 15: this percentage is the average accuracy for ChatGPT-generated data using Tables 6 and 7.

Additionally, once non-English languages are introduced, these detectors are easily exacerbated. We investigate submissions made in Spanish and see that the average accuracy for human data lowers to an average of \(\sim 70.99\%\)17, and ChatGPT-generated data reduces to an abysmal \(\sim 17.50\%\)18. Though only Spanish was investigated, it introduces the need for additional research into alternative languages (non-English).

Footnote 15: this percentage is the average accuracy for human data using Tables 6 and 7.

Presently, all LLM-generated text detectors struggle with languages other than English, code, and special symbols, resulting in fairly inaccurate results. As a point of clarity, it would be ideal for these detectors to explicitly state their limitations and aim to produce human predictions in such cases.

In terms of usability, LLM-generated text detectors need some improvements. Although they are intuitive to use and generate acceptable reports, many of them are not well documented at a technical level, some do not have APIs making them more difficult to integrate into local and larger systems (e.g., Learning Management Systems), and the support of these detectors is limited. Furthermore, some of these detectors require processing fees.

From our results, LLM-generated text detectors appear to lack in understandability. We are aware that all of these detectors leverage similar large language models for detection purposes. However, they might differ in terms of their technical implementation, parameters, pre-trained data, etc. These are unlikely to be revealed since most of the detectors are for commercial-use and, thus, proprietary. While some detectors highlight sentences that are more likely to be AI-generated (Table 13), the results produced by the detectors are not clear enough for users of these detectors.

## 6. Threats to Validity

Our study has several threats to validity:

* The findings of the study reflect detector results that are accurate as of April 2023. The detectors are volatile, and owners of these detectors could update their models. Results could change based on updates to LLM-generated text detectors.
* Accuracy, false positives, and resilience were arguably sufficient to represent effectiveness. However, additional findings can be obtained by considering other effectiveness metrics.
* The data sets were obtained from two institutions; one uses English as the operational language while another uses Spanish. This means that the findings might not be generalizable to other institutions, especially those with different operational languages.
* While we believe that the data sets are sufficient to support our findings, we acknowledge that more data sets can strengthen the findings.

## 7. Conclusion

This paper examines eight LLM-generated text detectors on the basis of effectiveness. The paper shows that while detectors manage to achieve a reasonable accuracy, they are still prone to flaws and can be challenging to interpret by the human eye. Ultimately, LLM-generated text detectors, while not yet reliable for academic integrity or plagiarism detection, show relatively accurate results for human-generated data compared to ChatGPT-generated data. However, false positives are a significant concern, especially when used for plagiarism detection in educational institutions. When a paraphrasing tool like QuillBot is employed, the accuracy decreases for both human and ChatGPT-generated data. Additionally, the detectors struggle with non-English languages, resulting in even lower accuracy. It is crucial for these detectors to acknowledge their limitations and aim for improved performance in various language contexts.

### Future Work

Future detectors could attempt to incorporate a combination of metrics along with their accuracy for AI detectors. A combination of many factors along with the accuracy and false positive rates may give educators better insights into the predictions. This could include text-based features such as burstiness and repetition as well as AI-learned features such as probabilities. These detectors could further be fine-tuned for specific domains to improve their reliability.

Additionally, there is a fundamental need to have accurate and understandable LLM-generated text detectors available for educators to combat against the rising concern of academic integrity due to these publicly available LLMs. It is also important for the researchers to contact the creators of these detectors to better understand the related issues and needs of the end users, but also to facilitate a deeper conversation about the functionality and correctness of their instruments.

Finally, there is an apparent need to investigate the use of non-English languages using these detectors as large language models, like the one(s) used by ChatGPT, can produce content in languages other than English.

## References

* (1)
* Alberaki et al. (2021) Balqis Alberaki, Nazar Zaki, and Hany Alashwal. 2021. A Systematic Literature Review of Student' Performance Prediction Using Machine Learning Techniques. _Education Sciences_ 11, 9 (2021). https://doi.org/10.3390/educsci11909552 * Behera and Bhaskari (2015) Chandan Kumar Behera and D Lalitha Bhaskari. 2015. Different obfuscation techniques for code protection. _Procedia Computer Science_ 70 (2015), 757-763.
* Blanchard et al. (2022) Jeremiah Blanchard, John R. Hott, Vincent Berry, Rebecca Carroll, Bob Edmison, Richard Glassey, Oscar Karnalim, Brian Plancher, and Seain Russell. 2022. Stop Reinventing the Wheel! Promoting Community Software in Computing Education. In _2022 Working Group Reports on Innovation and Technology in Computer Science Education_ (Dublin, Ireland). Association for Computing Machinery, 261-292. https://doi.org/10.1145/3571785.3574129
* Bucci (2018) Enrico M. Bucci. 2018. Automatic detection of image manipulations in the biomedical literature. _Cell Death & Disease_ 9 (2018). https://doi.org/10.1038/s41419-018-0430-3
* Image Based Attendance System: A Low Cost Solution to Record Student Attendance in a Classroom. In _2018 IEEE International Symposium on Multimedia (ISM)_ 259-266. https://doi.org/10.1109/ISM.2018.00037
* Carlini et al. (2021) Nicholas Carlini, Florian Tramer, Eric Wallace, Matthew Jagielski, Ariel Herbert-Voss, Katherine Lee, Adam Roberts, Tom B Brown, Dawn Song, Ulfar Erlingsson, et al. 2021. Extracting Training Data from Large Language Models.. In _USENIX Security Symposium_, Vol. 6.
* Cavalcanti et al. (2021) Anderson Pinheiro Cavalcanti, Arthur Barbosa, Ruan Carvalho, Fred Freitas, Yi-Shan Tsai, Dragan Gasevic, and Rafael Ferreira Mello. 2021. Automatic feedback in online learning environments: A systematic literature review. _Computers and Education: Artificial Intelligence_ 2 (2021), 100027. https://doi.org/10.1016/j.caea.2021.100027
* Cheers et al. (2021) Hayden Cheers, Yuqing Lin, and Shannus P. Smith. 2021. Academic source code plagiarism detection by measuring program behavioral similarity. _IEEE Access_ 9 (2021), 50391-50412. https://doi.org/10.1109/ACCESS.2021.3069367
* Chen et al. (2020) Lijia Chen, Pingping Chen, and Zhijian Lin. 2020. Artificial Intelligence in Education: A Review. _IEEE Access_ 8 (2020), 75264-75278. https://doi.org/10.1109/ACCESS.2020.2988510
* CopyLeaks (2023) CopyLeaks. 2023. CopyLeaks AI Content Detector beta. Accessed: 2023-03-01. https://copyleaks.com/ai-content-detector.
* Croft et al. (2010) W Bruce Croft, Donald Metzler, and Trevor Strohman. 2010. _Search Engines: Information Retrieval in Practice_.
* Dawson et al. (2020) Phillip Dawson, Wendy Sutherland-Smith, and Mark Ricksen. 2020. Can software improve marker accuracy at detecting contract cheating? A pilot study of the Turnitin authorship investigate alpha. _Assessment & Evaluation in Higher Education_ 45, 4 (2020), 473-482. https://doi.org/10.1080/02602938.2019.1662884
* Dendir and Maxwell (2020) Seife Dendir and R. Stockton Maxwell. 2020. Cheating in online courses: Evidence from online proctoring. _Computers in Human Behavior Reports_ 2 (2020), 100033. https://doi.org/10.1016/j.chbr.2020.100033
* Fraser (2014) Robert Fraser. 2014. Collaboration, collusion and plagiarism in computer science coursework. _Informatics in Education_ 13, 2 (2014), 179-195. https://doi.org/10.15388/infelou.2014.10
* Ganesh (2023) Sachin Ganesh. 2023. GPTKit. Accessed: 2023-03-01. https://quillbot.com/.
* Gehrmann et al. (2019) Sebastian Gehrmann, Hendrik Strobelt, and Alexander M. Rush. 2019. GLTR: Statistical Detection and Visualization of Generated Text. https://doi.org/10.48550/ARKIV.1906.04043
* Gillham (2023) Jonathan Gillham. 2023. Can Originality.AI Detect GPT 3, GPT 3.5 And ChatGPT Generated Text? Accessed: 2023-03-01. https://originality.ai/can-gpt-3-5-chatgpt-be-detected.
* Gillham (2023) Jonathan Gillham. 2023. Originality AI Content Detector. Accessed: 2023-03-01. https://originality.ai/.
* Kale and Prasad (2017) Sunil Digamberrao Kale and Rajesh Shardanand Prasad. 2017. A systematic review on author identification methods. _International Journal of Rough Sets and Data Analysis (JJRSDA)_ 4, 2 (2017), 81-91.
* Karnalim et al. (2019) Oscar Karnalim, Simon, and William Chivers. 2019. Similarity detection techniques for academic source code plagiarism and collusion: a review. In _IEEE International Conference on Engineering, Technology and Education_. https://doi.org/10.1109/TALE48000.2019.9225953
* A systematic literature review. _Information and Software Technology_ 51, 1 (2009), 7-15. https://doi.org/10.1016/j.infsof.2008.09.009
* Klieger (2023) Benjamin Klieger. 2023. CheckForAI. Accessed: 2023-03-01. https://checkforai.com/.
* Krishna et al. (2023) Kalpesh Krishna, Yixiao Song, Marzena Karpinska, John Wieting, and Mohit Iyyer. 2023. Paraphrasing evades detectors of AI-generated text, but retrieval is an effective defense. arXiv:2303.13408 [cs.CL]
* Krizkova et al. (2016) Sarka Krizkova, Hana Tomaskova, and Martin Gavalec. 2016. Preference comparison for plagiarism detection systems. In _2016 IEEE International Conference on Fuzzy Systems (FUZZ-IEEE)_. IEEE, 1760-1767.
* Lancaster (2018) Thomas Lancaster. 2018. Academic integrity for computer science instructors. In _Higher Education Computer Science_. 59-71. https://doi.org/10.1007/978-3-319-98590-9_5
* Lancaster and Clarke (2009) Thomas Lancaster and Robert Clarke. 2009. Automated essay spinning-an initial investigation. In _10 th Annual Conference of the Subject Centre for Information and Computer Sciences_. 25.
* Lancaster and Clarke (2016) Thomas Lancaster and Robert Clarke. 2016. Contract cheating: The outsourcing of assessed student work. _Handbook of academic integrity_ 1 (2016), 639-654.
* Li and Wong (2021) Kam Cheong Li and Billy Tak-Ming Wong. 2021. Features and trends of personalised learning: a review of journal publications from 2001 to 2018. _Interactive Learning Environments_ 29, 2 (2021), 182-195. https://doi.org/10.1080/10494820.2020.1811735
* Liu et al. (2006) Chao Liu, Chen Chen, Jiawei Han, and Philip S Yu. 2006. GPlag: detection of software plagiarism by program dependence graph analysis. In _12th ACM SIGKDD International Conference on Knowledge Discovery and Data Mining_. 872-881. https://doi.org/10.1145/1150402.1150522 * Liu et al. (2019) Yinhan Liu, Myle Ott, Naman Goyal, Jingfei Du, Mandar Joshi, Danqi Chen, Omer Levy, Mike Lewis, Luke Zettlemoyer, and Veselin Stoyanov. 2019. RoBERTa: A Robustly Optimized BERT Pretraining Approach. https://doi.org/10.48550/ARKIV.1907.11692
* Ljubovic and Pajic (2020) Vedran Ljubovic and Enil Pajic. 2020. Plagiarism detection in computer programming using feature extraction from ultra-fine-grained repositories. _IEEE Access_ 8 (2020), 96505-96514. https://doi.org/10.1109/ACCESS.2020.2996146
* Dakhel et al. (2023) Arghavan Moradi Dakhel, Vahid Majdinasab, Amin Nikanjam, Foutse Khomh, Michel C. Desmarais, and Zhen Ming (Jack) Jiang. 2023. GitHub Copilot AI pair programmer: Asset or Liability? _Journal of Systems and Software_ 203 (2023), 111734. https://doi.org/10.1016/j.jss.2023.11734
* Mousavinasab et al. (2021) Elham Mousavinasab, Nahid Zarifsanaiey, Shararek R. Niakan Kalhori, Mahnaz Rakhshan, Leila Keikha, and Marjan Ghazi Saeedi. 2021. Intelligent tutoring systems: a systematic review of characteristics, applications, and evaluation methods. _Interactive Learning Environments_ 29, 1 (2021), 142-163. https://doi.org/10.1080/10494820.2018.1558257
* Nicolescu and Tudorache (2022) Luminita Nicolescu and Monica Tcedorac. 2022. Human-Computer Interaction in Customer Service: The Experience with AI Chatbotts& A Systematic Literature Review. _Electronics_ 11, 10 (2022). https://doi.org/10.3390/electronics11101579
* OpenAI (2023) OpenAI. 2023. AI Text Classifier. Accessed: 2023-01-31. https://beta.openai.com/ai- text-classifier.
* Orenstrakh (2023) Michael Sheimman Orenstrakh. 2023. How I Improved the GPT2 Output Detector. Accessed: 2023-03-01. https://medium.com/gopenai/how-i-improved-the-gpt2-output-detector-fe4?ba133235.
* Perkins et al. (2023) Mike Perkins, Jasper Roe, Darius Postma, James McGaughran, and Don Hickerson. 2023. Game of Tones: Faculty detection of GPT-4 generated content in university assessments. _arXiv preprint arXiv:2305.18081_ (2023).
* Peeveler et al. (2019) Matthew Peeveler, Tushar Gurjar, Evan Macius, Andrew Aikens, Alexander Christoforides, and Barbara Cutler. 2019. Lichen: customizable, open source plagiarism detection in Submitry. In _50th ACM Technical Symposium on Computer Science Education_. https://doi.org/10.1145/3287324.3293867
* Prechelt et al. (2002) Lutz Prechelt, Guido Malpohl, and Michael Philippsen. 2002. Finding plagiarisms among a set of programs with JPlag. _Journal of Universal Computer Science_ 8, 11 (2002), 1016-1038.
* Prentice and Kinden (2018) Felicity M. Prentice and Clare E. Kinden. 2018. Paraphrasing tools, language translation tools and plagiarism: an exploratory study. _International Journal for Educational Integrity_ 14 (2018), 11. https://doi.org/10.1007/s40979-018-0036-7
* Puryear and Sprint (2022) Ben Puryear and Gina Sprint. 2022. Github copilot in the classroom: learning to code with AI assistance. _Journal of Computing Sciences in Colleges_ 38, 1 (2022), 37-47.
* Quillbot (2023) Quillbot. 2023. Quillbot. Accessed: 2023-03-01. https://quillbot.com/.
* Raghkitwetsagul et al. (2018) Chaiyong Raghkitwetsagul, Jens Krinke, and David Clark. 2018. A comparison of code similarity analysers. _Empirical Software Engineering_ 23, 4 (2018), 2464-2519. https://doi.org/10.1007/s10664-017-9564-7
* Rowland et al. (2018) Susan Rowland, Christine Slade, Kai-Sheng Wong, and Brooke Whiting. 2018. 'Just turn to us': the persuasive features of contract cheating websites. _Assessment & Evaluation in Higher Education_ 43, 4 (2018), 652-665. https://doi.org/10.1080/02602938.2017.1391948
* Sadasivan et al. (2023) Vinu Sankar Sadasivan, Aounon Kumar, Sriram Balasubramanian, Wenxiao Wang, and Soheil Feizi. 2023. Can AI-Generated Text be Reliably Detected? arXiv:2303.11156 [cs.CL]
* Sanh et al. (2019) Victor Sanh, Lysandre Debut, Julien Chaumond, and Thomas Wolf. 2019. DistilBERT, a distilled version of BERT: smaller, faster, cheaper and lighter https://doi.org/10.48550/ARKIV.1910.01108
* Volume 1_ (Lugano and Virtual Event, Switzerland) _(ICER '22)_. Association for Computing Machinery, New York, NY, USA, 27-43. https://doi.org/10.1145/3501385.3543957
* Samon et al. (2020) Simon, Oscar Karnalim, Judy Sheard, Ilor Dema, Amey Karkare, Juho Leinonen, Michael Latt, and Renee McCauley. 2020. Choosing Code Segments to Exclude from Code Similarity Detection. In _ACM Working Group Reports on Innovation and Technology in Computer Science Education_. 1-19. https://doi.org/10.1145/3437800.3439201
* Simon et al. (2018) Simon, Judy Sheard, Michael Morgan, Andrew Petersen, Amber Settle, and Jane Sinclair. 2018. Informing students about academic integrity in programming. In _20th Australasian Computing Education Conference_. 113-122. https://doi.org/10.1145/3160489.3160502
* Solaiman et al. (2019) Irene Solaiman, Miles Brundage, Jack Clark, Amanda Askell, Ariel Herbert-Voss, Jeff Wu, Alec Radford, Gretchen Krueger, Jong Wook Kim, Sarah Kreps, Miles McCain, Alex Newhouse, Jason Blazakis, Kris McGuffie, and Jasmine Wang. 2019. Release Strategies and the Social Impacts of Language Models. , 45 pages. https://d4mucfpskywv.cloudfront.net/papers/GPT_2_Report.pdf
* Tahaei and Noelle (2018) Narjes Tahaei and David C. Noelle. 2018. Automated plagiarism detection for computer programming exercises based on patterns of resubmission. In _ACM Conference on International Computing Education Research_. 178-186. https://doi.org/10.1145/3230977.3231006
* Tang et al. (2023) Ruixiang Tang, Yu-Neng Chuang, and Xia Hu. 2023. The Science of Detecting LLM-Generated Texts. arXiv: 2303.07205 [cs.CL]
* Tian (2023) Edward Tian. 2023. GPTZero Classrooms. Accessed: 2023-03-01. https://gptzero.substack.com/p/gptzero-classrooms.
* Tian (2023) Edward Tian. 2023. GPTZero Release Tweet. Accessed: 2023-03-01. https://twitter.com/elward_the/status/1610067688449007618.
* Ullah et al. (2018) Farhan Ullah, Junfeng Wang, Muhammad Farhan, Masood Habib, and Shekhaad Khalid. 2018. Software plagiarism detection in multiprogramming languages using machine learning approach. _Concurrency and Computation: Practice and Experience_ 33, 4 (Oct 2018), e5000. https://doi.org/10.1002/cpe.5000
* Yamamoto and Lennon (2018) Kentaro Yamamoto and Mary Louise Lennon. 2018. Understanding and detecting data fabrication in large-scale assessments. _Quality Assurance in Education_ 26, 2 (2018), 196-212. https://doi.org/10.1108/QAE-07-2017-0038
* Yan et al. (2018) Lisa Yan, Nick McKeown, Mehran Sahami, and Chris Piech. 2018. TMOSS: Using intermediate assignment work to understand excessive collaboration in large classes. In _49th ACM Technical Symposium on Computer Science Education_. 110-115. https://doi.org/10.1145/3159450.3159490 