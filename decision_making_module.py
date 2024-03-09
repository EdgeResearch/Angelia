import pandas as pd

news_df = pd.read_csv('./datasets/news_sentiment_testing.csv')
evidences_df = pd.read_csv('./datasets/evidences_sentiment_testing.csv')

testing_result_data = {
    'index': [],
    'news': [],
    'label': [],
    'negativity_score': [],
    'negativity_label': []
}
testing_result_df = pd.DataFrame(testing_result_data)


def get_news_evidences_indexes(index):
    evidences = []

    for row in evidences_df.itertuples(index=True):
        if row.news_i == index:
            evidences.append(row[0])
        if row.news_i > index:
            break
    return evidences


def get_row_aggregated_sentiment(row):
    sentiment_score = 0

    if row.sentiment_transformers == 'POSITIVE':
        sentiment_score += 1
    if row.sentiment_transformers == 'NEGATIVE':
        sentiment_score -= 1

    if row.sentiment_textblob == 'POSITIVE':
        sentiment_score += 1
    if row.sentiment_textblob == 'NEGATIVE':
        sentiment_score -= 1

    if row.sentiment_sentiment == 'POSITIVE':
        sentiment_score += 1
    if row.sentiment_sentiment == 'NEGATIVE':
        sentiment_score -= 1

    if row.sentiment_natural == 'POSITIVE':
        sentiment_score += 1
    if row.sentiment_natural == 'NEGATIVE':
        sentiment_score -= 1

    if sentiment_score > 0:
        return 'POSITIVE'
    if sentiment_score < 0:
        return 'NEGATIVE'

    return 'NEUTRAL'


def verify_heuristics(text):
    if "fake" in text.lower() or text.lower().startswith("no, ") or "false" in text.lower() or text.lower().startswith("no ") or text.lower().startswith("no."):
        return True
    return False


original_neutral = 0

for row in news_df.itertuples():
    news_sentiment = get_row_aggregated_sentiment(row)
    if news_sentiment == 'NEUTRAL':
        original_neutral += 1
    evidence_indexes = get_news_evidences_indexes(row.index)

    if len(evidence_indexes) == 0:
        negativity_score = 0
        negativity_label = 'No result.'

    else:
        contradictory_score = 0

        for index in evidence_indexes:
            evidence_row = evidences_df.loc[index]
            evidence_sentiment = get_row_aggregated_sentiment(evidence_row)
            if evidence_sentiment != news_sentiment:
                contradictory_score += 1

            news_heuristics = verify_heuristics(row.news)
            evidence_heuristics = verify_heuristics(evidence_row.evidence)

            if (evidence_sentiment == 'NEGATIVE' and news_sentiment == 'NEGATIVE') and (news_heuristics != evidence_heuristics):
                contradictory_score += 1

        negativity_score = contradictory_score/(len(evidence_indexes))*100
        print(negativity_score)
        if negativity_score == 0:
            negativity_label = 'Trustable.'
        elif negativity_score < 25:
            negativity_label = 'Likely Trustable.'
        elif negativity_score < 50:
            negativity_label = 'Likely Fake.'
        elif negativity_score < 75:
            negativity_label = 'Most Likely Fake.'
        else:
            negativity_label = 'Fake.'

        print(negativity_label)

    new_row = {'index': row.index, 'news': row.news, 'label': row.label, 'negativity_score': negativity_score, 'negativity_label': negativity_label }
    testing_result_df.loc[len(testing_result_df)] = new_row

testing_result_df.to_csv('./testing_result_dataset.csv', index=False)