# Demystifying Large Language Model Fine-Tuning: Making AI Understand You Better

We often say: "Understanding technology is more important than mastering the technology itself." In the AI era, large language models will become infrastructure like water and electricity—not everyone needs to build from scratch, but rather learn **how to use them effectively**.

For ordinary users, mastering large language model usage has two levels:

1. **Prompt Engineering**: Like giving clearer, more precise instructions when chatting with AI.
2. **Large Language Model Fine-Tuning**: Making the large model more "aligned with your needs"—today's protagonist.

Let's understand large language model fine-tuning in the most intuitive way. First, imagine a large language model as a super translator:

It's responsible for translating input "sequence X" into output "sequence Y":

```
Input sequence X = [x1, x2, ..., xm]
```

```
Output sequence Y = [y1, y2, ..., yn]
```

Their relationship can be simplified as Y = W \* X

Here, `W` is the model's brain—all knowledge is stored in these parameters. "Large models" are brains with particularly many parameters, some even reaching **hundreds of billions or trillions**!

> Of course, actual models are far more complex than this, but this analogy is sufficient to help understand fine-tuning.

## Why Fine-Tune Large Language Models?

1. **High Cost**: Training a large model from scratch, building wheels from the ground up, is almost only affordable for large companies.
2. **Prompt Limitations**: Prompts that are too long increase inference costs and may be truncated, affecting performance.
3. **Proprietary Data**: Companies have their own industry data, making models more knowledgeable about professional content through fine-tuning.
4. **Personalized Services**: Tailoring small fine-tuned models for each user.
5. **Data Security**: Sensitive data cannot be transmitted to third-party large model services, requiring in-house fine-tuning.

In simple terms: Prompting is like telling AI "how to do it," while fine-tuning is making AI "adapt to your habits."

## Two Routes of Fine-Tuning

From a parameter scale perspective, large language model fine-tuning mainly has two approaches:

1. **Full Fine-Tuning (FFT)**

   - Retraining the entire brain.
   - Advantages: Best performance in specific domains.
   - Disadvantages: High cost, prone to forgetting original knowledge (catastrophic forgetting).

2. **Parameter-Efficient Fine-Tuning (PEFT)**
   - Only training partial parameters, like adding "extensions" to the brain.
   - Advantages: Low cost, preserves original capabilities.

## What Fine-Tuning Methods Are Available?

From training data and methods, large language model fine-tuning mainly has three categories:

1. **Supervised Fine-Tuning (SFT)**
   - Training models with human-annotated data, teaching AI the "correct answers."
2. **Reinforcement Learning from Human Feedback (RLHF)**
   - Using human evaluations to adjust AI, making its output more aligned with human expectations.
3. **Reinforcement Learning from AI Feedback (RLAIF)**
   - Using AI-generated feedback to improve efficiency and reduce costs of collecting human data.

> Regardless of the method, the goal is **using the lowest cost to make models smarter in specific scenarios**.

## Popular PEFT Approaches

As Large Language Models (LLMs) are widely applied across various fields, **fine-tuning** technology has become a key means to make models more "understandable." However, Full Fine-tuning often requires enormous computational resources and data costs. Thus, a series of **Parameter-Efficient Fine-Tuning (PEFT)** methods have emerged.

This article will take you deep into several currently most popular PEFT technical approaches:
**Prompt Tuning**, **Prefix Tuning**, **LoRA**, and **QLoRA**.

### 1. Prompt Tuning: Manipulating the Input

#### Core Concept

The core idea of Prompt Tuning is:

> Without changing the large model's parameters, only adding a small trainable "prompt vector" (Prompt Embedding) at the input front.

In other words, it trains a small portion of "virtual tokens" that don't exist in the vocabulary but are parameters specifically learned by the model.

During inference, these virtual tokens are concatenated to the front of the input sequence to **guide the model to generate expected outputs**.

![image-20251021211731527](pictures/prompt_tuning_diagram.png)_Figure 1 source: [The Power of Scale for Parameter-Efficient Prompt Tuning](https://arxiv.org/abs/2104.08691)_

#### Mathematical Principle

Given the original input sequence:

```
X = [x₁, x₂, ..., xₘ]
```

Prompt Tuning constructs a new input:

```
X' = [p₁, p₂, ..., pₖ; x₁, x₂, ..., xₘ]
```

Where `p₁...pₖ` are trainable **Prompt Embeddings**.

The model output is:

```
Y = W * X'
```

This method influences output results through input-side "prompts" without changing the model backbone.

#### Implementation Characteristics

- Only adjusts at the **Embedding layer**;
- Model parameters are completely frozen;
- High training efficiency, extremely low cost;
- Suitable for classification, generation, Q&A tasks.

Recommended paper: [The Power of Scale for Parameter-Efficient Prompt Tuning (2021)](https://arxiv.org/abs/2104.08691)

### 2. Prefix Tuning: Adding "Prefix" to Network Structure

#### Core Concept

Prefix Tuning's inspiration comes from Prompt Engineering:

> Adding appropriate contextual conditions to models can significantly improve generation quality.

Unlike Prompt Tuning, Prefix Tuning **not only modifies the input layer** but **injects additional trainable prefix vectors in every Transformer layer**.

![image-20251021211343986](pictures/prefix_tuning_diagram.png)

_Figure 2 source: [Prefix-Tuning: Optimizing Continuous Prompts for Generation (2021)](https://arxiv.org/abs/2101.00190)_

#### Mathematical Principle

In standard Transformers, output is typically:

```
Y = W * X
```

Prefix Tuning concatenates a set of trainable parameters before `W`:

```
W' = [Wₚ; W]
```

Resulting in new output:

```
Y = W' * X
```

That is, it introduces additional "prefix key-value pairs" in each layer's attention mechanism, allowing the model to reference this extra information during inference.

#### Implementation Characteristics

- Model backbone is completely frozen;
- Introduces prefixes in multi-head attention of Encoder and Decoder;
- Usually requires more memory than Prompt Tuning;
- Performs better in generation tasks (like text continuation, summarization).

Recommended paper: [Prefix-Tuning: Optimizing Continuous Prompts for Generation (2021)](https://arxiv.org/abs/2101.00190)

### 3. LoRA: Low-Rank Decomposition, Lightweight and Efficient

#### Core Concept

LoRA (Low-Rank Adaptation) takes a different route.
It assumes that large language models are **over-parameterized**, meaning only a small portion of parameters in the model are truly important for output.

![image-20251021211511552](pictures/lora_diagram.png)

_Figure 3 source: [LoRA: Low-Rank Adaptation of Large Language Models (2021)](https://arxiv.org/abs/2106.09685)_

Therefore, LoRA doesn't directly modify the complete weight matrix `W`, but injects a **low-rank update matrix ΔW**:

```
Y = (W + ΔW) * X
```

#### Mathematical Principle

LoRA assumes ΔW is a low-rank matrix that can be decomposed as:

```
ΔW = A * B
```

Where:

- `A` is an m×r matrix
- `B` is an r×n matrix
- `r` ≪ min(m, n) (low-rank constraint)

During training, only `A` and `B` need to be learned, while original parameters `W` remain frozen.

During inference, only ΔW needs to be added to the computation.

#### Advantages

- Significantly reduces trainable parameter count (typically only 0.1%～ 1%);
- Fast training speed, almost no additional overhead during inference;
- Easy task switching:

  ```
  (W + ΔW₁) → (W + ΔW₂)
  ```

  Simple matrix replacement suffices.

Recommended paper: [LoRA: Low-Rank Adaptation of Large Language Models (2021)](https://arxiv.org/abs/2106.09685)

### 4. QLoRA: More Memory-Efficient Quantized Fine-Tuning

#### Core Concept

LoRA is already very efficient, but may still face memory limitations on models with tens of billions of parameters.
Thus, **QLoRA (Quantized LoRA)** further incorporates **quantization** technology on top of LoRA.

![image-20251021211607473](pictures/qlora_diagram.png)

_Figure 4 source: [QLoRA: Efficient Finetuning of Quantized LLMs (2023)](https://arxiv.org/abs/2305.14314)_

The core idea of quantization is:

> Using lower bit-width to represent parameters without significantly losing precision.

#### Working Principle

QLoRA quantizes original 16-bit floating-point parameters to 4-bit, dramatically reducing memory usage.

For example, the paper shows:
On LLaMA-65B model,
traditional fine-tuning requires **780GB GPU memory**,
while using QLoRA only needs **48GB** — performance barely drops, but cost decreases by over tenfold.

#### Advantages

- Significantly reduces GPU memory requirements;
- Can fine-tune large models on single consumer-grade graphics cards;
- Maintains LoRA's modularity and flexibility;
- Can quickly switch between different domain fine-tuning results in multi-task scenarios.

Recommended paper: [QLoRA: Efficient Finetuning of Quantized LLMs (2023)](https://arxiv.org/abs/2305.14314)

### Extended Reading: PEFT Technology Spectrum

Beyond the four methods above, Parameter-Efficient Fine-Tuning has many variants:

- **Adapter Tuning**: Inserting small trainable modules in each layer;
- **BitFit**: Only fine-tuning bias parameters;
- **Prompt-based Mixture of Experts**: Automatically selecting fine-tuning components by task.

![image-20251021212158680](pictures/peft_spectrum_diagram.png)
_Figure 5 source: [Scaling Down to Scale Up: A Guide to Parameter-Efficient Fine-Tuning (2023)](https://arxiv.org/abs/2306.08019)_

### Summary

| Method        | Modifies Backbone Parameters | Trainable Parameters | Memory Usage | Applicable Scenarios               |
| ------------- | ---------------------------- | -------------------- | ------------ | ---------------------------------- |
| Prompt Tuning | No                           | Minimal              | Very Low     | Classification, Instruction Tuning |
| Prefix Tuning | No                           | Few                  | Low          | Text Generation, Dialogue          |
| LoRA          | Local Low-Rank Injection     | Small                | Medium       | General Tasks                      |
| QLoRA         | LoRA + Quantization          | Small                | Very Low     | Large Model Scenarios              |

> If "full fine-tuning" is re-educating the model, then "PEFT fine-tuning" is **teaching it new skills without changing the model's brain**.

In the future, as LoRA, QLoRA, and other methods mature, ordinary researchers will be able to train their own professional large models on consumer-grade devices.

## References

1. [The Power of Scale for Parameter-Efficient Prompt Tuning](https://arxiv.org/abs/2104.08691)
2. [Prefix-Tuning: Optimizing Continuous Prompts for Generation](https://arxiv.org/abs/2101.00190)
3. [LoRA: Low-Rank Adaptation of Large Language Models](https://arxiv.org/abs/2106.09685)
4. [QLoRA: Efficient Finetuning of Quantized LLMs](https://arxiv.org/abs/2305.14314)
5. [Scaling Down to Scale Up: A Guide to Parameter-Efficient Fine-Tuning](https://arxiv.org/abs/2302.00072)
