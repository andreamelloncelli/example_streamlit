import streamlit as st
from app.streamlit.common.download import convert_df
from app.streamlit.common.plots import frequency_plot, wordcloud
from app.streamlit.common.transformations import most_frequent_words
from app.streamlit.common.importer import read_dataframe


def app():
    st.title("python-scheleton example")
    st.subheader("Text Analysis Page")

    df = read_dataframe()

    csv = convert_df(df)

    st.download_button(
        label="Download data as CSV",
        data=csv,
        file_name="text_df.csv",
        mime="text/csv",
    )

    mfwords, word_list = most_frequent_words(df)

    st.dataframe(mfwords)

    freq_plot = frequency_plot(mfwords)
    st.plotly_chart(freq_plot)

    wordcloud_plot = wordcloud(word_list)
    st.pyplot(wordcloud_plot)
