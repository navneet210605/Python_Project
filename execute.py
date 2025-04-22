import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_excel(r"C:\Users\navne\OneDrive\Desktop\day.xls")
print(df.head())
print(df.isnull().sum())


df.info()
df.describe()

# Checking for outliers in Casual VS Registered

fig, axs = plt.subplots(1, 2, figsize=(12, 6))

sns.boxplot(data=df, x="Casual", ax=axs[0], color="skyblue")
axs[0].set_xlabel("Rentals per day")
axs[0].set_title("Casual Rentals")


sns.boxplot(data=df, x="Registered", ax=axs[1], color="lightgreen")
axs[1].set_xlabel("Rentals per day")
axs[1].set_title("Registered Rentals")

plt.tight_layout()
plt.show()


# Outliers in Casual Rentals based on various conditions

fig0, axs0 = plt.subplots(2,3, figsize = (18, 12))

xval = ["Workingday", "Holiday", "Weekday", "Weather", "Season"]
idx = 0

for r in range(0,2):
    for c in range(0,3):
        if(idx<5):
            sns.boxplot(data=df, x = xval[idx], y = "Casual",ax = axs0[r][c], color = "skyblue")
            
            axs0[r][c].set_xlabel(xval[idx])
            axs0[r][c].set_ylabel("Rentals per day")
            axs0[r][c].set_title("Casual rentals for " + xval[idx])
            
            idx = idx + 1

        else:
            break
        
plt.axis("off")
plt.tight_layout()
plt.show()
        

# For Registered Users

# print("***** For Registered Users *****")

# for xaxis in ["Holiday", "Weekday", "Weather", "Season"]:

#     sns.boxplot(data=df, x = xaxis, y="Registered")
#     plt.xlabel(xaxis)
#     plt.ylabel("Rentals per day")
#     plt.title("Registered rentals for " + xaxis)
#     plt.grid()
#     plt.show()





fig, axs = plt.subplots(3,3,figsize=(15, 12))

#--------Total--------

sns.barplot(data = df, x = "Season", y = "Total Rented", ax = axs[0,0], color = "coral")
axs[0,0].set_title('Average Bike Rentals per Season (Total)')
axs[0,0].set_xlabel("Season")
axs[0,0].set_ylabel('Average Rentals')
# plt.show()

sns.barplot(data = df, x = "Workingday", y = "Total Rented", ax = axs[0,1], color = "coral")
axs[0,1].set_title('Average Bike Rentals per Workingday (Total)')
axs[0,1].set_xlabel("Workingday")
axs[0,1].set_ylabel('Average Rentals')
# plt.show()

sns.barplot(data = df, x = "Weather", y = "Total Rented", ax = axs[0,2], color = "coral")
axs[0,2].set_title('Average Bike Rentals in each Weather (Total)')
axs[0,2].set_xlabel("Weather")
axs[0,2].set_ylabel('Average Rentals')
# plt.show()


#---------Casual-----------

sns.barplot(data = df, x = "Season", y = "Casual", ax = axs[1,0], estimator=np.median, color = "skyblue")
axs[1,0].set_title('Average Bike Rentals per Season (Casual)')
axs[1,0].set_xlabel("Season")
axs[1,0].set_ylabel('Average Rentals')
# plt.show()

sns.barplot(data = df, x = "Workingday", y = "Casual", ax = axs[1,1], estimator=np.median, color = "skyblue")
axs[1,1].set_title('Average Bike Rentals per Workingday (Casual)')
axs[1,1].set_xlabel("Workingday")
axs[1,1].set_ylabel('Average Rentals')
# plt.show()

sns.barplot(data = df, x = "Weather", y = "Casual", ax = axs[1,2], estimator=np.median, color = "skyblue")
axs[1,2].set_title('Average Bike Rentals in each Weather (Casual)')
axs[1,2].set_xlabel("Weather")
axs[1,2].set_ylabel('Average Rentals')
# plt.show()

#-------Registered----------

sns.barplot(data = df, x = "Season", y = "Registered", ax = axs[2,0], color="lightgreen")
axs[2,0].set_title('Average Bike Rentals per Season (Registered)')
axs[2,0].set_xlabel("Season")
axs[2,0].set_ylabel('Average Rentals')
# plt.show()

sns.barplot(data = df, x = "Workingday", y = "Registered",ax = axs[2,1], color="lightgreen")
axs[2,1].set_title('Average Bike Rentals per Workingday (Registered)')
axs[2,1].set_xlabel("Workingday")
axs[2,1].set_ylabel('Average Rentals')
# plt.show()

sns.barplot(data = df, x = "Weather", y = "Registered", ax = axs[2,2], color="lightgreen")
axs[2,2].set_title('Average Bike Rentals in each Weather (Registered)')
axs[2,2].set_xlabel("Weather")
axs[2,2].set_ylabel('Average Rentals')
# plt.show()

plt.tight_layout()
plt.show()



values = [df["Casual"].sum(), df["Registered"].sum()]
lbl = ("Casual Users", "Registered Users")

plt.pie(values, labels = lbl, autopct = "%.1f%%", colors = ("#FFB6C1", "#B0E0E6"))
plt.title("Share of Casual vs Registered Users")
plt.show()



df2 = df[["Temp", "Atemp", "Humidity", "Windspeed", "Casual", "Registered", "Total Rented"]]

corr_matrix = df2.corr()

sns.heatmap(data = corr_matrix, annot = True, cmap = "YlGnBu",vmin = -1, vmax = 1)
plt.title("Correlation Heatmap")
# plt.tight_layout()
plt.show()



sns.scatterplot(data = df, x = "Temp", y = "Total Rented", hue = "Atemp")
plt.title("Temperature VS Total Rentals")
plt.xlabel("Temperature")
plt.ylabel("Total Bikes Rented")
plt.tight_layout()
plt.show()



plt.figure(figsize=(15,8))
# plt.plot(df["Date"], df["Total Rented"], color="coral")
plt.plot(df["Date"], df["Casual"], color = "skyblue")
plt.plot(df["Date"], df["Registered"], color = "lightgreen")

plt.title("Rentals Over Time", fontsize=16)
plt.xlabel("Date", fontsize=14)
plt.ylabel("Rentals per day", fontsize=14)
plt.grid()
plt.tight_layout()
plt.show()
