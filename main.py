import os
import time
from datetime import datetime

# reformats Windows default filepath 
def windows_reformat(filepath):
    filepath = filepath.replace('\\', '/')
    if filepath.startswith('"') and filepath.endswith('"'):
        filepath = filepath[1:-1]
    return filepath

input_path = input("Enter the path to your XML file: ")
output_path = os.path.dirname(windows_reformat(input_path)) 
filename = 'list-{}.txt'.format(datetime.now().strftime("%Y-%m-%d-%H-%M-%S"))
output_file = os.path.join(output_path, filename)

# searches for titles defined as a <series_title> element and writes them to the output file as plaintext, stripping XML data
with open(windows_reformat(input_path)) as input, open(output_file, "w") as output:
        for textline in input:
            if "<series_title>" in textline:
                output.write(textline.replace("        <series_title><![CDATA[", "").replace("]]></series_title>", ""))
                
print("Conversion complete.")
time.sleep(3)
