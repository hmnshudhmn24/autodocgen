# 🧠 AutoDocGen — AI Code Documentation & Test Generator  

**AutoDocGen** is an intelligent tool built on **CodeT5** that automatically generates high-quality documentation, inline comments, and unit tests for your source code.  


## 🚀 Features  
✨ **Automatic Docstring Generation** — Instantly create detailed Python docstrings.  
🧩 **Unit Test Creation** — Generate unit tests directly from your functions.  
🧠 **Trainable & Extendable** — Fine-tune on your own dataset for domain-specific results.  


## 📂 Project Structure  

| File / Folder | Description |
|----------------|-------------|
| `train_codet5_docgen.py` | Script to fine-tune the CodeT5 model for documentation generation |
| `inference.py` | Run the trained model to generate docstrings or comments |
| `cli.py` | Command-line interface for easy model interaction |
| `configs/train_config.json` | Configuration file containing training parameters |
| `data_examples/` | Example dataset and code samples for training/testing |
| `tests/` | Unit test folder to validate model outputs |


## 🧠 Model Overview  

AutoDocGen fine-tunes **CodeT5-small** from [Hugging Face Transformers](https://huggingface.co/) on a curated dataset of Python code and natural language descriptions.  
It learns to understand code semantics and produce accurate, readable documentation and test cases.


## ⚙️ Installation  

```bash
# Clone the repository
git clone https://github.com/hmnshudhmn24/AutoDocGen.git
cd AutoDocGen

# Install dependencies
pip install -r requirements.txt
```


## 🧪 Usage  

### Generate Docstrings
```bash
python inference.py --input your_code.py
```

### Train on Custom Dataset
```bash
python train_codet5_docgen.py --config configs/train_config.json
```
