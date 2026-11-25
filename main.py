# Generates a short funny rant about Monday mornings.

import os

TEXT = (
    "Monday morning is a wet sock pressed firmly against the soul of humanity. "
    "The alarm rings not as a sound, but as a physical blow from a rusted crowbar "
    "wielded by a god who hates your career choices and wishes you had studied "
    "forestry instead."
)

def main():
    output_dir = os.environ.get('MAKEFUN_OUTPUT_DIR', '/output')
    os.makedirs(output_dir, exist_ok=True)
    file_path = os.path.join(output_dir, 'entry.txt')
    
# The gate allows 1-400 characters and the file must contain only the entry plus a trailing newline.
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(TEXT + '\n')

if __name__ == '__main__':
    main()
