
from pickle import load
import pandas as pd
import json

def init(context):
    # Qua ti setti il nome del modello che vuoi caricare
    model_name = "cancer_classifier"

    # prendi l'entity model sulla base del nome
    model = context.project.get_model(entity_name=model_name)
    path = model.download()
    with open(path, "rb") as f:
        svc_model = load(f)
    
    # settare model nel context di nuclio (non su project che è il context nostro)
    setattr(context, "model", svc_model)

def serve(context, event):

    # Sostanzialmente invochiamo la funzione con una chiamata REST
    # Nel body della richiesta mandi l'inference input
    
    if isinstance(event.body, bytes):
        body = json.loads(event.body)
    else:
        body = event.body
    context.logger.info(f"Received event: {body}")
    inference_input = body["inference_input"]
    
    data = json.loads(inference_input)
    pdf = pd.json_normalize(data)

    result = context.model.predict(pdf)

    # Convert the result to a pandas DataFrame, reset the index, and convert to a list
    jsonstr = str(result.tolist())
    return json.loads(jsonstr)
