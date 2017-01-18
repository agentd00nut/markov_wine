rm prep1.txt 2>/dev/null

# capture output of script
python get-reviews.py >> prep1.txt

# remove all lines that indicate progress of script
#cat grep -E -v '^-' prep1.txt > prep2.txt

# add the words "BEGIN NOW" to the beginning of each line
cat prep1.txt | sed 's/^/BEGIN NOW /' > prep2.txt

# add the word "END" to the end of each line
cat prep2.txt | sed 's/$/ END/' > prep3.txt

# Scrub the end of the lines of link text.
sed 's/Drink now.*END/END/g' prep3.txt > wine-reviews.txt


mkdir -p prep/
mv prep1.txt prep2.txt prep3.txt prep/
