import subprocess

def generate_random_base64():
    # Esegui il comando openssl
    result = subprocess.run(['openssl', 'rand', '-base64', '42'], capture_output=True, text=True)
    
    # Restituisci il risultato (random base64 string)
    return result.stdout.strip()

# Esegui la funzione e stampa il risultato
random_string = generate_random_base64()
print(random_string)
