texts = """As a term, data analytics predominantly refers to an assortment of applications, from basic business intelligence (BI), reporting and online analytical processing (OLAP) to various forms of advanced analytics. In that sense, it's similar in nature to business analytics, another umbrella term for approaches to analyzing data -- with the difference that the latter is oriented to business uses, while data analytics has a broader focus. The expansive view of the term isn't universal, though: In some cases, people use data analytics specifically to mean advanced analytics, treating BI as a separate category. Data analytics initiatives can help businesses increase revenues, improve operational efficiency, optimize marketing campaigns and customer service efforts, respond more quickly to emerging market trends and gain a competitive edge over rivals -- all with the ultimate goal of boosting business performance. Depending on the particular application, the data that's analyzed can consist of either historical records or new information that has been processed for real-time analytics uses. In addition, it can come from a mix of internal systems and external data sources. At a high level, data analytics methodologies include exploratory data analysis (EDA), which aims to find patterns and relationships in data, and confirmatory data analysis (CDA), which applies statistical techniques to determine whether hypotheses about a data set are true or false. EDA is often compared to detective work, while CDA is akin to the work of a judge or jury during a court trial -- a distinction first drawn by statistician John W. Tukey in his 1977 book Exploratory Data Analysis. Data analytics can also be separated into quantitative data analysis and qualitative data analysis. The former involves analysis of numerical data with quantifiable variables that can be compared or measured statistically. The qualitative approach is more interpretive -- it focuses on understanding the content of non-numerical data like text, images, audio and video, including common phrases, themes and points of view."""

def probability_of_word_occurrence_data(text):
    import re
    lines = re.split(r'\. |\.\n', text)
    
    probabilities = []
    
    for line in lines:
        words = line.split()
        word_count = len(words)
        data_count = sum(1 for word in words if word.lower() == "data")
        probability = data_count / word_count if word_count > 0 else 0
        probabilities.append(probability)
    
    return probabilities


def distribution_of_distinct_word_counts(text):
    import re
    from collections import Counter
    
    lines = re.split(r'\. |\.\n', text)
    
    word_counts = []
    
    for line in lines:
        words = re.findall(r'\b\w+\b', line.lower())
        
        distinct_words = set(words)
        word_counts.append(len(distinct_words))
    
    distribution = Counter(word_counts)
    
    return distribution

def probability_of_analytics_after_data(text):
    import re
    
    pattern = re.compile(r'\bdata analytics\b', re.IGNORECASE)
    data_analytics_count = len(pattern.findall(text))
    
    data_count = len(re.findall(r'\bdata\b', text, re.IGNORECASE))
    
    probability = data_analytics_count / data_count if data_count > 0 else 0
    
    return probability, data_analytics_count, data_count





if __name__ == '__main__':
    print("jawaban untuk pertayaan 1 What is the probability of the word “data” occurring in each line ? \n")
    probabilities = probability_of_word_occurrence_data(texts)
    for i, prob in enumerate(probabilities, start=1):
        print(f"Line {i} probability: {prob:.4f}")

    print("\n")
    print("jawaban untuk pertayaan 2 What is the distribution of distinct word counts across all the lines ? \n")
    distribution = distribution_of_distinct_word_counts(texts)
    for word_count, freq in distribution.items():
        print(f"Distinct word count: {word_count}, Frequency: {freq}")

    
    print("\n")
    print("jawaban untuk pertayaan 3 What is the probability of the word “analytics” occurring after the word “data” ? \n")
    probability, data_analytics_count, data_count = probability_of_analytics_after_data(texts)
    print("probability :", probability, "data_analytic_count :", data_analytics_count, "data_count :", data_count)





