import torch
import sys
from transformers import AutoTokenizer, AutoModelForCausalLM, BitsAndBytesConfig
import re
from peft import PeftModel

FINE_TUNED_WEIGHTS = "weights"
BASE_MODEL_ID = "meta-llama/Meta-Llama-3-8B"


def main():
    if len(sys.argv) == 2:
        description = sys.argv[1]

        tokenizer, ft_model = load_model()

        raw_answer = run_model(description, tokenizer, ft_model)
        parsed_betas = parse_betas(raw_answer)

        print("Description: " + description + " | SMPL-X Shape parameters: " + str(parsed_betas))
    else:
        print("Invalid argument. Correct usage: python demo.py \"avatar description\"")
    

def load_model():
    print("[Load model start]")
    bnb_config = BitsAndBytesConfig(
        load_in_4bit=True,
        bnb_4bit_use_double_quant=True,
        bnb_4bit_quant_type="nf4",
        bnb_4bit_compute_dtype=torch.bfloat16
    )
    base_model = AutoModelForCausalLM.from_pretrained(
        BASE_MODEL_ID,
        quantization_config=bnb_config,
        device_map="cuda",
        trust_remote_code=True,
    )
    tokenizer = AutoTokenizer.from_pretrained(BASE_MODEL_ID, add_bos_token=True, trust_remote_code=True)
    ft_model = PeftModel.from_pretrained(base_model, FINE_TUNED_WEIGHTS)
    print("[Load model complete]")
    return tokenizer, ft_model


def run_model(input_text, tokenizer, ft_model):
    print("[Inference start]")
    eval_prompt = "### Description: " + input_text + "\n ### Shape parameters: "
    model_input = tokenizer(eval_prompt, return_tensors="pt").to("cuda")
    ft_model.eval()
    with torch.no_grad():
        answer = tokenizer.decode(ft_model.generate(**model_input, max_new_tokens=100)[0], skip_special_tokens=True)
    print("[Inference complete]")
    return answer


def parse_betas(text):
    # Extract the first ten floats from the response to remove noise
    parsed_betas = re.findall(r'-?\d+\.\d+', text)
    parsed_betas = [float(num) for num in parsed_betas]
    return parsed_betas[:10]


if __name__ == "__main__":
    main()
