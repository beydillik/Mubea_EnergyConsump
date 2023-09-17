import streamlit as st
import pandas


st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/KemalB.jpg", width=400)

with col2:
    st.title("Kemal Beydilli")
    content = """
    Experienced Plant Controller with a demonstrated history of working in the automotive industry. 
    Reporting Professional with a Master's degree focused in Business Engineering and CPA certificate from TURMOB. 
    Skilled in Visual Basic for Applications (VBA) for Excel, Financial Reporting, Variance Analysis, Financial Analysis, Budgeting and Cost Accounting. 
    Started a University Software Engineering program in 2021, learning mainly object-oriented programming and expected to be graduated in 2025.
    """
    st.info(content)

content = "Bu bölüm deneme amaçlı yazılmıştır, tüm satırı kaplaması amaçlanmıştır. Bu bölüm deneme amaçlı yazılmıştır, tüm satırı kaplaması amaçlanmıştır."
st.write(content)

col3, empty_col,  col4 = st.columns([1.5, 0.5, 1.5])

df=pandas.read_csv("data.csv", sep=";")

with col3:
    for index, row in df[:10].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Source Code]({row['url']})")

with col4:
    for index, row in df[10:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Source Code]({row['url']})")