# Serving Generative Models

Serving generative models means exposing trained models through APIs so that applications can send requests and receive generated outputs in real time. Once deployed, the runtime environment manages inference requests, routing, preprocessing, and response generation.

On the platform, these interactions are performed, where possible, through **OpenAI-compatible APIs**, allowing applications and tools to interact with deployed models using standard OpenAI protocols. This enables easy integration of generative AI capabilities into applications, automation pipelines, and development tools without requiring custom APIs. By combining these serving options with OpenAI-compatible APIs, the DigitalHub platform enables users to quickly deploy and operate generative AI models without implementing custom inference services. Using the available runtimes, users can configure and deploy models directly through the platform by specifying only a small set of parameters such as the model model name, runtime type, and optional adapters or runtime arguments.

This approach enables **no-code or low-code model deployment**, where the platform automatically handles the underlying infrastructure required to run the model, including container configuration, API exposure, and runtime orchestration.

Different runtimes support different types of generative workloads. Specifically, we distinguish between

- **Text Generation Tasks**
- **Embedding and Vector Tasks**
- **Speech Processing Tasks**

The following examples illustrate typical runtime tasks that can be executed on the platform using either the platform SDK or the core console UI as indicated below.

---

## Text Generation Tasks

Text generation tasks, such as completion and chat generation, may be performed either through the [**vllmserve-text**](../runtimes/llmserve.md#vllm-serving-runtime) runtime or with the [**kubeai-text**](../runtimes/llmserve.md#kubeai-text-runtime) runtime.

The [**vllmserve-text**](../runtimes/llmserve.md#vllm-serving-runtime) runtime is commonly used for text generation and conversational workloads. Through the OpenAI-compatible APIs available in the DigitalHub platform, applications can send prompts or chat messages and receive generated responses. VLLM runtime can be configured in the same way the vLLM engine, it allows for integrating multiple LoRA adapters, etc.

The [**kubeai-text**](../runtimes/llmserve.md#kubeai-text-runtime) runtime is a more advanced alternative that allows for serving multiple models or adapters and auto-scaling, allowing for using both vLLM and OLLama engines for different types of scenarios. For example, OLLama is more appropriate for CPU-only workloads, while vLLM is more suitable for GPU workloads and is more flexible for production-oriented tasks.

### Example of vllmserve-textruntime tasks

**Chat assistants**

Applications send chat completion requests to generate conversational responses.

Example:

- A chatbot sends a user prompt asking for help writing an email.
- The request is sent to the model using the OpenAI **chat completions API**.
- The generated response is streamed back to the client application.

From the Core Manage UI, users can create a chat assistant API task of kind 'vllmserve-text+serve:run' as shown.

![configure model](../images/runtimes/vllmserve-text-stepper1.png)

![customize parameters](../images/runtimes/vllmserve-text-stepper2.png)

Users can view the API endpoints for their deployed services in the 'services' tab.

![services](../images/runtimes/vllmserve-text-services.png)

### Interact with the model directly in the console

Once a text generation service is running, it can be tested interactively directly from the console using the built-in [Chat Client](../runtimes/chat-client.md). The Chat Client is automatically selected for any service that exposes an OpenAI-compatible chat API (both `vllmserve-text` and `kubeai-text`). It supports streaming responses, multi-turn conversation history, and response regeneration — no external tooling required.

---

## Embedding and Vector Tasks

Frequently genAI applications require supporting tasks, such as embedding, ranking, scoring, and encoding. They are required, for example, for generating vector embeddings used in search, recommendation systems, and semantic analysis. In the platform these tasks may be implemented using the [**vllmserve-pooling**](../runtimes/llmserve.md#vllm-serving-runtime) runtime or the [**kubeai-text**](../runtimes/llmserve.md#kubeai-text-runtime) runtime (only for embedding).

### Example of vllmserve-pooling runtime tasks

**Semantic search**

Applications convert queries and documents into embeddings to perform similarity searches.

Example:

- A user searches for documents related to a specific topic.
- The runtime generates an embedding vector for the query.
- The search engine compares it with stored document embeddings.

From the Core Manage UI, users can create a chat assistant API task of kind 'vllmserve-pooling+serve:run' as shown.

![configure model](../images/runtimes/vllmserve-pooling-stepper1.png)

Users can view the API endpoints for their deployed services in the 'services' tab.

![services](../images/runtimes/vllmserve-pooling-services.png)

### Example of kubeai-text runtime tasks

**Text embedding with KubeAI**

Applications convert text into vector embeddings for semantic search and similarity analysis.

Example:

- A document management system needs to index and search documents.
- The runtime generates embedding vectors for documents and queries.
- Similarity comparisons identify relevant documents.

From the Core Manage UI, users can create a text embedding API task of kind 'kubeai-text+serve:run' and the services will be avaliable as shown below.

![configure model](../images/runtimes/kubeai-text-run.png)

---

## Audio Processing Tasks

Audio processing tasks, such as speech recognition and translation, may be performed through the [**vllmserve-speech**](../runtimes/llmserve.md#vllm-serving-runtime) runtime or with the [**kubeai-speech**](../runtimes/llmserve.md#kubeai-speech-runtime) runtime.

The [**vllmserve-speech**](../runtimes/llmserve.md#vllm-serving-runtime) runtime supports audio-based AI tasks such as speech recognition and translation. These capabilities are also accessible through OpenAI-compatible audio APIs exposed by the platform.

### Example vllmserve-speech runtime tasks

**Speech transcription**

Audio recordings are processed and converted into text.

Example:

- A meeting recording is uploaded through the **audio transcription API**.
- The runtime invokes the speech model.
- The generated transcript is returned to the client.

From the Core Manage UI, users can create a chat assistant API task of kind 'vllmserve-speech+serve:run' as shown.

![configure model](../images/runtimes/vllmserve-speech-stepper1.png)

Users can view the API endpoints for their deployed services in the 'services' tab.

![services](../images/runtimes/vllmserve-speech-services.png)

---

## Summary

On the DigitalHub platform, generative models can be served using multiple runtimes while maintaining a **consistent OpenAI-compatible API interface**. This enables applications to perform a variety of AI tasks—such as text generation, speech processing, and embedding creation—without changing the client-side integration.

| Runtime           | Example Tasks                                                     | Console Client                            |
| ----------------- | ----------------------------------------------------------------- | ----------------------------------------- |
| vllmserve-text    | chat generation, text completion, code generation                 | [Chat Client](../runtimes/chat-client.md) |
| kubeai-text       | multi-model serving, adapter routing, autoscaling, text embedding | [Chat Client](../runtimes/chat-client.md) |
| vllmserve-pooling | embeddings, semantic search, recommendations                      | —                                         |
| vllmserve-speech  | speech transcription, audio translation                           | —                                         |
| kubeai-speech     | speech transcription                                              | —                                         |

**Note**: Refer to the Tutorial section for more detailed usage and examples.
