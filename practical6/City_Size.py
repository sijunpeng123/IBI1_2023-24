uk_cities=[0.56,0.62,0.04,9.7]
uk_name=["Edinburgh","Glasgow","Stirling","London"]
import matplotlib.pyplot as plt
plt.figure(figsize=(20,10))
plt.subplot(1,2,1)
plt.bar(uk_name,uk_cities)
plt.title('UK_City_Size')
plt.xlabel('City')
plt.ylabel('Population')
china_cities=[0.58,8.4,29.9,22.2]
china_name=['Haining','Hangzhou','Shanghai','Beijing']
plt.subplot(1,2,2)
plt.bar(china_name,china_cities)
plt.title('China_City_size')
plt.xlabel('City')
plt.ylabel('Population')
plt.show()
plt.clf()