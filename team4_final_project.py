import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st
plt.style.use('seaborn')

st.title("E-Commerce Shipping Data")
df=pd.read_csv('train.csv')
df = df.sample(5000).reset_index(drop=True)

if st.checkbox('Show dataframe'):
    df

st.sidebar.header("Mode")
st.title("Function")
input= st.sidebar.number_input('Which index data do you want to watch?(<4999)',value=0, min_value = 0, max_value = 5000)
st.write("watch input index data")
data=pd.DataFrame(df.iloc[[input]])
st.dataframe(data)

options = st.sidebar.multiselect(
   'What Warehouse_block do you want to show',
    ('A', 'B', 'C','D','F'), ('A'))

shipment_filter = st.sidebar.multiselect(
   'What Warehouse_block do you want to show',
    ('Flight', 'Ship', 'Road'), ('Flight'))

gender_filter = st.sidebar.multiselect(
   'Choose the gender type:',
    ('Male', 'Female'), ('Male'))

Price_filter = st.slider('Cost_of_the_Product:', 120, 250) 

df=df.loc[df['Warehouse_block'].isin(list(options))]

#Warehouse_block distribution
st.subheader("Warehouse block distribution")
f=plt.figure(figsize=(10,6))
plt.pie(df.Warehouse_block.value_counts(),startangle=90,autopct='%.2f%%',labels=list(df.Warehouse_block.value_counts().index),radius=10,colors=['orange','pink','gray','yellow','purple'])
plt.axis('equal')
plt.title('Warehouse Block',fontdict={'fontsize':22,'fontweight':'bold'})
st.pyplot(f)

#Whether the products reach on time or not
st.subheader("Products reach on time or not")
f=plt.figure(figsize=(10,6))
category=df['Reached.on.Time_Y.N'].value_counts()
category.plot(kind='bar',color='orange')
st.pyplot(f)

st.title("plots")

#Weight-cost histogram
st.subheader("Weight distribution of product")
f=plt.figure(figsize=(15,6))
plt.hist(df.Weight_in_gms,bins=50,color='orange')
plt.xlabel('Weight',fontsize=20)
st.pyplot(f)

#Rating distribution histogram
st.subheader("Rating distribution of product")
f=plt.figure(figsize=(15,6))
plt.hist(df.Customer_rating,bins=50,color='orange')
plt.xlabel('Rating',fontsize=20)
st.pyplot(f)

#Cost of product boxplot
st.subheader("Boxplot of cost")
f=plt.figure(figsize=(10,6))
plt.boxplot(df.Cost_of_the_Product, widths=0.1, 
            notch=False,
            vert=True,
            meanline=True,
            patch_artist=True,
            showmeans=True,
            showcaps=True,
            showfliers=True,
            meanprops = {"color": "black", "linewidth": 1.5},
            medianprops={"color": "red", "linewidth": 0.5},
            boxprops={"facecolor": "C0", "edgecolor": "black","linewidth": 0.5, "alpha":0.4},
            whiskerprops={"color": "black", "linewidth": 1.5, "alpha":0.8},
            capprops={"color": "C0", "linewidth": 1.5},
            sym="+",labels=['cost of product'])
#plt.xlabel('cost of product',fontsize=20)
st.pyplot(f)

#Pairwise Feature Relationship Scatter Plot
st.subheader("Discount offered with weight and product cost")
f, ax = plt.subplots(ncols=2,figsize=(20, 10))
ax[0].scatter(df['Discount_offered'],df['Weight_in_gms'],color='orange')
ax[0].set_xlabel('Discount_offered',fontsize=20)
ax[0].set_ylabel('Weight_in_gms',fontsize=20)
ax[1].scatter(df['Discount_offered'],df['Cost_of_the_Product'],color='orange')
ax[1].set_xlabel('Discount_offered',fontsize=20)
ax[1].set_ylabel('Cost_of_the_Product',fontsize=20)
st.pyplot(f)

