
"""
tokenizer 和 训练数据配置文件
"""

# https://huggingface.co/baichuan-inc/Baichuan-7B/blob/main/tokenizer.model
# TOKENIZER_MODEL = "tokenizers/baichuan/tokenizer.model" # the baichuan sentencepiece tokenizer model
# TOKENIZER_BIN = "tokenizers/baichuan/tokenizer.bin" # binary version of the tokenizer for inference in C

# https://huggingface.co/ziqingyang/chinese-llama-2-7b/blob/main/tokenizer.model
TOKENIZER_MODEL = "tokenizers/llama2enzh/tokenizer.model" # the llama2.
TOKENIZER_BIN = "tokenizers/llama2enzh/tokenizer.bin" # binary version of the tokenizer for inference in C

# base llama2，
# TOKENIZER_MODEL = "tokenizers/llama2en/tokenizer.model" # the llama2-enzh.
# TOKENIZER_BIN = "tokenizers/llama2en/tokenizer.bin" # binary version of the tokenizer for inference in C