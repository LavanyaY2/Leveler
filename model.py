import pandas as pd
from sentence_transformers import SentenceTransformer, util

model = SentenceTransformer('paraphrase-MiniLM-L6-v2')
df = pd.read_csv("hf://datasets/jacob-hugging-face/job-descriptions/training_data.csv")
rel_df = df[['position_title', 'company_name', 'job_description']]
rel_df = rel_df.rename(columns={'position_title':'title', 'company_name':'company', 'job_description':'desc'})
job_embeddings = model.encode(rel_df['desc'].tolist(), convert_to_tensor=True)

def match_descs(education, experience, skills):
    global rel_df
    user_exp = education + " " + experience + " " + skills
    user_exp = user_exp.strip()
    user_embedding = model.encode(user_exp, convert_to_tensor=True)
    similarity_scores = util.pytorch_cos_sim(user_embedding, job_embeddings)[0]
    rel_df['similarity_score'] = similarity_scores.cpu().numpy()
    rel_df = rel_df.sort_values(by='similarity_score', ascending=False)
    rel_df['similarity_score'] = (rel_df['similarity_score']*100).astype(str) + "%"

    return rel_df



#return only title, company, job desc, and score. add option to filter by top 10, 50, etc.
