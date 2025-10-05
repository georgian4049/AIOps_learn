from pypdf import PdfReader
import json

# Read CV PDF
try:
    reader = PdfReader("./data/Ayush_Resume.pdf")
    cv = ""
    # for page in reader.pages:
    #     text = page.extract_text()
    #     if text:
    #         cv += text
    cv = """
          Full-stack developer with a proven track record in building scalable Single Page Application using ReactJs, backend
(Flask, Django), and robust databases (PostgreSQL). Experienced in delivering end-to-end solutions within diverse agile
development environments, from fast-paced startups to established institutions and research institutes. Currently com-
pleting a Master’s in AI & Generative AI while leading front-end teams. Available for full-time roles from November 1,
2025, and based in Germany with full EU relocation flexibility.
Experience
AI Research- (Intern), NECLABS Europe – Heidelberg, Germany July 2025 - Oct 2025
• Developing an in silico pipeline integrating ESM-LLMs lineage predictions with AlphaFold to assess virus mutational
impacts and predicting next possible evolution for Drug/Vaccine Design. Modeled changes in protein-protein
interaction (PPI) interfaces to prioritize variants with enhanced host-receptor binding affinity.
• Fine-tuning and transfer learning for protein LLM, ESM models. Improved accuracy by 9% and reduced training time
by almost 66% as part of different works.
• Developed a Phylogenetic Distance regression model using ESM embedding and MLP and achieved Pearson
correlation of 0.998 and Spearman correlation of 0.997, hence replacing existing time consuming phylogenetic
distance calculator (Blosum 62). In Silico modelling now takes hours instead of days.
GenAI/ Full Stack Developer (Werkstudent), BASF – Ludwigshafen, Germany Nov 2024 - May 2025
• Engineered a Python solution to identify similar time series patterns, automating a critical data analysis process.
• Prototyped Multi Agent open source LLM-based contract summarizer
• Developed in house React-Typescript dashboard for time series data analysis consisting of important features like
Charts, Figures, Tables etc
Full Stack Developer- Inline Process Solutions( Startup), Germany Feb 2023 - Oct 2024
• Architected and served as the lead Front end developer for the core client-facing application, delivering a robust
platform that became the primary interface for pilot users and secured positive initial feedback.
• The interactive Single Page Application mostly served featrues like Forms, Charts, Images.
Frontend Lead (Werkstudent), Co2Opt( Startup) – Hamburg, Germany • Led the front-end development of a core SaaS application, creating an intuitive UI.
• Delivered responsive UI with SPA principles, applying progressive enhancement for performance
Jun 2022 - Jul 2023
Full Stack Developer, GreatLearning & Altimetrik (Startups/Mid Size) – Bengaluru, India Jan 2020 - Apr 2022
• Delivered a full-stack (ReactJs, Django, PostgreSQL) analytics platform that provided actionable insights into students
behavior, helping course managers increase in student engagement.
• Mentored and led a team of 4 interns to develop a successful prototype that automated a project initiation workflow.
Projects
In Silico modelling- Virus Evolution Prediction- (Pytorch, ESM-LLMs, AlphaFold) Private Repo
• Researching on predicting protein sequences using pure ESM embedding instead of Blosum62/80 matrix technique.
• Using Embedding Cosine Distance and Phylogenetic Distance as loss function to drive the evolution process.
• Following Insertion, deletion and substitution of Amino acids to generate evolutions.
Multi-Agent Research Paper Literature Reviewer- (Python, Microsoft’s Autogen, GenAI)
• A MAS that downloads or uploads research papers and generates literature review along with human feedback loop.
Style transfer on synthetic Time series Data (Transformers, GANs, Pytorch). Private Repo
• Used GANs and Transformers to augment synthetic time series data to look like real world data.
Gemini Document Extractor(Closed Source Model- Gemini AI(GenAI), React)
• Single page application to extract key information from documents. Developed using Google’s Gemini.
Education
M.Sc., Computer Science(AI/ML), TU Kaiserslautern (RPTU), Germany Apr 2022 - Oct 2025
• Research Thesis: Leveraging Hierarchies via multimodal prompt learning for Fine-Grained Image Recognition.
• Keywords: Computer Vision, Natural Language Processing, CLIP (OpenAI), VLM (Vision Language Model), Transfer
Learning, Prompt Learning
B.E., Information Science, CGPA: 8.21/10, MVJ College Of Engineering (VTU) – Bengaluru May 2016 - Apr 2020
Technical Skills
Languages: Python, JavaScript, TypeScript, HTML/CSS
ML/NLP: Transformers, LLMs, Generative AI, Diffusion Models, RAG, Ollama, ESM-LLMs, MCP
Frameworks: PyTorch, HuggingFace, React, Flask-FastAPI, Django, LangChain, ExpressJs
Ops(Basic): Docker, AWS, Lambda, Kubernetes, Terraform, CI/CD, MLFlow, AirFlow
Databases: MongoDB, PostgreSQL, Pinecone(VectorDB), SQL
Git: Github, Gitlab, BitBucket, DVC
Achievements
• Basyx Digital Twins Hackathon Winner, Fraunhofer IESE, Kaiserslautern Germany(Oct 2023)
• GEM Award, Altimetrik India Pvt Ltd, Bengaluru India(Jun 2020)
• Reimagine Waste Hackathon, Runners Up, IISc, Bengaluru India(Sep 2018)
          """
except FileNotFoundError:
    cv = "CV not available"

# Read other data files
with open("./data/summary.txt", "r", encoding="utf-8") as f:
    summary = f.read()

with open("./data/style.txt", "r", encoding="utf-8") as f:
    style = f.read()

with open("./data/facts.json", "r", encoding="utf-8") as f:
    facts = json.load(f)
    

    