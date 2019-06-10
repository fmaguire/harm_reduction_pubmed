import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
sns.set_context('notebook')
sns.set(rc={'figure.figsize':(9,8)})
sns.set_style('ticks')

if __name__ == '__main__':

    df = pd.read_csv('affiliation_counts.csv')

    df = df.sort_values('count')
    sns.barplot(data = df, y='speciality', x='count')
    plt.xlabel('Number of Affiliations')
    plt.ylabel('CMA Medical Specialties')
    plt.title('PubMed Articles mentioning "Harm Reduction"')
    sns.despine()
    plt.tight_layout()
    plt.savefig('harm_reduction.png')

