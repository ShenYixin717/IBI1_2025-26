'''
1.Library import and dataset creation
2.DataFrame row insertion
3.Gene expression bar chart plotting
4.Specific gene expression query
5.Average gene expression calculation
'''
import pandas as pd
import matplotlib.pyplot as plt
#Create a DataFrame with gene expression data
data = {"Gene":["TP53","EGFR","BRCA1","PTEN","ESR1"],"Expression":[12.4,15.1,8.2,5.3,10.7]}
print("The initial data is",data)
df = pd.DataFrame(data)

#Add a new row to the DataFrame
new_row = {"Gene": "MYC", "Expression": 11.6}
df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)
print("The data that adds a gene is:")
print(df)

#Plot the gene expression levels
ax = df.plot(x="Gene", y="Expression", kind="bar", legend=False)
ax.set_xlabel("Gene")
ax.set_ylabel("Expression Level")
ax.set_title("Gene Expression Levels")
ax.set_xticklabels(df["Gene"], rotation = 45)
ax.grid(axis="y")
plt.show()

#Query the expression level of a specific gene
gene_of_interest = "TP53" 

if gene_of_interest in df["Gene"].values:
    expr_value = df[df["Gene"] == gene_of_interest]["Expression"].values[0]
    print(f"\nGene '{gene_of_interest}' expression level: {expr_value}")
else:
    print(f"\nError: Gene '{gene_of_interest}' is not present in the dataset.")


# Calculate and print the average expression level of all genes
average_expression = df["Expression"].mean()
print(f"\nAverage gene expression level: {average_expression:.2f}")