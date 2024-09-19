# BodyShapeGPT: SMPL Body Shape Manipulation with LLMs

Official repository of "BodyShapeGPT: SMPL Body Shape Manipulation with LLMs" [ECCVW 2024]

[Baldomero R. Árbol](https://www.linkedin.com/in/baldomero-rodríguez-árbol-716132224/), [Dan Casas](https://dancasas.github.io/)

In [European Conference on Computer Vision Workshops (ECCVW) 2024](https://eccv.ecva.net), [Workshop on Foundation Models for 3D Humans](https://human-foundation.github.io/workshop-eccv-2024/)

[PDF📄](./img/BodyShapeGPT_summary.gif)

![BodyShapeGPT Summary](./img/BodyShapeGPT_summary.gif)

Generative AI models provide a wide range of tools capable of performing complex tasks in a fraction of the time it would take a human. Among these, Large Language Models (LLMs) stand out for their ability to generate diverse texts, from literary narratives to specialized responses in different fields of knowledge. This paper explores the use of fine-tuned LLMs to identify physical descriptions of people, and subsequently create accurate representations of avatars using the SMPL-X model by inferring shape parameters. Our results demonstrate that LLMs can be trained to understand and manipulate the shape space of SMPL, allowing the control of 3D human shapes through natural language. This approach promises to improve human-machine interaction and opens new avenues for customization and simulation in virtual environments.

## Installation
Please follow the steps below to use BodyShapeGPT. 
### 1. The following tools are required:
* [Nvidia CUDA Toolkit 11.5](https://developer.nvidia.com/cuda-11-5-0-download-archive) or higher
* [Python 3.9](https://www.python.org/downloads/release/python-390/) installed

### 2. Clone this repository
```
git clone https://github.com/baldoarbol/BodyShapeGPT
```
### 3. Install all the library and dependencies
```
pip install -r requirements.txt
```
### 4. Download the model weights
Use [this OneDrive link](https://urjc-my.sharepoint.com/:u:/g/personal/baldomero_rodriguez_urjc_es/EUvZWSzuoEJAtJQB-iWWzdYBuDYj51hwOFmxQ429VeajEg?e=PpQ9QM) to download the LoRa model weights (.safetensors file). After downloading, place the .safetensors file into the "weights" folder located within the project directory.

## Running the Model
You can use the script demo.py to try our model. Usage:
```
python3.9 demo.py "[avatar description]"
```
demo.py runs a single inference on the provided prompt and outputs the result betas for a gender-neutral SMPL-X body. Feel free to customize the script as needed to better fit your use case.

## Dataset
In the root directory of this project, you'll find the `BodyShapeGPT_dataset.jsonl` file, which contains 21,000 natural language descriptions of avatars, each paired with their corresponding gender-neutral SMPL-X shape parameters.

## Citation
If you find this repository useful please cite our work:

```
@InProceedings{R-ARBOL_2024_ECCV_BodyShapeGpt,
    author = {R. Árbol, Baldomero and Casas, Dan},
    title = {BodyShapeGPT: SMPL Body Shape Manipulation with LLMs},
    booktitle = {European Conference on Computer Vision Workshops (ECCVW) 2024}, 
    year = {2024}
}
```

