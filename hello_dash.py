import matplotlib
matplotlib.use("agg")
import dash
from dash import html, dcc
from dash.dependencies import Input, Output
import matplotlib.pyplot as plt
from plotly.tools import mpl_to_plotly
import numpy as np

def create_sine_graph(n=3):
    fig, ax = plt.subplots()

    x = np.linspace(0, n*np.pi, 100)
    ax.plot(x, np.sin(x))
    ax.set_title("Sine graph")

    return mpl_to_plotly(fig)

app = dash.Dash(__name__, assets_folder="other_assets")

app.layout = html.Div([
    html.H1("First Dash app"),
    html.H3("Bruxelles Formation 2024"),
    html.Div([
        dcc.Slider(0, 20, 2, value=10, id="graph-slider"),
        dcc.Graph(figure=create_sine_graph(), id="sine-graph"),
    ]),
], className="border")

@app.callback(Output("sine-graph", "figure"), [Input("graph-slider", "value")])
def update_sine_graph(slider_value):
    return create_sine_graph(slider_value)



if __name__ == "__main__":
    app.run(debug=True)