import os
import subprocess

def setup_dit():
    # Clone the DiT repository
    subprocess.run(["git", "clone", "https://github.com/facebookresearch/DiT.git"])
    
    # Change to the DiT directory
    os.chdir("DiT")
    
    # Install the requirements
    subprocess.run(["pip", "install", "-r", "requirements.txt"])
    
    print("DiT repository has been cloned and set up successfully.")

if __name__ == "__main__":
    setup_dit()
