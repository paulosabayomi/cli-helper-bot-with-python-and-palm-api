import google.generativeai as palm
import os, sys
from dotenv import load_dotenv

load_dotenv()

print("configuring API...")

palm.configure(api_key=os.environ['API_KEY'])

print("parsing CLI arguments...")
argz = sys.argv[1:]
print("CLI arguments parsed")

print("checking command type...")

is_completion = "--completion" in argz or "-c" in argz

argz = ' '.join([x for x in argz if x != "--completion" and x != "-c"])




if is_completion:
    print("Generating reponse for ", argz, " using palm.generate_text...")
    generative = palm.generate_text(
        prompt=argz,
        temperature=1.0
    )
    print(generative.result)
else:
    print("Generating reponse for ", argz, " using palm.chat...")
    response = palm.chat(
        prompt=argz,
        temperature=1.0
    )
    print(response.candidates[0]['content'])



