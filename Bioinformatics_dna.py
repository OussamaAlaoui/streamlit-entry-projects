
import pandas as pd
import streamlit as st
import altair as alt # For displaying the charts


st.write("""
# DNA Nucleotide Count Web App
This app counts the nucleotide composition of query DNA!
***
""")


#st.sidebar.header('Enter DNA sequence')
st.header('Enter DNA sequence')

sequence_input = ">DNA Query \ntgactgacatccgccggcacccaggataaattctactaatcttaagcgatactcgcgaaa\natggggtagtcaacccgtagaggtgccttttgttctagcacggattggaagggtatctct\naccgccgcgataacgctagcagcacggtcggtcatatccggcggaacttgtgtgtggtcg\ntgcaggacacggtcttgttggttacgaactggctttcgccggctagacggcgtttttccg\nagtcttcatgtgaacaaaactcgaggaacaatgatctgctatctgggttccgtcaaagta\ntatacagccgtacgtcgtctagctgcatatacccgacccggggaagtagccaaactgtac\ngattacgtccgggttccctaactgggactgacgtgcgtgacaccgtttgctccaaaaccc\ntaagtgagttggcgactgagcaatattacagggatatgacattagcacctcttcgccaaa\nagctagtcccggaataggttccactacggccaagatccattcaattttgtaagatcagtg\nttttgctggatctttacaggctactagacaagtctaaggaaccagtcgtatcacccttgt\ngcaccacataccccggagggccatcttcctgcgtgtaggtgccgcattttcgacgcatac\nttgatgcgcaggagaggttgcgatgaatcgaaagtatctctttcgaccggagtcccgact\nggacccagacccctcgtaactggtcctctgcagacccatagtgttcagggtgaggatgag\ncgcgaaaagtgtcattctcatgccctggcacaagttgggggtgccacatcaatcgtattt\ncacgtacacaggctctcatataactgaaccgcctatgccaccctggatcccccagtgcca\nttcatctaggaacgttaatagtgtggtgtaatcgcgagagctcacgaagcgcatagggta\nggtggcttctgccaccgacgggtgaatctaggtgtacgag"
sequence_input=sequence_input.upper()
sequence = st.text_area("Sequence input", sequence_input, height=250)
sequence = sequence.splitlines()
st.write("""
### Splitting the sequence into lines
""")
sequence
sequence = sequence[1:]
st.write("""
### Removing the title ( DNA Query )
""")
sequence
sequence = "\n".join(sequence)
st.write("""
### Concatenating the list to make a string
""")
sequence

st.write("""
***
""")

st.header('INPUT (DNA Query)')
sequence

st.header('OUTPUT (DNA Nucleotide Count)')

st.subheader('1. Print dictionary')
# Calculating each nucleotide in our DNA query
def DNA_nucleotide_count(seq):
  d = dict([
            ('A',seq.count('A')),
            ('T',seq.count('T')),
            ('G',seq.count('G')),
            ('C',seq.count('C'))
            ])
  return d

X = DNA_nucleotide_count(sequence)
X

st.subheader('2. Print text')
st.write('There are  ' + str(X['A']) + ' adenine (A)')
st.write('There are  ' + str(X['T']) + ' thymine (T)')
st.write('There are  ' + str(X['G']) + ' guanine (G)')
st.write('There are  ' + str(X['C']) + ' cytosine (C)')

st.subheader('3. Display DataFrame')
df = pd.DataFrame.from_dict(X, orient='index')
df = df.rename({0: 'count'}, axis='columns')
df.reset_index(inplace=True)
df = df.rename(columns = {'index':'nucleotide'})
st.write(df)

st.subheader('4. Display Bar chart')
p = alt.Chart(df).mark_bar(size=40).encode(
    x='nucleotide',
    y='count'
)
p = p.properties(
    # width=alt.Step(60),
    width=400,
    height=400,
)
st.write(p)