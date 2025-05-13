import dash
import os
from dash import dcc, html
import plotly.express as px
import pandas as pd

# Exemple de données à remplacer par les vraies via fichier/parquet/BDD
df = pd.DataFrame({
    "Article": ["News 1", "News 2"],
    "Sentiment": [0.2, -0.1]
})

app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1("Sentiment des News"),
    dcc.Graph(figure=px.bar(df, x="Article", y="Sentiment", title="Analyse de sentiment"))
])

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run_server(host="0.0.0.0", port=port)
