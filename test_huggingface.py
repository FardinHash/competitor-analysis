from transformers import AutoModelForCausalLM, AutoTokenizer
import re

def clean_response(response):
    lines = response.split("\n")
    unique_lines = []
    seen = set()
    for line in lines:
        line_clean = line.strip()
        if line_clean not in seen and line_clean:  
            unique_lines.append(line_clean)
            seen.add(line_clean)
    return "\n".join(unique_lines)

def test_huggingface():
    try:
        model_name = "facebook/opt-350m"
        tokenizer = AutoTokenizer.from_pretrained(model_name)
        model = AutoModelForCausalLM.from_pretrained(model_name)
        
        prompt = "Provide a SWOT analysis for Tesla:\n\nStrengths:\n-"
        inputs = tokenizer(prompt, return_tensors="pt")
        outputs = model.generate(
            inputs.input_ids,
            max_length=200,
            num_return_sequences=1,
            temperature=0.7, 
            top_k=50  
        )

        response = tokenizer.decode(outputs[0], skip_special_tokens=True) 
        cleaned_response = clean_response(response)
        
        print("Generated Response:")
        print(cleaned_response)
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    test_huggingface()
