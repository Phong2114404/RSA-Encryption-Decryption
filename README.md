# RSA Encryption/Decryption Application

## Overview
This project implements the RSA encryption and decryption algorithm in Python. It features:
- A command-line-based RSA encryption and decryption module.
- A user-friendly graphical interface (GUI) for interacting with the RSA algorithm using PyQt5.

The application satisfies the requirements to generate RSA keys, encrypt plaintext messages, and decrypt ciphertext without relying on external RSA libraries.

---

## Features
1. **Key Generation**:
   - Generates two large prime numbers \(p\) and \(q\) with a minimum size of 512 bits.
   - Calculates the RSA public and private keys (\(e, d\)).

2. **Encryption**:
   - Converts plaintext messages into ciphertext using the public key (\(e, n\)).

3. **Decryption**:
   - Recovers plaintext from ciphertext using the private key (\(d, n\)).

4. **Miller-Rabin Primality Test**:
   - Ensures the primality of \(p\) and \(q\) using a probabilistic primality test.

5. **Graphical Interface**:
   - Provides an easy-to-use GUI built with PyQt5 for key generation, encryption, and decryption.

---

## File Structure
### 1. `RSA.py`
This file implements the core RSA functionalities:
- **Primality Testing**: Uses the Miller-Rabin algorithm to test primality of randomly generated numbers.
- **Key Generation**: Generates public and private keys.
- **Encryption and Decryption**: Performs RSA encryption and decryption using modular arithmetic.

### 2. `UI.py`
This file implements the PyQt5-based GUI for interacting with the RSA algorithm:
- Allows users to input plaintext for encryption.
- Displays generated RSA keys and results of encryption and decryption.

---

## How to Run

### **Requirements**
1. Python 3.7 or higher
2. PyQt5 library
   - Install via pip:
     ```bash
     pip install PyQt5
     ```

### **Running the Application**
1. Run the GUI:
   ```bash
   python UI.py
   ```
  - The GUI window will open, allowing you to:
    - Enter a plaintext message.
    - Generate RSA keys.
    - Encrypt and decrypt messages.
2. Run the Command-Line Application:
   ```bash
   python RSA.py
   ```
  - Follow the prompts to input plaintext, view keys, and display the encrypted/decrypted text.  

## Usage Instructions

### Using the GUI (`UI.py`)

1. **Enter Message**:
   - Input the plaintext message in the **"Enter Message"** field.

2. **View RSA Keys**:
   - After running the program, the following values will be displayed:
     - **p, q**: The two large prime numbers.
     - **e, d, n**: The public key \((e, n)\) and private key \((d, n)\).

3. **Encrypt Message**:
   - The **"Encrypt"** field shows the ciphertext after encryption.

4. **Decrypt Message**:
   - The **"Decrypt"** field shows the plaintext message recovered from the ciphertext.

5. **Clear All**:
   - The **"Clear All"** button resets all fields.

## Example Output

### User Interface Example:
![UI Example](ui_example "Preview of the User Interface")

### Command-Line Example:
![Command Line Example](cmdline_example "Preview of the Command Line")

## Implementation Details

### Mathematical Background

1. **Key Generation**:
   - \( n = p \times q \)
   - \( \phi(n) = (p - 1) \times (q - 1) \)
   - Choose \( e \) such that \( 1 < e < \phi(n) \) and \( \text{gcd}(e, \phi(n)) = 1 \).
   - Calculate \( d \) as the modular inverse of \( e \) modulo \( \phi(n) \).

2. **Encryption**:
   - Ciphertext (\( C \)) is computed as:
     \[
     C = M^e \mod n
     \]

3. **Decryption**:
   - Plaintext (\( M \)) is recovered as:
     \[
     M = C^d \mod n
     \]

### Primality Testing
- Uses the Miller-Rabin algorithm to ensure \( p \) and \( q \) are prime.

## Limitations

1. The application only supports plaintext messages in **ASCII characters**.
2. Large messages may require segmentation for encryption.

---

## Authors

1. Phong Tran - 2114404 - The Faculty of Computer Science and Engineering, HCMUT
2. Phat Vu - 2114391 - The Faculty of Computer Science and Engineering, HCMUT


