import os
import subprocess
import sys

def pip_install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

def path_install(package):
	subprocess.check_call([sys.executable, "-m", "python", "spacy", package])

pip_packages = ["adjustText", 
				"beautifulsoup4", 
				"bs4", 
				"en-core-web-sm", 
				"future", 
				"gensim", 
				"joblib", 
				"nltk", 
				"num2words", 
				"numpy", 
				"pandas",
				"plotly", 
				"pyLDAvis", 
				"requests", 
				"scattertext",
				"scikit-learn", 
				"scipy", 
				"seaborn",
				"selenium",
				"spacy", 
				"statsmodels", 
				"text2num",
				"tqdm"] 

path_packages = ["python -m spacy download en_core_web_sm",
				 'pip install "notebook>=5.3" "ipywidgets>=7.2"']  

for package in pip_packages:
	pip_install(package)

for package in path_packages:
	os.system(package)

