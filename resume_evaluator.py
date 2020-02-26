# Install docx2txt
# pip install docx2txt

# Importing
import docx2txt

# Uploading two files - 1. Resume
#                       2. Job Description
from google.colab import files
uploaded = files.upload()

# Storing resume file in the variable
resume = docx2txt.process("python_resume.docx")

# Printing it
print(resume)

# Storing job description in a variable
job_description = docx2txt.process("job_description.docx")

# Printing it
print(job_description)

# Creating a list for future comparision
text = [resume, job_description]


# Importing CountVectorizer from sklearn
from sklearn.feature_extraction.text import CountVectorizer

# Storing it in a variable
cv = CountVectorizer()

# Using count_matrix
count_matrix = cv.fit_transform(text)

# Importing cosine_similarity from sklearn
from sklearn.metrics.pairwise import cosine_similarity

print("\nSimilarity Scores:")

# Printing the similarity scores (we get this  in the form of matrix)
print(cosine_similarity(count_matrix))

# Converting the matrix scores into percentage 
matchPercentage = cosine_similarity(count_matrix)[0][1] * 100

matchPercentage = round(matchPercentage, 2) # Show upto 2 decimal places

# Finally displaying the similarity between job description and the resume of the candidate
print("Your resume matches about "+ str(matchPercentage)+ "% of the job description.")
