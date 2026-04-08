
# Serving Machine Learning Models

Serving machine learning models means exposing trained models through APIs so that applications can send requests and receive predictions in real time. Once deployed, the runtime environment manages inference requests, routing, preprocessing, and response generation.

On the platform, these interactions are performed through **standard ML APIs**, allowing applications and tools to interact with deployed models using industry-standard protocols, such as [Open Inference v2](https://github.com/kserve/open-inference-protocol) protocol. This enables easy integration of machine learning capabilities into applications, automation pipelines, and development tools without requiring custom APIs.

Using the available runtimes, users can configure and deploy models directly through the platform by specifying only a small set of parameters such as the model name, runtime type, and optional runtime arguments.

This approach enables **no-code or low-code model deployment**, where the platform automatically handles the underlying infrastructure required to run the model, including container configuration, API exposure, and runtime orchestration.

Different runtimes support different types of machine learning workloads. The following examples illustrate typical runtime tasks that can be executed on the platform using either the platform SDK or the core console UI.

---

## Scikit-Learn Model Serving

The [**sklearnserve runtime**](../runtimes/sklearnserve.md) is commonly used for serving scikit-learn models for classification, regression, and clustering tasks. Applications can send feature vectors and receive predictions through standardized prediction APIs.

### Example runtime tasks

**Classification predictions**

Applications send feature data to generate classification predictions.

Example:
- Train a breast cancer classifier, deploy it as a REST API service.

From the Core Manage UI, users can create a model serving task of kind 'sklearnserve+serve:run'.

![configure model](../images/runtimes/sklearnserve-stepper.png)

Users can view the API endpoints for their deployed services in the 'services' tab.

![services](../images/runtimes/sklearnserve-services.png)

---

## MLflow Model Serving

The [**mlflowserve runtime**](../runtimes/mlflowserve.md) is designed for serving models tracked and logged with MLflow, supporting multiple frameworks including scikit-learn, TensorFlow, PyTorch, and XGBoost. These tasks can be executed through MLflow's standard serving API.

### Example runtime tasks

**Multi-framework model serving**

Applications send inference requests to models regardless of the underlying framework.

Example:
- Train an iris classifier (e.g., scikit-learn), log the model with MLflow, and deploy the logged artifact as a REST serving endpoint.

From the Core Manage UI, users can create a model serving task of kind 'mlflowserve+serve:run'.

![configure model](../images/runtimes/mlflowserve-stepper.png)

Users can view the API endpoints for their deployed services in the 'services' tab.

![services](../images/runtimes/mlflowserve-services.png)

---

## Custom Model Serving 

It is possible to expose a custom model through the [**python serverless**](../runtimes/python.md) or [**openinference**](../runtimes/oi.md) runtimes. In the first case, the API is not limited to a specific format or protocol, and it is possible to define arbitrary HTTP API for interacting with the model. In the second case the exposed API is defined by the Open Inference v2 protocol, and allows for both HTTP and gRPC protocols. A custom model can be loaded from a local file or from a remote URL. 

### Example runtime tasks

- Train a computer vision object detector using HuggingFace transformers library and publish the model on huggingface.co
- Define a Python inference function that accespts the image as byte array input and returns a prediction
- Define the corresponding input and ouptu tensor definitions and deploy the function using the Open Inference runtime.

---

## Summary

On the DigitalHub platform, machine learning models can be served using multiple runtimes while maintaining **consistent prediction API interfaces**. This enables applications to perform various ML inference tasks without changing client-side integration.

| Runtime | Example Tasks |
|---------|---------------|
| sklearnserve | classification, regression, clustering |
| mlflowserve | multi-framework serving, model versioning, A/B testing |
| python serverless | custom model serving |
| openinference | custom model serving with Open Inference v2 protocol |

**Note**: Refer to the Tutorial section for more detailed usage and examples.