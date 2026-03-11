# import pandas as pd

# df = pd.read_csv("insurance.csv")

# print(df.head())
# print(df.info())
# print(df.describe())

# #calculate average medical cost for smokers 
# smoker_cost = df.groupby("smoker")["charges"].mean()
# print(smoker_cost)

# #visulaization
# import matplotlib.pyplot as plt

# df.boxplot(column="charges", by="smoker")
# plt.title("Medical Charges by Smoking Status")
# plt.suptitle("")
# plt.xlabel("Smoker")
# plt.ylabel("Charges")
# plt.show()

# #calculate BMI - scatter plot 
# plt.scatter(df["bmi"], df["charges"])
# plt.xlabel("BMI")
# plt.ylabel("Medical Charges")
# plt.title("BMI vs Medical Charges")
# plt.show()

# #most expensive region 
# region_cost = df.groupby("region")["charges"].mean()
# print(region_cost)

# #optional plot
# region_cost.plot(kind="bar")
# plt.title("Average Medical Cost by Region")
# plt.ylabel("Charges")
# plt.show()



# # import pandas as pd
# # import matplotlib.pyplot as plt

# # # load dataset
# # df = pd.read_csv("insurance.csv")

# # # create figure
# # fig, ax = plt.subplots()

# # # plot
# # ax.scatter(df["bmi"], df["charges"])

# # ax.set_xlabel("BMI")
# # ax.set_ylabel("Medical Charges")
# # ax.set_title("BMI vs Medical Charges")

# # save figure
# fig.savefig("healthcare-results/bmi_vs_charges.png")
# fig.savefig("healthcare-results/Medical_Charges_by_Smoking_Status.png")
# fig.savefig("healthcare-results/Average_Medical_Cost_by_Region.png")

# # show plot
# plt.show()


import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("insurance.csv")

print(df.head())
print(df.info())
print(df.describe())

# calculate average medical cost for smokers
smoker_cost = df.groupby("smoker")["charges"].mean()
print(smoker_cost)

# -------------------------
# Visualization 1: Boxplot
# -------------------------
df.boxplot(column="charges", by="smoker")
plt.title("Medical Charges by Smoking Status")
plt.suptitle("")
plt.xlabel("Smoker")
plt.ylabel("Charges")

plt.style.use("ggplot")
plt.savefig("healthcare-results/Medical_Charges_by_Smoking_Status.png")
plt.show()

# -------------------------
# Visualization 2: BMI Scatter
# -------------------------
plt.scatter(df["bmi"], df["charges"])
plt.xlabel("BMI")
plt.ylabel("Medical Charges")
plt.title("BMI vs Medical Charges")

plt.style.use("ggplot")
plt.savefig("healthcare-results/bmi_vs_charges.png")
plt.show()

# -------------------------
# Most expensive region
# -------------------------
region_cost = df.groupby("region")["charges"].mean()
print(region_cost)

# -------------------------
# Visualization 3: Region Bar Plot
# -------------------------
region_cost.plot(kind="bar")
plt.title("Average Medical Cost by Region")
plt.ylabel("Charges")

plt.style.use("ggplot")
plt.savefig("healthcare-results/Average_Medical_Cost_by_Region.png")
plt.show()