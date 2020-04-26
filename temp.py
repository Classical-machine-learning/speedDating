# %% codecell
import pandas as pd
import numpy as np
import seaborn as sns

df = pd.read_csv("speed-dating-experiment/Speed Dating Data.csv", encoding="ISO-8859-1")

df.head(10)
# %% codecell
df.shape
# %% markdown
# # Cleaning
# %% codecell
to_remove = []
# %% codecell
for a in df.columns:
    if df[a].isna().sum() > 4000:
        to_remove.append(a)
# %% codecell
df = df.drop(to_remove, axis=1)
# %% codecell
df.shape
# %% codecell
df2 = df.copy()
# %% markdown
# ## Only filter out people who got to the second date
# %% codecell
df2['match'].shape
# %% codecell
pd.crosstab(index=df2["match"], columns="count")
# %% codecell
(1380/6998) * 100
# %% codecell
matched = df2[df2["match"] == 1]
matched.head(5)
# %% codecell
matched.shape
# %% markdown
# ## Attributes
# %% markdown
# ### Race
# %% codecell
pd.crosstab(index=matched["samerace"], columns="count")
# %% codecell

# %% markdown
# ### Age
# %% codecell
age = pd.crosstab(index=matched["age_o"], columns="count").reset_index()
age.head(3)
# %% codecell
sns.barplot(x=age["age_o"], y=age["count"]).set_xticklabels(
    rotation=45, labels=age["age_o"]
)

# %% markdown
# ### Job
# %% codecell
cols = [
    "Law  ",
    "Math",
    "Social Science, Psychologist ",
    "Medical Science, Pharmaceuticals, and Bio Tech ",
    "Engineering  ",
    "English/Creative Writing/ Journalism ",
    "History/Religion/Philosophy ",
    "Business/Econ/Finance ",
    "Education, Academia ",
    "Biological Sciences/Chemistry/Physics",
    "Social Work ",
    "Undergrad/undecided ",
    "Political Science/International Affairs ",
    "Film",
    "Fine Arts/Arts Administration",
    "Languages",
    "Architecture",
    "Other",
]
# %% codecell
fields = pd.crosstab(index=matched["field_cd"], columns="count").reset_index()
fields
# %% codecell
sns.barplot(x=fields["field_cd"], y=fields["count"]).set_xticklabels(
    rotation=90, labels=cols
)

# %% markdown
# ### Goal
# %% codecell
cols2 = [
    "Seemed like a fun night out",
    "To meet new people",
    "To get a date",
    "Looking for a serious relationship",
    "To say I did it",
    "Other",
]
# %% codecell
goal = pd.crosstab(index=matched["goal"], columns="count").reset_index()
goal
# %% codecell
sns.barplot(x=goal["goal"], y=goal["count"]).set_xticklabels(
    rotation=90, labels=cols2
)

# %% codecell
for a in enumerate(matched.columns):
    print(a)
# %% codecell

# %% codecell
df_interests = pd.concat([matched.iloc[:, 47:63], matched["gender"]], axis=1)
df_interests.head(10)
# %% codecell
sns.pairplot(df_interests, hue="gender")


# %% markdown
# -> dining, hiking, clubbing, reading, music
# %% markdown
# attr5_1 
# Attractive
# sinc5_1
# Sincere
# int5_1
# Intelligent
# fun5_1
# Fun
# amb5_1
# Ambitious
# %% codecell


def ret_cross_attr(atrr2):
    temp = pd.crosstab(index=matched[atrr2], columns="count").reset_index()
    return sns.barplot(x=temp[atrr2], y=temp["count"])


# %% markdown
# ### Go out
# %% markdown
# 	Several times a week=1
# 	Twice a week=2
# 	Once a week=3
# 	Twice a month=4
# 	Once a month=5
# 	Several times a year=6
# 	Almost never=7
# %% codecell
ret_cross_attr("go_out")
# %% markdown
# ### How they felt about themselves -> Attractiveness
# %% codecell
ret_cross_attr("attr5_1")
# %% markdown
# ### How they felt about themselves -> Fun
# %% codecell
ret_cross_attr("fun5_1")
# %% markdown
# ### How they felt about themselves -> Ambitious
# %% codecell
ret_cross_attr("amb5_1")
# %% markdown
# ### How happy do you expect it will make you?
# %% codecell
ret_cross_attr("exphappy")
# %% markdown
# ### Compare with personal confidence
#
# %% codecell
ret_cross_attr("match_es")
# %% codecell
temp = pd.crosstab(
    index=df2[df2["match"] == 0]["match_es"], columns="count"
).reset_index()
sns.barplot(x=temp["match_es"], y=temp["count"], color="b")
ret_cross_attr("match_es")
# %% markdown
# ### Rating
# %% codecell
ret_cross_attr("attr_o")
# %% markdown
# ## Features of the ones who got a 10
# %% codecell
ten = matched[matched["attr_o"] == 10]
ten.head(5)
# %% codecell
ten.shape
# %% markdown
# ### Race
# %% codecell
pd.crosstab(index=ten["samerace"], columns="count")
# %% markdown
# ### Age
# %% codecell
age = pd.crosstab(index=ten["age_o"], columns="count").reset_index()
age.head(3)
# %% codecell
sns.barplot(x=age["age_o"], y=age["count"]).set_xticklabels(
    rotation=45, labels=age["age_o"]
)

# %% markdown
# ### Job
# %% codecell
cols = [
    "Law  ",
    "Math",
    "Social Science, Psychologist ",
    "Medical Science, Pharmaceuticals, and Bio Tech ",
    "Engineering  ",
    "English/Creative Writing/ Journalism ",
    "History/Religion/Philosophy ",
    "Business/Econ/Finance ",
    "Education, Academia ",
    "Biological Sciences/Chemistry/Physics",
    "Social Work ",
    "Undergrad/undecided ",
    "Political Science/International Affairs ",
    "Film",
    "Fine Arts/Arts Administration",
    "Languages",
    "Architecture",
    "Other",
]
# %% codecell
fields = pd.crosstab(index=ten["field_cd"], columns="count").reset_index()
fields
# %% codecell
sns.barplot(x=fields["field_cd"], y=fields["count"]).set_xticklabels(
    rotation=90, labels=cols
)

# %% codecell


def ret_cross_attr(atrr2):
    temp = pd.crosstab(index=ten[atrr2], columns="count").reset_index()
    return sns.barplot(x=temp[atrr2], y=temp["count"])


# %% codecell
ret_cross_attr("attr5_1")
# %% markdown
# ### How they felt about themselves -> Fun
# %% codecell
ret_cross_attr("fun5_1")
# %% markdown
# ### How they felt about themselves -> Ambitious
# %% codecell
ret_cross_attr("amb5_1")
# %% markdown
# ### How happy do you expect it will make you?
# %% codecell
ret_cross_attr("exphappy")
# %% codecell
ret_cross_attr("go_out")
# %% codecell

# %% codecell

# %% codecell

# %% codecell

# %% codecell

# %% markdown
# # Observations
# %% markdown
# - 20.740 got a second date
