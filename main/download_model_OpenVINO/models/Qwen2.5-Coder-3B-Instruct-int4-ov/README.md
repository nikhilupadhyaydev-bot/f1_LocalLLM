---
license: apache-2.0
license_link: https://huggingface.co/Qwen/Qwen2.5-Coder-3B-Instruct/blob/main/LICENSE
language:
- en
base_model: 
  - Qwen/Qwen2.5-Coder-3B-Instruct
pipeline_tag: text-generation
library_name: transformers
tags:
- code
- codeqwen
- chat
- qwen
- qwen-coder
base_model_relation: quantized
---

# Qwen2.5-Coder-3B-Instruct-int4-ov
 * Model creator: [Qwen](https://huggingface.co/Qwen)
 * Original model: [Qwen2.5-Coder-3B-Instruct](https://huggingface.co/Qwen/Qwen2.5-Coder-3B-Instruct)

## Description
This is [Qwen2.5-Coder-3B-Instruct](https://huggingface.co/Qwen/Qwen2.5-Coder-3B-Instruct) model converted to the [OpenVINO™ IR](https://docs.openvino.ai/2025/documentation/openvino-ir-format.html) (Intermediate Representation) format with weights compressed to INT4 by [NNCF](https://github.com/openvinotoolkit/nncf).

## Quantization Parameters

Weight compression was performed using `nncf.compress_weights` with the following parameters:

* mode: **INT4_ASYM**

For more information on quantization, check the [OpenVINO model optimization guide](https://docs.openvino.ai/2025/openvino-workflow/model-optimization-guide/weight-compression.html).


## Compatibility

The provided OpenVINO™ IR model is compatible with:

* OpenVINO version 2025.2.0 and higher
* Optimum Intel 1.25.0 and higher

## Running Model Inference with [Optimum Intel](https://huggingface.co/docs/optimum/intel/index)

1. Install packages required for using [Optimum Intel](https://huggingface.co/docs/optimum/intel/index) integration with the OpenVINO backend:

```
pip install optimum[openvino]
```

2. Run model inference:

```
from transformers import AutoTokenizer
from optimum.intel.openvino import OVModelForCausalLM

model_id = "OpenVINO/Qwen2.5-Coder-3B-Instruct-int4-ov"
tokenizer = AutoTokenizer.from_pretrained(model_id)
model = OVModelForCausalLM.from_pretrained(model_id)

inputs = tokenizer("write a quick sort algorithm.", return_tensors="pt")

outputs = model.generate(**inputs, max_length=200)
text = tokenizer.batch_decode(outputs)[0]
print(text)
```

For more examples and possible optimizations, refer to the [Inference with Optimum Intel](https://docs.openvino.ai/2025/openvino-workflow-generative/inference-with-optimum-intel.html).

## Running Model Inference with [OpenVINO GenAI](https://github.com/openvinotoolkit/openvino.genai)


1. Install packages required for using OpenVINO GenAI.
```
pip install openvino-genai huggingface_hub
```

2. Download model from HuggingFace Hub
   
```
import huggingface_hub as hf_hub

model_id = "OpenVINO/Qwen2.5-Coder-3B-Instruct-int4-ov"
model_path = "Qwen2.5-Coder-3B-Instruct-int4-ov"

hf_hub.snapshot_download(model_id, local_dir=model_path)

```

3. Run model inference:

```
import openvino_genai as ov_genai

device = "CPU"
pipe = ov_genai.LLMPipeline(model_path, device)
pipe.get_tokenizer().set_chat_template(pipe.get_tokenizer().chat_template)
print(pipe.generate("write a quick sort algorithm.", max_length=200))
```

More GenAI usage examples can be found in OpenVINO GenAI library [docs](https://docs.openvino.ai/2025/openvino-workflow-generative/inference-with-genai.html) and [samples](https://github.com/openvinotoolkit/openvino.genai?tab=readme-ov-file#openvino-genai-samples)

You can find more detaild usage examples in OpenVINO Notebooks:

- [LLM](https://openvinotoolkit.github.io/openvino_notebooks/?search=LLM)
- [RAG text generation](https://openvinotoolkit.github.io/openvino_notebooks/?search=RAG+system&tasks=Text+Generation)

## Limitations

Check the original [model card](https://huggingface.co/Qwen/Qwen2.5-Coder-3B-Instruct) for limitations.

## Legal information

The original model is distributed under [Apache License Version 2.0](https://huggingface.co/Qwen/Qwen2.5-Coder-3B-Instruct/blob/main/LICENSE) license. More details can be found in [Qwen2.5-Coder-3B-Instruct](https://huggingface.co/Qwen/Qwen2.5-Coder-3B-Instruct).

## Disclaimer

Intel is committed to respecting human rights and avoiding causing or contributing to adverse impacts on human rights. See [Intel’s Global Human Rights Principles](https://www.intel.com/content/dam/www/central-libraries/us/en/documents/policy-human-rights.pdf). Intel’s products and software are intended only to be used in applications that do not cause or contribute to adverse impacts on human rights.
