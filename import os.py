import os

# Target base directory
base_dir = r"E:\Personal\GitHub\Python Code Repo\financesignallab"

# Folders required for Minimal Mistakes
folders = [
    "_includes",
    "_layouts",
    "_data",
    "assets",
    "assets/css",
    "assets/images"
]

def create_structure():
    for folder in folders:
        path = os.path.join(base_dir, folder)
        try:
            os.makedirs(path, exist_ok=True)
            print(f"Created: {path}")
        except Exception as e:
            print(f"Error creating {path}: {e}")

if __name__ == "__main__":
    create_structure()
    print("\nFolder structure setup complete.")
