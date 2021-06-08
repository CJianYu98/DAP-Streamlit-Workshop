import streamlit as st
import pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

def app():

    analyzer = SentimentIntensityAnalyzer()

    # Add a title
    st.title("F&B Food Review App")

    # Add some description
    st.markdown("""
    ### Wanna know how your customer feels about your food?\n
    Option 1) Paste a review for our App to evaluate it.\n
    Option 2) Upload a csv file with customer reviews. Make sure the reviews column has a header named **"Review"**.
    """)

    # Add a subheader
    st.subheader('Single Review Evaluation')

    # Add text box for user to paste their review
    single_review = st.text_area('Paste a review')

    if single_review:
        score = analyzer.polarity_scores(single_review)
        if score['compound'] > 0.05:
            st.success("The review is positive!")
        elif score['compound'] < -0.05:
            st.error('The review is negative!')
        else:
            st.warning('The review is nuetral!')

    # Add a subheader
    st.subheader('Upload a CSV file')

    # Add file upload option
    review_csv = st.file_uploader("")

    # Process the csv file
    if review_csv:
        df = pd.read_csv(review_csv)
        
        def get_polarity(text):
            compound_score = analyzer.polarity_scores(text)['compound']
            if compound_score > 0.05:
                return 'Positive'
            elif compound_score < -0.05:
                return 'Negative'
            else:
                return 'Neutral'

        df['Sentiment'] = df['Review'].apply(lambda x: get_polarity(x))
        df_output = df[['Review', 'Sentiment']]
        st.table(df_output)

