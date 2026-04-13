# AI Service Guardrails

Guardrails are safety and control mechanisms placed around AI models and services to ensure that their inputs and outputs meet defined quality, safety, and policy requirements. They act as a protective layer that intercepts, inspects, and optionally modifies or blocks requests and responses, without changing the underlying model itself.

In practice, guardrails are used to:

- **Filter harmful or inappropriate content** — block requests containing toxic, offensive, or policy-violating text before they reach the model, and filter model outputs before they are returned to the user.
- **Prevent prompt injection attacks** — detect and neutralize attempts to manipulate a model's behaviour through adversarial instructions embedded in user input.
- **Enforce output structure and validity** — ensure responses conform to an expected schema, format, or value range, especially for structured output tasks.
- **Detect and redact sensitive information** — identify and mask personally identifiable information (PII) or confidential data in both inputs and outputs.
- **Monitor for model drift and anomalies** — flag responses that fall outside expected behavioural boundaries, signalling potential degradation or misuse.
- **Apply domain or business rules** — enforce organisation-specific policies such as topic restrictions, regulatory compliance, or brand-safe language.

### Guardrails for LLM Services

Large language models are particularly sensitive to the quality and intent of user inputs, and their open-ended outputs require careful monitoring. Guardrails for LLMs are commonly applied at two stages: before the model receives a prompt (**pre-processing**) and after the model generates a response (**post-processing**).

Pre-processing guardrails (input)

- **Toxicity and hate speech detection** — Scan user messages for harmful language and either reject the request or sanitise the input before forwarding it to the model.
- **Prompt injection detection** — Identify attempts to override system instructions or extract sensitive information through maliciously crafted prompts.
- **PII detection and anonymisation** — Detect names, emails, ID numbers, or other personal data in the input and redact or substitute them before the model processes the request.
- **Topic and intent classification** — Route or reject requests based on the detected topic, ensuring the model only handles in-scope queries.
- **Input length and rate limiting** — Enforce token limits or rate constraints to prevent abuse.

Post-processing guardrails (output)

- **Output toxicity filtering** — Re-scan generated text for harmful content that the model may have produced despite a safe input.
- **Fact grounding and hallucination detection** — Compare the model's answer against a knowledge base or retrieved context to flag ungrounded claims.
- **Sensitive data masking** — Prevent the model from leaking PII or confidential information that may have been present in retrieved context.
- **Format and schema validation** — Ensure the response matches the expected structure (e.g., valid JSON, specific field values) before returning it to the caller.
- **Brand and tone enforcement** — Check that the language, style, and sentiment of the response align with organisational guidelines.

### Guardrails for Inference Services

Beyond LLMs, guardrails are equally valuable for traditional machine learning inference services that serve classification, regression, or scoring models.

- **Input validation** — Verify that incoming feature vectors contain values within expected ranges, have no missing mandatory fields, and match the schema the model was trained on. Reject or impute malformed requests before they reach the model.
- **Distribution monitoring** — Compare incoming data against the training distribution to detect data drift. Flag requests where input features differ significantly from what the model has seen, as predictions in these regions are likely unreliable.
- **Output range checking** — Ensure prediction scores, probabilities, or regression outputs fall within plausible bounds, catching numerical errors or model failures early.
- **Confidence thresholding** — Block or escalate low-confidence predictions instead of returning uncertain results directly to the caller.
- **Audit logging** — Record inputs and outputs for compliance, debugging, and monitoring, without exposing them to downstream systems.

---

### Architecture Patterns

There is no single way to deploy guardrails. The right architecture depends on how the AI service is consumed, who controls the client, and how much latency overhead is acceptable. The following patterns represent the most common approaches.

#### Application-integrated Guardrails

In this pattern the guardrail logic lives inside the application that calls the AI service. Before sending a request the application invokes a validation function, and after receiving a response it runs output checks. No additional infrastructure is required.

```
User → Application → [input guard] → AI Service → [output guard] → Application → User
```

**When to use:** when the client application is under your control, when you need access to application-level context (user identity, session history) during validation, or when you want to keep infrastructure simple.

**Trade-offs:** guardrail coverage depends on every client implementing it correctly. If the AI service is called from multiple applications, each must independently apply the same logic, which creates duplication and inconsistency risk. Bypassing guardrails by calling the AI service directly is possible.

Typical implementations use libraries such as [LangChain guardrails](https://docs.langchain.com/oss/python/langchain/guardrails) or [NeMo Guardrails](https://docs.nvidia.com/nemo/guardrails/latest/integration/langchain/langchain-integration.html) integration for LangChain.


#### Proxy / Gateway Guardrails

In this pattern the guardrail logic is incapsulated in a dedicated server that sits between the AI service and the client and exposes the same API, such as Open AI-compatible APIs. This is particularly useful when the AI service is consumed by multiple clients or third-party applications, or when you need guaranteed, centralised enforcement that cannot be bypassed, and making the guardrail more scalable and efficient. Also, for LLM guardrails the proxy service implements the asynchronous streaming API, which is useful for handling long-running conversations.

```
User → Proxy  → [input guard] → AI Service → [output guard] → Proxy / Gateway → User
```

**When to use:** when the API requires complex flows (e.g., LLM streaming), when the AI service is consumed by multiple clients or third-party applications, when you need guaranteed, centralised enforcement that cannot be bypassed, or when guardrail rules must change without redeploying client code.

**Trade-offs:** the proxy is an additional network hop and a potential bottleneck. 

Typical implementation of this  pattern use libraries like [NeMo Guardrails API Server](https://docs.nvidia.com/nemo/guardrails/latest/run-rails/index.html) or [Guardrails AI](https://guardrailsai.com/guardrails/docs).

---

#### Pre / Post Validation Services

In this pattern the guardrail logic is factored into dedicated, independently deployed microservices. The calling component — either the application or a gateway — calls these services explicitly as part of the request lifecycle.

```
                ┌──────────────────┐
User → App ────►│ Pre-validation   │──► AI Service
                │ Service          │         │
                └──────────────────┘         │
                                             ▼
                                ┌──────────────────┐
User ◄── App ◄──────────────────│ Post-validation  │
                                │    Service       │
                                └──────────────────┘
```

**When to use:** when guardrail management is complex enough to warrant its own lifecycle (independent scaling, versioning, and testing), when different services share the same validation logic and you want a single authoritative implementation, or when guardrail models (e.g., a safety classifier) are large and should be loaded once rather than once per application instance.

**Trade-offs:** adds operational complexity — each validation service must be monitored, scaled, and kept available. Network latency for each validation call adds to end-to-end response time.

This pattern is common in enterprise deployments where a content safety classifier (e.g., **Llama Guard** or **Azure AI Content Safety**) is hosted as a shared service, and multiple AI-powered features call it via a common SDK or internal API.

In the platform we implement the pre- and post- validation services as Python functions deployed using the [Guardrail runtime](../runtimes/guardrail.md) and attached to the AI service via the [Envoy Gateway extension](../extensions/envoygw.md). The Envoy Gateway intercept the request and response and calls the pre- and post- validation services via [ExtProc Envoy extension services](https://www.envoyproxy.io/docs/envoy/latest/configuration/http/http_filters/ext_proc_filter). 

#### Pattern Comparison

| Aspect | Application-integrated | Proxy / Gateway | Pre / Post Services |
|---|---|---|---|
| Enforcement guarantee | Dependent on client | Centralised | Centralised |
| Infrastructure overhead | None | Services required | Services and gateway required |
| Independent scaling | No | Limited | Yes |
| Multi-client reuse | Requires duplication | Automatic | Automatic |
| Latency impact | Low | Low | Medium |
| Suitable for | Single-app, simple rules | Multi-client APIs | Complex or shared rules |

---

### LLM Guardrail Frameworks

A growing ecosystem of tools and frameworks has emerged to help implement guardrails. The following are widely used examples.

**NeMo Guardrails**

[NVIDIA NeMo Guardrails](https://github.com/NVIDIA/NeMo-Guardrails) is an open-source toolkit designed specifically for adding programmable constraints to LLM-based conversational applications. It uses a declarative language called **Colang** to define allowed and disallowed dialogue flows, integrating directly with the LLM to steer conversations and prevent undesirable outputs.

Key capabilities:

- Input and output rail definitions in a human-readable configuration format.
- Built-in integrations with popular LLM providers (OpenAI, HuggingFace, NVIDIA NIM).
- Support for fact-checking, hallucination detection, and topic restrictions.
- Composable rail types: topical, safety, execution, and dialog rails.

Patterns supported:

- Application integration: directly inside the application, through integration extensions (e.g., with LangChain)
- Proxy: through the NeMo Guardrails API Server

NeMo Guardrails is particularly well suited for chat assistant applications where conversation control and safety are critical.

**Guardrails AI**

[Guardrails AI](https://github.com/guardrails-ai/guardrails) is an open-source Python framework focused on enforcing structured, validated outputs from LLMs. It wraps LLM calls with a validation layer defined using a library of pre-built **validators** (called *guards*), and can automatically re-prompt the model if the output fails validation.

Key capabilities:

- A rich library of validators covering format, content, PII, and more.
- Support for defining custom validators.
- Integration with major LLM providers and frameworks (OpenAI, Anthropic, LangChain).
- Automatic retry and self-correction loop when outputs do not meet requirements.

Patterns supported:

- Application integration: directly inside the application, through integration extensions (e.g., with LangChain, MLFlow genAI)
- Proxy: through the Guardrails Server
- Pre- and post-processing: using the Guardrails Validators

**Llama Guard**

[Llama Guard](https://ai.meta.com/research/publications/llama-guard-llm-based-input-output-safeguard-for-human-ai-conversations/) (by Meta) is a fine-tuned LLM designed to classify both user inputs and model outputs against a configurable safety taxonomy. It acts as a separate safety classifier that can be deployed alongside the main serving model and queried as part of the request pipeline.

Key capabilities:

- Classifies content into a set of harm categories (violence, hate speech, sexual content, etc.).
- Can be used as both a pre-processing and a post-processing rail.
- Configurable taxonomy allows organisations to customise the set of categories to check.
- Available as open weights models (Llama Guard 3 family) on HuggingFace.

Llama Guard is appropriate when a lightweight, self-hosted safety classifier is preferred over a third-party API, especially in privacy-sensitive deployments.

**Azure AI Content Safety**

[Azure AI Content Safety](https://learn.microsoft.com/en-us/azure/ai-services/content-safety/overview) is a cloud API service that analyses text and images for harmful content. It provides ready-made classifiers for hate speech, violence, self-harm, and sexual content, returning severity scores that can be used to gate whether a request or response should be allowed.

Key capabilities:

- Multi-category content analysis with configurable severity thresholds.
- Prompt Shield endpoint to detect prompt injection attempts.
- Groundedness detection to identify LLM hallucinations with respect to a supplied context.
- Available as a managed API with no infrastructure to maintain.

---

### Guardrails on the Platform

On the platform, guardrails may be implemented in different ways, for what concerns the proxy or pre- and post-processing services.

First, it is possible to deploy proxy using the corresponding frameworks such as NeMo Guardrails and Guardrails AI. These frameworks provide the ready to use server APIs that can be used for chat applications. [Container](../runtimes/container.md) Runtime can be used to deploy the proxy as a container.

Second, for custom AI services and ML services, one can deploy custom proxy logic using the [Python Serverless](../runtimes/python.md) or [Container](../runtimes/container.md) runtimes.

Finally, it is possible to deploy the corresponding pre- and post-processing functions using the [Guardrail runtime](../runtimes/guardrail.md). In this case, each function operates as either a **preprocessor** (applied to incoming requests), a **postprocessor** (applied to outgoing responses), or a **wrapprocessor** (applied to both), and is exposed as a gRPC service following the [Envoy ExtProc](https://www.envoyproxy.io/docs/envoy/latest/configuration/http/http_filters/ext_proc_filter) specification.

To attach guardrails to a deployed service, use the [Envoy Gateway extension](../extensions/envoygw.md). The extension creates a proxy configuration so that all traffic to the protected service passes through the guardrail functions first. Guardrail logic can leverage any external framework (such as those described above) by declaring the required libraries as Python dependencies in the function specification.

See the [Guardrail runtime reference](../runtimes/guardrail.md) and the [SDK guardrail documentation](https://scc-digitalhub.github.io/sdk-docs/reference/runtimes/guardrail/overview/) for implementation details.
