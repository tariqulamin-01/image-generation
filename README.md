# Image Generation using DreamShaper-7

## Overview
This project utilizes **DreamShaper-7**, a powerful AI model for generating high-quality images from text prompts. The model is based on Stable Diffusion and fine-tuned for artistic and realistic outputs.

## Features
- Generate stunning images from textual descriptions
- Support for different styles and resolutions
- Customizable parameters for fine-tuned output
- Easy integration into existing AI workflows

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/tariqulamin-01/image-generation.git
   cd image-generation
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Download the DreamShaper-7 model from the official source and place it in the `models/` directory.

## Usage
Run the script to generate images from text prompts:
```bash
python app.py 
```
### Available Arguments
- `--prompt` (str): The text description of the image to be generated.
- `--steps` (int, optional): Number of inference steps (default: 50).
- `--guidance_scale` (float, optional): Higher values enhance prompt adherence (default: 7.5).
- `--output_dir` (str, optional): Directory to save generated images (default: `outputs/`).

## Example
```bash
python app.py 
```

## Output
Generated images will be saved in the `outputs/` directory with a timestamped filename.

## Model Information
DreamShaper-7 is a fine-tuned model based on **Stable Diffusion**. It is optimized for:
- High-quality artistic renders
- Improved realism and detail
- Versatile creative applications

## License
This project is licensed under the **MIT License**. See the `LICENSE` file for more details.

## Contributions
Contributions are welcome! Feel free to open issues or submit pull requests.

## Acknowledgments
- [Stable Diffusion](https://stablediffusionweb.com/)
- DreamShaper-7 model creators

## Contact
For any inquiries, reach out via GitHub Issues or email **amintariqul01@gmail.com**.

---
Happy Generating! 🚀

