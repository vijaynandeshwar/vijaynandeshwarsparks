#!/usr/bin/env python
# coding: utf-8

# In[111]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')


# In[112]:


#Reading the data from source


# In[113]:


#D:\SampleSuperstore - SampleSuperstore.csv


# In[114]:


retaildata = pd.read_csv('D:\SampleSuperstore - SampleSuperstore.csv')


# In[115]:


retaildata


# In[116]:


#Exploring the details about dataset


# In[117]:


retaildata.describe()


# In[118]:


retaildata.info()


# In[119]:


retaildata.columns


# In[120]:


retaildata['Ship Mode'].unique().shape


# In[121]:


for i in retaildata.columns:
    print('Number of unique categories in', i + 'is',retaildata[i].unique())


# In[122]:


#checking for outliers


# In[123]:


retaildata.boxplot()


# In[124]:


#Ship Mode and it's Impact on Sales


# In[125]:


#Shipmodewise Total Sales


# In[126]:


x = retaildata['Ship Mode'].unique()
x.sort()
x


# In[127]:


y = retaildata.groupby(['Ship Mode'])['Sales'].sum()
y


# In[128]:


#Shipmodewise Total Profit


# In[129]:


ypro = retaildata.groupby(['Ship Mode'])['Profit'].sum()
ypro


# In[130]:


#Shipmodewise Total Discount


# In[131]:


ydisc = retaildata.groupby(['Ship Mode'])['Discount'].sum()
ydisc


# In[132]:


fig,(ax1,ax2,ax3) = plt.subplots(1,3,figsize=(20,6))
ax1.bar(x,y,color=['red', 'blue', 'purple', 'green'])
ax2.bar(x,ypro,color=['red', 'blue', 'purple', 'green'])
ax3.bar(x,ydisc,color=['red', 'blue', 'purple', 'green'])
ax1.set_title('Shipmodewise Total Sales')
ax2.set_title('Shipmodewise Total Profit')
ax3.set_title('Shipmodewise Total Discount')
plt.show()


# In[133]:


#Conclusion=1)The Graph shows that Sales for the ship mode of standard class is having more Sales as Compared to others
#2)We got more profit in Standard Class ship mode.So we have to use this strategis to improve our Sales and Profit


# In[134]:


x = retaildata['Ship Mode'].unique()
x.sort()
x


# In[135]:


#Shipmodewise Avg Sales


# In[136]:


y = retaildata.groupby(['Ship Mode']).agg({'Sales':np.average})
y = y.iloc[:,-1]
y


# In[137]:


#Shipmodewise Avg Profit


# In[138]:


yprof = retaildata.groupby(['Ship Mode']).agg({'Profit':np.average})
yprof = yprof.iloc[:,-1]
yprof


# In[139]:


fig,(ax1,ax2) = plt.subplots(1,2,figsize=(20,10))
ax1.bar(x,y,color=['red', 'blue', 'purple', 'green'])
ax2.bar(x,yprof,color=['red', 'blue', 'purple', 'green'])
ax1.set_title('Shipmodewise Avg Sales')
ax2.set_title('Shipmodewise Avg Profit')
plt.show()


# In[140]:


#Conclusion:1)The Graph shows that average Sales & Avg Profit for the ship mode of standard class is having less avg Sales & avg profit as compared to others
#2)We have to think about this mode and we have to think how we can improve our average sales and profit is standard class


# #SegmentWise Sales and it's Impact
# 
# 

# In[141]:


#SegmentWise Total sales


# In[142]:


x1 = retaildata['Segment'].unique()
x1


# In[143]:


y1 = retaildata.groupby(['Segment'])['Sales'].sum()
y1


# In[144]:


#SegmentWise Total Profit


# In[145]:


y1pro = retaildata.groupby(['Segment'])['Profit'].sum()
y1pro


# In[146]:


#SegmentWise Total Discount


# In[147]:


y1disc = retaildata.groupby(['Segment'])['Discount'].sum()
y1disc


# In[ ]:





# In[80]:


fig, (ax1, ax2,ax3) = plt.subplots(1,3,figsize=(15,5))
ax1.bar(x1,y1,color=['red','blue','green'])
ax2.bar(x1,y1pro,color=['red','blue','green'])
ax3.bar(x1,y1disc,color=['red','blue','green'])
ax1.set_title('Segmentwise Total Sales')
ax2.set_title('Segmentwise Total Profit')
ax3.set_title('Segmentwise Total Discount')
plt.show()


# In[81]:


#Conculusion 1)From the above graphs we can say that the Consumer segment performance is very good and also for Coorporate Segment
#2)As we can see here the consumer segment is performing very good because we gave discount on that products
#3)so we have to give some discpunt on Coorporte and home office segment products also we can increase the profit and sales


# In[82]:


#SegmentWise Average Sales


# In[83]:


x1 = retaildata['Segment'].unique()
x1


# In[84]:


y1 = retaildata.groupby(['Segment']).agg({'Sales':np.average})
y1


# In[85]:


#SegmentWise Average Profit


# In[86]:


y1pro = retaildata.groupby(['Segment']).agg({'Profit':np.mean})
y1pro


# In[ ]:


#Sub-Categoriwise Order Counts


# In[89]:


plt.figure(figsize=(20,10))
sns.countplot(x=data['Sub-Category'],orient='h', order=(retaildata['Sub-Category'].value_counts()).index)
plt.title('Sub-Categoriwise Sold Counts')
plt.show


# In[91]:


#conclusion:By looking at above graph we can say 80% of orders are coming from 7 to 8 Cities only


# In[92]:


##State-wise Performance of Orders Counts


# In[95]:


plt.figure(figsize=(20,10))
sns.countplot(x=retaildata['State'],order=(retaildata['State'].value_counts().head(50)).index)
plt.xticks(rotation=90)
plt.show()
                            


# In[96]:


#conclusion: By looking at above graph we can say 80% of orders are coming from 7 states only


# In[97]:


#Regionwise Total sales and profit performance


# In[98]:


y2 = retaildata.groupby(['Region'])['Sales'].sum()
y2


# In[99]:


y2prof = retaildata.groupby(['Region'])['Profit'].sum()
y2prof


# In[100]:


#Regionwise Average Sales


# In[101]:


y2 = retaildata.groupby(['Region']).agg({'Sales':np.average})
y2 = y2.iloc[:,-1]
y2


# In[105]:


#sub-categoriwise average sales


# In[106]:


y4 = retaildata.groupby(['Sub-Category']).agg({'Sales':np.average})
y4 = y4.iloc[:,-1]
y4


# In[ ]:


Thank you 
The Spark Foundation 
Completed By Vijay Nandeshwar


# In[ ]:




