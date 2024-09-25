import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import streamlit as st

from sklearn.cluster import AgglomerativeClustering
from sklearn.preprocessing import StandardScaler

import scipy.cluster.hierarchy as shc

from scipy.spatial.distance import pdist, squareform
from scipy.cluster.hierarchy import linkage, fcluster, dendrogram
from gower import gower_matrix

def main():
	st.set_page_config(page_title = "Projeto Módulo 31", layout="wide")

	link = 'https://archive.ics.uci.edu/dataset/468/online+shoppers+purchasing+intention+dataset'
	st.markdown("# Projeto Módulo 31")
	st.write("Neste projeto, utilizamos o algoritmo de **K-Means** para realizar o agrupamento de dados de comportamento de compras online no setor de varejo. O objetivo foi identificar padrões e tendências no comportamento dos consumidores, facilitando a criação de estratégias direcionadas. Confira a base de dados utilizada: ['Online Shoppers Purchasing Intention Dataset'](https://archive.ics.uci.edu/dataset/468/online+shoppers+purchasing+intention+dataset) e veja [a solução implementada aqui](https://github.com/ohallao/RFV/blob/main/Pre-Streamlit.ipynb).")

	st.markdown("---")
	st.markdown("## Dataframe")
	df = pd.read_csv("./kmeans_data.csv", index_col=0)
	st.write(df)

	st.markdown("## Tabela de Frequências")


	variaveis = ['VisitorType','Month', 'Weekend', 'Revenue']
	grupos = ['3_grupos', '4_grupos', '5_grupos', '6_grupos',
	       '7_grupos', '8_grupos', '9_grupos']
	
	var = st.selectbox("Variável a ser analisada", variaveis, key='s1')
	
	col1, col2 = st.columns(2, gap='large')
	with col1:
		grupo1 = st.selectbox("Quantidade de grupos", grupos, key='s2')
		ct1 = pd.crosstab(df[var], df[grupo1])
		st.markdown(f"Variável **{var}** para **{grupo1[:1]}** grupos")
		st.write(ct1)
		
		fig, ax = plt.subplots(nrows=1, ncols=1, figsize=(10, 6))
		df.groupby([grupo1, var])[var].count().unstack().plot.bar(ax=ax)
		st.pyplot(fig=fig)

	with col2:
		
		grupo2 = st.selectbox("Quantidade de grupos", [g for g in grupos if g!=grupo1], key='s3')
		ct2 = pd.crosstab(df[var], df[grupo2])
		st.markdown(f"Variável **{var}** para **{grupo2[:1]}** grupos")
		st.write(ct2)
		
		fig, ax = plt.subplots(nrows=1, ncols=1, figsize=(10, 6))
		df.groupby([grupo2, var])[var].count().unstack().plot.bar(ax=ax)
		st.pyplot(fig=fig)

	# fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(12, 4))

	# for i in range(2):
		# df.groupby([grupos[i], 'Weekend'])['Weekend'].count().unstack().plot.bar(ax=axes[i])
	# st.pyplot(fig=fig, use_container_width=False)

		        

if __name__ == '__main__':
	main()
