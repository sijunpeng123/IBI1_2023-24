import matplotlib.pyplot as plt
Activity= ["sleeping", "classes", "Studying", "TV", "Music","Others"]  
Time_spent= [8, 6, 3.5, 2, 1,3.5]
plt.figure()
plt.pie(Time_spent, labels=Activity, startangle=90)
plt.show