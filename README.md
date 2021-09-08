# python 1

This project is intended to be a bare-bones example of how to start a python project.

To start the virtual env:

    pipenv shell

To install the dependencies:

    pipenv install
    pipenv install --dev

Make sure the python interpreter used by VS Code is set to the python installed in your project .venv

To run the project:

    python3 app.py

To test the project:

    pytest

To close the session:

    CTRL + C
    exit


-----

## Substitution Cipher

To run the substitution cipher program...

First, make sure you have a plaintext.txt file with some text in it, and a keyword.txt file with a word in it, and put them in the same folder as the substitution-cipher.py file.

Change into the substitution-cipher folder:

    cd substitution-cipher

Then type the following into your command terminal:

    python3 substitution-cipher.py

This will create a file named ciphertext.txt if it does not already exist, and store the encrypted text there.

To decrypt the ciphertext.txt file type the following into your command terminal:

    python3 substitution-cipher.py -d -i ciphertext.txt -o decryptedtext.txt -k keyword.txt

This will create a file named decryptedtext.txt if it does not already exist, and store the decrypted text there.

At this point the contents of decryptedtext.txt and plaintext.txt should be the same.
