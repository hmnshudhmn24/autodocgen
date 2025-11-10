from transformers import AutoTokenizer, AutoModelForSeq2SeqLM, Trainer, TrainingArguments
from datasets import load_dataset
import torch, json

def train_model():
    model_name = "Salesforce/codet5-small"
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

    dataset = load_dataset("json", data_files={"train": "data_examples/sample_dataset.jsonl"})
    def preprocess(batch):
        inputs = tokenizer(batch["code"], truncation=True, padding="max_length", max_length=128)
        labels = tokenizer(batch["doc"], truncation=True, padding="max_length", max_length=128)
        inputs["labels"] = labels["input_ids"]
        return inputs
    tokenized = dataset["train"].map(preprocess, batched=True)

    args = TrainingArguments(
        output_dir="results",
        num_train_epochs=3,
        per_device_train_batch_size=2,
        save_strategy="epoch",
        logging_dir="logs",
    )

    trainer = Trainer(model=model, args=args, train_dataset=tokenized)
    trainer.train()
    model.save_pretrained("trained_model")
    tokenizer.save_pretrained("trained_model")

if __name__ == "__main__":
    train_model()
