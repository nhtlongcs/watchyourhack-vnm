import re
import yaml
import nltk

nltk.download('punkt')
from openai import OpenAI

client = OpenAI(api_key='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')  # Replace with your OpenAI API key
chunk_size = 1000

def translate_text_with_openai(text, target_language):
    prompt = f"Translate the following English text to {target_language}, keep the original word not suitable translate, like name or proper words:\n\n{text}\n\n output:"

    response = client.completions.create(
        model="gpt-3.5-turbo-instruct",
        prompt=prompt,
        max_tokens=2048
    )
    # Extract and return the translated text from the OpenAI API response
    translated_text = response.choices[0].text
    return translated_text


def extract_content(markdown_content):
    # Define a regex pattern to match the YAML front matter
    front_matter_pattern = re.compile(r'^---\s*([\s\S]*?)\s*---', re.DOTALL)

    # Extract YAML front matter using the regex pattern
    front_matter_match = re.match(front_matter_pattern, markdown_content)
    if front_matter_match:
        front_matter = front_matter_match.group(1)
        header = '---\n' + front_matter + '\n---\n'
    else:
        header = {}
    
    # Remove YAML front matter from the content
    content_without_front_matter = re.sub(front_matter_pattern, '', markdown_content, count=1)
    
    return header, content_without_front_matter.strip()

def split_into_sentences(text):
    sentences = nltk.sent_tokenize(text)
    return sentences

def translate_jekyll_md_file(input_file, output_file, target_language):
    with open(input_file, 'r', encoding='utf-8') as file:
        original_text = file.read()

    header, content = extract_content(original_text)
    # Split content into sentences
    sentences = split_into_sentences(content)

    # Split sentences into chunks while maintaining sentence integrity
    current_chunk = ""
    translated_chunks = []

    for sentence in sentences:
        if len(current_chunk) + len(sentence) <= chunk_size:
            current_chunk += sentence
        else:
            translated_chunk = translate_text_with_openai(current_chunk, target_language)
            translated_chunks.append(translated_chunk)
            current_chunk = sentence

    # Translate the last chunk
    translated_chunk = translate_text_with_openai(current_chunk, target_language)
    translated_chunks.append(translated_chunk)

    # Merge translated chunks and write to output file
    translated_text = header + ''.join(translated_chunks)
    with open(output_file, 'w', encoding='utf-8') as file:
        file.write(translated_text)

if __name__ == "__main__":
    input_file_path = "/Users/nhtlong/Workspace/tmp/Docker/README.md"
    output_file_path = "output_file.md"
    target_language = "vietnamese"  # Change to your target language code

    translate_jekyll_md_file(input_file_path, output_file_path, target_language)
