# In[7]:


import sklearn

import numpy as np
import scipy as sp
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[8]:


sales_data = pd.read_csv('Sales_Table.csv')


# In[10]:


X = sales_data.drop(['item','sale_price'], axis=1)
Y = sales_data['sale_price']


# In[11]:


##Checking to see if the one hot encoding worked correctly
##Entry 12530 should have a 1 in the "zumiez" column 
X.head(12532)[12525:12540]


# In[13]:


print(X.shape)
print(Y.shape)


# In[14]:


from sklearn.model_selection import train_test_split

x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size = 0.2)


# In[15]:


x_train.shape, x_test.shape


# In[16]:


y_train.shape, y_test.shape


# In[17]:


from sklearn.linear_model import Ridge

model = Ridge(alpha = 1, normalize = True) 

model.fit(x_train, y_train)


# In[18]:


print('Training_score : ', model.score(x_train,y_train))


# In[19]:


y_pred = model.predict(x_test)


# In[ ]:


df_pred_actual = pd.DataFrame({'predicted' : y_pred, 'actual' : y_test})


# In[ ]:


df_pred_actual.head(50)


# In[ ]:


df_pred_actual.to_csv('Results.csv')


# In[22]:


from sklearn.metrics import r2_score

print('Testing score : ', r2_score(y_test,y_pred))
