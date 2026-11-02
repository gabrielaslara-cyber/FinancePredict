"""FinancePredict — educational data science portfolio app."""
import streamlit as st
import pandas as pd
from model import load_data, evaluate_models

st.set_page_config(page_title='FinancePredict | Ciência de Dados', page_icon='📈', layout='wide')
st.title('FinancePredict')
st.caption('Ciência de Dados Financeiros | Classificação experimental de risco de crédito')
st.warning('Estudo acadêmico com dados históricos. NÃO usar resultados para conceder, negar ou precificar crédito. Não há avaliação de justiça, calibração ou validação externa para produção.')
st.markdown('**Base:** German Credit, UCI / OpenML • 1.000 registros históricos • 20 atributos.')
try:
    X, y = load_data()
except Exception as exc:
    st.error('Não foi possível obter a base pública. Verifique a conexão e tente novamente.')
    st.stop()
col1, col2, col3 = st.columns(3)
col1.metric('Registros', f'{len(X):,}'.replace(',','.'))
col2.metric('Variáveis', X.shape[1])
col3.metric('Classe de maior risco na base', f'{100*y.mean():.1f}%'.replace('.',','))
st.subheader('Distribuição da classificação histórica')
st.bar_chart(pd.DataFrame({'Categoria':['good','bad'],'Registros':[(y==0).sum(),(y==1).sum()]}).set_index('Categoria'))
st.subheader('Comparação de modelos')
st.write('Divisão estratificada: 75% treinamento e 25% teste. Mesmo conjunto de teste para os dois modelos.')
with st.spinner('Treinando e avaliando os modelos...'):
    metrics, fitted = evaluate_models(X,y)
st.dataframe(metrics.style.format({'ROC-AUC':'{:.3f}','PR-AUC':'{:.3f}','Acurácia balanceada':'{:.3f}'}), hide_index=True, use_container_width=True)
selected = st.selectbox('Matriz de confusão', metrics['Modelo'].tolist())
mat = fitted[selected]['matrix']
st.table(pd.DataFrame(mat,index=['Real: good','Real: bad'],columns=['Previsto: good','Previsto: bad']))
st.markdown('''### Limitações e cuidados
- Dados de outro país e período histórico; **não representam a população brasileira atual**.
- Comparações são exploratórias, sem ajuste de hiperparâmetros ou validação externa.
- Os atributos incluem variáveis demográficas potencialmente sensíveis, e seu uso pode reproduzir vieses.
- Uma futura versão deverá documentar qualidade, calibração, justiça e estabilidade dos modelos.
- Métricas não significam autorização para decisões automatizadas sobre pessoas.
''')
st.caption('Fonte: Hofmann, H. (1994). Statlog (German Credit Data). UCI ML Repository, DOI: 10.24432/C5NC77. Dados via OpenML credit-g.')
