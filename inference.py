from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

def generate_doc(code_snippet):
    model_name = "trained_model"
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

    inputs = tokenizer(code_snippet, return_tensors="pt")
    outputs = model.generate(**inputs, max_length=128)
    return tokenizer.decode(outputs[0], skip_special_tokens=True)

if __name__ == "__main__":
    print(generate_doc("def multiply(a, b): return a * b"))
