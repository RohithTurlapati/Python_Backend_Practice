import streamlit as st


st.header("My first streamlit app")
st.subheader("Introduction")
st.text("Streamlit is a web framework for python used in especially in data science, machine learning and AI")
st.markdown("**Note:** *This is just a practice session*")
st.markdown("---")
st.latex(r"\begin{pmatrix}a&b&c\\d&e&f\\g&h&i\end{pmatrix}")
code ="""
public static void main(String args[]){
    system.out.print("Hello world");
}
"""
st.code(code, language="java")
data = {"a": "1,2,3",
        "b": "4,5,6",
        "c": "7,8,9"
        }
st.json(data)

st.write("hello world")