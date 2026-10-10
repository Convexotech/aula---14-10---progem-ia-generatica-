# NOTAS DE ESTUDOS 
import streamlit as st
import pandas as pd
from sklearn.linear_model import LinearRegression
import pandas as pd

dados =  pd.read_excel('vendas.xlsx')
print(dados)

df =  pd.DataFrame(dados)

X = df[['Meses']] # bidimensional 
y = df['Vendas']

modelo =  LinearRegression()

modelo.fit(X,y)

novo = pd.DataFrame({'Meses':[9]})

resultado = modelo.predict(novo)

print(resultado[0])




# st.header('ANALISE DE NOTAS - PREVENDO')

# estudos = pd.DataFrame({
# 'notas':[1,2,4,6,8,10],
# 'horas':[2,4,5,7,9,10]
# })

# st.bar_chart(estudos, x = 'notas', y  =  'horas')

# #st.scatter_chart(estudos, x = 'horas', y= 'notas')
# modelo_escola = LinearRegression() 
# modelo_escola.fit(estudos[['horas']], estudos['notas'])

# h_estudo = st.number_input('Digite a hora estudada')
# nota_final = modelo_escola.predict([[h_estudo]])
# print(nota_final)

# st.metric(f'sua nota seria' ,f'{min(nota_final[0], 10.0):.1f}')

# if nota_final > 7:
#     st.write('APROVADA')
# elif nota_final >= 5 and nota_final <7:
#     st.write('RECUPERAÇÃO')
# else:
#     st.write('REPROVADA')    
