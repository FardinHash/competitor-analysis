from transformers import AutoModelForCausalLM, AutoTokenizer
from utils.hf_auth import authenticate_hf

class SWOTAnalysisAgent:
    def __init__(self):
        authenticate_hf()
        self.tokenizer = AutoTokenizer.from_pretrained("meta-llama/Llama-2-7b-chat-hf")
        self.model = AutoModelForCausalLM.from_pretrained(
            "meta-llama/Llama-2-7b-chat-hf",
            device_map="auto",
            torch_dtype="auto"
        )

    def clean_response(self, response):
        lines = response.split("\n")
        unique_lines = []
        seen = set()
        for line in lines:
            line_clean = line.strip()
            if line_clean not in seen and line_clean:
                unique_lines.append(line_clean)
                seen.add(line_clean)
        return "\n".join(unique_lines)

    def analyze(self, data, company_name):
        google_summary = data.get("google_summary", [])
        wikipedia_summary = data.get("wikipedia_summary", "No summary available")

        google_summary_text = "\n".join(google_summary) if google_summary else "No data available"
        prompt = (
            f"Perform a detailed SWOT analysis for the company '{company_name}' based on the following information:\n\n"
            f"Google Summary:\n{google_summary_text}\n\n"
            f"Wikipedia Summary:\n{wikipedia_summary}\n\n"
            "Provide the analysis in the format:\n"
            "Strengths:\n- Point 1\n- Point 2\n\n"
            "Weaknesses:\n- Point 1\n- Point 2\n\n"
            "Opportunities:\n- Point 1\n- Point 2\n\n"
            "Threats:\n- Point 1\n- Point 2"
        )

        try:
            inputs = self.tokenizer(prompt, return_tensors="pt")
            outputs = self.model.generate(
                inputs.input_ids,
                max_length=800,
                num_return_sequences=1,
                do_sample=True,
                temperature=0.7,
                top_k=50,
            )
            response = self.tokenizer.decode(outputs[0], skip_special_tokens=True)
            return self.clean_response(response)
        except Exception as e:
            return f"Error generating SWOT analysis: {e}"
