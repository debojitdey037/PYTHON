import pandas as p
d = {
    "name":["alice","shubham","rohit",],
    "age":[22,25,25],
    "score":[85,92,95]

}
df = p.DataFrame(d)
print(df)
print(df.head(2))
print(df.info())
print(df['score'])
print(df[['name','age']])
df['location'] = ["USA","Delhi","Noida"]
print(df)
df.drop(columns=["age"])
print(df)

