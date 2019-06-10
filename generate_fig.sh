#!/bin/bash
echo "Getting pubs"
esearch -db pubmed -query "harm reduction" | efetch -format "medline" | grep "AD  - "  > pubmed_harm_reduction_affiliations.txt

echo "Tallying affiliations"
echo "speciality,count" > affiliation_counts.csv
while IFS="\n" read -r line
do
    echo "$line,$(grep -c -i -E "$line" pubmed_harm_reduction_affiliations.txt)" >> affiliation_counts.csv
done < speciality_list.txt

echo "Plotting data"
python plot.py
